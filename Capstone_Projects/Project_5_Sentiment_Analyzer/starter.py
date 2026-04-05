"""
Capstone Project 5: Movie Review Sentiment Analyzer
=====================================================
NLP-based binary sentiment classification on the IMDB dataset.

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
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    confusion_matrix, classification_report, f1_score, accuracy_score,
)

FIGURES_DIR = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)

# Hyperparameters
VOCAB_SIZE = 10000       # Keep top 10,000 words
MAX_LEN = 250            # Pad/truncate reviews to this length
EMBEDDING_DIM = 128      # Dimension of the embedding vectors
BATCH_SIZE = 64
EPOCHS = 20
VALIDATION_SPLIT = 0.15
RANDOM_SEED = 42


# ---------------------------------------------------------------------------
# Step 1: Load and Explore
# ---------------------------------------------------------------------------
def load_data():
    """Load the IMDB dataset.

    Returns:
        tuple: (X_train, y_train, X_test, y_test) as integer-encoded sequences.
    """
    (X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=VOCAB_SIZE)
    print(f"Training samples: {len(X_train)}")
    print(f"Test samples    : {len(X_test)}")
    print(f"Positive / Negative (train): {sum(y_train)} / {len(y_train) - sum(y_train)}")
    return X_train, y_train, X_test, y_test


def get_word_index():
    """Load and augment the IMDB word index for decoding reviews.

    Returns:
        tuple: (word_index, reverse_index)
    """
    word_index = imdb.get_word_index()
    # Offset indices by 3 to account for special tokens
    word_index = {k: v + 3 for k, v in word_index.items()}
    word_index["<PAD>"] = 0
    word_index["<START>"] = 1
    word_index["<UNK>"] = 2
    word_index["<UNUSED>"] = 3
    reverse_index = {v: k for k, v in word_index.items()}
    return word_index, reverse_index


def decode_review(encoded_review, reverse_index):
    """Convert an integer-encoded review back to text.

    Args:
        encoded_review (list[int]): Integer-encoded review.
        reverse_index (dict): Mapping from int -> word.

    Returns:
        str: Decoded review text.
    """
    return " ".join(reverse_index.get(i, "?") for i in encoded_review)


def plot_review_length_distribution(X_train, save=True):
    """Histogram of review lengths."""
    lengths = [len(review) for review in X_train]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(lengths, bins=50, edgecolor="black", alpha=0.7)
    ax.axvline(x=MAX_LEN, color="red", linestyle="--", label=f"MAX_LEN = {MAX_LEN}")
    ax.set_xlabel("Review Length (words)")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Review Lengths")
    ax.legend()
    plt.tight_layout()
    if save:
        fig.savefig(os.path.join(FIGURES_DIR, "review_lengths.png"), dpi=150)
    plt.show()
    print(f"Mean length: {np.mean(lengths):.0f}, Median: {np.median(lengths):.0f}")


# ---------------------------------------------------------------------------
# Step 2: Preprocess Sequences
# ---------------------------------------------------------------------------
def preprocess_sequences(X_train, y_train, X_test, y_test):
    """Pad sequences and create a validation split.

    Returns:
        tuple: (X_train, y_train, X_val, y_val, X_test, y_test)
    """
    # TODO: Pad/truncate sequences to MAX_LEN using pad_sequences.
    # TODO: Split a validation set from training data.
    pass


# ---------------------------------------------------------------------------
# Step 3: Model Architectures
# ---------------------------------------------------------------------------
def build_lstm_model():
    """Architecture A: Bidirectional LSTM.

    Returns:
        keras.Model: Compiled model.
    """
    model = keras.Sequential([
        layers.Embedding(VOCAB_SIZE, EMBEDDING_DIM, input_length=MAX_LEN),
        layers.Bidirectional(layers.LSTM(64, return_sequences=True)),
        layers.Bidirectional(layers.LSTM(32)),
        layers.Dropout(0.5),
        layers.Dense(64, activation="relu"),
        layers.Dropout(0.3),
        layers.Dense(1, activation="sigmoid"),
    ])

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )
    model.summary()
    return model


def build_cnn_model():
    """Architecture B: 1D CNN.

    Returns:
        keras.Model: Compiled model.
    """
    model = keras.Sequential([
        layers.Embedding(VOCAB_SIZE, EMBEDDING_DIM, input_length=MAX_LEN),
        layers.Conv1D(128, 5, activation="relu"),
        layers.GlobalMaxPooling1D(),
        layers.Dense(64, activation="relu"),
        layers.Dropout(0.5),
        layers.Dense(1, activation="sigmoid"),
    ])

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )
    model.summary()
    return model


def build_hybrid_model():
    """Architecture C: CNN + LSTM Hybrid.

    Returns:
        keras.Model: Compiled model.
    """
    model = keras.Sequential([
        layers.Embedding(VOCAB_SIZE, EMBEDDING_DIM, input_length=MAX_LEN),
        layers.Conv1D(64, 5, activation="relu"),
        layers.MaxPooling1D(pool_size=4),
        layers.LSTM(64),
        layers.Dense(1, activation="sigmoid"),
    ])

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )
    model.summary()
    return model


# ---------------------------------------------------------------------------
# Step 4: Train
# ---------------------------------------------------------------------------
def get_callbacks():
    """Return training callbacks."""
    return [
        callbacks.EarlyStopping(
            monitor="val_loss", patience=3, restore_best_weights=True
        ),
        callbacks.ReduceLROnPlateau(
            monitor="val_loss", factor=0.5, patience=2, verbose=1
        ),
    ]


def train_model(model, X_train, y_train, X_val, y_val, model_name="model"):
    """Train a model and return the history.

    Args:
        model (keras.Model): Compiled model.
        X_train, y_train: Training data.
        X_val, y_val: Validation data.
        model_name (str): Label for logging.

    Returns:
        keras.callbacks.History: Training history.
    """
    print(f"\n--- Training {model_name} ---")
    # TODO: Fit the model with get_callbacks(), return history.
    pass


# ---------------------------------------------------------------------------
# Step 5: Evaluate
# ---------------------------------------------------------------------------
def plot_training_history(history, model_name="Model", save=True):
    """Plot accuracy and loss curves."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # TODO: Plot training/validation accuracy on ax1.
    ax1.set_title(f"{model_name} -- Accuracy")
    ax1.set_xlabel("Epoch")
    ax1.set_ylabel("Accuracy")
    ax1.legend()

    # TODO: Plot training/validation loss on ax2.
    ax2.set_title(f"{model_name} -- Loss")
    ax2.set_xlabel("Epoch")
    ax2.set_ylabel("Loss")
    ax2.legend()

    plt.tight_layout()
    if save:
        safe_name = model_name.lower().replace(" ", "_")
        fig.savefig(os.path.join(FIGURES_DIR, f"history_{safe_name}.png"), dpi=150)
    plt.show()


def evaluate_model(model, X_test, y_test, model_name="Model"):
    """Evaluate a model on the test set.

    Args:
        model: Trained model.
        X_test, y_test: Test data.
        model_name (str): Label for output.

    Returns:
        dict: Metrics dictionary.
    """
    loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
    y_pred_probs = model.predict(X_test).flatten()
    y_pred = (y_pred_probs >= 0.5).astype(int)

    f1 = f1_score(y_test, y_pred)
    print(f"\n{model_name} -- Test Accuracy: {accuracy:.4f}, F1: {f1:.4f}")
    print(classification_report(y_test, y_pred, target_names=["Negative", "Positive"]))

    return {"Model": model_name, "Accuracy": accuracy, "F1": f1, "Loss": loss}


def plot_confusion_matrix(model, X_test, y_test, model_name="Model", save=True):
    """Confusion matrix heatmap."""
    y_pred = (model.predict(X_test).flatten() >= 0.5).astype(int)
    cm = confusion_matrix(y_test, y_pred)

    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax,
                xticklabels=["Negative", "Positive"],
                yticklabels=["Negative", "Positive"])
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title(f"Confusion Matrix -- {model_name}")
    plt.tight_layout()
    if save:
        safe_name = model_name.lower().replace(" ", "_")
        fig.savefig(os.path.join(FIGURES_DIR, f"cm_{safe_name}.png"), dpi=150)
    plt.show()


def show_sample_predictions(model, X_test, y_test, reverse_index,
                            n_correct=5, n_wrong=5):
    """Display correctly and incorrectly classified reviews.

    Args:
        model: Trained model.
        X_test: Padded test sequences.
        y_test: True labels.
        reverse_index: Int-to-word mapping.
        n_correct: Number of correct predictions to show.
        n_wrong: Number of wrong predictions to show.
    """
    y_pred_probs = model.predict(X_test).flatten()
    y_pred = (y_pred_probs >= 0.5).astype(int)

    correct_idx = np.where(y_pred == y_test)[0]
    wrong_idx = np.where(y_pred != y_test)[0]

    labels = {0: "Negative", 1: "Positive"}

    print("\n=== Correctly Classified ===")
    for idx in np.random.choice(correct_idx, min(n_correct, len(correct_idx)), replace=False):
        review = decode_review(X_test[idx], reverse_index)
        print(f"  True: {labels[y_test[idx]]}, Pred: {labels[y_pred[idx]]} "
              f"(conf: {y_pred_probs[idx]:.3f})")
        print(f"  Review: {review[:200]}...\n")

    print("=== Misclassified ===")
    for idx in np.random.choice(wrong_idx, min(n_wrong, len(wrong_idx)), replace=False):
        review = decode_review(X_test[idx], reverse_index)
        print(f"  True: {labels[y_test[idx]]}, Pred: {labels[y_pred[idx]]} "
              f"(conf: {y_pred_probs[idx]:.3f})")
        print(f"  Review: {review[:200]}...\n")


# ---------------------------------------------------------------------------
# Step 6: Predict on Custom Text
# ---------------------------------------------------------------------------
def predict_sentiment(text, model, word_index, max_len=MAX_LEN):
    """Predict sentiment for a raw review string.

    Args:
        text (str): Raw review text.
        model: Trained Keras model.
        word_index (dict): Word-to-integer mapping.
        max_len (int): Sequence length for padding.

    Returns:
        tuple: (label, confidence)
    """
    # TODO: Lowercase the text, split into words.
    # TODO: Encode each word using word_index (use 2 for unknown words).
    # TODO: Pad the sequence to max_len.
    # TODO: Predict with model, return label and confidence.
    pass


# ---------------------------------------------------------------------------
# Main Pipeline
# ---------------------------------------------------------------------------
def main():
    """Run the full sentiment analysis pipeline."""
    np.random.seed(RANDOM_SEED)
    tf.random.set_seed(RANDOM_SEED)

    print("Step 1: Loading IMDB dataset...")
    X_train_raw, y_train_raw, X_test_raw, y_test_raw = load_data()
    word_index, reverse_index = get_word_index()

    # Decode and display a sample review
    print("\nSample review (decoded):")
    print(decode_review(X_train_raw[0], reverse_index)[:300], "...")
    print(f"Label: {'Positive' if y_train_raw[0] == 1 else 'Negative'}\n")

    plot_review_length_distribution(X_train_raw)

    print("Step 2: Preprocessing sequences...")
    X_train, y_train, X_val, y_val, X_test, y_test = preprocess_sequences(
        X_train_raw, y_train_raw, X_test_raw, y_test_raw
    )

    # --- Train and evaluate multiple architectures ---
    architectures = {
        "Bidirectional LSTM": build_lstm_model,
        "1D CNN": build_cnn_model,
        "CNN-LSTM Hybrid": build_hybrid_model,
    }

    all_results = []

    for name, build_fn in architectures.items():
        print(f"\nStep 3: Building {name}...")
        model = build_fn()

        print(f"Step 4: Training {name}...")
        history = train_model(model, X_train, y_train, X_val, y_val, model_name=name)

        print(f"Step 5: Evaluating {name}...")
        plot_training_history(history, model_name=name)
        metrics = evaluate_model(model, X_test, y_test, model_name=name)
        all_results.append(metrics)
        plot_confusion_matrix(model, X_test, y_test, model_name=name)

    # Model comparison table
    import pandas as pd
    results_df = pd.DataFrame(all_results)
    print("\n=== Model Comparison ===")
    print(results_df.to_string(index=False))

    # Use the best model for demos
    best_idx = results_df["F1"].idxmax()
    best_name = results_df.loc[best_idx, "Model"]
    print(f"\nBest model: {best_name}")

    # Rebuild and retrain the best model (or keep a reference)
    best_model = list(architectures.values())[best_idx]()
    # TODO: Retrain or load the best model.

    print("\nStep 6: Sample predictions on custom reviews...")
    sample_reviews = [
        "This movie was absolutely fantastic! Great acting and a gripping story.",
        "Terrible film. The plot made no sense and the acting was wooden.",
        "It was okay. Not great, not terrible. A decent way to spend an evening.",
        "One of the worst movies I have ever seen. Complete waste of time.",
        "A masterpiece of modern cinema. Truly unforgettable experience.",
    ]
    for review in sample_reviews:
        label, confidence = predict_sentiment(review, best_model, word_index)
        print(f"  [{label:8s} {confidence:.1%}] {review[:80]}")

    print("\nPipeline complete. Figures saved to:", FIGURES_DIR)


if __name__ == "__main__":
    main()
