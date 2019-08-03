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
from midi import play_music
from create_playlist import create_pl, add_to_pl
import subprocess
import os.path
from generate_music import *

with open("playlist_names.pkl", mode="rb") as opened_file:
    database = pickle.load(opened_file)
desc=None
dbName=None
#generate song, set to variable midi file
midi_file=None




@app.route('/')
def homepage():
    return "Cooper Smells"

@ask.launch
def start_skill():
    welcome_message = 'Hi! Would you like to generate, play, or display a song?'
    download_model()
    download_predictor()
    load_dlib_models()
    #play randomly generated song and assign to variable
    return question(welcome_message)

@ask.intent("AddIntent")
def add_intent():
    global desc
    global dbname
    #takes picture to return name, descriptor
    name, desc = main(database)
    path = './playlists/{}/'.format(name)
    play_audio(midi_file)
###STOPPED HERE
    if "Unknown" not in name:
        face_msg = 'Hello {}'.format(name)
        #assign name to global variable
        dbname = name
        if os.path.exists(path):
            return question(face_msg+". Do you want to add the song to your playlist?")
        else:
            #creates folder with name
            create_pl(path)
            return question(face_msg+". Do you want to add the song to your playlist?")
    else:
        return question("What's your name?")

@ask.intent("YesIntent")
def yes_intent():
    global dbname
    global midi_file
    path = './playlist/{}/'.format(dbname)
    # add numbered folder with midi in playlist
    add_to_pl(path, midi_file)
    return question(dbname+", your song has been added. Would you like to do anything else?")


@ask.intent("NameIntent")
def assign_name(name,uk,german,cogworks):
    global database
    global desc
    global dbname

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
    return question(face_msg + ". Do you want to add the song to your playlist?")

@ask.intent("PlayIntent")
def play_intent(name, song_number):
    path = './playlists/{}/'.format(name)
    allmidis=os.listdir(path)
    with open(path+'{}'.format(allmidis[song_number-1]),mode="rb") as f:
        play_audio(f)
    return question("Would you like to do anything else?")


@ask.intent("DisplayIntent")
def display_intent(name, number):
    path = './playlists/{}/'.format(name)
    allmidis = os.listdir(path)
    with open(path + '{}'.format(allmidis[number-1]), mode="rb") as f:
        c = converter.parse(f)
        c.show('musicxml.png')
    return question("Would you like to do anything else?")

@ask.intent("NoIntent")
def no_intent():
    bye_text = 'Okay, goodbye'
    with open("playlist_names.pkl", mode="rb") as opened_file:
        pickle.dump(database, opened_file)
    return statement(bye_text)

@ask.intent("ImprovIntent")
def improv_intent(songname):
    #path = r'C:\Users\prazu\prazul\Cog_Week4\JazzImprov\improv_rnn\improvised_song\{}'.format(name)
    path = r'./improvised_song/{}/'.format(songname)

    generate_test(songname, path)

    all_improv = os.listdir(path)
    play_audio(all_improv[len(all_improv)-1])
    return question("Would you like to navigate to your playlist? Say 'add'")



if __name__ == '__main__':
    app.run(debug=True)
