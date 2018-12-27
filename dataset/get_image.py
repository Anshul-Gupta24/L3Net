'''
Extracts frames from the video to form the visual input to the network
'''


import numpy as np
import cv2
import os
import math


def run(vid, num):

	cap = cv2.VideoCapture(vid)

	fps = int(math.ceil(cap.get(cv2.CAP_PROP_FPS)))
	num_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
	#print(num_frames)
	#print(fps)
	frame_seq = int(fps/2)

	i = 0
	while(frame_seq < num_frames and i < 10):

		cap.set(cv2.CAP_PROP_POS_FRAMES, frame_seq - 1)
		ret, frame = cap.read()
		#print('frame '+str(frame_seq))
		#print(ret)

		if ret==True:
			img = cv2.resize(frame, (224,224))
			cv2.imwrite('./image/img'+str(num)+'_'+str(i)+'.png', img)

		frame_seq += fps
		i += 1



if __name__=='__main__':

	print()
	print('Getting images for dataset')
	print()

	for vid in os.listdir('./vids'):
		print(vid)
		run('./vids/'+vid, vid[3:-4])
