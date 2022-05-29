import requests
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from surprise import Reader, Dataset, SVD
from surprise.model_selection import cross_validate
import requests


#st.set_page_config(layout="wide")

def app():

 st.title('Trending movies for you!! ')


#  ratings_dict=pickle.load(open('ratings_dict.pkl','rb'))
#  ratings=pd.DataFrame(ratings_dict)

 smd_dict=pickle.load(open('smd_dict.pkl','rb'))
 smd=pd.DataFrame(smd_dict)


#  id_map_dict=pickle.load(open('id_map_dict.pkl','rb'))
#  id_map=pd.DataFrame(id_map_dict)

#  gen_md_dict=pickle.load(open('gen_md_dict.pkl','rb'))
#  gen_md=pd.DataFrame(gen_md_dict)

#  md_dict=pickle.load(open('gen_md_dict.pkl','rb'))
#  md=pd.DataFrame(md_dict)

#  cosine_sim=pickle.load(open('cosine_sim_dict.pkl','rb'))



 # Poster fetch

 def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=1f89872193572f0dd8db4a2404e00c8a&language=en-US'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/original/' + data['poster_path']
 
 
 smd['popularity']=smd['popularity'].astype('float')
 
 recommended_movies_poster=[]
 recommended_movies=[]
 movie_list = smd.sort_values('popularity', ascending=False)
 counter = 0
 
 for i in range(len(movie_list)):
        if counter != 12:
            movie_id = (movie_list.iloc[i].id)
            recommended_movies.append(movie_list.iloc[i].title)
            recommended_movies_poster.append(fetch_poster(movie_list.iloc[i].id))
            counter += 1
        else:
            break
     
     
 col1, col2, col3 = st.columns(3)

 with col1:
        st.header(recommended_movies[0])
        st.image(recommended_movies_poster[0])
 with col2:
        st.header(recommended_movies[1])
        st.image(recommended_movies_poster[1])
 with col3:
        st.header(recommended_movies[2])
        st.image(recommended_movies_poster[2])
        
 col1, col2, col3 = st.columns(3)
 
 with col1:
        st.header(recommended_movies[3])
        st.image(recommended_movies_poster[3])
 
 with col2:
        st.header(recommended_movies[4])
        st.image(recommended_movies_poster[4])
 with col3:
        st.header(recommended_movies[5])
        st.image(recommended_movies_poster[5])
 
 col1, col2, col3 = st.columns(3)
 with col1:
        st.header(recommended_movies[6])
        st.image(recommended_movies_poster[6])
 with col2:
        st.header(recommended_movies[7])
        st.image(recommended_movies_poster[7])
 with col3:
        st.header(recommended_movies[8])
        st.image(recommended_movies_poster[8])
        



         
 

