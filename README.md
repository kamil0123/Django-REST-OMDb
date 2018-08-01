# Django-REST-OMDb

The goal of the project is to implement REST API in Django - a basic movie database interacting with external API. 

### Native Installation

Following steps shows how to quickly get the application running on Ubuntu. There can be some differences on other operationg systems. 
I assume you already have installed Python3 and PostgreSQL installed.

1. Clone repository to your computer.
2. In folder with cloned repository activate a virual environment.

```bash
source bin/activate
```

3. In PostgreSQL create new empty database to store data about movies. Open file djangoRestOmdb/settings.py, find in it DATABASES and change name, user and password to your new database credentials. 

4. Prepare migration file

```bash
python manage.py makemigrations
```

5. Migrate model to PostgreSQL

```bash
python manage.py migrate
```

Application is ready to run! :)

### Running

Start web server with command

```bash
$ python manage.py runserver
```

In your browser enter this address:

```browser
http://127.0.0.1:8000/
```

Check if server is running. 

#### Movies endpoints

To see list of all movies open:

```browser
http://127.0.0.1:8000/movies/
```

To get data from Omdb about a movie you must input it title. You can do that by putting on GET content (with media type application/json):

```json
{"title":"Lion King"}
```

and clicking GET. You shoud see json response from Omdb and when you go back to /movies/ your movie will be on the list.

#### Comments endpoints

To see list of all comments open:

```browser
http://127.0.0.1:8000/comments/
```

To post new comment you must choose movie and write a comment Text.

To filter comments for specific movie add movie id to web address, example:

```browser
http://127.0.0.1:8000/comments/?movie=1
```

### Tests

Test cases are written in file /moviesApi/tests.py. To run tests use command:

```browser
python manage.py test
```

### Heroku

I've tried to deploy my app on Heroku. I created required files (requirements.txt, Procfile, runtime.txt), modified settings (for example added import dj_database_url, change DEBUG = False), created Heroku account. But when I try to 'git push heroku master' I get error:

ModuleNotFoundError: No module named 'dj_database_url'

I've got installed this module and I have it in requirements.txt. I'm still working on solution to it.