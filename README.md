# tweet-explo
## Pre API implementation:
- All 5 tweets are available in the database.


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






 
