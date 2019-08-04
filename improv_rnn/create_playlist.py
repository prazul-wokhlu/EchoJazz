import os
import shutil
def create_pl(path):
    #path = './playlists/{}/'.format(name)
    os.mkdir(path)


def add_to_pl(old_dir,new_dir,song_name):
    #path = './playlists/{}/'.format(name)
    ###Figure out what path is - where midi goes
    # with open(path+"{}".format(song), mode="wb") as opened_file:
    #     #FluidSynth().play_midi('input.mid')
    #     opened_file.write(song)
    os.rename(old_dir+song_name,new_dir+song_name)
