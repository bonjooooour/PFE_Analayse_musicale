import subprocess
from os import walk
   

fluidsynth_path = r"Chords_generation\\midi_utils\\fluidsynth-2.3.4-win10-x64\\bin\\fluidsynth.exe"


midi_utils_directory = "Chords_generation\\midi_utils"

soundfont_files = []
instruments = []

for (repertoire, sousRepertoires, fichiers) in walk(midi_utils_directory):
    for fichier in fichiers:
        if fichier.lower().endswith(('.sf2', '.sf3')):
            soundfont_files.append(f"{midi_utils_directory}\\{fichier}")
            # Récupération des 6 premiers caractères du nom du fichier
            instrument_name = fichier[:6] if len(fichier) >= 6 else fichier
            # Ajout de "_" après le nom
            instrument_name += "_"
            instruments.append(instrument_name)

print("Liste des fichiers soundfont:")
print(soundfont_files[12])

print("Liste des instruments:")
print(instruments[12])


midi_directory = "Chords_generation\\chords_midi"
wav_directory = "Chords_generation\\chords_wav"

listeFichiers = []
for (repertoire, sousRepertoires, fichiers) in walk(midi_directory):
    listeFichiers.extend(fichiers)

print(listeFichiers)

for soundfont_file, instrument in zip(soundfont_files, instruments):
    for file in listeFichiers:
        midi_file = f"{midi_directory}\\{file}"
        output_wav = f"{wav_directory}\\{instrument}{file.split('.')[0]}.wav"
        print(midi_file)
        command = [
            fluidsynth_path, '-a', 'dsound', '-o', 'audio.driver=dsound',
            '-i', '-l', '-s', '-g', '1.0', soundfont_file, midi_file, '-F', output_wav
        ]

        try:
            subprocess.run(command, check=True, shell=True)
            print(f'OK ==> {output_wav}')
        except subprocess.CalledProcessError as e:
            print(f'ERROR : {e}')





"""



import subprocess
from os import walk

fluidsynth_path = r"Chords_generation\\midi_utils\\fluidsynth-2.3.4-win10-x64\\bin\\fluidsynth.exe"

soundfont_file = r"Chords_generation\\midi_utils\\Guitar.SF2" 
instrument = 'G_'

# soundfont_file = r"Chords_generation\\midi_utils\\Guitar_StudioPack.SF2" 
# instrument = 'G_'

# soundfont_file = r"Chords_generation\midi_utils\Flute.sf2" 
# instrument = 'F_'

# soundfont_file = r"Chords_generation\midi_utils\Piano.sf2" 
# instrument = 'P_'

# soundfont_file = r"Chords_generation\midi_utils\198_Legato_strings.sf2" 
# instrument = 'V_'

listeFichiers = []
for (repertoire, sousRepertoires, fichiers) in walk("Chords_generation\\chords_midi"):
 listeFichiers.extend(fichiers)

print(listeFichiers)

for i in range(100):
   for file in listeFichiers:
      midi_file = "Chords_generation\\chords_midi\\" + file
      output_wav = "Chords_generation\\chords_wav\\" + instrument + file.split('.')[0]+'_'+ str(i)#+100) + ".wav"
      print(midi_file)
      command = [fluidsynth_path, '-a', 'dsound', '-o', 'audio.driver=dsound', '-i', '-l', '-s', '-g', '1.0', soundfont_file, midi_file, '-F', output_wav]

      try:
         subprocess.run(command, check=True, shell=True)
         print(f'OK ==> {output_wav}')
      except subprocess.CalledProcessError as e:
         print(f'ERROR : {e}') 



"""        