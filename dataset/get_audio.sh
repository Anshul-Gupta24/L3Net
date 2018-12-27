'''
Script to extract audio from the videos. Audio clips are saved in ./audio
'''


for vid in ./vids/*; do
	ffmpeg -i $vid -vn -acodec copy ./audio/aud${vid:10:-4}.aac
done
