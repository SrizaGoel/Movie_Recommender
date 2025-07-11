import streamlit as st
import pickle
import pandas as pd
import requests
import io
def load_similarity_from_gdrive(file_id):
    URL = f"https://drive.google.com/uc?export=download&id={file_id}"
    response = requests.get(URL)
    if response.status_code != 200:
        raise Exception("Failed to download file from Google Drive.")
    similarity = pickle.load(io.BytesIO(response.content))
    return similarity
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
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

selected_movie_name = st.selectbox("", movies['title'].values)

def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=52a0de76bc69c31d70655fa04975291f'
    response = requests.get(url)
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']
similarity = load_similarity_from_gdrive("Y1oLIsPMPinPABHL42f4cr9INwwusZbckV")
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
            st.markdown(
    f"""
    <div style='
        height: 3.5em;
        width: 100%;
        color: white;
        text-align: center;
        overflow-y: auto;
        word-wrap: break-word;
        font-weight: bold;
    '>{names[0]}</div>
    """,
    unsafe_allow_html=True
)

            st.image(posters[0])
        with col2:
            st.markdown(
    f"""
    <div style='
        height: 3.5em;
        width: 100%;
        color: white;
        text-align: center;
        overflow-y: auto;
        word-wrap: break-word;
        font-weight: bold;
    '>{names[1]}</div>
    """,
    unsafe_allow_html=True
)

            st.image(posters[1])
        with col3:
            st.markdown(
    f"""
    <div style='
        height: 3.5em;
        width: 100%;
        color: white;
        text-align: center;
        overflow-y: auto;
        word-wrap: break-word;
        font-weight: bold;
    '>{names[2]}</div>
    """,
    unsafe_allow_html=True
)

            st.image(posters[2])
        with col4:
            st.markdown(
    f"""
    <div style='
        height: 3.5em;
        width: 100%;
        color: white;
        text-align: center;
        overflow-y: auto;
        word-wrap: break-word;
        font-weight: bold;
    '>{names[3]}</div>
    """,
    unsafe_allow_html=True
)

            st.image(posters[3])
        with col5:
            st.markdown(
    f"""
    <div style='
        height: 3.5em;
        width: 100%;
        color: white;
        text-align: center;
        overflow-y: auto;
        word-wrap: break-word;
        font-weight: bold;
    '>{names[4]}</div>
    """,
    unsafe_allow_html=True
)

            st.image(posters[4])


