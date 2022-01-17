from keras.models import load_model



def pred(arr):
	classifier = load_model('dtc.sav')
	prediction = classifier.predict(arr)
	return prediction

vec = np.array([[ 885.1578445866667,853.7637300000001,140.97274123567058,15.55450455844723,69.49995211314423,0.5333333333333333,1009.249419006743,15.52260250018865,0.015380343260901031]])
vec.reshape(1,-1)
print(pred(vec))
