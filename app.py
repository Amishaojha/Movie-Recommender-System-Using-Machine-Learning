import streamlit as st
import pandas as pd
import pickle

# Movie recommendation function
def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        recommended_movies = []
        
        for i in movies_list:
            movie_id = i[0]
            # Fetch poster from API (placeholder)
            recommended_movies.append(movies.iloc[movie_id].title)
        
        return recommended_movies
    except IndexError:
        st.error("Movie not found in the dataset.")
        return []

# Load movie data and similarity matrix
try:
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
except FileNotFoundError as e:
    st.error(f"File not found: {e.filename}. Please check that the file exists.")

# Streamlit app title
st.title('Movie Recommender System')

# Select box to choose a movie
selected_movie_name = st.selectbox('Select a movie', movies['title'].values)

# When the button is clicked, show recommendations
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    if recommendations:
        st.subheader('Recommended Movies:')
        for i in recommendations:
            st.write(i)
