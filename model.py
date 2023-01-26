# Upload an image to a flask website and use a trained fastai pk1 file to predict the image  

# Path: model.py
from pathlib import Path
from fastbook import *
from fastai.vision.widgets import *

path = Path("export.pk1")
learn = load_learner(path)

def predict_image(img_bytes):
    img = PILImage.create(img_bytes)
    pred,pred_idx,probs = learn.predict(img)
    if pred != 'hot dog':
        is_hotdog = 'Not a hot dog'
    else:
        is_hotdog = f'This is a {pred}. I am {probs[pred_idx]*100:.02f}% sure'
    return is_hotdog