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

 st.title('Content based Recommender System')

 ratings_dict=pickle.load(open('ratings_dict.pkl','rb'))
 ratings=pd.DataFrame(ratings_dict)

 smd_dict=pickle.load(open('smd_dict.pkl','rb'))
 smd=pd.DataFrame(smd_dict)


 id_map_dict=pickle.load(open('id_map_dict.pkl','rb'))
 id_map=pd.DataFrame(id_map_dict)

 gen_md_dict=pickle.load(open('gen_md_dict.pkl','rb'))
 gen_md=pd.DataFrame(gen_md_dict)

 md_dict=pickle.load(open('gen_md_dict.pkl','rb'))
 md=pd.DataFrame(md_dict)

 cosine_sim=pickle.load(open('cosine_sim_dict.pkl','rb'))



# Poster fetch

 def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=1f89872193572f0dd8db4a2404e00c8a&language=en-US'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/original/' + data['poster_path']

 recommended_movies_poster=[]
 recommended_movies =[]

# Content Based Recommender ......................................................................................

 indices = pd.Series(smd.index, index=smd['title'])

 def improved_recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:26]
    movie_indices = [i[0] for i in sim_scores]
    
    movies = smd.iloc[movie_indices][['title', 'vote_count', 'vote_average', 'year','id']]
    vote_counts = movies[movies['vote_count'].notnull()]['vote_count'].astype('int')
    vote_averages = movies[movies['vote_average'].notnull()]['vote_average'].astype('int')
    C = vote_averages.mean()
    m = vote_counts.quantile(0.60)
    qualified = movies[(movies['vote_count'] >= m) & (movies['vote_count'].notnull()) & (movies['vote_average'].notnull())]
    qualified['vote_count'] = qualified['vote_count'].astype('int')
    qualified['vote_average'] = qualified['vote_average'].astype('int')
    qualified['wr'] = qualified.apply(lambda x: (x['vote_count']/(x['vote_count']+m) * x['vote_average']) + (m/(m+x['vote_count']) * C), axis=1)

    qualified = qualified.sort_values('wr', ascending=False).head(10)
    
    for i in range(len(qualified)):
       recommended_movies.append(qualified.iloc[i].title)
       recommended_movies_poster.append(fetch_poster(qualified.iloc[i].id)) 
    
   
    

 selectbox_title = []

 for i in smd['title']:
    selectbox_title.append(i)

 selectbox_title = set(selectbox_title)

 selected_title = st.selectbox(
    'select movie title ', 
    selectbox_title)


 improved_recommendations(selected_title)


 if st.button('Recommend'):

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



# Simple Recommender on the basis of genre,cast and director ...................................................

#  def build_chart(genre, percentile=0.85):
#     df = gen_md[gen_md['genre'] == genre]
#     vote_counts = df[df['vote_count'].notnull()]['vote_count'].astype('int')
#     vote_averages = df[df['vote_average'].notnull()]['vote_average'].astype('int')
#     C = vote_averages.mean()
#     m = vote_counts.quantile(percentile)
    
#     qualified = df[(df['vote_count'] >= m) & (df['vote_count'].notnull()) & (df['vote_average'].notnull())][['title', 'year', 'vote_count', 'vote_average', 'popularity']]
#     qualified['vote_count'] = qualified['vote_count'].astype('int')
#     qualified['vote_average'] = qualified['vote_average'].astype('int')
    
#     qualified['wr'] = qualified.apply(lambda x: (x['vote_count']/(x['vote_count']+m) * x['vote_average']) + (m/(m+x['vote_count']) * C), axis=1)
#     qualified = qualified.sort_values('wr', ascending=False).head(250)
    
#     return qualified