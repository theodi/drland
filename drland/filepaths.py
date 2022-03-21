from pathlib import Path
import os

ROOT_DIR = Path(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

LENS_TRAINING_DATA = ROOT_DIR / 'data' / 'lens_training.spacy'
LENS_VALID_DATA = ROOT_DIR / 'data' / 'lens_valid.spacy'
