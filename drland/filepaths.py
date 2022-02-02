from pathlib import Path
import os

ROOT_DIR = Path(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))
WORKS_RESULTS = ROOT_DIR / 'results' / 'works_results.csv'
WORKS_RESULTS_INCLUDE = ROOT_DIR / 'results' / 'works_results_include.csv'
WORKS_RESULTS_EXCLUDE = ROOT_DIR / 'results' / 'works_results_exclude.csv'

TOP_FUNDERS_RESULTS = ROOT_DIR / 'results' / 'top_funders_results.csv'
TOP_FUNDERS_RESULTS_INCLUDE = ROOT_DIR / 'results' / 'top_funders_results_include.csv'
TOP_FUNDERS_RESULTS_EXCLUDE = ROOT_DIR / 'results' / 'top_funders_results_exclude.csv'

FUNDERS_INCLUDE = ROOT_DIR / 'data' / 'funders_include.txt'
FUNDERS_EXCLUDE = ROOT_DIR / 'data' / 'funders_exclude.txt'

LENS_RESULTS = ROOT_DIR / 'results' / 'Lens Dataset - Pre-Cull (Ten keywords; Title, Abstract, Keyword, Field; 2012-2022; Has Funding) - Lens Dataset - Pre-Cull (Ten keywords; Title, Abstract, Keyword, Field; 2012-2022; Has Funding.csv'
LENS_RESULTS_FILTER = ROOT_DIR / 'results' / 'Lens Dataset (Ten keywords; Title, Abstract, Keyword, Field; 2012-2022; Has Funding; Limited to only UK funders).csv'
# LENS_RESULTS_FILTER_NOT = ROOT_DIR / 'results' / 'Lens Dataset - NOT INCLUDED Post-Cull (Ten keywords; Title, Abstract, Keyword, Field; 2012-2022; Has Funding) - Lens Dataset - Pre-Cull (Ten keywords; Title, Abstract, Keyword, Field; 2012-2022; Has Funding.csv'

ALL_FUNDERS_LENS_RESULTS = ROOT_DIR / 'results' / 'all_funders_in_lens_results.csv'

GTR_PROJECTS = ROOT_DIR / 'data' / 'projectsearch-1643043544989.csv'

