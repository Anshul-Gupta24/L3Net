'''
Creates the train and test csv dataset files
'''


import numpy as np
import pandas as pd
import sklearn.model_selection
import csv
import os


def get_corr(csvfile):

	cfile = open(csvfile, 'a')

	wr = csv.writer(cfile, delimiter=' ', quoting=csv.QUOTE_ALL)
	wr.writerow([' ', 'image', 'spectrogram', 'label'])

	for i, img in enumerate(os.listdir('./image')):
		
		spec = 'plt'+img[3:]
		data = [i, img, spec, str(1)]
		#print(data)
		wr.writerow(data)



def get_noncorr(csvfile):

	cfile = open(csvfile, 'a')

	wr = csv.writer(cfile, delimiter=' ', quoting=csv.QUOTE_ALL)

	plots = os.listdir('./spectrogram')
	num_spec = len(plots)

	for i, img in enumerate(os.listdir('./image')):

		spec_ind = np.random.randint(num_spec)
		spec = plots[spec_ind]
		
		# To make sure visual-audio pair is not from the same video
		while(spec[3:-6]==img[3:-6]):
			spec_ind = np.random.randint(num_spec)
			spec = plots[spec_ind]

		data = [i, img, spec, str(0)]
		#print(data)
		wr.writerow(data)


def get_train_test(csvfile):

	train_df = pd.DataFrame()	
	test_df = pd.DataFrame()	

	
	df = pd.read_csv(csvfile, delimiter=' ')

	imgs = df['image'].values
	specs = df['spectrogram'].values
	lbls = df['label'].values

	train_images, test_images, train_spectrograms, test_spectrograms, train_labels, test_labels = sklearn.model_selection.train_test_split(imgs, specs, lbls, test_size=0.2)

	train_df['image'] = train_images
	train_df['spectrogram'] = train_spectrograms
	train_df['label'] = train_labels

	test_df['image'] = test_images
	test_df['spectrogram'] = test_spectrograms
	test_df['label'] = test_labels

	train_df.to_csv('train_dataset.csv', sep=' ')
	test_df.to_csv('test_dataset.csv', sep=' ')


if __name__=='__main__':

	print()
	print('Creating Dataset')
	print()

	exists = os.path.isfile('dataset.csv')
	if exists:
		print('Removing old csv file')
		print()
		os.rename('dataset.csv','./removed/dataset.csv')
	
	get_corr('dataset.csv')
	get_noncorr('dataset.csv')
	get_train_test('dataset.csv')
