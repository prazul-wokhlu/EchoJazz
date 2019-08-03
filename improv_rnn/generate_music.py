import subprocess
import pickle

num_choruses = 2
with open('song_chords.pkl','rb') as f:
    song_chords=pickle.load(f)
with open('song_midis.pkl','rb') as f:
    song_midis=pickle.load(f)
def generate_real(songname,filepath):

    subprocess.call(['improv_rnn_generate','--config=chord_pitches_improv',
                     '--run_dir=/Users/cooperbosch/Desktop/localjazzmodel/run_dir_new',
                     '--output_dir={}'.format(filepath),
                     '--num_outputs=1','--primer_midi={}'.format(song_midis[songname]),
                     '--backing_chords={}'.format(song_chords[songname]*num_choruses), '--render_chords' 
                     '--hparams="batch_size=128,rnn_layer_sizes=[128,128]"'])



def generate_test(songname,filepath):
    subprocess.call(['improv_rnn_generate', '--config=chord_pitches','--bundle_file=${BUNDLE_PATH}',
                     '--output_dir={}'.format(filepath), '--num_outputs=1', '--primer_midi={}'.format(song_midis[songname]),
                     '--backing_chords={}'.format(song_chords[songname]*num_choruses), '--render_chords'])

