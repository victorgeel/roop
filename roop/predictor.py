import threading
import numpy
from PIL import Image
from keras import Model
from roop.typing import Frame

PREDICTOR = None
THREAD_LOCK = threading.Lock()
MAX_PROBABILITY = 0.85


def get_predictor() -> Model:
    global PREDICTOR

    
def clear_predictor() -> None:
    global PREDICTOR

    PREDICTOR = None

