#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import numpy as np
from model import LLLNet
import get_data
from keras.callbacks import ModelCheckpoint
import keras
import sklearn.model_selection


if __name__ == '__main__':
	
	model = LLLNet()("train")
	model.compile(optimizer=keras.optimizers.Adam(lr=1e-4, decay=1e-5), 
              loss='categorical_crossentropy',
              metrics=['accuracy'])
	
	
	filepath = "model.h5"
	checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, mode='min', period=1)
	callbacks_list = [checkpoint]


	train_images, train_spectrograms, train_labels = get_data.get('./dataset','train_dataset.csv')

	
	model.fit([train_spectrograms, train_images], train_labels, epochs=5, callbacks=callbacks_list)
	'''

	model = keras.models.load_model('model.h5')

	test_images, test_spectrograms, test_labels = get_data.get('./dataset','test_dataset.csv')

	pred = model.predict([test_spectrograms, test_images])
	
	print(pred)
	'''
	
