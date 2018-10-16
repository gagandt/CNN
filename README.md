Author  : GaganDeep Tomar
Started : 16 October 2018
A project to classify images builing a Convolutional Neural Network in Flask.

Using only Numpy.
=======

Based on the idea of Mammaliam Visul Cortex.
	- Local Connecions
	- Layering
	- Spatial Invariance : independent of orientation.

Based on Layers (series of operations). 

Receptive Field is the part of the image that we are focused on (the [art on which we apply our convulational to).
We slide over the image (applying a dot product between a weight matrix and every part of that image).

=======

We can split the CNN into two seperate categories.
	- Feature learning part.
		Convolution -> ReLU -> Pooling
			Then it is flattened.
	- Classificatoin.
		Using Softmax function.

======

We can thing of an image as a 3D matrix. 
	- L X B are the dimensions of the image (x, y).
	- Now think that we have 3 values for 'z'.
		Or we have 3 layers comprising information about R, G and B. 

We'll use CIFAR datase. CoCo is an alternative. 


======================================================================================

Step 1 
	Preparing a a dataset for images.
	CIFAR.

Step 2
	Convolution.
		Taking two sets of data and combining them.
		eg : converting a 6X6 image to 3X3 image.
	Convolving / Combining the weight matrix (feature map) with the input.

Step 3
	Pooling.
		To reduce the computational complexity of that model. 

Step 4
	Normalisation.
		- ReLU (Activation Function).
		- Non - important values are removed.

Step 5
	Regulisation.

Step 5H
	Dropout.
		To prevent overfitting.

Step 6
	Probability Conversion.
		Using SoftMax function.
		Hits the biggest using ArgMAx function.

Step 7
	Chooosing the most likely Label.
