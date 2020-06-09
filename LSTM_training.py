import tensorflow as tf
from tensorflow import keras
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras import layers

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

link = "https://s3-us-west-1.amazonaws.com/helen.assignment/sentiment_master.csv"
df = pd.read_csv(link)
df.drop(['Unnamed: 0', 'magnitude'], axis=1, inplace=True)

print("data load finished")
x = df['comments'].values
y = df['sentiment'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=123)

tokenizer = Tokenizer(num_words=100)
tokenizer.fit_on_texts(x)
xtrain= tokenizer.texts_to_sequences(x_train)
xtest= tokenizer.texts_to_sequences(x_test)

maxlen=10
xtrain=pad_sequences(xtrain,padding='post', maxlen=maxlen)
xtest=pad_sequences(xtest,padding='post', maxlen=maxlen)

vocab_size=len(tokenizer.word_index)+1

embedding_dim=50
model=Sequential()
model.add(layers.Embedding(input_dim=vocab_size,
         output_dim=embedding_dim,
         input_length=maxlen))
model.add(layers.LSTM(units=50,return_sequences=True))
model.add(layers.LSTM(units=10))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(8))
model.add(layers.Dense(1, activation="sigmoid"))
model.compile(optimizer="adam", loss="binary_crossentropy", 
     metrics=['accuracy'])
model.summary()

model.fit(xtrain,y_train, epochs=20, batch_size=16, verbose=True)
model.save('my_model')
print ('model saved!')

loss, acc = model.evaluate(xtrain, y_train, verbose=True)
print("Training Accuracy: ", acc)
 
loss, acc = model.evaluate(xtest, y_test, verbose=True)
print("Test Accuracy: ", acc)

ypred=model.predict(xtest)

result=zip(x_test[:10], y_test[:10], ypred[:10])
for i in result:
    print(i)

print('End of script')