# spotify-to-sqlite

CLI tool to save data from Spotify to a sqlite database.

## Installation

```bash
pip install spotify-to-sqlite
```

or clone the repository!

## Data

### Download From Spotify

1. Go to [your account page](https://spotify.com/us/account) and enter your login credentials.
2. In the menu on the left-hand side of the screen, click on Privacy settings.
3. Scroll down to the Download your data section.
4. Go to Step 1 > Request.
5. You will receive an on-screen notification saying Spotify is processing your data. It could take up to 30 days.
6. When the processing is complete, you will receive an email.
After seeing the email, return to Privacy settings; you will now have access to Step 3.
7. Click on Download.

Run:

```bash
spotify-to-sqlite datadump --path=/path/to/download
```

### API

#### Authentication

To get a client_id for accessing the Spotify API, you need to go to [your developer dashboard](https://developer.spotify.com/dashboard) and make a new application. After answering a series of questions, you'll be issued a client id and client secret. Run this command with the secret:

```bash
spotify-to-sqlite auth
```

This will create a file called `auth.json` in your current directory containing the required value. To save the file at a different path or filename, use the `--auth=myauth.json` option.

## Challenges

tktk

## Thanks

This package is inspired by [Dogsheep](https://simonwillison.net/2019/Oct/7/dogsheep/) and [Datasette](https://github.com/simonw/datasette) by [Simon Willison](https://github.com/simonw). The choice of CLI interface for the project is inspired by Tobias Kunze's [goodreads-to-sqlite](https://github.com/rixx/goodreads-to-sqlite).
