import numpy as np
import time
import cv2

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Reshape
from keras.layers import Conv2D, Conv2DTranspose, UpSampling2D
from keras.layers import LeakyReLU, Dropout
from keras.layers import Input,Conv2D,MaxPooling2D,UpSampling2D, Concatenate
from keras.models import Model
from keras.optimizers import RMSprop
from keras.layers import BatchNormalization
from keras.optimizers import Adam, RMSprop


def autoencoder():
    x, y, c = 64, 64, 3
    input_img = Input(shape=(x, y, c))
    input_age = Input(shape=(6,))

    depth = 64
    dropout = 0.4
    alpha = 0.2

    conv1 = Conv2D(depth, (3, 3), padding='same')(input_img)
    relu1 = LeakyReLU(alpha=alpha)(conv1)
    dropout1 = Dropout(dropout)(relu1)
    pool1 = MaxPooling2D(pool_size=(2, 2))(dropout1)

    conv2 = Conv2D(depth*2, (3, 3), padding='same')(pool1)
    relu2 = LeakyReLU(alpha=alpha)(conv2)
    dropout2 = Dropout(dropout)(relu2)
    pool2 = MaxPooling2D(pool_size=(2, 2))(dropout2)

    conv3 = Conv2D(depth*4, (3, 3), padding='same')(pool2)
    relu3 = LeakyReLU(alpha=alpha)(conv3)
    dropout3 = Dropout(dropout)(relu3)
    pool3 = MaxPooling2D(pool_size=(2, 2))(dropout3)

    conv4 = Conv2D(depth*8, (3, 3), padding='same')(pool3)
    relu4 = LeakyReLU(alpha=alpha)(conv4)
    dropout4 = Dropout(dropout)(relu4)
    pool4 = MaxPooling2D(pool_size=(2, 2))(dropout4)

    flatten = Flatten()(pool4)

    dense1 = Dense(100)(flatten)

    concat = Concatenate(axis=-1)([dense1, input_age])

    dense2 = Dense(8192)(concat)

    reshape = Reshape((4, 4, 512))(dense2)

    conv5 = Conv2D(depth*8, (3, 3), padding='same')(reshape)
    relu5 = LeakyReLU(alpha=alpha)(conv5)
    dropout5 = Dropout(dropout)(relu5)
    up1 = UpSampling2D((2,2))(dropout5)


    conv6 = Conv2D(depth*4, (3, 3), padding='same')(up1)
    relu6 = LeakyReLU(alpha=alpha)(conv6)
    dropout6 = Dropout(dropout)(relu6)
    up2 = UpSampling2D((2,2))(dropout6)

    conv7 = Conv2D(depth*2, (3, 3), padding='same')(up2)
    relu7 = LeakyReLU(alpha=alpha)(conv7)
    dropout7 = Dropout(dropout)(relu7)
    up3 = UpSampling2D((2,2))(dropout7)
    
    conv8 = Conv2D(depth, (3, 3), padding='same')(up3)
    relu8 = LeakyReLU(alpha=alpha)(conv8)
    dropout8 = Dropout(dropout)(relu8)
    up4 = UpSampling2D((2,2))(dropout8)

    decoded = Conv2D(3, (3,3), activation='sigmoid', padding='same')(up4)
    
    model = Model(inputs=[input_img, input_age], outputs=[decoded])
    model.compile(loss='mean_squared_error', optimizer=RMSprop())
    model.summary()

    return model

def test(model, test_image, test_age):
    print(test_image.shape, test_age.shape)
    pred = model.predict([test_image, test_age])
    print(pred)
    cv2.imwrite('output.jpg', pred[0])


batch_size = 32
model = autoencoder()

test(model, np.expand_dims(cv2.imread('the_bean.jpg'), axis=0), np.array([[0, 0, 0, 0, 1, 0]]))


