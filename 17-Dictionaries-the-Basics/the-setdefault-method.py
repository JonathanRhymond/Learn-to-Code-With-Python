film_directors = {
    "The Godfather": "Francis Ford Coppola",
    "The Rock": "Micheal Bay",
    "Goodfellas": "Martin Scorsese"
}

print(film_directors.get("Goodfellas"))
print(film_directors.get("Bad Boys", "Michael Bay"))
print(film_directors)

film_directors.setdefault("Bad Boys", "Micheal Bay")
print(film_directors)

film_directors.setdefault("Bad Boys", "A good director")
print(film_directors)