'''
Extracts 1s audio clips and saves their spectrograms as audio input to the network.
'''


import scipy.signal
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm


#http://signalsprocessed.blogspot.com/2016/08/audio-resampling-in-python.html

def get_spec(audio, num, fs=44100, eps=1e-10):

	freqs, times, amplitudes = scipy.signal.spectrogram(audio, fs=fs)


	# NOTE: Load as grayscale with cv2.imread(<img_path>, 0)

	plt.figure(figsize=(2.50,1.92), dpi=100)
	plt.pcolormesh(times, freqs, np.log(amplitudes + eps), cmap=cm.gray)		# save as greyscale
	#plt.pcolormesh(times, freqs, np.log(amplitudes))	# save as color
	#plt.xlabel("Time in Seconds")
	#plt.ylabel("Frequency in Hz")

	plt.gca().set_axis_off()
	plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
	plt.margins(0,0)
	plt.gca().xaxis.set_major_locator(plt.NullLocator())
	plt.gca().yaxis.set_major_locator(plt.NullLocator())
	plt.savefig("./spectrogram/plt"+num+".png", bbox_inches = 'tight', pad_inches = 0)
	plt.close()



def run(audio, num):

	data = AudioSegment.from_file(audio, "aac") 
	fs = data.frame_rate
	#print data.channels
	data = data.split_to_mono()[0]
	#play(data)
	num_data = np.array(data.get_array_of_samples())
	#print num_data.shape


	remove_samples = len(num_data)%fs
	num_data = num_data[:-remove_samples]
	num_data = num_data.reshape(-1,fs)
	#print num_data.shape

	for i in range(min(num_data.shape[0], 10)):

		get_spec(num_data[i], str(num)+'_'+str(i), fs)



if __name__== '__main__':

	print()
	print('Getting spectrograms for dataset')
	print()

	for aud in os.listdir('./audio'):

		print(aud)
		run('./audio/'+aud, aud[3:-4])
