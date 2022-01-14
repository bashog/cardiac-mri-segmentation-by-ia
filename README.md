# Cardiac MRI Segmentation by IA

## Context
In the field of medical imaging, the diagnosis of a cardiac image by magnetic resonance sometimes requires the intervention of radiologists who must manually delimit the different structures of the heart in order to extract functional information such as the cardiac volume over time or the ejection fraction. Since heartbeats involve every part of the cardiac complex, delineating the heart alone may not be sufficient depending on the application, and a segmentation of the different structures composing it (right and left ventricle, myocardium) is often necessary.

Machine Learning, and more particularly Deep Learning with Computer Vision, have allowed the emergence of new algorithms that are gradually becoming the standard in the image processing community.

## Project motivations and purposes
In a world where technology is constantly taking the place of humans, the medical field is one of the fields that can benefit enormously from technology. This is the case of medical imaging, with AI taking on an inordinate amount of importance in many sectors to facilitate the life of professionals for example. AI can make it possible to do certain tasks, which until now were done by cardiologists but which can now be done by machines. Especially since manual segmentation requires a lot of time from doctors. Thus, the development of such a technology would free up a considerable amount of time for cardiologists, time that they could use by being more available for the patient or for tasks that cannot yet be automated. On the other hand, it would provide much faster diagnoses which, as we know, can be crucial in certain cases. The objective would be to create an artificial intelligence that would provide doctors with a segmented image of the heart. Of course, the results will always have to be verified by a doctor to avoid any error because, as we know, AIs are never infallible. However, the time savings are considerable considering the time it takes cardiologists today to perform this task by hand.

The delineation of the different parts of the heart is costly and time consuming, so the development of automatic segmentation methods is highly recommended to help radiologists in their work and participate in the facilitation of the diagnosis of the heart. The objective of the project is to build an image segmentation model based on neural networks to facilitate the work of radiologists.

## Example


## Technical details of U-Net : neural networks for computer vision
U-NET is a neural network model dedicated to Computer Vision tasks and more particularly to Semantic Segmentation problems. Semantic segmentation consists in labeling each pixel of an image with a class corresponding to what is represented. It is also called "dense prediction", because each pixel must be predicted. 

There are different methods to solve semantic segmentation problems. The traditional approaches consist in detecting points, lines or edges. It is also possible to rely on morphology, or to assemble clusters of pixels.

One of the most used neural networks for image segmentation is U-NET. It is a fully convolutional neural network model. This model was originally developed by Olaf Ronneberger, Phillip Fischer, and Thomas Brox in 2015 for medical image segmentation.

The architecture of U-NET consists of two paths. The first is the contraction path, also called the encoder. It is used to capture the context of an image. It is in fact an assembly of convolution layers and "max pooling" layers allowing to create a map of the characteristics of an image and to reduce its size in order to reduce the number of parameters of the network.The second path is the symmetrical expansion path, also called decoder. It also allows a precise localization thanks to the transposed convolution.

![Architecture of a U-Net](https://datascientest.com/wp-content/uploads/2021/05/u-net-architecture-1536x1023.png)
*Architecture of a U-Net*

 The code of the model is available at this address: https://github.com/Emma-IA/PT_Segmentation_IRM

## The interactive platform
As a continuation of the project, we wanted to deploy our machine learning model to make it accessible to the medical world in the form of an online platform only accessible to the medical world. Only accessible to the medical world for data protection reasons because medical data can be sensitive.
This brings a double advantage. First, radiologists will not have to worry about setting up the algorithm, they will just have to send the MRI. The model running on an external server will return the segmentation. The site also allows for an interactive layer-by-layer visualization of the MRI. Moreover, if radiologists and patients agree, the sent MRIs could be sources of training data to improve the model later on.

We decided to use Flask to create the site. It is a web development framework in Python. It provides useful tools and features that make it easy to create web applications in Python. It allows both to run HTML pages and to use Python functions in the back-end. The pages of the site are therefore dynamic and the project is very scalable. We could easily add features in the future.
For the visualization, we decided to use the Plotly library. It allows to create interactive graphs and supports many types of input data. The MRIs are three-dimensional files (different images per layer). We naturally turned to this solution.

### Structure of the code
- *medias* contains the data files useful for visualization and prediction. There are both the data provided by users (radiologists) and those for the demonstrations on the home page of the platform.
- *model* contains the machine learning model files. For security and data protection reasons, only the model weights are here and not the training data. 
- *templates* contains the different HTML pages of the website
- *app.py* is the main file running Flask. It allows both to call Python functions (like the machine learning model) and HTML files allowing the generation of dynamic web pages
- *requirements* is the configuration file

## How to use the project platform
1. Download the project
2. Download thethe necessary libraries listed in *requirements*
3. Run the flask program


