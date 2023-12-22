import cython
import mido
import numpy as np
import scipy as sp
from madmom.audio.chroma import DeepChromaProcessor
from madmom.features.chords import DeepChromaChordRecognitionProcessor
from madmom.processors import SequentialProcessor

_pretrained_models = [f"{__file__.removesuffix('better_chroma.py')}chroma_models\chroma_dnn_{i}.pkl" for i in range(1,9)]

_dcp = DeepChromaProcessor(fmin=30, fmax=5500, unique_filters=False, models=_pretrained_models)
_decode = DeepChromaChordRecognitionProcessor()

def getChromaProcessor(models: list or str = [], fmin : int = 30, fmax : int = 5500, unique_filters : bool = False) -> DeepChromaProcessor :
    if models == []:
        return _dcp
    models = list(models) if type(models) == str else models
    return DeepChromaProcessor(fmin=fmin, fmax=fmax, unique_filters= unique_filters , models= models)

def getRecognitionProcessor(model : str = None, fps : int = 10) -> DeepChromaChordRecognitionProcessor:
    if model == None:
        return _decode
    return DeepChromaChordRecognitionProcessor(model = model, fps= fps)

def getSequentialProcessor(dcp = getChromaProcessor(), decode = _decode) -> DeepChromaChordRecognitionProcessor:
    return SequentialProcessor([dcp,decode])


