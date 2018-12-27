import numpy as np
import pandas as pd
import os
import cv2


def get(root, csvfile):

	df = pd.read_csv(root+'/'+csvfile, delimiter=' ')

	imgs = df['image'].values
	specs = df['spectrogram'].values
	lbls = df['label'].values

	im_dic = {}
	for img in os.listdir(root+'/image'):
		
		im_dic[img] = cv2.imread(root+'/image/'+img)

		
	spec_dic = {}
	for spec in os.listdir(root+'/spectrogram'):
		
		spec_dic[spec] = np.expand_dims(cv2.imread(root+'/spectrogram/'+spec, 0), 2)


	images = np.zeros((len(imgs), 224, 224, 3))
	spectrograms = np.zeros((len(specs), 199, 257, 1))
	labels = np.zeros((len(lbls), 2))
	
	
	for i, img in enumerate(imgs):

		images[i] = im_dic[img] / 255.0

	for i, spec in enumerate(specs):

		spectrograms[i] = spec_dic[spec] / 255.0

	for i, lbl in enumerate(lbls):
	
		labels[i][lbl] = 1

	
	
	return images, spectrograms, labels


if __name__=='__main__':

	a,b,c = get('./dataset','dataset.csv')
