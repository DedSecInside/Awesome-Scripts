import requests
import random
import json
import sqlite3

def does_movie_exist(conn, imdb_id):
    """
    Return true if the movie already exists.

    Args:
        conn: (todo): write your description
        imdb_id: (str): write your description
    """
  c = conn.cursor()
  c.execute('SELECT * FROM movies_watched WHERE imdb_id=' + '"' +  imdb_id + '"')
  return c.fetchone()

def get_a_movie(conn):
    """
    Get movie movie by movie id.

    Args:
        conn: (str): write your description
    """
  id = str(random.randint(0,9999999))
  imdb_id =  "tt" + id.rjust(7, '0')
  if does_movie_exist(conn, imdb_id):
    return get_a_movie(conn)
  movies = json.loads(requests.get("http://www.omdbapi.com/?i=" + imdb_id + "&apikey=6096630").text)
  if len(movies.keys()) < 3:
    return get_a_movie(conn)
  return movies

def create_table_if_not_exists(conn):
    """
    Creates the table if it doesn t exist.

    Args:
        conn: (todo): write your description
    """
  c = conn.cursor()
  c.execute(
    """
      CREATE TABLE IF NOT EXISTS movies_watched (id INTEGER PRIMARY KEY AUTOINCREMENT, imdb_id INTEGER);
    """
  )
  conn.commit()

def insert_into_table(conn, imdb_id):
    """
    Inserts a new table into the database.

    Args:
        conn: (todo): write your description
        imdb_id: (str): write your description
    """
  c = conn.cursor()
  c.execute(
    """
      INSERT INTO movies_watched (imdb_id) VALUES (""" + '"' +  imdb_id + '"' + """);
    """
  )
  conn.commit()

conn = sqlite3.connect('movie.db')
create_table_if_not_exists(conn)
movie = get_a_movie(conn)
print(movie)
name, rating, id = movie['Title'], movie['imdbRating'], movie['imdbID']
movie = input("Do you like this movie? Name: " + name + " Rating: " + rating + " Id: " + id)
if movie and movie.lower()[0] == 'y':
  insert_into_table(conn, id)
conn.close()
