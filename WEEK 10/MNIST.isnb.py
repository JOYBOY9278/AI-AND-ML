import matplotlib.pyplot as plt
import tensorflow as tf
from keras.utils import to_categorical
from keras.datasets import fashion_mnist


layers=tf.keras.layers 
(x_train,x_test),(y_train,y_test)=fashion.mnist.load_data()
y_train=to_categorical(y_train,num_classes=10)
y_test=to_categorical(y_test,num_classes=10)


print('x_train:'+str(x_train))
print('y_train:'+str(y_train))
print('x_test:'+str(x_test))
print('x_test:'+str(y_test))

plt.figure(figsize=(18,10))
for i in range (1,15):
    plt.subplot(5,5,i)
    plt.imshow(x_train[i],cmap=plt.get_cmap('gray'))
plt.show()

model=tf.keras.Sequential()
model.add(layers.Flatten())
model.add(layers.Dense(64,activation='relu'))
model.add(layers.Dense(64,activation='relu'))
model.add(layers.Dense(64,activation='relu'))
model.add(layers.Dense(64,activation='relu'))
model.add(layers.Dense(10,activation='softmax'))

model.compile(optimizer='adam',loss='catogorical_crossentropy',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=10)

loss,accuracy=model.evaluate(x_test,y_test)

print('\n\nTest loss',loss)
print('Test accracy',accuracy)