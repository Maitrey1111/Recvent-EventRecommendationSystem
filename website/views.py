from flask import Blueprint, render_template, request, Flask
import pandas as pd
import numpy as np
import requests
import json
import urllib.request

#Data Processing
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
# 

views = Blueprint('views', __name__)

data = pd.read_csv("data.csv")
d = data.copy()
df = d.drop(['link', 'venue', 'price'], axis=1)
df.head()

df['desc'] = data['description'] + data['city'] + ' ' + data['genre']
df['desc'] = df['desc'].fillna(' ')

vectorizer = TfidfVectorizer(analyzer = "word", stop_words = "english", token_pattern=r'\w{1,}', strip_accents='unicode')
tfidfmatrix = vectorizer.fit_transform(df["desc"])

raw_sim_matrix = cosine_similarity(tfidfmatrix)
sim_matrix = pd.DataFrame(raw_sim_matrix)

indices = pd.Series(df.index, index=df["title"])   

#Recommendation
def recommend(event_name):
  #get event index
  if(indices[event_name].size >=1):
    event_val = indices[event_name][0]
  else:
    event_val = ""
    pass
  #find their similarity scores
  sim_scores = sim_matrix[event_val]
  
  #similarity scores are
  scores = list(enumerate(sim_scores))
  sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
  
  #top-10 recommendations shown
  recs = sorted_scores[1:11]

  #get indices of ranked movies
  recs = [x[0] for x in recs]

  #returns titles from original dataset, with indices as in recs
  return list(df['title'].iloc[recs])

cities = list(set(data["city"]))

events = list(set(data["title"]))

@views.route('/', methods=['GET', 'POST'])
@views.route('/home', methods=['GET', 'POST'])
def home():
    imList = request.form
    selected_event = imList.getlist('event')
    if(selected_event):
        return render_template("home.html",
        len = len(output), 
        total_events = len(events),
        selected_event = sel_event,  
        output=output, 
        events=events)
    print(selected_event)
    sel_event = selected_event[0]
    # if(len(selected_event) >= 1):
    # sel_event = selected_event[0]
    output = recommend(selected_event[0])
    # else:
    #     sel_event = "Ritviz – ‘Mimmi’ Album Launch Tour"
    #     output = recommend("Ritviz – ‘Mimmi’ Album Launch Tour")


# return based on availability