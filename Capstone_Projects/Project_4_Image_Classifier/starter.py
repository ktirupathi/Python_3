"""
Capstone Project 4: Image Classifier Using CIFAR-10
=====================================================
CNN-based image classification with TensorFlow/Keras.

Usage:
    python starter.py
"""

import os

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, callbacks
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, classification_report

FIGURES_DIR = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)

CLASS_NAMES = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck",
]

BATCH_SIZE = 64
EPOCHS = 100
VALIDATION_SPLIT = 0.1
RANDOM_SEED = 42


# ---------------------------------------------------------------------------
# Step 1: Load and Visualize
# ---------------------------------------------------------------------------
def load_data():
    """Load CIFAR-10 dataset.

    Returns:
        tuple: (X_train, y_train, X_test, y_test) as raw NumPy arrays.
    """
    (X_train, y_train), (X_test, y_test) = cifar10.load_data()
    print(f"Training set : {X_train.shape}, Labels: {y_train.shape}")
    print(f"Test set     : {X_test.shape}, Labels: {y_test.shape}")
    return X_train, y_train, X_test, y_test


def visualize_samples(X, y, n=25, save=True):
    """Display a grid of sample images with labels.

    Args:
        X (np.ndarray): Image array.
        y (np.ndarray): Label array.
        n (int): Number of samples to display.
    """
    cols = 5
    rows = n // cols
    fig, axes = plt.subplots(rows, cols, figsize=(12, 10))

    indices = np.random.choice(len(X), n, replace=False)
    for i, ax in enumerate(axes.flat):
        ax.imshow(X[indices[i]])
        ax.set_title(CLASS_NAMES[int(y[indices[i]])])
        ax.axis("off")

    fig.suptitle("CIFAR-10 Sample Images", fontsize=14)
    plt.tight_layout()
    if save:
        fig.savefig(os.path.join(FIGURES_DIR, "sample_images.png"), dpi=150)
    plt.show()


# ---------------------------------------------------------------------------
# Step 2: Preprocess
# ---------------------------------------------------------------------------
def preprocess(X_train, y_train, X_test, y_test):
    """Normalize pixels and one-hot encode labels.

    Returns:
        tuple: (X_train, y_train_cat, X_val, y_val_cat, X_test, y_test_cat)
    """
    # TODO: Normalize pixel values to [0, 1].
    # TODO: One-hot encode labels with to_categorical(y, 10).
    # TODO: Split a validation set from training data.
    pass


# ---------------------------------------------------------------------------
# Step 3: Data Augmentation
# ---------------------------------------------------------------------------
def create_data_generator():
    """Build an ImageDataGenerator with augmentation transforms.

    Returns:
        ImageDataGenerator
    """
    datagen = ImageDataGenerator(
        rotation_range=15,
        width_shift_range=0.1,
        height_shift_range=0.1,
        horizontal_flip=True,
    )
    return datagen


def visualize_augmentation(datagen, X_train, idx=0, n=6, save=True):
    """Show original image alongside augmented versions.

    Args:
        datagen (ImageDataGenerator): Fitted generator.
        X_train (np.ndarray): Normalized training images.
        idx (int): Index of the image to augment.
        n (int): Number of augmented copies to show.
    """
    fig, axes = plt.subplots(1, n + 1, figsize=(3 * (n + 1), 3))
    axes[0].imshow(X_train[idx])
    axes[0].set_title("Original")
    axes[0].axis("off")

    # TODO: Generate n augmented versions of X_train[idx] and display them.
    for i in range(1, n + 1):
        axes[i].axis("off")

    fig.suptitle("Data Augmentation Examples", fontsize=14)
    plt.tight_layout()
    if save:
        fig.savefig(os.path.join(FIGURES_DIR, "augmentation_examples.png"), dpi=150)
    plt.show()


# ---------------------------------------------------------------------------
# Step 4: Build the CNN
# ---------------------------------------------------------------------------
def build_model(input_shape=(32, 32, 3), num_classes=10):
    """Construct the CNN architecture.

    Args:
        input_shape (tuple): Shape of input images.
        num_classes (int): Number of output classes.

    Returns:
        keras.Model: Compiled model.
    """
    model = keras.Sequential([
        # --- Block 1 ---
        layers.Conv2D(32, (3, 3), padding="same", activation="relu",
                      input_shape=input_shape),
        layers.BatchNormalization(),
        layers.Conv2D(32, (3, 3), activation="relu"),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.2),

        # --- Block 2 ---
        layers.Conv2D(64, (3, 3), padding="same", activation="relu"),
        layers.BatchNormalization(),
        layers.Conv2D(64, (3, 3), activation="relu"),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.3),

        # --- Block 3 ---
        layers.Conv2D(128, (3, 3), padding="same", activation="relu"),
        layers.BatchNormalization(),
        layers.Conv2D(128, (3, 3), activation="relu"),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.4),

        # --- Classifier Head ---
        layers.Flatten(),
        layers.Dense(256, activation="relu"),
        layers.BatchNormalization(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ])

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )

    model.summary()
    return model


# ---------------------------------------------------------------------------
# Step 5: Train
# ---------------------------------------------------------------------------
def get_callbacks():
    """Return a list of training callbacks.

    Returns:
        list: Keras callbacks.
    """
    return [
        callbacks.EarlyStopping(
            monitor="val_loss", patience=10, restore_best_weights=True
        ),
        callbacks.ReduceLROnPlateau(
            monitor="val_loss", factor=0.5, patience=5, verbose=1
        ),
        callbacks.ModelCheckpoint(
            os.path.join(os.path.dirname(__file__), "best_model.keras"),
            monitor="val_accuracy", save_best_only=True, verbose=1
        ),
    ]


def train_model(model, datagen, X_train, y_train, X_val, y_val):
    """Train the model using the augmented data generator.

    Args:
        model (keras.Model): Compiled model.
        datagen (ImageDataGenerator): Fitted augmentation generator.
        X_train, y_train: Training data.
        X_val, y_val: Validation data.

    Returns:
        keras.callbacks.History: Training history.
    """
    # TODO: Fit the model using datagen.flow() and the callbacks.
    # TODO: Return the history object.
    pass


# ---------------------------------------------------------------------------
# Step 6: Evaluate
# ---------------------------------------------------------------------------
def plot_training_history(history, save=True):
    """Plot accuracy and loss curves over epochs."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # TODO: Plot training and validation accuracy on ax1.
    ax1.set_title("Model Accuracy")
    ax1.set_xlabel("Epoch")
    ax1.set_ylabel("Accuracy")
    ax1.legend()

    # TODO: Plot training and validation loss on ax2.
    ax2.set_title("Model Loss")
    ax2.set_xlabel("Epoch")
    ax2.set_ylabel("Loss")
    ax2.legend()

    plt.tight_layout()
    if save:
        fig.savefig(os.path.join(FIGURES_DIR, "training_history.png"), dpi=150)
    plt.show()


def evaluate_model(model, X_test, y_test, save=True):
    """Evaluate on the test set and generate visualizations.

    Args:
        model (keras.Model): Trained model.
        X_test (np.ndarray): Test images (normalized).
        y_test (np.ndarray): Test labels (one-hot).
    """
    # Overall accuracy
    loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
    print(f"\nTest Loss    : {loss:.4f}")
    print(f"Test Accuracy: {accuracy:.4f}")

    # Predictions
    y_pred_probs = model.predict(X_test)
    y_pred = np.argmax(y_pred_probs, axis=1)
    y_true = np.argmax(y_test, axis=1)

    # Classification report
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred, target_names=CLASS_NAMES))

    # Confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax,
                xticklabels=CLASS_NAMES, yticklabels=CLASS_NAMES)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("True")
    ax.set_title("Confusion Matrix")
    plt.tight_layout()
    if save:
        fig.savefig(os.path.join(FIGURES_DIR, "confusion_matrix.png"), dpi=150)
    plt.show()


def show_misclassified(model, X_test, y_test, n=16, save=True):
    """Display a grid of misclassified images.

    Args:
        model: Trained model.
        X_test: Normalized test images.
        y_test: One-hot test labels.
        n: Number of misclassified images to show.
    """
    y_pred = np.argmax(model.predict(X_test), axis=1)
    y_true = np.argmax(y_test, axis=1)
    misclassified_idx = np.where(y_pred != y_true)[0]

    # TODO: Randomly sample n indices from misclassified_idx.
    # TODO: Display images in a grid with "True: X / Pred: Y" titles.
    pass


# ---------------------------------------------------------------------------
# Main Pipeline
# ---------------------------------------------------------------------------
def main():
    """Run the full image classification pipeline."""
    np.random.seed(RANDOM_SEED)
    tf.random.set_seed(RANDOM_SEED)

    print("Step 1: Loading CIFAR-10...")
    X_train_raw, y_train_raw, X_test_raw, y_test_raw = load_data()
    visualize_samples(X_train_raw, y_train_raw)

    print("Step 2: Preprocessing...")
    X_train, y_train, X_val, y_val, X_test, y_test = preprocess(
        X_train_raw, y_train_raw, X_test_raw, y_test_raw
    )

    print("Step 3: Setting up data augmentation...")
    datagen = create_data_generator()
    datagen.fit(X_train)
    visualize_augmentation(datagen, X_train)

    print("Step 4: Building CNN...")
    model = build_model()

    print("Step 5: Training...")
    history = train_model(model, datagen, X_train, y_train, X_val, y_val)

    print("Step 6: Evaluating...")
    plot_training_history(history)
    evaluate_model(model, X_test, y_test)
    show_misclassified(model, X_test, y_test)

    print("Step 7: Saving model...")
    model.save(os.path.join(os.path.dirname(__file__), "cifar10_classifier.keras"))
    print("Done! Figures saved to:", FIGURES_DIR)


if __name__ == "__main__":
    main()
