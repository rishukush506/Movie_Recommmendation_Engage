# Movie_Recommmendation_Engage
## About App
This is a movie recommendation system which recommend you movies on three categories:
- [x] Trending Movies
- [x] Content-Based Recommender
- [x] User-Based Recommender
## Work Flow and Algorithms used in each recommender:

### Trending Movies:
> This recommender is simply giving movies sorted on the basis of weighted rating that have been calculated by using vote counts and average votes given to a particular movie.

![Trending Movies](./Images/trending.png "Trending Movies")

### Content-Based Recommender:
> This recommender computes similarity between movies based on certain metrics and suggests movies that are most similar to a particular movie. I build content based-recommender based on movie’s cast, crew, genres and keywords.  I plan on doing is creating a metadata dump for every movie which consists of genres, director, main actors and keywords. I then use a Count Vectorizer to create our count matrix. We now have a pairwise cosine similarity matrix for all the movies in our dataset. We can directly show top similar via using cosine similarity matrix but to improve this recommendation I have also added a mechanism to remove bad movies and return movies which are popular and have had a good critical response.
<br> In the app it will ask you for a movie title and recommend you movies that are similar to the given movie. 
<br>

![Content-Based Movies](./Images/content-based.png "Content-Based Recommender")

<br>

### User-Based Recommender:
> In user based recommendation I have used collabrative filtering. Collaborative Filtering is based on the idea that users similar to a me can be used to predict how much I will like a particular product or service those users have used/experienced but I have not.I have used the Surprise library that used extremely powerful algorithms like Singular Value Decomposition (SVD) to minimise RMSE (Root Mean Square Error) and give great recommendations.
<br>The Singular-Value Decomposition, or SVD  is a matrix decomposition method for reducing a matrix to its constituent parts in order to make certain subsequent matrix calculations simpler.<br>In the app it will ask you a user id and movie title and then recommend movies on the basis of user taste (whose id is given) and similar to the given movie.
<br>

![User-Based Movies](./Images/user-1.png "User-Based Recommender")

<br>
<br>

![User-Based Movies](./Images/user-2.png "User-Based Recommender")

<br>  As you can see for same movie title "The Fighter" It is showing different results because of different user ids.

<br>

## How I Completed this project.
<br>
Microsoft and the Acehacker team kept various sessions for us to learn more about the work culture at Microsoft. We also learned about new technologies that have been developed by Microsoft .<br><br>

In the <strong>first week</strong>, I was very much confused in choosing projects, switching from one project to another.

In the <strong>second week</strong>, I finalised <strong>algorithms project</strong> and decided on building a movie recommmendation system and start working on its design .

In the <strong>third week</strong>, I worked on jupyter notebook and learned various concepts of machine learning. I played with data a lot and try to apply various concepts like stemming and word to vector. I also try to apply different algorithms for efficient working of the system. <br>

In the <strong>last week</strong> I finalised data and made ui for my web app using streamlit (which saves a lot of my time ). <br>

I completely enjoyed the process.
<br>

## Prerequisites

You must have the following installed:

- [Python 3.10](https://www.python.org/downloads/)

Running the Web App on your Local System
--------------------------------

To run the web app in your local device, run the following commands in your terminal:-

Clone the GitHub repository into your local device by running the following command:
```bash
git clone https://github.com/rishukush506/Movie_Recommmendation_Engage

cd Movie_Recommmendation_Engage
```

In the project directory run:

```bash 
streamlit run app.py
```

And there you go !!!


