import streamlit as st
import pickle
import pandas as pd
import requests
import io

url = "https://huggingface.co/artisticme/movie-recommender-assets/blob/main/similarity.pkl"
response = requests.get(url)
similarity = pickle.loads(response.content)
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1458053688450-eef5d21d43b3?q=80&w=1173&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-attachment: fixed;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
    .stButton>button {
        color: white;
        background-color: #ff4b4b;
        padding: 0.5em 1em;
        border-radius: 8px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ff1f1f;
    }
    .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1 style='text-align: center; color: white;'>🎬 Movie Recommender System </h1>",
    unsafe_allow_html=True
)
st.write(' ')
st.markdown(
    "<h5 style='text-align: left; color: white;'>Select Movie</h5>",
    unsafe_allow_html=True
)
#similarity = pickle.load(open('similarity.pkl','rb'))
selected_movie_name = st.selectbox("", movies['title'].values)

def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=52a0de76bc69c31d70655fa04975291f'
    response = requests.get(url)
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:
        movie_id=movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

st.write(' ')
if st.button('Recommend'):
    with st.spinner("Finding similar movies..."):
        
        names,posters = recommend(selected_movie_name)
        col1,col2,col3,col4,col5 = st.columns(5)
        with col1:
      
            st.image(posters[0])
            st.markdown(
    f"""
    <div style='
        background-color: rgba(0, 0, 0, 0.7);  /* translucent black */
        border: 2px solid white;
        border-radius: 8px;
        padding: 0.5em;
        min-height: 3.5em;
        max-height: 6em;
        width: 100%;
        color: white;
        text-align: center;
        overflow-y: auto;
        word-wrap: break-word;
        font-weight: bold;
        display: flex;
        align-items: center;
        justify-content: center;
    '>{names[0]}</div>
    """,
    unsafe_allow_html=True
)


        with col2:
            

            st.image(posters[1])
            st.markdown(
    f"""
    <div style='
        background-color: rgba(0, 0, 0, 0.7);  /* translucent black */
        border: 2px solid white;
        border-radius: 8px;
        padding: 0.5em;
        min-height: 3.5em;
        max-height: 6em;
        width: 100%;
        color: white;
        text-align: center;
        overflow-y: auto;
        word-wrap: break-word;
        font-weight: bold;
        display: flex;
        align-items: center;
        justify-content: center;
    '>{names[1]}</div>
    """,
    unsafe_allow_html=True
)

        with col3:
            st.image(posters[2])
            st.markdown(
    f"""
    <div style='
        background-color: rgba(0, 0, 0, 0.7);  /* translucent black */
        border: 2px solid white;
        border-radius: 8px;
        padding: 0.5em;
        min-height: 3.5em;
        max-height: 6em;
        width: 100%;
        color: white;
        text-align: center;
        overflow-y: auto;
        word-wrap: break-word;
        font-weight: bold;
        display: flex;
        align-items: center;
        justify-content: center;
    '>{names[2]}</div>
    """,
    unsafe_allow_html=True
)

        with col4:
            st.image(posters[3])
            st.markdown(
    f"""
    <div style='
        background-color: rgba(0, 0, 0, 0.7);  /* translucent black */
        border: 2px solid white;
        border-radius: 8px;
        padding: 0.5em;
        min-height: 3.5em;
        max-height: 6em;
        width: 100%;
        color: white;
        text-align: center;
        overflow-y: auto;
        word-wrap: break-word;
        font-weight: bold;
        display: flex;
        align-items: center;
        justify-content: center;
    '>{names[3]}</div>
    """,
    unsafe_allow_html=True
)


        with col5:
           

            st.image(posters[4])
            st.markdown(
    f"""
    <div style='
        background-color: rgba(0, 0, 0, 0.7);  /* translucent black */
        border: 2px solid white;
        border-radius: 8px;
        padding: 0.5em;
        min-height: 3.5em;
        max-height: 6em;
        width: 100%;
        color: white;
        text-align: center;
        overflow-y: auto;
        word-wrap: break-word;
        font-weight: bold;
        display: flex;
        align-items: center;
        justify-content: center;
    '>{names[4]}</div>
    """,
    unsafe_allow_html=True
)


