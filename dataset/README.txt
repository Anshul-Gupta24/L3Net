Fast Process

Required folders:
1. vids
2. audio
3. removed
4. image
5. spectrogram

To download videos:
>>bash download.sh

To create dataset:
>> bash run.sh


--------------------------------------------------------------------------------
--------------------------------------------------------------------------------


Step by Step Process

To download the videos:
>>bash download.sh

To get the audio:
>>bash get_audio.sh

To remove videos with no audio:
>>python3 remove_vids.py

To get frames:
>>python3 get_image.py

To get spectrograms:
>>python3 get_spectrogram.py

To remove frames with no audio pair:
>>python3 remove_image.py

To create dataset:
>>python3 create_dataset.py

