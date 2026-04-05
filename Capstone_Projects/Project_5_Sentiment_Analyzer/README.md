# Capstone Project 5: Movie Review Sentiment Analyzer

## Objective

Build a deep learning model that classifies movie reviews as positive or negative using
Natural Language Processing (NLP) techniques. Starting from raw text, you will implement
the full NLP pipeline -- tokenization, text cleaning, sequence padding, word embeddings,
and recurrent/convolutional neural network architectures -- to achieve strong binary
sentiment classification on the IMDB dataset.

---

## Skills Practiced

| Skill | Details |
|---|---|
| Text Preprocessing | Tokenization, stopword removal, stemming/lemmatization |
| Sequence Modeling | Padding, truncation, vocabulary management |
| Word Embeddings | Keras Embedding layer, optional pre-trained GloVe vectors |
| Deep Learning for NLP | LSTM, Bidirectional LSTM, 1D CNN, combined architectures |
| Model Evaluation | Accuracy, F1-Score, confusion matrix, misclassification analysis |

---

## Dataset

**IMDB Movie Reviews** -- Built directly into Keras (no external download required).

```python
from tensorflow.keras.datasets import imdb
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=10000)
```

| Property | Value |
|---|---|
| Training samples | 25,000 |
| Test samples | 25,000 |
| Classes | 2 (positive / negative) |
| Average review length | ~230 words |
| Vocabulary (capped) | 10,000 most frequent words |

Alternatively, for a richer preprocessing experience, download the raw text version:

| Source | URL |
|---|---|
| Keras built-in | `tensorflow.keras.datasets.imdb` |
| Stanford AI Lab | https://ai.stanford.edu/~amaas/data/sentiment/ |
| Kaggle | https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews |

---

## Step-by-Step Instructions

### Step 1 -- Load and Explore
- Load the IMDB dataset using `keras.datasets.imdb.load_data(num_words=10000)`.
- Print shapes and class distribution.
- Decode a few integer-encoded reviews back to text using the word index:
  ```python
  word_index = imdb.get_word_index()
  reverse_index = {v + 3: k for k, v in word_index.items()}
  reverse_index[0] = "<PAD>"
  reverse_index[1] = "<START>"
  reverse_index[2] = "<UNK>"
  ```
- Plot the distribution of review lengths (histogram).

### Step 2 -- Preprocess Sequences
- Choose a maximum sequence length (e.g., `MAX_LEN = 250`).
- Pad shorter reviews and truncate longer ones:
  ```python
  from tensorflow.keras.preprocessing.sequence import pad_sequences
  X_train = pad_sequences(X_train, maxlen=MAX_LEN, padding='post', truncating='post')
  X_test  = pad_sequences(X_test,  maxlen=MAX_LEN, padding='post', truncating='post')
  ```
- Split a validation set (15 %) from the training data.

### Step 3 -- Build Model Architectures

Implement and compare at least two of the following:

#### Architecture A: LSTM-based
```
Input (MAX_LEN,)
  -> Embedding(vocab_size, 128, input_length=MAX_LEN)
  -> Bidirectional(LSTM(64, return_sequences=True))
  -> Bidirectional(LSTM(32))
  -> Dropout(0.5)
  -> Dense(64, relu)
  -> Dropout(0.3)
  -> Dense(1, sigmoid)
```

#### Architecture B: 1D CNN-based
```
Input (MAX_LEN,)
  -> Embedding(vocab_size, 128, input_length=MAX_LEN)
  -> Conv1D(128, 5, activation='relu')
  -> GlobalMaxPooling1D()
  -> Dense(64, relu) -> Dropout(0.5)
  -> Dense(1, sigmoid)
```

#### Architecture C: CNN + LSTM Hybrid
```
Input (MAX_LEN,)
  -> Embedding(vocab_size, 128)
  -> Conv1D(64, 5, activation='relu')
  -> MaxPooling1D(pool_size=4)
  -> LSTM(64)
  -> Dense(1, sigmoid)
```

### Step 4 -- Compile and Train

```python
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy'],
)
```

Use callbacks:
- `EarlyStopping(patience=3, restore_best_weights=True)`
- `ReduceLROnPlateau(factor=0.5, patience=2)`

Train for up to 20 epochs (NLP models typically converge faster than image models).

### Step 5 -- Evaluate
- Plot training/validation accuracy and loss curves.
- Report final test accuracy and F1-score.
- Generate a confusion matrix.
- Display 5 correctly classified and 5 misclassified reviews with their true labels
  and predicted probabilities.

### Step 6 -- Predict on Custom Text
Build a helper function that:
1. Accepts a raw text string.
2. Tokenizes and pads it to match the training format.
3. Returns the predicted sentiment and confidence score.

```python
def predict_sentiment(text, model, word_index, max_len=250):
    """Predict sentiment for a raw review string."""
    # TODO: Tokenize, encode, pad, predict.
    pass

# Example usage:
predict_sentiment("This movie was absolutely fantastic! Great acting.", model, word_index)
```

---

## Expected Deliverables

1. `starter.py` with at least two model architectures, training code, and evaluation.
2. Training history plots (accuracy and loss curves) for each architecture.
3. Model comparison table (test accuracy, F1-score for each architecture).
4. Confusion matrix for the best model.
5. Working `predict_sentiment()` function demonstrated on 5+ custom reviews.

**Target accuracy:** Aim for 87-90 % test accuracy with the LSTM or hybrid architecture.

---

## Bonus Challenges

- Use **pre-trained GloVe embeddings** (100d or 300d) instead of training the embedding layer from scratch. Compare the results.
- Implement an **Attention mechanism** on top of the LSTM to let the model focus on the most sentiment-bearing words.
- Build a **Transformer-based classifier** using multi-head self-attention (mini-BERT style).
- Create a **Gradio** or **Streamlit** web interface where users can type a review and see the predicted sentiment in real time.
- Fine-tune a pre-trained **BERT** model from Hugging Face Transformers on the IMDB dataset and compare with your custom architectures.
- Perform **error analysis** -- categorize the types of reviews the model gets wrong (sarcasm, negation, mixed sentiment) and discuss why.
