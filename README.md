# Cardiac MRI Segmentation by IA

## Context
In the field of medical imaging, the diagnosis of a cardiac image by magnetic resonance sometimes requires the intervention of radiologists who must manually delimit the different structures of the heart in order to extract functional information such as the cardiac volume over time or the ejection fraction. Since heartbeats involve every part of the cardiac complex, delineating the heart alone may not be sufficient depending on the application, and a segmentation of the different structures composing it (right and left ventricle, myocardium) is often necessary.

Machine Learning, and more particularly Deep Learning with Computer Vision, have allowed the emergence of new algorithms that are gradually becoming the standard in the image processing community.

## Project motivations and purposes
In a world where technology is constantly taking the place of humans, the medical field is one of the fields that can benefit enormously from technology. This is the case of medical imaging, with AI taking on an inordinate amount of importance in many sectors to facilitate the life of professionals for example. AI can make it possible to do certain tasks, which until now were done by cardiologists but which can now be done by machines. Especially since manual segmentation requires a lot of time from doctors. Thus, the development of such a technology would free up a considerable amount of time for cardiologists, time that they could use by being more available for the patient or for tasks that cannot yet be automated. On the other hand, it would provide much faster diagnoses which, as we know, can be crucial in certain cases. The objective would be to create an artificial intelligence that would provide doctors with a segmented image of the heart. Of course, the results will always have to be verified by a doctor to avoid any error because, as we know, AIs are never infallible. However, the time savings are considerable considering the time it takes cardiologists today to perform this task by hand.

The delineation of the different parts of the heart is costly and time consuming, so the development of automatic segmentation methods is highly recommended to help radiologists in their work and participate in the facilitation of the diagnosis of the heart. The objective of the project is to build an image segmentation model based on neural networks to facilitate the work of radiologists.

## Technical details

### U-Net : neural networks for computer vision
U-NET is a neural network model dedicated to Computer Vision tasks and more particularly to Semantic Segmentation problems. Semantic segmentation consists in labeling each pixel of an image with a class corresponding to what is represented. It is also called "dense prediction", because each pixel must be predicted. 

There are different methods to solve semantic segmentation problems. The traditional approaches consist in detecting points, lines or edges. It is also possible to rely on morphology, or to assemble clusters of pixels.

One of the most used neural networks for image segmentation is U-NET. It is a fully convolutional neural network model. This model was originally developed by Olaf Ronneberger, Phillip Fischer, and Thomas Brox in 2015 for medical image segmentation.

The architecture of U-NET consists of two paths. The first is the contraction path, also called the encoder. It is used to capture the context of an image. It is in fact an assembly of convolution layers and "max pooling" layers allowing to create a map of the characteristics of an image and to reduce its size in order to reduce the number of parameters of the network.The second path is the symmetrical expansion path, also called decoder. It also allows a precise localization thanks to the transposed convolution.



## How to use it ?
