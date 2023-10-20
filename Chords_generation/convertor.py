""" 
This scripts permits the convertion of midi files into wav files
To use it first start by "pip install mingus" on your env
"""

import subprocess
from os import walk

fluidsynth_path = r'midi_utils\fluidsynth-2.3.4-win10-x64\bin\fluidsynth.exe'

# Uncomment the font you like, in the created files will be recognized by a letter, G for Guitar, P for Piano, F for flute and V for Violin

# soundfont_file = 'midi_utils\Guitar.SF2' 
# instrument = 'G_'

# soundfont_file = 'midi_utils\Flute.sf2'
# instrument = 'F_'

# soundfont_file = 'midi_utils\Piano.sf2'
# instrument = 'P_'

soundfont_file = 'midi_utils\RolandMarcatoStrings.sf2'
instrument = 'V_'


listeFichiers = []
for (repertoire, sousRepertoires, fichiers) in walk('chords_midi'):
 listeFichiers.extend(fichiers)

for file in listeFichiers:
   midi_file = "chords_midi/" + file
   output_wav = "chords_wav/" + instrument + file.split('.')[0] + ".wav"
   command = [fluidsynth_path, '-a', 'dsound', '-o', 'audio.driver=dsound', '-i', '-l', '-s', '-g', '1.0', soundfont_file, midi_file, '-F', output_wav]

   try:
    subprocess.run(command, check=True, shell=True)
    print(f'OK ==> {output_wav}')
   except subprocess.CalledProcessError as e:
    print(f'ERROR : {e}')    