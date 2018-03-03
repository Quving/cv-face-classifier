[![Build Status](http://drone.quving.com/api/badges/Quving/cv-face-classifier/status.svg)](http://drone.quving.com/Quving/cv-face-classifier)

## Cv-face-classifier
This repository provides a bunch of codes written in python in order to classify faces. It starts an API json based server which receives images stored in numpy arrays and returns the corresponded labels. If you intend to use [docker](https://www.docker.com/) the Dockerfile in this image also download the weights of a pre-trained model to classify faces.

## Installation
If you've got an appropiate GPU which can be used by tensorflow (further information can be obtained [here](https://www.tensorflow.org/programmers_guide/using_gpu). You can install python library:

``` pip install tensorflow-gpu ```

after that you need to install the other python dependencies as well:

``` pip install -r requirements.txt ```

**Hint**: If you do not possess an appropiate GPU, please be aware that the training process takes much longer since it runs on the CPU. Also using [docker](https://www.docker.com/) disable the processing on the GPU but on CPU.

``` docker build -t letsfaceit:latest . ```

## Usage 

To run the api-server locally without dockerization:

``` bash start.sh ```

Using docker:

``` docker run -it -e UPDATE_WEIGHTS=0 -p 6500:6500 pingu/letsfaceit:latest ```

or using your own built docker image:

``` docker run -it -e UPDATE_WEIGHTS=0 -p 6500:6500 letsfaceit:latest ```

Once the scripts are ran, the API is accessible at **http://localhost:6500/api/predict**


Using python and [requests](http://docs.python-requests.org/en/master/) a request can look like this:

``` 
def send_request(image_np):
    url = "http://localhost:6500/api/predict"
    data = {}
    data["image"]= json.dumps(image_np.tolist())
    data["mode"]= "predict"
    response = requests.post(url, json = data)
    return response
 ```

## Training

In the data directory you will find plenty scripts. Let's say you're Wilson from now on to make it easy explainable.
#### Create training samples
- Create a folder called "original_samples" and inside of it create "wilson".
- Copy pictures of yourself in it.
- Navigate to the directory of **data** and run ``` bash generate_samples.sh ``` to create augmented samples.
- Ensure that there are new datas stored in 
  - *../data/training*
  - *../data/validation*
  - *../data/test*


#### Train the model
- Create the needed directories before you can start the training process: ``` bash initalize.sh ```
- Start the training process: ``` cd cnn && python2.7 keras_bottleneck_multiclass.py ```
- The trained model is persisted to the folder called **models/**, the class_indice is stored to **class_indices/**.




