from sklearn.datasets import make_classification
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense,activations
X,y=make_classification(n_samples=1000, n_features=20,n_informative=15,n_redundant=5,n_classes=3,random_state=42)

num_classes=3
y=to_categorical(y,num_classes)
model=Sequential()
model.add(Dense(units=32,input_dim=20))
model.add(activations('relu'))
model.add(Dense(units=3))
model.add(activations('softmax'))
model.compile(loss='categorical_crossentorpy',optimizer='adam',metrics=['accuracy'])
model.fit(X,y,epochs=5,batch_size=32)
loss,accuracy=model.evaluate(X,y)
print('Loss',loss)
print('Accuracy',accuracy)
