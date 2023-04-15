import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# from dotenv import load_dotenv
# import os

class suggest:
    # def configure():
    #     load_dotenv()

    def generate_recommendations(search):
        df=songs.drop(['id','name','artists','indexes'], axis = 1)
        # df=df.drop('sim',axis=1)
        search=search.drop(['id','name','artists','indexes'])
        songs['sim'] = cosine_similarity(df.values, search.values.reshape(1, -1))
        return songs
    
    def generate_songs(searched):
        df=suggest.generate_recommendations(searched)
        df=df.sort_values(by=['sim'],ascending=False).head(10)
        df=df.iloc[0:5]
        name=df['name'].to_list()
        artists=df['artists'].to_list()
        id=df['id'].to_list()
        return name,artists,id

    def image_find(id):
        images=["ll"]
        # for i in range (len(id)):
        #     images.append(sp.track(id[i])['album']['images'][0]['url'])
        return images

    def find(songname):
        songs['indexes']=songs['name'].str.contains(songname,0)
        searched=songs[songs['indexes']==True]
        # print(searched.iloc[0])
        name,artists,id=suggest.generate_songs(searched.iloc[0])
        images=suggest.image_find(id)
        return name, artists, images
    
    def trending():
        name=["ll"]
        images=["ll"]
        artists=["ll"]
        # for i in range(5):
        #     name.append(sp.playlist('37i9dQZEVXbLZ52XmnySJg')['tracks']['items'][i]['track']['name'])
        #     artists.append(sp.playlist('37i9dQZEVXbLZ52XmnySJg')['tracks']['items'][i]['track']['artists'][0]['name'])
        #     images.append(sp.track(sp.playlist('37i9dQZEVXbLZ52XmnySJg')['tracks']['items'][i]['track']['id'])['album']['images'][0]['url'])
        return name,artists,images    

# suggest.configure()
songs = pd.read_csv("data/new.csv")
# client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'))
# sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)