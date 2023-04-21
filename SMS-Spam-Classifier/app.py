import streamlit as st
import pickle as pk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

import string

ps = PorterStemmer() 

def converter(text):
    text = text.lower()
    text = text.split()
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for word in text:
        y.append(word)
    text = y[:]
    y.clear()

    for word in text:
        if word not in stopwords.words('english') and word not in string.punctuation:
            y.append(word)
    
    text = y[:]
    y.clear()

    for word in text:
        y.append(ps.stem(word))

    text = y[:]
    y.clear()

    return " ".join(text)

tfidf = pk.load(open('vectorizer.pkl','rb'))
model = pk.load(open('model.pkl','rb'))

st.header('Spam Message Classifer')
text = st.text_area("Enter message ")

if st.button('Predict'):
    transformed_sms = converter(text)
    vector = tfidf.transform([transformed_sms])
    result = model.predict(vector)[0]

    if result==0:
        st.write("Not Spam")
    elif result==1:
        st.write("Spam")