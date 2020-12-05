# ViolenceDetectionAndLocalization
 A Violence Detectot with localization , part of A graduation project submited to Birzeit University
 
 
## Requirements

This code requires you have Keras 2 and TensorFlow 1.4 or greater installed. Please see the `requirements.txt` file. To ensure you're up to date, run:

`pip install -r requirements.txt`

If you are Using `Tesnorflow2` Please use the Tesnorflow2 Compatible project in the link below.

https://www.linkhere.com 
 
 
##How to run

1. Download the Pre-trained models Kinetics model and lables and the TensorFlow .pb , .pptxt files from [here](https://u.pcloud.link/publink/show?code=kZlcALXZplDJ4el6eKjNYLPcbHGXsX7qmfV7).

All models are trained on Kinetics-400 and coco dataset. 

2. Extract the Downloaded files to 
>	| ViolenceDetectionAndLocalization
> >		...

3. Run the video classfier using 

`	$ Object_detection_video --input ./path_to_video`


