import sqlite3
import json
import os

conn = sqlite3.connect('spotify_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE songs(track_name text, artist_name text, ms_played integer, end_time text)''')

for filename in os.listdir(os.getcwd()):
    if 'StreamingHistory' in filename:
        with open(filename) as json_file:
            data = json.load(json_file)
        for song in data:
            track = song['trackName']
            artist = song['artistName']
            date_time = song['endTime']
            ms_played = song['msPlayed']
            c.execute("INSERT INTO songs VALUES (?, ?, ?, ?)", (track, artist, ms_played, date_time))
            conn.commit()

conn.close()
