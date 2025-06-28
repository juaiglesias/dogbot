# dogbot

Source code of [twitter bot](https://twitter.com/DogbotDog)

## Required environment variables

- `URL_GET_DOG` - endpoint used to fetch dog images
- `DOG_API_KEY` - API key for the dog image service
- `TWITTER_API_KEY` - Twitter application API key
- `TWITTER_API_SECRET` - Twitter application API secret
- `TWITTER_ACCESS_TOKEN` - Twitter user access token
- `TWITTER_ACCESS_TOKEN_SECRET` - Twitter user access token secret
- `FOLLOWING_USERS_PER_HOUR` - number of users that `autofollow.py` follows every hour

## Install dependencies

Run:

```bash
pip install -r requirements.txt
```

## Running

To tweet a single dog photo locally run:

```bash
python bot.py
```

To run the scheduled tweeting and auto-following jobs run either:

```bash
python clock.py
```

or, if using a process manager such as Heroku, rely on the `Procfile`:

```bash
clock: python clock.py
```
