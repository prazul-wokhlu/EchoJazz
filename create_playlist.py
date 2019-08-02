import os
def create_pl(path):
    #path = './playlists/{}/'.format(name)
    os.mkdir(path)


def add_to_pl(path, song):
    #path = './playlists/{}/'.format(name)
    ###Figure out what path is - where midi goes
    with open(path+"/{}/".format(song), mode="wb") as opened_file:
        #FluidSynth().play_midi('input.mid')
        opened_file.write(song)