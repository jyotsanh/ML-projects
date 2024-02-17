from flask import Flask, render_template, request
import pickle
import pandas as pd
import requests

app = Flask(__name__)



def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=201dadbac9d90432aa44713682a9eb60&language=en-US')
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']



movies_list = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl','rb'))




def recommend(movie):
    movie_index = movies[movies['title']== movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommend_movies = []
    recommend_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        #fetch the movie poster
        recommend_movies.append(movies.iloc[i[0]].title)
        #fetches the poster from API
        recommend_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies,recommend_movies_poster



@app.route('/')
def index():
    return render_template('index.html',all = movies['title'].values)


@app.route('/predict', methods=['POST'])
def predict():
    movie_name = request.form['movie']
    recommend_movies,recommend_movies_poster = recommend(movie_name)
    obj = {
        'movie':recommend_movies,
        'poster':recommend_movies_poster
        
    }

    return render_template('index.html', obj=recommend_movies)



if __name__ == '__main__':
    app.run(debug=True)
