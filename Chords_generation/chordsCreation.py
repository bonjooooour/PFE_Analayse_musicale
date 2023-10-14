# %%
""" 
This scripts permits the creation of all kind of chords artificialy
To use it first start by "pip install mingus" on your env
"""

# %%
from mingus.core import chords
from mingus.containers import NoteContainer
from mingus.midi import midi_file_out as MidiFileOut

# %%
list_notes = ['C','C#','Db','D','D#','Eb','E','F','F#','Gb','G','G#','Ab','A','A#','Bb','B'] # Will be the tonic of ecah chords combination
list_type_chords3sounds = ['maj','min', 'aug', 'dim', 'sus2', 'sus4']

# %%
# Creation of all the combinaison of combination of 3 sounds chords

chords3sounds = []

for notes in list_notes:
    for type in list_type_chords3sounds:
        chords3sounds.append(notes+type)

len(chords3sounds) 

# %%
# Get the 3 notes of each chords

compo_chords3sounds = {}

for item in chords3sounds:
    compo_chords3sounds[item] = chords.from_shorthand(item)

# %%
chords.from_shorthand('Amaj')

# %%
# Creation of midi files of each chords

note_container_3sounds = []

for i in range(len(chords3sounds)):
    n = NoteContainer()
    n.add_notes([compo_chords3sounds[chords3sounds[i]][0],compo_chords3sounds[chords3sounds[i]][1],compo_chords3sounds[chords3sounds[i]][2]])
    note_container_3sounds.append(n)
    MidiFileOut.write_NoteContainer("chords_midi/" + chords3sounds[i]+".mid", n)

len(note_container_3sounds)


