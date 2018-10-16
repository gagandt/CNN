import pickle
import numpy as numpy
from app.model.preprocessor import Preprocessor as imp_prep

#Optical Character Recogniton class
class LiteOCR:
	def __init__(self, fn = "alpha_weights.pkl", pool_size = 2):
		#loading the weight form the pickle file.
		[weight, meta] =  pickle.load(open(fn, 'rb'), encoding = 'latin1')
		#list to store labels
		self.vocab = meta["vocab"]

		#defining the rows and colums of the image
		self.img_rows = meta["img_side"]
		self.img_cols = meta["img_side"]

		#loading CNN
		self.CNN = LiteCNN()
		#combining with weights
		self.CNN.load_weights(weights)
		#pooling layers size
		self.CNN.pool_size = int(pool_size)


	def predict(self, image)
		print(image.shape)

		#changing the shape of the image
		X = np.reshape(image, (1, 1, self.img_rows, self.img_cols))
		X = X.astype("float32")

		#predicting
		predicted_i = self.CNN.predict(X)

		return self.vocab[predicted_i]








	