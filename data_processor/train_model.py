import os

from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from keras.callbacks import EarlyStopping
from keras import Sequential


train_datagen = ImageDataGenerator(rescale=1. / 255,
                                           shear_range=0.2,
                                           rotation_range=0.2,
                                           width_shift_range=0.2,
                                           height_shift_range=0.2,
                                           horizontal_flip=True,
                                           fill_mode='nearest')

test_datagen = ImageDataGenerator(rescale=1. / 255)
print(os.getcwd())
training_set = train_datagen.flow_from_directory(directory='./data/face-expression-recognition-dataset/images/train',
                                              target_size=(48, 48),
                                              class_mode='categorical',
                                              batch_size=32,
                                              classes=['Angy', 'Disgust', 'Fear',
                                                       'Happy', 'Neutral', 'Sad',
                                                       'Surprise'])

test_set = test_datagen.flow_from_directory(directory='./data/face-expression-recognition-dataset/images/validation',
                                            target_size=(48, 48),
                                            class_mode='categorical',
                                            batch_size=32,
                                            classes=['Angy', 'Disgust', 'Fear',
                                                     'Happy', 'Neutral', 'Sad',
                                                     'Surprise'])

print("Training et test dataset initalized ✅")

classifier = Sequential()
classifier.add(Conv2D(filters=16,
                              kernel_size=(2, 2),
                              padding='valid',
                              input_shape=(48, 48, 3),
                              activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
classifier.add(Conv2D(filters=32,
                              kernel_size=(2, 2),
                              padding='valid',
                              input_shape=(48, 48, 3),
                              activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
classifier.add(Conv2D(filters=64,
                              kernel_size=(2, 2),
                              padding='valid',
                              input_shape=(48, 48, 3),
                              activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
classifier.add(Flatten())
classifier.add(Dense(units=64, activation='relu'))
classifier.add(Dropout(0.5))
classifier.add(Dense(units=7, activation='softmax'))

print("Model initalized ✅")

classifier.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print("model compiled ✅")


earlystop = EarlyStopping(monitor='val_accuracy',
                                  min_delta=0.01,
                                  patience=5,
                                  mode='max',
                                  verbose=1,
                                  restore_best_weights=True)

classifier.fit(training_set, epochs=2, validation_data=test_set, callbacks=[earlystop])
print("model trained ✅")

model_path = "./data/model.h5"
classifier.save(model_path)

print("model saved ✅")

