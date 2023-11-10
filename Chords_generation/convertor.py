import subprocess
from os import walk

fluidsynth_path = r"Chords_generation\\midi_utils\\fluidsynth-2.3.4-win10-x64\\bin\\fluidsynth.exe"

# soundfont_file = r"Chords_generation\\midi_utils\\Guitar.SF2" 
# instrument = 'G_'

# soundfont_file = r"Chords_generation\midi_utils\Flute.sf2" 
# instrument = 'F_'

# soundfont_file = r"Chords_generation\midi_utils\Piano.sf2" 
# instrument = 'P_'

soundfont_file = r"Chords_generation\midi_utils\RolandMarcatoStrings.sf2" 
instrument = 'V_'

listeFichiers = []
for (repertoire, sousRepertoires, fichiers) in walk("Chords_generation\\chords_midi"):
 listeFichiers.extend(fichiers)

print(listeFichiers)

for file in listeFichiers:
   midi_file = "Chords_generation\\chords_midi\\" + file
   output_wav = "Chords_generation\\chords_wav\\" + instrument + file.split('.')[0] + ".wav"
   print(midi_file)
   command = [fluidsynth_path, '-a', 'dsound', '-o', 'audio.driver=dsound', '-i', '-l', '-s', '-g', '1.0', soundfont_file, midi_file, '-F', output_wav]

   try:
    subprocess.run(command, check=True, shell=True)
    print(f'OK ==> {output_wav}')
   except subprocess.CalledProcessError as e:
    print(f'ERROR : {e}') 

   

