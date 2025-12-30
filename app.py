from flask import Flask, request, render_template #flaask : Use to create a webpage.,
#request : It handles the request in web pagee ,render_template :Used to display on html page.

from sklearn.feature_extraction.text import TfidfVectorizer #Represents the importance of what the document.
#sklearn Is the library function used in this program
from sklearn.metrics.pairwise import cosine_similarity
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer #Italy is the sentiment and provides the score
import nltk #It helps to analysis the language.and remove the words.
from string import punctuation #It controls the characters.
import re #The user to announce is the patrons and text manipulation.
from nltk.corpus import stopwords #It collects the common words.

nltk.download('stopwords') #It deletes themultiple stoppots in the dataset.

set(stopwords.words('english')) #It stops the multiple stoppots in the Dataset.

app = Flask(__name__)#It determines the root path of the program.

#This part helps to.when the function runs.it acts the URLto the website.
@app.route('/')
def my_form():
    return render_template('form.html')

#It helps to functionpost requests tothe url.
@app.route('/', methods=['POST'])
def my_form_post():
    stop_words = stopwords.words('english')
    
    #convert to lowercase
    text1 = request.form['text1'].lower()
    
    text_final = ''.join(c for c in text1 if not c.isdigit())
    
    #remove punctuations
    #text3 = ''.join(c for c in text2 if c not in punctuation)
        
    #remove stopwords    
    processed_doc1 = ' '.join([word for word in text_final.split() if word not in stop_words])

    sa = SentimentIntensityAnalyzer() #Create a object.
    dd = sa.polarity_scores(text=processed_doc1)#Performs sentiment analysis on the Text.

    compound = round((1 + dd['compound'])/2, 2)#normalize the sentiment.

#Process the sentiment scoreinto positive or negative ornatural.
    return render_template('form.html', final=compound, text1=text_final,text2=dd['pos'],text5=dd['neg'],text4=compound,text3=dd['neu'])

#Direct the application through the host id and Port.
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5002, threaded=True)
