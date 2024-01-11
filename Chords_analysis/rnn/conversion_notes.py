import os
import sqlite3
import pandas as pd
import numpy as np

from mingus.core import chords
from mingus.containers import NoteContainer
from mingus.midi import midi_file_out as MidiFileOut

# Nettoyage des données pour le dataset ISOPHONICS

notes = ['C','D','E','F','G','A','B']
demi_ton = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
demi_ton_b = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']

dict_intervalle = {'b2': 1, '2': 1, 'b3': 3, '3': 3, 'b4': 4, '4': 4, 'b5': 5, '5': 5, 'b6': 6, '6': 6, 'b7': 7, '7': 7}
dict_ton = {'b2': 0.5, '2': 1, 'b3': 1.5, '3': 2, 'b4': 2.5, '4': 3, 'b5': 3, '5': 3.5, 'b6': 4, '6': 4.5, 'b7': 5, '7': 5}

def get_fund(liste):
    chords_cut = []
    for i in range(len(liste)):
        if ":" in liste[i]:
           chords_cut.append(liste[i].split(':')[0])
        else: 
            chords_cut.append(liste[i].split('/')[0])

    return chords_cut

def get_type(liste):
    chords_cut = [] 
    for i in range(len(liste)):
        val = liste[i]
        temp = 'M'
        if ":" in liste[i]:
           temp = liste[i].split(':')[1]
           if "/" in temp:
               chords_cut.append(temp.split('/')[0])
           else:
               chords_cut.append(temp)
        else: 
            chords_cut.append(temp)

    return chords_cut

def get_basse_mod(liste):
    chords_cut = []
    for i in range(len(liste)):
        if ":" in liste[i]:
            temp = liste[i].split(':')[1]
            if "/" in temp:
                chords_cut.append(temp.split('/')[1])
            else:
                chords_cut.append(' ')
        else: 
            if "/" in liste[i]:
                chords_cut.append(liste[i].split('/')[1])
            else: 
                chords_cut.append(' ')

    return chords_cut

def get_basse_inter(liste):
    key_to_find = liste[2]
    if key_to_find in dict_intervalle:
        intervalle = dict_intervalle[key_to_find]

        fund = liste[0]
        if len(fund) >=2:
            fund = fund[0]

        idx = notes.index(fund)
        idx_basse = idx + intervalle
        if idx_basse >= 7:
            idx_basse -= 7
        inter_basse = notes[idx_basse-1]
    else:
        return 'No basse modification'
    return inter_basse

def get_basse_ton(liste):
    key_to_find = liste[2]
    fund_basse = ''
    
    if key_to_find in dict_ton:
        val_ton = dict_ton[key_to_find]*2
        idx = demi_ton.index(liste[0])
        idx_basse = idx + val_ton
        if idx_basse >= 12:
            idx_basse -= 12
        inter_basse_ton = demi_ton[int(idx_basse)]

        note_inter = get_basse_inter(liste)

        if len(inter_basse_ton) >=2:
            fund_basse = inter_basse_ton[0]
        
        if note_inter != fund_basse:
            inter_basse_ton = demi_ton_b[int(idx_basse)]

    else:
        inter_basse_ton = ''

    return inter_basse_ton

def concat(lis1,lis2,lis3):
    total = []
    for i in range(len(lis1)):
        total.append([lis1[i],lis2[i],lis3[i]])
    return total

def pretitify(list):
    res = []
    for value in list:
        if value[2] != ' ':
            res.append(value[0]+value[1]+'/'+ get_basse_ton(value))
        else:
            res.append(value[0]+value[1])
    return res

# Création d'un df sur toutes les chansons d'un fichier

def create_df(dossier):
    # Obtenez la liste des fichiers dans le dossier
    fichiers = [f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))]

    # Initialisez un DataFrame vide
    df_final = pd.DataFrame()

    # Parcourez chaque fichier dans le dossier
    for fichier in fichiers:
        if fichier.endswith('.lab'):  # Assurez-vous que le fichier est au format LAB
            chemin_fichier = os.path.join(dossier, fichier)
            
            # Lisez le fichier LAB et créez un DataFrame
            df_temp = pd.read_csv(chemin_fichier, delimiter=' ', header=None, names=['start', 'end', 'chords'])
            
            # Ajoutez une colonne avec le nom du fichier
            df_temp['NomFichier'] = fichier[5:-4]
            
            # Concaténez le DataFrame temporaire au DataFrame final
            df_final = pd.concat([df_final, df_temp], ignore_index=True)

    return df_final

# Application des fonctions de nettoyage sur le df
def cleaning_df(df):
    new_df = df
    new_df['Decompo'] = concat(get_fund(new_df['chords']),get_type(new_df['chords']),get_basse_mod(new_df['chords']))
    new_df['Good_chords'] = pretitify(new_df['Decompo'])
    new_df['notes'] = new_df['Good_chords'].apply(lambda x: chords.from_shorthand(x) if 'N' not in x else np.nan)
    new_df['taille_sequence'] = new_df['notes'].apply(lambda x: len(x) if isinstance(x, list) else np.nan)
    # Les listes ne sont pas prises en charge dans les table sql
    new_df['Decompo'] = new_df['Decompo'].astype(str)
    new_df['notes'] = new_df['notes'].astype(str)
    return new_df

