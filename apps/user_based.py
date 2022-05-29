import requests
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from surprise import Reader, Dataset, SVD
from surprise.model_selection import cross_validate
import requests


# st.set_page_config(layout="wide")


def app():


 st.title('User Based Recommender')

 ratings_dict = pickle.load(open('ratings_dict.pkl', 'rb'))
 ratings = pd.DataFrame(ratings_dict)

 smd_dict = pickle.load(open('smd_dict.pkl', 'rb'))
 smd = pd.DataFrame(smd_dict)


 id_map_dict = pickle.load(open('id_map_dict.pkl', 'rb'))
 id_map = pd.DataFrame(id_map_dict)

 gen_md_dict = pickle.load(open('gen_md_dict.pkl', 'rb'))
 gen_md = pd.DataFrame(gen_md_dict)

 md_dict = pickle.load(open('gen_md_dict.pkl', 'rb'))
 md = pd.DataFrame(md_dict)

 cosine_sim = pickle.load(open('cosine_sim_dict.pkl', 'rb'))


# Poster fetch

 def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=1f89872193572f0dd8db4a2404e00c8a&language=en-US'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/original/' + data['poster_path']


 recommended_movies_poster = []

# Hybrid Recommender ..............................................................................................


 @st.cache(suppress_st_warning=True)
 def svd_calculation():
    reader = Reader()
    data = Dataset.load_from_df(
        ratings[['userId', 'movieId', 'rating']], reader)
    svd = SVD()
    cross_validate(svd, data, measures=['RMSE', 'MAE'], cv=10, verbose=True)
    trainset = data.build_full_trainset()
    svd.fit(trainset)
    return svd


 svd = svd_calculation()

 indices = pd.Series(smd.index, index=smd['title'])
 indices_map = id_map.set_index('id')


 def hybrid(userId, title):
    idx = indices[title]
    tmdbId = id_map.loc[title]['id']
    # print(idx)
    movie_id = id_map.loc[title]['movieId']

    sim_scores = list(enumerate(cosine_sim[int(idx)]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:26]
    movie_indices = [i[0] for i in sim_scores]

    movies = smd.iloc[movie_indices][[
        'title', 'vote_count', 'vote_average', 'year', 'id']]
    movies['est'] = movies['id'].apply(lambda x: svd.predict(
        userId, indices_map.loc[x]['movieId']).est)
    movies = movies.sort_values('est', ascending=False)

    k = 0
    ans = []
    for i in range(len(movies)):
        if k != 10:
            ans.append(movies.iloc[i].title)
            recommended_movies_poster.append(fetch_poster(movies.iloc[i].id))
        else:
            break
        k += 1
    return ans

# user id ranges between 1 to 670


 selectbox_id = []

 k = 1
 while k <= 670:
    selectbox_id.append(k)
    k += 1


 selected_id = option = st.selectbox(
    'Give me user id ranging 1 to 670 ',
    selectbox_id)


 selectbox_title = []

 for i in smd['title']:
    selectbox_title.append(i)

 selectbox_title = set(selectbox_title)

 selected_title = st.selectbox(
    'select movie title ',
    selectbox_title)


 recommended_movies = hybrid(selected_id, selected_title)

# st.write(selected_title)
# st.write(selected_id)


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
