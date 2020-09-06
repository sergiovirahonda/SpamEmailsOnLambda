import json
import pickle
import sklearn
import warnings
warnings.filterwarnings("ignore")

clf = pickle.load(open('SVM.pki','rb'))
vect = pickle.load(open('tfidf.pki','rb'))

def input_preprocessing(text):
    text = text.replace('!','').replace('?','').replace(',','').replace('[','').replace(']','').replace('(','').replace(')','').replace('...','')
    text = text.replace('>','').replace('<','').replace('\n',' ').replace('-','').replace('+','').replace('#','')
    return text

def predict(event):
    sample =event['body']
    input_data = [sample]
    input_data[0] = input_preprocessing(input_data[0])
    input_data = vect.transform(input_data)
    prediction = clf.predict(input_data)
    if prediction[0] == 0:
        prediction = 'Ham'
    else:
        prediction = 'Spam'
    return prediction

def lambda_handler(event,context):
    result = predict(event)
    return {'StatusCode':200,
    'body':str(result)}

# To launch the function, use:
# serverless invoke local -f lambda-spam-ham -d '{"body":"Take advantage of our Insurance plan discounts"}'

