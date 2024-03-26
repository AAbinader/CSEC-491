import time
import pandas as pd
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, Dropout
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer

"""Neural Network"""

# Function that runs the neural net model using the supplied data
def neural_net_model(data, epochs, display_time=False):

    start_time = time.time()
    df = pd.read_csv(data)
    df['sentiment'] = df['sentiment'].apply(lambda x: [x])

    texts = df['reviews'].tolist()
    labels = df['sentiment'].tolist()

    default_filters = '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
    custom_filters = default_filters.replace('!', '')

    tokenizer = Tokenizer(num_words=5000, lower=False, filters=custom_filters)
    tokenizer.fit_on_texts(texts)
    sequences = tokenizer.texts_to_sequences(texts)
    data = pad_sequences(sequences, maxlen=100)

    mlb = MultiLabelBinarizer()
    encoded_labels = mlb.fit_transform(labels)
    x_train, x_test, y_train, y_test = train_test_split(data, encoded_labels, test_size=0.2)

    model = Sequential()
    model.add(Embedding(input_dim=5000, output_dim=128))
    model.add(LSTM(128, return_sequences=False))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(mlb.classes_), activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(x_train, y_train, batch_size=32, epochs=epochs, validation_data=(x_test, y_test))
    end_time = time.time()

    if display_time:
        total_time = end_time - start_time
        print("NN Model Time: %fs" % (total_time))

    loss, accuracy = model.evaluate(x_test, y_test)
    return accuracy

# Neural Net takes about 2 minutes to run

og_accuracy = neural_net_model('../data/reviews_labeled.csv', 6)
short_accuracy = neural_net_model('../data/reviews_relabeled_short.csv', 6)
long_accuracy = neural_net_model('../data/reviews_relabeled.csv', 10)

with open('neuralnet_output.txt', 'w') as file:

    file.write("OG Data\n")
    file.write("Accuracy: " + str(round(og_accuracy*100, 2)) + "%\n")
    
    file.write("\n")
    file.write("New Data (Short)\n")
    file.write("Accuracy: " + str(round(short_accuracy*100, 2)) + "%\n")

    file.write("\n")
    file.write("New Data (Long)\n")
    file.write("Accuracy: " + str(round(long_accuracy*100, 2)) + "%\n")
