import os

# constant
year = 2023
months = list(range(1, 7)) # January until June
month_strings = [f"{x:02d}" for x in months]
brand = "esso"
cities = ["muenchen", "berlin", "frankfurt"]
fuel_type = "diesel"
rolling_window_size = 14

display_intermediate_dataframes = False
project_base_dir = "/home/vboxuser/dic-project/"
visualisation_dir = os.path.join(project_base_dir, "visualisation/")

def recursive_file_retrieval(path, directory_filters = [], results = []):
    if os.path.isfile(path):
        results.append(path)
    elif os.path.isdir(path):
        for f in os.listdir(path):
            full_path = os.path.join(path, f)
            if os.path.isdir(full_path) and f not in directory_filters:
                continue
            results.extend(recursive_file_retrieval(full_path, directory_filters, []))
    return results