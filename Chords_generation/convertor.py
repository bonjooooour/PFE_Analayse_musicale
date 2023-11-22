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


c:/Users/mgere/VS_Code_Workspace/ESEO/PFE_Analayse_musicale/Chords_generation/convertor.py
  File "c:\Users\mgere\VS_Code_Workspace\ESEO\PFE_Analayse_musicale\Chords_generation\convertor.py", line 25
    for fichiers in walk("C:\Users\mgere\VS_Code_Workspace\ESEO\PFE_Analayse_musicale\Chords_generation\chords_midi"):
                                  
                                  
                                  
              ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

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
    