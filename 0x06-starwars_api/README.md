# 0x06. Star Wars API

> This repository contains the tasks for `Star Wars API` project and a description of what each program or function does:


## Learning Objectives

* The `Star Wars API`, or "swapi" [(Swah-pee)](https://swapi-api.alx-tools.com/) is the world's first quantified and programmatically-accessible data source for all the data from the Star Wars canon universe! All the data is accessible through their HTTP web API. Consult the  [documentation](https://swapi-api.alx-tools.com/documentation) to get started.

* To solve the given question, you need to write a script that prints all the character names from a specific Star Wars movie based on the movie ID provided as a command-line argument. The script utilizes the Star Wars API and the `request` module to make HTTP requests. It retrieves the movie details using the `/films/` endpoint, extracts the character URLs from the response, and then makes individual requests to each character URL to retrieve and print the character names in the same order as the "characters" list in the movie endpoint's response.


## Tasks

### Task: 0-starwars_characters.js

* Write a script that prints all characters of a Star Wars movie:

- [x] Usage: `./0-starwars_characters.js <movieId>`
- [x] The first positional argument passed is the Movie ID - example: `3` = “Return of the Jedi”
- [x] Display one character name per line **in the same order as the “characters” list in the `/films/` endpoint**
- [x] You must use the [Star wars API](https://swapi-api.alx-tools.com/)
- [x] You must use the `request` module
- [x] Format: see example
    ```
        ubuntu@ubuntu:~ $ ./0-starwars_characters.js 3
        Luke Skywalker
        C-3PO
        R2-D2
        Darth Vader
        Leia Organa
        Obi-Wan Kenobi
        Chewbacca
        Han Solo
        Jabba Desilijic Tiure
        Wedge Antilles
        Yoda
        Palpatine
        Boba Fett
        Lando Calrissian
        Ackbar
        Mon Mothma
        Arvel Crynyd
        Wicket Systri Warrick
        Nien Nunb
        Bib Fortuna
        ubuntu@ubuntu:~ $ 
    ```
---


