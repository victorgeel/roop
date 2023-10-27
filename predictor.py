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


def predict_frame(target_frame: Frame) -> bool:
    image = Image.fromarray(target_frame)
    views = numpy.expand_dims(image, axis=0)
    _, probability = get_predictor().predict(views)[0]
    return probability > MAX_PROBABILITY


def predict_image(target_path: str) -> bool:
    

def predict_video(target_path: str) -> bool:
     return any(probability > MAX_PROBABILITY for probability in probabilities)
