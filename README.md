# tweet-explo

# Django setup

- Clone the project
- cd to the directory where requirements.txt is located
- activate your `virtualenv`
- run: `pip install -r requirements.txt` in your shell


## Pre API usage:
- A CSV file, located in the `csv` directory, contains a dataset of tweets
- `cd` into the project directory
- Run `py manage.py makemigrations` , `py manage.py migrate` and `py manage.py ProcessCsv` [ignore all warnings]


## Tweet model
- Tweet
- Date and time of creation
- Twitter Username
- ID of the tweet

## Endpoints (GET)
- `localhost:8000/api/tweet/` => all tweets in DB
- `localhost:8000/api/tweet/{username}/{id}` => specific nth tweet. // to be done
- `localhost:8000/api/tweet/username?={username}` => search tweets based on username.

## Response codes
- `200` (found)
- `500` (server error)
- `404` (resource not found)







 
