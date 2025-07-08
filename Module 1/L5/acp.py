import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Load the data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the data (0-255 → 0-1)
x_train = x_train / 255.0
x_test = x_test / 255.0

# One-hot encode the labels
y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)

model = Sequential([
    Flatten(input_shape=(28, 28)),          # Input layer (28x28 pixels)
    Dense(128, activation='relu'),          # Hidden layer with 128 neurons
    Dense(64, activation='relu'),           # Another hidden layer
    Dense(10, activation='softmax')         # Output layer (10 classes for digits 0–9)
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(x_train, y_train_cat, epochs=5, validation_split=0.1)

test_loss, test_acc = model.evaluate(x_test, y_test_cat)
print(f"Test Accuracy: {test_acc:.4f}")

predictions = model.predict(x_test)

# Predict a single digit
def show_prediction(index):
    plt.imshow(x_test[index], cmap='gray')
    plt.title(f"Actual: {y_test[index]} | Predicted: {np.argmax(predictions[index])}")
    plt.show()

show_prediction(0)
