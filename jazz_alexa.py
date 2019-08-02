import os
import pickle
from flask import Flask
from flask_ask import Ask, statement, question
from flask_ask.models import _Response
app = Flask(__name__)
ask = Ask(app, '/')
from dlib_models import download_model, download_predictor, load_dlib_models
from main_copy import main
import portfolio_methods_copy as portfolio
from music21 import *
#from midi2audio import FluidSynth
from midi import play_audio
from create_playlist import create_pl

with open("playlist_names.pkl", mode="rb") as opened_file:
    database = pickle.load(opened_file)
desc=None
dbName=None

@app.route('/')
def homepage():
    return "Cooper Smells"

@ask.launch
def start_skill():
    welcome_message = 'Hello there, what would you like to do?'
    download_model()
    download_predictor()
    load_dlib_models()
    return question(welcome_message)

@ask.intent("AddIntent")
def add_intent():
    global desc
    global dbname
    name, desc = main(database)
    #print("Desc",desc.shape )
    if "Unknown" not in name:
        face_msg = 'Hello {}'.format(name)
        dbname = name
        create_pl(midifile)
        return statement(face_msg+". Your song has been added.")
    else:
        return question("What's your name?")

@ask.intent("NameIntent")
def assign_name(name,uk,german,cogworks):
    global database
    global desc
    global dbname
    #print("Desc2", desc.shape)

    if name is not None:
        dbname=name
    elif cogworks is not None:
        dbname=cogworks
    elif uk is not None:
        dbname=uk
    elif german is not None:
        dbname=german

    #print(name,uk,german,cogworks)
    database = portfolio.create_profile(desc, dbname, database)
    face_msg = 'Hello {}'.format(dbname)
    create_pl(midifile)
    return statement(face_msg + ". Your song has been added.")

@play.intent("PlayIntent")
def play_intent(song_number):
    global dbname
    path = './playlists/{}/'.format(dbname)
    with open(path+song,mode="rb") as f:
        play_audio(f)
    return question("Say 'add' to add the song to your playlist")
@display.intent("DisplayIntent")
def display_intent(playlist, song_number):
    c = converter.parse('name.mid')
    c.show('musicxml.png')



