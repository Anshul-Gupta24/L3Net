## Keras implementation of Look, Listen and Learn (Arandjelović et al., 2017).

#### The architecture consists of an audio and visual subnetwork. The outputs from each of the subnetworks is concatenated and passed through two dense layers to predict whether the input audio and image correspond or not.
#### </br>

### Requirements
* Python 3
* Keras
* Pandas
* Numpy
* Scipy
* Pydub
* FFmpeg
* Matplotlib
* Sklearn
* Opencv
#### </br>

### Dataset
#### Navigate to the 'dataset' folder.
#### Download the list of URLs from http://data.csail.mit.edu/soundnet/urls_public.txt. To download the videos, run:
#### ```>>bash download.sh``` 
#### This downloads the videos upto a maximum length of 20 seconds (We use only the first 10s of data). Note that several of the links do not work.
#### To create the dataset, run:
#### ```>>python create_dataset.py```
#### </br>


### Running the Code
#### To train the model, run:
#### ```python train.py```
#### The model is saved in an h5 file as 'model.h5' at the end of every epoch. 
#### </br>

### References
#### Arandjelovic, R., & Zisserman, A. (2017, October). Look, listen and learn. In 2017 IEEE International Conference on Computer Vision (ICCV) (pp. 609-617). IEEE.

