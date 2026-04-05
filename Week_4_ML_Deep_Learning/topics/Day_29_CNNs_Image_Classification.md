# Day 29: Convolutional Neural Networks for Image Classification

## Why CNNs?

Standard neural networks (dense/fully-connected) treat each pixel independently and
ignore spatial relationships. A 256x256 color image has 196,608 input features -- a dense
network would need millions of parameters and would ignore the fact that nearby pixels
are related.

**Convolutional Neural Networks** (CNNs) solve this by:
- Detecting local patterns (edges, textures) with small filters
- Sharing weights across the image (parameter efficiency)
- Building hierarchical features (edges -> shapes -> objects)

---

## Core CNN Components

### 1. Convolutional Layer

A convolutional layer slides a small **filter** (kernel) across the image, computing
a dot product at each position to produce a **feature map**.

```
Input Image     Filter (3x3)     Feature Map
[1 2 3 0]      [1 0 1]          [? ? ]
[0 1 2 3]  *   [0 1 0]    =     [? ? ]
[3 0 1 2]      [1 0 1]
[2 3 0 1]
```

**Key parameters:**
- `filters`: Number of filters (each detects a different pattern)
- `kernel_size`: Size of the sliding window (typically 3x3 or 5x5)
- `strides`: How many pixels the filter moves each step
- `padding`: 'valid' (no padding) or 'same' (pad to keep dimensions)

```python
from tensorflow.keras import layers

# 32 filters of size 3x3
layers.Conv2D(32, kernel_size=(3, 3), activation='relu', padding='same')
```

### 2. Pooling Layer

Reduces spatial dimensions by taking the maximum or average of small regions.
Provides translational invariance and reduces computation.

```python
# Max pooling: take the max value in each 2x2 region
layers.MaxPooling2D(pool_size=(2, 2))

# Average pooling
layers.AveragePooling2D(pool_size=(2, 2))
```

A 2x2 max pool reduces each dimension by half (e.g., 28x28 -> 14x14).

### 3. Flatten Layer

Converts the 2D feature maps into a 1D vector for the dense layers:

```python
layers.Flatten()
# Shape goes from (batch, height, width, channels) to (batch, height*width*channels)
```

---

## Typical CNN Architecture

```
Input -> [Conv -> ReLU -> Pool] x N -> Flatten -> Dense -> Output
```

Early layers detect low-level features (edges, colors).
Later layers detect high-level features (shapes, objects).

---

## Building a CNN with Keras

### MNIST Handwritten Digits

```python
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Load data
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

# Preprocess: normalize and reshape
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# Add channel dimension: (28, 28) -> (28, 28, 1)
X_train = X_train[..., np.newaxis]
X_test = X_test[..., np.newaxis]

print(f"Training: {X_train.shape}, Test: {X_test.shape}")

# Build the CNN
model = keras.Sequential([
    # First convolutional block
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),

    # Second convolutional block
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Third convolutional block
    layers.Conv2D(64, (3, 3), activation='relu'),

    # Classifier head
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])

model.summary()
```

### Compiling and Training

```python
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=64,
    validation_split=0.1,
    verbose=1
)

# Evaluate
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f"Test accuracy: {test_acc:.4f}")
```

---

## CIFAR-10: Color Image Classification

```python
# Load CIFAR-10 (32x32 color images, 10 classes)
(X_train, y_train), (X_test, y_test) = keras.datasets.cifar10.load_data()

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# Normalize
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# Build a deeper CNN
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(32, 32, 3)),
    layers.BatchNormalization(),
    layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.25),

    layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
    layers.BatchNormalization(),
    layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.25),

    layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.25),

    layers.Flatten(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

# Train
history = model.fit(X_train, y_train, epochs=30, batch_size=64,
                    validation_split=0.1, verbose=1)
```

---

## Data Augmentation

Artificially expand your training set with transformations:

```python
data_augmentation = keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),
    layers.RandomTranslation(0.1, 0.1),
])

# Use in the model
model = keras.Sequential([
    data_augmentation,
    layers.Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(32, 32, 3)),
    # ... rest of the model
])
```

Data augmentation helps prevent overfitting and improves generalization, especially
when your dataset is small.

---

## Transfer Learning

Use a pre-trained model (trained on millions of images) and adapt it to your task.
This is the most practical approach for real-world image classification.

```python
# Use a pre-trained model (MobileNetV2) as feature extractor
base_model = keras.applications.MobileNetV2(
    weights='imagenet',
    include_top=False,          # Remove the classification head
    input_shape=(224, 224, 3)
)

# Freeze the base model weights
base_model.trainable = False

# Add custom classifier on top
model = keras.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()
```

### Fine-Tuning

After training the classifier head, unfreeze some of the base model layers for fine-tuning:

```python
# Unfreeze the last 20 layers of the base model
base_model.trainable = True
for layer in base_model.layers[:-20]:
    layer.trainable = False

# Recompile with a lower learning rate
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-5),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Continue training
model.fit(X_train, y_train, epochs=5, validation_split=0.1)
```

---

## Visualizing What CNNs Learn

### Visualize Filters

```python
# Get the first conv layer's filters
filters, biases = model.layers[0].get_weights()
print(f"Filter shape: {filters.shape}")

# Plot first 16 filters
fig, axes = plt.subplots(4, 4, figsize=(8, 8))
for i, ax in enumerate(axes.flat):
    if i < filters.shape[-1]:
        ax.imshow(filters[:, :, 0, i], cmap='gray')
    ax.axis('off')
plt.suptitle('Conv Layer 1 Filters')
plt.show()
```

### Visualize Feature Maps

```python
# Create a model that outputs intermediate layer activations
layer_outputs = [layer.output for layer in model.layers[:6]]
activation_model = keras.Model(inputs=model.input, outputs=layer_outputs)

# Get activations for a sample image
activations = activation_model.predict(X_test[:1])

# Plot feature maps from the first conv layer
first_layer_activation = activations[0]
fig, axes = plt.subplots(4, 8, figsize=(16, 8))
for i, ax in enumerate(axes.flat):
    if i < first_layer_activation.shape[-1]:
        ax.imshow(first_layer_activation[0, :, :, i], cmap='viridis')
    ax.axis('off')
plt.suptitle('Feature Maps - Layer 1')
plt.show()
```

---

## Common CNN Architectures

| Architecture | Year | Key Innovation |
|-------------|------|----------------|
| LeNet-5 | 1998 | First practical CNN |
| AlexNet | 2012 | Deep CNN, ReLU, dropout |
| VGG | 2014 | Very deep with small 3x3 filters |
| GoogLeNet/Inception | 2014 | Inception modules (parallel filters) |
| ResNet | 2015 | Skip connections (residual learning) |
| MobileNet | 2017 | Depthwise separable convolutions (efficiency) |
| EfficientNet | 2019 | Compound scaling |

All available in `keras.applications`.

---

## Callbacks for Better Training

```python
callbacks = [
    # Stop when validation loss stops improving
    keras.callbacks.EarlyStopping(monitor='val_loss', patience=5,
                                  restore_best_weights=True),
    # Reduce learning rate when plateau detected
    keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.5,
                                      patience=3, min_lr=1e-7),
    # Save the best model
    keras.callbacks.ModelCheckpoint('best_model.keras',
                                    monitor='val_accuracy',
                                    save_best_only=True),
]

model.fit(X_train, y_train, epochs=50, validation_split=0.1,
          callbacks=callbacks, batch_size=64)
```

---

## Key Takeaways

1. CNNs use convolutional layers to detect spatial patterns with shared weights.
2. The typical architecture: Conv -> ReLU -> Pool (repeated) -> Flatten -> Dense.
3. Batch normalization and dropout are essential for training deeper CNNs.
4. Data augmentation artificially expands training data and improves generalization.
5. Transfer learning from pre-trained models is the standard approach for real projects.
6. Fine-tuning unfreezes later layers of a pre-trained model for task-specific adaptation.
7. Callbacks (EarlyStopping, ReduceLROnPlateau) automate training management.
