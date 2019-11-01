import subprocess
import pickle
import os
from os import path
num_choruses = 2
with open('song_chords.pkl','rb') as f:
    song_chords=pickle.load(f)
with open('song_midis.pkl','rb') as f:
    song_midis=pickle.load(f)

song_midis =  {k.lower(): v for k, v in song_midis.items()}
song_chords =  {k.lower(): v for k, v in song_chords.items()}
print(song_midis)
print(song_chords)
def generate_real(songname,filepath):

    subprocess.call(['improv_rnn_generate','--config=chord_pitches_improv',
                     '--run_dir=/Users/cooperbosch/Desktop/localjazzmodel/run_dir_new',
                     '--output_dir={}'.format(filepath),
                     '--num_outputs=1','--primer_midi={}'.format(song_midis[songname.lower]),
                     '--backing_chords={}'.format(song_chords[songname.lower]*num_choruses), '--render_chords'
                     '--hparams="batch_size=128,rnn_layer_sizes=[128,128]"'])



def generate_test(songname,filepath):
    # arr=['improv_rnn_generate', '--config=chord_pitches',
    #                  r'--bundle_file=./chord_pitches_improv.mag',
    #                  '--output_dir={}'.format(filepath), '--num_outputs=1', '--primer_midi={}'.format(song_midis[songname]),
    #                  '--backing_chords={}'.format(song_chords[songname]*num_choruses), '--render_chords']
    if not path.exists(filepath):
        os.mkdir(filepath)
    arr=['python3','improv_rnn_generate.py', '--config=chord_pitches_improv',
                     r'--bundle_file=./batchfile.mag',
                     '--output_dir={}'.format(filepath), '--num_outputs=1', '--primer_midi={}'.format(song_midis[songname]),
                     '--backing_chords={}'.format((song_chords[songname]+' ')*num_choruses), '--render_chords']
    arr2=['python3','improv_rnn_generate.py', '--config=chord_pitches_improv',
                     r'--bundle_file=./chord_pitches_improv.mag',
                     '--output_dir={}'.format(filepath), '--num_outputs=1', '--primer_melody=[60]',
                     '--backing_chords={}'.format((song_chords[songname]+' ')*num_choruses), '--render_chords']
    try:
        subprocess.check_call(arr)
    except:
        subprocess.call(arr2)
