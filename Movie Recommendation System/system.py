import streamlit as st 
import pandas as pd 
import pickle
import requests

def posture(movie):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie}?api_key=201dadbac9d90432aa44713682a9eb60')
    path = response.json()
    poster_path = path['poster_path']
    return "https://image.tmdb.org/t/p/w500/"+poster_path


dice = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similar.pkl','rb'))
df = pd.DataFrame(dice)

#API key = 201dadbac9d90432aa44713682a9eb60


def recommend(movie):
    OK = []
    id = []
    index = df[df['title']==movie].index[0]
    
    distance = similarity[index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:9]
    for i in movies_list:
        OK.append( df.iloc[ i[0] ]['title'] )
        id.append( df.iloc[ i[0] ]['id'] )
    return OK,id

def main():
    st.header("Exopy")
    choice = st.selectbox("Enter Movie Name ",
                        df['title'])

    clicked = st.button("Recommend")

    if clicked:
        name,id = recommend(choice)
        for i in range(len(name)):
            st.write(name[i])
            st.image(posture(id[i]))




main()