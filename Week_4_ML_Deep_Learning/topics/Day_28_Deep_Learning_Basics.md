# Day 28: Deep Learning -- Neural Network Basics, TensorFlow/Keras Intro

## What is Deep Learning?

Deep learning is a subset of machine learning that uses **artificial neural networks**
with multiple layers (hence "deep") to learn complex patterns from data. It excels at
tasks like image recognition, natural language processing, and speech recognition where
traditional ML methods struggle.

### When to Use Deep Learning

| Use Deep Learning When | Stick with Traditional ML When |
|----------------------|-------------------------------|
| Massive amounts of data | Small datasets |
| Complex patterns (images, text, audio) | Structured/tabular data |
| Compute resources available (GPU) | Need interpretability |
| Feature engineering is hard | Features are well-defined |

---

## The Artificial Neuron (Perceptron)

A single neuron computes:

```
output = activation( w1*x1 + w2*x2 + ... + wn*xn + b )
```

1. **Weighted sum**: Multiply each input by a weight and sum them up.
2. **Bias**: Add a bias term.
3. **Activation function**: Apply a nonlinear function to produce the output.

---

## Activation Functions

Activation functions introduce **nonlinearity**, allowing the network to learn complex patterns.

| Function | Formula | Range | Use Case |
|----------|---------|-------|----------|
| Sigmoid | 1/(1+e^-z) | (0, 1) | Binary output, output layer |
| Tanh | (e^z - e^-z)/(e^z + e^-z) | (-1, 1) | Hidden layers (centered) |
| ReLU | max(0, z) | [0, inf) | Hidden layers (most common) |
| Leaky ReLU | max(0.01z, z) | (-inf, inf) | Hidden layers (fixes dying ReLU) |
| Softmax | e^zi / sum(e^zj) | (0, 1) | Multi-class output layer |

```python
import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(-5, 5, 200)

fig, axes = plt.subplots(1, 4, figsize=(16, 3))

axes[0].plot(z, 1/(1+np.exp(-z)))
axes[0].set_title('Sigmoid')

axes[1].plot(z, np.tanh(z))
axes[1].set_title('Tanh')

axes[2].plot(z, np.maximum(0, z))
axes[2].set_title('ReLU')

axes[3].plot(z, np.where(z > 0, z, 0.01*z))
axes[3].set_title('Leaky ReLU')

for ax in axes:
    ax.grid(True)
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)

plt.tight_layout()
plt.show()
```

---

## Neural Network Architecture

A neural network consists of:
- **Input layer**: One neuron per feature
- **Hidden layers**: Where the learning happens (more layers = deeper network)
- **Output layer**: Produces the final prediction

Each layer is **fully connected** (dense) -- every neuron connects to every neuron in
the next layer.

### Forward Pass

Data flows from input through hidden layers to output. Each layer applies:
`output = activation(W @ input + b)`

### Backpropagation

The algorithm for training neural networks:
1. **Forward pass**: Compute predictions.
2. **Compute loss**: Measure how wrong the predictions are.
3. **Backward pass**: Compute gradients of the loss with respect to each weight.
4. **Update weights**: Adjust weights in the direction that reduces loss.

This is done iteratively, one batch of data at a time.

---

## Introduction to TensorFlow and Keras

**TensorFlow** is Google's deep learning framework. **Keras** is its high-level API
that makes building neural networks simple and intuitive.

### Installation

```bash
pip install tensorflow
```

### Building Your First Neural Network

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Define the model
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(10,)),  # Hidden layer 1
    layers.Dense(32, activation='relu'),                      # Hidden layer 2
    layers.Dense(1, activation='sigmoid')                     # Output layer
])

# View architecture
model.summary()
```

### Compiling the Model

```python
model.compile(
    optimizer='adam',                        # Optimization algorithm
    loss='binary_crossentropy',             # Loss function
    metrics=['accuracy']                     # Metrics to track
)
```

**Common choices:**

| Task | Output Activation | Loss Function |
|------|------------------|---------------|
| Binary classification | sigmoid | binary_crossentropy |
| Multi-class classification | softmax | categorical_crossentropy |
| Multi-class (integer labels) | softmax | sparse_categorical_crossentropy |
| Regression | linear (none) | mse |

### Training the Model

```python
history = model.fit(
    X_train, y_train,
    epochs=50,              # Number of passes through the data
    batch_size=32,          # Samples per gradient update
    validation_split=0.2,   # Use 20% for validation
    verbose=1
)
```

### Evaluating and Predicting

```python
# Evaluate on test data
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test loss: {loss:.4f}")
print(f"Test accuracy: {accuracy:.4f}")

# Make predictions
predictions = model.predict(X_test)
```

---

## Complete Example: Binary Classification

```python
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load and prepare data
data = load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build model
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dropout(0.3),       # Regularization: randomly zero 30% of neurons
    layers.Dense(32, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train with early stopping
early_stop = keras.callbacks.EarlyStopping(
    monitor='val_loss', patience=10, restore_best_weights=True
)

history = model.fit(
    X_train, y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stop],
    verbose=0
)

# Evaluate
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test accuracy: {accuracy:.4f}")
```

### Plotting Training History

```python
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

ax1.plot(history.history['loss'], label='Train')
ax1.plot(history.history['val_loss'], label='Validation')
ax1.set_title('Loss')
ax1.set_xlabel('Epoch')
ax1.legend()

ax2.plot(history.history['accuracy'], label='Train')
ax2.plot(history.history['val_accuracy'], label='Validation')
ax2.set_title('Accuracy')
ax2.set_xlabel('Epoch')
ax2.legend()

plt.tight_layout()
plt.show()
```

---

## Regularization Techniques

### 1. Dropout

Randomly sets a fraction of neurons to zero during training:

```python
layers.Dropout(0.5)  # Drop 50% of neurons randomly each batch
```

### 2. L2 Regularization (Weight Decay)

```python
layers.Dense(64, activation='relu',
             kernel_regularizer=keras.regularizers.l2(0.01))
```

### 3. Early Stopping

Stop training when validation loss stops improving (shown above).

### 4. Batch Normalization

Normalizes layer inputs, stabilizes and accelerates training:

```python
model = keras.Sequential([
    layers.Dense(64, input_shape=(30,)),
    layers.BatchNormalization(),
    layers.Activation('relu'),
    layers.Dense(32),
    layers.BatchNormalization(),
    layers.Activation('relu'),
    layers.Dense(1, activation='sigmoid')
])
```

---

## Optimizers

| Optimizer | Description |
|-----------|-------------|
| SGD | Basic stochastic gradient descent |
| SGD + Momentum | Accelerates SGD with momentum |
| RMSprop | Adapts learning rate per parameter |
| Adam | Combines momentum + adaptive rates (most popular) |
| AdamW | Adam with weight decay (preferred for modern models) |

```python
# Custom optimizer with learning rate
optimizer = keras.optimizers.Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
```

---

## Saving and Loading Models

```python
# Save entire model
model.save('my_model.keras')

# Load model
loaded_model = keras.models.load_model('my_model.keras')

# Save only weights
model.save_weights('my_weights.weights.h5')
model.load_weights('my_weights.weights.h5')
```

---

## Key Takeaways

1. Neural networks learn by stacking layers of neurons with nonlinear activations.
2. Backpropagation computes gradients; optimizers like Adam update the weights.
3. Keras provides a simple Sequential API: stack layers, compile, fit, evaluate.
4. Match your output activation and loss function to your task type.
5. Regularization (Dropout, early stopping, L2) prevents overfitting.
6. Always scale your input features before feeding them to a neural network.
7. Monitor both training and validation metrics to detect overfitting.
