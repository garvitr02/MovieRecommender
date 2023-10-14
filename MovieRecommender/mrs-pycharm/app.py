

import pandas as pd
import streamlit as st
import pickle
import numpy as np

import os
movies_dict = pickle.load(open('C:\\Users\\garvi\\1_MachineLearning\\MovieRecommender\\movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)


model_path = 'C:\\Users\\garvi\\1_MachineLearning\\MovieRecommender\\similarity.pkl'

with (open(model_path, "rb") as pickle_in):
    similarity = pickle.load(pickle_in)
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


st.title('Movie Recommender System')

selected_movie = st.selectbox('Type or select a movie from the dropdown', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)