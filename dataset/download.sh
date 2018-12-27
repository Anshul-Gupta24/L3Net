#!/bin/sh
'''
Script to download videos. Videos are saved in ./vids
'''

URL_FILE="urls_public.txt"
num=0

while IFS='' read -r url || [[ -n "$url" ]]; do

	ffmpeg $(youtube-dl -g $url | sed "s/.*/ -i &/") -t 20 -c copy ./vids/vid$num.mkv
	((num=num+1))	

done < "$URL_FILE"
