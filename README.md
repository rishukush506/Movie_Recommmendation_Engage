# Movie_Recommmendation_Engage
## About App
This is a movie recommendation System which recommend you movies on three categories:
- [x] Trending Movies
- [x] Content-Based Recommender
- [x] User-Based Recommender
## Work Flow and Algorithms used in each recommender:

### Trending Movies:
> This recommender is simply giving movies sorted on the basis of weighted rating that have been calculated by using vote counts and average votes given to a particular movie.

### Content-Based Recommender:
> This recommender computes similarity between movies based on certain metrics and suggests movies that are most similar to a particular movie. I build content based-recommender based on movie’s cast, crew, genres and keywords.  I plan on doing is creating a metadata dump for every movie which consists of genres, director, main actors and keywords. I then use a Count Vectorizer to create our count matrix. We now have a pairwise cosine similarity matrix for all the movies in our dataset. We can directly show top similar via using cosine similarity matrix but to improve this recommendation I have also added a mechanism to remove bad movies and return movies which are popular and have had a good critical response.

### User-Based Recommender:
> 
