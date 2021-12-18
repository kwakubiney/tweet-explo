##Django setup

- Clone the project
- cd to the directory where requirements.txt is located
- activate your `virtualenv`
- run: `pip install -r requirements.txt` in your shell


## Pre API usage:
- All 5 tweets are available in the database.

NB. Due to Twitter's policy on scraping, Selenium was not used but Tweet data was read from a CSV containing tweets
about Marvel's Avengers! #EndGame

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






 
