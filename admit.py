import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow
from tensorflow import keras
from tensorflow.keras import layers

df = pd.read_csv('')

df.head()

df.describe()

df.count()

df.dtypes

for i in df.columns:
    sns.displot(df[i])
    plt.show()

plt.figure(figsize=(20,10))
sns.heatmap(df.corr(), annot=True)
plt.show()

df.head()

x = df.drop('Chance of Admit ', axis=1)
y = df['Chance of Admit ']

x.head()

y.head()

model = keras.Sequential()
model.add(layers.Dense(7,activation='relu'))
model.add(layers.Dense(2,activation='relu'))
model.add(layers.Dense(1))

model.compile(loss='mean_squared_error',optimizer='adam', metrics=['mean_squared_error'])
hist = model.fit(x,y,validation_split=0.2,batch_size=32,epochs=150)

model.summary()

plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Train', 'Test'],loc='upper right')
plt.show()

x_pred = np.array([[340,120,5,5,5,10,0]])
x_pred = np.array(x_pred,dtype=np.float64)
y_pred = model.predict(x_pred)
print('x = ', x_pred[0], '\nChance of Admit = ', y_pred[0][0]*100,'%')
