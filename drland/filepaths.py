from pathlib import Path
import os

ROOT_DIR = Path(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))
DATA_RESEARCH_FUNDERS_FILEPATH = ROOT_DIR / 'data' / 'data_research_funders.csv'
