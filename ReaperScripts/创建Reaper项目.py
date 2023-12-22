from reathon.nodes import Project, Track, Item, Source # note new nodes Item() and Source()
from pathlib import Path
import random
import wave

def get_audio_length(filename):
    with wave.open(filename, 'rb') as audio_file:
        frames = audio_file.getnframes()
        framerate = audio_file.getframerate()
        duration = frames / float(framerate)
        return duration
    

sources = []
path = r"C:\Users\v_lmylliu\Music"
# create a source object for each of the .wav files in a directory (can you tell I love comprehensions)
sources = [
    Source(file=f'{str(x)}')
    for x in Path(path).rglob("*.wav") # you would point it to an actual folder of sounds, not just 'my-sounds'
]
#print(get_audio_length(sources[0].file))
track = Track() # create a blank Track()

pos = 0.0 # set our initial position to 0
for x in range(len(sources)): # 1000 grains
    grain = random.choice(sources) # random file from our sources
    print(grain.file)
    
    
    length = random.uniform(0.1, 0.5) # random length of the item
    length = get_audio_length(grain.file)
    track.add(
        Item(
            grain, # Item()'s have a child Source() node, which is randomly selected above
            position = pos, # and we set the position
            length = length # and we set the length
        )
    )
    pos += length+5 # increment the position by the length to create contiguous blocks

project = Project(track) # create the project with our composed track
project.write(str(path)+"\\rea.rpp") # write it out