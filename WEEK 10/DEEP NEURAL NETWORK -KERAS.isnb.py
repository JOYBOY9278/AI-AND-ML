import pandas as pd
from seaborn import load_dataset
data=pd.read_csv('diabetes.csv')
x=data.drop("Outcome",axis=1)
y=data["Outcome"]

from keras.model import Sequential
from keras.layers import Dense

model=Sequential()

model.add(Dense(12,input_dim=8,activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(1,activation='sigmoid'))
model=Sequential()

model.add(Dense(12,input_dim=8,activation="relu"))
model.add(Dense(8,activation="sigmoid"))

model.compile(loss="binary_crossentropy",optimizer="adam",metrics=["accuracy"])

model.fit(x,y,epochs=150,batch_size=10)
_accracy=model.evaluate(x,y)
print("model accuracy:%.2f"%(accuracy*100))
prediction=model.predict(x)
rounded=[rounded(x[0])for x in prediction]