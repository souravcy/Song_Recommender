import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib

class suggest:
    def generate_songs(suggestions):
        name=suggestions['title'].to_list()
        artists=suggestions['artist'].to_list()
        images=suggestions['image'].to_list()
        return name,artists,images

    def generate_recommendations(search):
        model = joblib.load("model.pkl")
        songs['sim']=model[search].tolist()
        suggestions=songs.sort_values(by=['sim'],ascending=False).iloc[0:6]
        name,artists,images=suggest.generate_songs(suggestions)
        return name,artists,images

    def find(songname):
        songs['indexes']=songs['title'].str.contains(songname,0)
        searched=songs[songs['indexes']==True]
        name,artists,images=suggest.generate_recommendations(searched.iloc[0]['Unnamed: 0']-1)
        return name, artists, images
    
    def trending():
        df=songs.loc[songs['year']==2019]
        df=df.sort_values(by=['year'],ascending=False).iloc[0:5]
        name=df['title'].to_list()
        artists=df['artist'].to_list()
        images=df['image'].to_list()
        return name,artists,images    

songs = pd.read_csv("data/songs.csv")