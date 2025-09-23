import cv2
import numpy as np

def display_image(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def apply_filter(img, filter_type, strngth=0):
    filtered_img = img.copy()
    if filter_type == 'blur':
        filtered_img = cv2.blur(img, (5, 5))
    elif filter_type == 'gaussian':
        filtered_img = cv2.GaussianBlur(img, (5, 5), 0)
    elif filter_type == 'median':
        filtered_img = cv2.medianBlur(img, 5)
    elif filter_type == 'bilateral':
        filtered_img = cv2.bilateralFilter(img, 9, 75, 75)
    elif filter_type == 'sharpen':
        kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
        filtered_img = cv2.filter2D(img, -1, kernel)
    elif filter_type == 'edge':
        filtered_img = cv2.Canny(img, 100, 200)
    elif filter_type == 'emboss':
        kernel = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])
        filtered_img = cv2.filter2D(img, -1, kernel)
    elif filter_type == 'increase_bright':
        filtered_img = cv2.convertScaleAbs(img, alpha=1, beta=strngth)
    elif filter_type == 'increase_contrast':
        filtered_img = cv2.convertScaleAbs(img, alpha=strngth, beta=0)
    return filtered_img

def main_image_filter():
    print("Image filtering demo using OpenCV")
    print("Supported filters: blur/gaussian/median/bilateral/sharpen/edge/emboss/increase_bright/increase_contrast")
    img_path = input("Enter image path: ")
    img = cv2.imread(img_path)
    if img is None:
        print("Invalid image path.")
        return
    display_image("Original", img)
    print("Filters: blur | gaussian | median | bilateral | sharpen | edge | emboss | increase_bright | increase_contrast")
    print("Example: blur")
    while True:
        filter_type = input("Pick filter (type 'exit' to quit): ").lower()
        if filter_type == 'exit':
            break
        strngth = 0
        if filter_type in ['increase_bright', 'increase_contrast']:
            strngth = int(input("Choose strength (e.g. 50): "))
        filtered_img = apply_filter(img, filter_type, strngth)
        display_image(filter_type, filtered_img)

if __name__ == "__main__":
    main_image_filter()
