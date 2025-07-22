# 🎬 Movie Recommender System

A simple and interactive Movie Recommendation System built using **Python**, **Pandas**, and **Streamlit**, which suggests movies similar to your favorite one based on content similarity (overview, genres, keywords, etc.).

---

## Live Demo

👉 [Click to try it out!](https://movierecommender-amxpqqf2cwnk7wn4xkkpab.streamlit.app/) 

---

## 💡 Features

- 🔍 **Search by movie title**
- 🎯 **Top 5 similar movies** based on cosine similarity
- 🖼️ **Movie posters** fetched from TMDB API
- 🎥 Built with **Streamlit** for an interactive experience

---

## 🛠️ Tech Stack

| Tech | Purpose |
|------|---------|
| 🐍 Python | Core logic |
| 📊 Pandas | Data handling |
| 🤖 Scikit-learn | Cosine Similarity |
| 🌐 TMDB API | Movie Posters |
| 🌈 Streamlit | UI Framework |

---

## 📁 Dataset

- Used the Kaggle's TMDB movie dataset.
- Includes fields like: title, overview, genres, keywords, cast, crew.

---

## 🧠 How It Works

1. Vectorize textual features.
2. Calculate **cosine similarity** between movie vectors.
3. When a user selects a movie, return the top 5 most similar ones.

---

## 📦 Installation

```bash
git clone https://github.com/SrizaGoel/Movie_Recommender.git
cd Movie_Recommender
pip install -r requirements.txt
streamlit run app.py
