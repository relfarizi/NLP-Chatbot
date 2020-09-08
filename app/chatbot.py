import nltk
import random as rd
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask,request,jsonify,render_template
from newspaper import Article

my_awesome_app = Flask(__name__)
#nltk.download('punkt') # first-time use only
#nltk.download('wordnet') # first-time use only

#f=open('corpus.txt','r',errors = 'ignore')

#Get the article URL
article = Article('https://expertsystem.com/machine-learning-definition/')
article.download() #Download the article
article.parse() #Parse the article
article.nlp() #Apply Natural Language Processing (NLP)
corpus = article.text

raw=corpus
raw=raw.lower()# converts to lowercase
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words

lemmer = nltk.stem.WordNetLemmatizer()
#WordNet is a semantically-oriented dictionary of English included in NLTK.

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return rd.choice(GREETING_RESPONSES)

def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize)
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response
    

@my_awesome_app.route('/')
def play() :
    return render_template("home.html")

@my_awesome_app.route('/get')
def chatbot():
    user_response = request.args.get('msg')
    print("ini ",user_response)
    user_response=str(user_response).lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            res = "ROBO: You are welcome.."
        else:
            if(greeting(user_response)!=None):
                res = "ROBO: "+greeting(user_response)
            else:
                #print("ROBO: ",end="")
                res = response(user_response)
                sent_tokens.remove(user_response)
    else:
        res = "ROBO: Bye! take care.."
    print(res)
    return str(res)


if __name__ == '__main__':
    my_awesome_app.run(host ='0.0.0.0', port = 5001, debug = True)
    #my_awesome_app.run()

"""
flag=True
print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("ROBO: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("ROBO: "+greeting(user_response))
            else:
                print("ROBO: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("ROBO: Bye! take care..")

"""
