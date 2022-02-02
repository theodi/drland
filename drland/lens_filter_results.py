import csv 

from numpy import NaN
import pandas as pd

import filepaths


def filter_results(results_df) -> pd.DataFrame:

    with open(filepaths.FUNDERS_INCLUDE, "r") as file_in:
        funders_include = list(set(file_in.read().splitlines()))

    include_inds = []
    all_funders = set()
    for index, row in results_df.iterrows():
        if row['Funding'] is NaN:
            continue
        
        funders = row['Funding'].split(';')
        funders = [funder.strip().replace(',', ' ') for funder in funders]
        all_funders.update(funders)
        overlap = list(set.intersection(set(funders_include), set(funders)))
        if len(overlap) > 0:
            include_inds.append(index) 
    
    all_funders = list(sorted(all_funders, key=str.casefold))

    with open(filepaths.ALL_FUNDERS_LENS_RESULTS, 'w') as file_out:
        writer = csv.writer(file_out)
        writer.writerow(["Funder", "Include"])
        for funder in all_funders:
            writer.writerow([funder, ""])
            # file_out.write(funder + "\n")
    # not_include_inds = list(set(results_df.index) - set(include_inds))
    # results_df.loc[results_df.index[not_include_inds]].to_csv(filepaths.LENS_RESULTS_FILTER_NOT)

    return results_df.loc[results_df.index[include_inds]]


if __name__ == "__main__":

    lens_results_df = pd.read_csv(filepaths.LENS_RESULTS)
    filtered_results = filter_results(lens_results_df)
    filtered_results.to_csv(filepaths.LENS_RESULTS_FILTER)
