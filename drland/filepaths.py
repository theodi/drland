from pathlib import Path
import os

ROOT_DIR = Path(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))
FUNDERS_INCLUDE = ROOT_DIR / 'data' / 'funders_include.txt'
FUNDERS_EXCLUDE = ROOT_DIR / 'data' / 'funders_exclude.txt'

GTR_PROJECTS = ROOT_DIR / 'data' / 'projectsearch-1643043544989.csv'

