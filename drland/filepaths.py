from pathlib import Path
import os

ROOT_DIR = Path(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))
WORKS_RESULTS = ROOT_DIR / 'results' / 'works_results.csv'
WORKS_RESULTS_INCLUDE = ROOT_DIR / 'results' / 'works_results_include.csv'
WORKS_RESULTS_EXCLUDE = ROOT_DIR / 'results' / 'works_results_exclude.csv'
# DATA_RESEARCH_FUNDERS_JSON = ROOT_DIR / 'data' / 'data_research_funders.json'

FUNDERS_INCLUDE = ROOT_DIR / 'data' / 'funders_include.txt'
FUNDERS_EXCLUDE = ROOT_DIR / 'data' / 'funders_exclude.txt'
