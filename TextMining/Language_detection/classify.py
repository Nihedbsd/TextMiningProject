from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle


#import the model
loaded_model = pickle.load(open('Language_detection/lang_model.sav', 'rb'))

#import the bow model
bow_model = pickle.load(open('Language_detection/bow_model.sav', 'rb'))

#classification function
def predict_lang(text):
	inst=[]
	inst.append(text)
	text_vect=bow_model.transform(inst)
	
	prob=loaded_model.predict_proba(text_vect)[0]
	
	x=prob[0]

	if x <0.8 and x>0.2:
		return("OTHER")
	else:
		return loaded_model.predict(text_vect)[0]

if __name__ == '__main__':		
	#test
	print(predict_lang("oaded_model hqjdhkqdjh zajdhazdlkamdk jqdqjdmaze لحميد العيب "))

