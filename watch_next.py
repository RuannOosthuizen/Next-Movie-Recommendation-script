import spacy

# Here the function is defined to find a similar movie
def find_similar_movie(descriptions):

    nlp = spacy.load('en_core_web_md')

    # Here the text file "movie.txt" is read
    with open("movies.txt", "r") as file:
        movie_data = file.readlines()

    # Here a list is prepared full of tuples containing movie titles and their descriptions
    movies = []

    for line in movie_data:
        title, desc = line.split(":")
        movies.append((title.strip(), desc.strip()))

    # Here the calculations for similarity score is caluclated and preseneted in vectors
    similarity_score = []

    for movie in movies:
        title, desc = movie
        desc_doc = nlp(desc)
        similarity = desc_doc.similarity(nlp(description))
        similarity_score.append((title, similarity))

    # Here the similarity score is sorted in descending order
    similarity_score.sort(key=lambda x: x[1], reverse=True)

    return similarity_score[0][0]

# Example use:
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"

similar_movie = find_similar_movie(description)

print("Next movie to watch:", similar_movie)
