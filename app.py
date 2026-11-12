import streamlit as st
import pickle
import joblib

st.title("Movie recommendation system")

similarities = joblib.load("similarities.joblib")

with open("movies.pickle","rb") as m:
    movies = pickle.load(m)

movie_names = movies["title"].values

def recommendation(movie_name):
  movie_index = movies[movies["title"]==movie_name].index[0]

  recommendation = similarities[movie_index]

  movie_list = sorted(list(enumerate(recommendation)),reverse=True,key=lambda x:x[1])[1:6]
  recommend_movies =[]

  for i in movie_list:
      recommend_movies.append(movies.iloc[i[0]].title)
      
  return recommend_movies  
movie_name = st.selectbox("Select a movie:",movie_names)


if st.button("Recommend"):
    r= recommendation(movie_name)
    st.write("The recommended movies are:")
    for i in r:
        st.write(i)
    
    

