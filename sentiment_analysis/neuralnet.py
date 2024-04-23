import time
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, Dropout
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

"""Neural Network"""

# Function that runs the neural net model using the supplied data
def neural_net_model(data, epochs, num_classes):
    start_time = time.time()
    df = pd.read_csv(data)
    df = df.dropna()

    texts = df['reviews'].tolist()
    labels = df['sentiment'].tolist()

    # Adjust filters for tokenizer
    default_filters = '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
    custom_filters = default_filters.replace('!', '')

    tokenizer = Tokenizer(num_words=5000, lower=False, filters=custom_filters)
    tokenizer.fit_on_texts(texts)
    sequences = tokenizer.texts_to_sequences(texts)
    data = pad_sequences(sequences, maxlen=100)

    # Convert string labels to integers
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(labels)
    labels = to_categorical(integer_encoded)

    x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2)

    model = Sequential([
        Embedding(input_dim=5000, output_dim=128),
        LSTM(128, return_sequences=False),
        Dense(64, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')  # Use softmax for multiclass classification
    ])

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(x_train, y_train, batch_size=32, epochs=epochs, validation_data=(x_test, y_test))
    end_time = time.time()

    total_time = end_time - start_time

    # Prediction and Evaluation
    y_pred = model.predict(x_test)
    y_pred_labels = np.argmax(y_pred, axis=1)
    y_test_labels = np.argmax(y_test, axis=1)

    # Generate classification report
    report = classification_report(y_test_labels, y_pred_labels, output_dict=True)
    print(classification_report(y_test_labels, y_pred_labels))

    # Prepare metrics to return
    accuracy = report['accuracy']
    precision = report['weighted avg']['precision']
    recall = report['weighted avg']['recall']
    f1_score = report['weighted avg']['f1-score']

    metrics = {
        'Time': total_time,
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall,
        'F1-Score': f1_score
    }

    return metrics

# Example usage:
og_metrics = neural_net_model('../data/reviews_labeled.csv', 6, 3)
short_metrics = neural_net_model('../data/reviews_relabeled_short.csv', 6, 3)
long_metrics = neural_net_model('../data/reviews_relabeled.csv', 10, 5)

with open('neuralnet_output.txt', 'w') as file:
    file.write(f"OG Data: \n{og_metrics}\n\n")
    file.write(f"Short Data: \n{short_metrics}\n\n")
    file.write(f"Long Data: \n{long_metrics}\n")
