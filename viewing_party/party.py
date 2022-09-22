# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if(title is None or genre is None or rating is None):
        return None
    else:
        new_movie = {"title" : title,
        "genre" : genre,
        "rating" : rating 
        }

    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
#
    total = 0.0
    if len(user_data["watched"]) == 0:
        return total

    for movie in user_data["watched"]:
        total += movie["rating"]
    
    return total/len(user_data["watched"])

def get_most_watched_genre(user_data):
    genre_count = {}
    max = 0
    max_genre = ""

    if len(user_data["watched"]) == 0:
        return None

    for movie in user_data["watched"]:
        if movie["genre"] not in genre_count:
            genre_count[movie["genre"]] = 1
        else:
            genre_count[movie["genre"]] = genre_count[movie["genre"]] + 1
    
    for genre in genre_count:
        if(genre_count[genre] > max):
            max = genre_count[genre]
            max_genre = genre

    return max_genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

