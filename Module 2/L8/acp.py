import cv2

def rotate_image(image):
    angle = 0
    center = (image.shape[1] // 2, image.shape // 2)

    def on_trackbar(val):
        nonlocal angle
        angle = val - 180
        rot_mat = cv2.getRotationMatrix2D(center, angle, 1)
        rotated = cv2.warpAffine(image, rot_mat, (image.shape[1], image.shape))
        cv2.imshow('Rotate & Align', rotated)

    cv2.namedWindow('Rotate & Align')
    cv2.createTrackbar('Angle', 'Rotate & Align', 180, 360, on_trackbar)
    on_trackbar(180)

    print("Rotate using slider; press 's' to confirm and continue.")
    while True:
        key = cv2.waitKey(100) & 0xFF
        if key == ord('s'):
            rot_mat = cv2.getRotationMatrix2D(center, angle, 1)
            rotated = cv2.warpAffine(image, rot_mat, (image.shape[1], image.shape))
            cv2.destroyWindow('Rotate & Align')
            return rotated

def brighten_image(image):
    brightness = 50

    def on_trackbar(val):
        bright_img = cv2.convertScaleAbs(image, alpha=1, beta=val)
        cv2.imshow('Brighten Image', bright_img)

    cv2.namedWindow('Brighten Image')
    cv2.createTrackbar('Brightness', 'Brighten Image', brightness, 100, on_trackbar)
    on_trackbar(brightness)

    print("Adjust brightness; press 's' to confirm and continue.")
    while True:
        key = cv2.waitKey(100) & 0xFF
        brightness = cv2.getTrackbarPos('Brightness', 'Brighten Image')
        if key == ord('s'):
            bright_img = cv2.convertScaleAbs(image, alpha=1, beta=brightness)
            cv2.destroyWindow('Brighten Image')
            return bright_img

def crop_image(image):
    roi = []
    clone = image.copy()

    def select_roi(event, x, y, flags, param):
        nonlocal roi
        if event == cv2.EVENT_LBUTTONDOWN:
            roi = [(x, y)]
        elif event == cv2.EVENT_LBUTTONUP:
            roi.append((x, y))
            cv2.destroyWindow('Crop Image')

    cv2.namedWindow('Crop Image')
    cv2.setMouseCallback('Crop Image', select_roi)

    print("Drag to select crop area in window. Press ESC to cancel cropping.")

    while True:
        img_copy = clone.copy()
        if len(roi) == 1:
            cv2.rectangle(img_copy, roi[0], (roi + 1, roi[1] + 1), (0, 255, 0), 2)
        elif len(roi) == 2:
            cv2.rectangle(img_copy, roi, roi[1], (0, 255, 0), 2)
        cv2.imshow('Crop Image', img_copy)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC key cancels cropping
            cv2.destroyWindow('Crop Image')
            return image
        if len(roi) == 2:
            break

    x1, y1 = roi
    x2, y2 = roi[1]
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])

    cropped = image[y1:y2, x1:x2]
    return cropped

def main():
    input_path = "example.jpg"  # Change to your input image filename
    img = cv2.imread(input_path)

    if img is None:
        print("Error: Could not load image.")
        return

    rotated_img = rotate_image(img)
    brightened_img = brighten_image(rotated_img)
    cropped_img = crop_image(brightened_img)

    cv2.imshow('Final Cropped Image', cropped_img)
    cv2.imwrite('output_cropped.jpg', cropped_img)
    print("Saved image as output_cropped.jpg")
    print("Press any key to exit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
