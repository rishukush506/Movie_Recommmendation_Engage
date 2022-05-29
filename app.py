import requests
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from surprise import Reader, Dataset, SVD
from surprise.model_selection import cross_validate
import requests



# Custom imports 
from multipage import MultiPage
from apps import trending_movies, content_based,user_based # import your pages here

# Create an instance of the app 
app = MultiPage()

st.set_page_config(layout="wide")
# Title of the main page
st.title('Movie Recommendation System')

# Add all your applications (pages) here
app.add_page("Trending Movies", trending_movies.app)
app.add_page("Content Based Recommender", content_based.app)
app.add_page("User based Recommender", user_based.app)


# The main app
app.run()











    


