# Capstone Project 4: Image Classifier Using CIFAR-10

## Objective

Design, train, and evaluate a Convolutional Neural Network (CNN) that classifies 32x32 color
images into 10 categories using the CIFAR-10 dataset. This project introduces deep learning
fundamentals -- convolutional layers, pooling, dropout, batch normalization, and data
augmentation -- all within the TensorFlow/Keras framework.

---

## Skills Practiced

| Skill | Details |
|---|---|
| Deep Learning Fundamentals | Layers, activations, loss functions, optimizers |
| CNN Architecture Design | Conv2D, MaxPooling, BatchNormalization, Dropout |
| Data Augmentation | ImageDataGenerator, random flips/rotations/shifts |
| Training Strategies | Learning rate scheduling, early stopping, callbacks |
| Model Evaluation | Accuracy, confusion matrix, per-class precision/recall |

---

## Dataset

**CIFAR-10** is built directly into Keras -- no download or external files required.

```python
from tensorflow.keras.datasets import cifar10
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
```

| Property | Value |
|---|---|
| Training samples | 50,000 |
| Test samples | 10,000 |
| Image size | 32 x 32 x 3 (RGB) |
| Classes | 10 |

**Classes:** airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck

---

## Step-by-Step Instructions

### Step 1 -- Load and Visualize
- Load CIFAR-10 using `keras.datasets.cifar10.load_data()`.
- Print shapes and data type of the arrays.
- Display a grid of 25 random sample images with their class labels.
- Plot the class distribution to verify balance.

### Step 2 -- Preprocess
- Normalize pixel values to the range [0, 1] by dividing by 255.0.
- One-hot encode the labels using `keras.utils.to_categorical`.
- Split a validation set (10-20 %) from the training data.

### Step 3 -- Data Augmentation
Use `ImageDataGenerator` to create augmented training batches:

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True,
)
datagen.fit(X_train)
```

Visualize a few augmented versions of the same image to confirm the transforms look reasonable.

### Step 4 -- Build the CNN Architecture

A recommended starting architecture:

```
Input (32, 32, 3)
  -> Conv2D(32, 3x3, padding='same', relu) -> BatchNorm -> Conv2D(32, 3x3, relu) -> BatchNorm
  -> MaxPooling2D(2x2) -> Dropout(0.2)

  -> Conv2D(64, 3x3, padding='same', relu) -> BatchNorm -> Conv2D(64, 3x3, relu) -> BatchNorm
  -> MaxPooling2D(2x2) -> Dropout(0.3)

  -> Conv2D(128, 3x3, padding='same', relu) -> BatchNorm -> Conv2D(128, 3x3, relu) -> BatchNorm
  -> MaxPooling2D(2x2) -> Dropout(0.4)

  -> Flatten
  -> Dense(256, relu) -> BatchNorm -> Dropout(0.5)
  -> Dense(10, softmax)
```

Feel free to experiment with the number of filters, layers, and dropout rates.

### Step 5 -- Compile and Train

```python
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'],
)
```

Use these callbacks:
- `EarlyStopping(patience=10, restore_best_weights=True)`
- `ReduceLROnPlateau(factor=0.5, patience=5)`
- `ModelCheckpoint('best_model.keras', save_best_only=True)`

Train for up to 100 epochs with the augmented data generator:
```python
history = model.fit(
    datagen.flow(X_train, y_train, batch_size=64),
    epochs=100,
    validation_data=(X_val, y_val),
    callbacks=[early_stop, reduce_lr, checkpoint],
)
```

### Step 6 -- Evaluate
- Plot training and validation accuracy over epochs.
- Plot training and validation loss over epochs.
- Evaluate the final model on the test set and print overall accuracy.
- Generate a confusion matrix heatmap (10 x 10).
- Print a classification report with per-class precision, recall, and F1-score.
- Display a grid of misclassified images with their true and predicted labels.

### Step 7 -- Save the Model
```python
model.save('cifar10_classifier.keras')
```

---

## Expected Deliverables

1. `starter.py` with the complete model definition, training loop, and evaluation.
2. Saved model file (`cifar10_classifier.keras`).
3. Training history plots (accuracy and loss curves).
4. Confusion matrix heatmap.
5. Grid of sample predictions and misclassified images.

**Target accuracy:** Aim for 88-93 % test accuracy with the architecture above and augmentation.

---

## Architecture Quick Reference

| Layer | Output Shape | Parameters |
|---|---|---|
| Conv2D(32, 3x3) | (32, 32, 32) | 896 |
| Conv2D(32, 3x3) | (30, 30, 32) | 9,248 |
| MaxPooling2D | (15, 15, 32) | 0 |
| Conv2D(64, 3x3) | (15, 15, 64) | 18,496 |
| Conv2D(64, 3x3) | (13, 13, 64) | 36,928 |
| MaxPooling2D | (6, 6, 64) | 0 |
| Conv2D(128, 3x3) | (6, 6, 128) | 73,856 |
| Conv2D(128, 3x3) | (4, 4, 128) | 147,584 |
| MaxPooling2D | (2, 2, 128) | 0 |
| Flatten | (512) | 0 |
| Dense(256) | (256) | 131,328 |
| Dense(10) | (10) | 2,570 |

---

## Bonus Challenges

- Implement a **ResNet-style skip connection** block and compare accuracy with the plain CNN.
- Use **transfer learning** with a pre-trained model (e.g., `MobileNetV2`) fine-tuned on CIFAR-10.
- Apply **Grad-CAM** to visualize which regions of an image the model focuses on for its predictions.
- Experiment with **mixup** or **cutout** data augmentation strategies.
- Convert the trained model to **TensorFlow Lite** and measure inference time on CPU.
- Train the same architecture on **CIFAR-100** (100 classes) and compare performance degradation.
