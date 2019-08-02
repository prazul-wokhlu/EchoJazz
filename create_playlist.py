import os
def create_pl(song):
    global dbname
    path = './playlists/{}/'.format(dbname)
    os.mkdir(path)
    with open(path+song, mode="wb") as opened_file:
        #FluidSynth().play_midi('input.mid')
        opened_file.write(mididata?)