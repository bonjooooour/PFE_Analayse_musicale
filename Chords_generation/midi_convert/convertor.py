""" 
This scripts permits the convertion of midi files into wav files
To use it first start by "pip install mingus" on your env
"""

import subprocess
from os import walk

fluidsynth_path = r'midi_convert\fluidsynth-2.3.4-win10-x64\bin\fluidsynth.exe'

soundfont_file = 'midi_convert\Guitar.SF2' # Sound of a guitar

listeFichiers = []
for (repertoire, sousRepertoires, fichiers) in walk('chords_midi'):
 listeFichiers.extend(fichiers)

for file in listeFichiers:
   midi_file = "chords_midi/" + file
   output_wav = "chords_wav/" + file.split('.')[0] + ".wav"
   command = [fluidsynth_path, '-a', 'dsound', '-o', 'audio.driver=dsound', '-i', '-l', '-s', '-g', '1.0', soundfont_file, midi_file, '-F', output_wav]

   try:
    subprocess.run(command, check=True, shell=True)
    print(f'OK ==> {output_wav}')
   except subprocess.CalledProcessError as e:
    print(f'ERROR : {e}')    
