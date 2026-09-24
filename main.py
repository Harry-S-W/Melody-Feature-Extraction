import os.path

from features import Features
import pandas as pd

"""
This python script extracts the following:

    - Mean F0 - DONE
    - Standard Error of Mean F0 
    - Median F0 - DONE
    - Uncertainty of Median F0 via Bootstrapping
    - F0 95th Percentile - DONE
    - Uncertainty of F0 (95th Percentile) via Bootstrapping
    - F0 5th Percentile  - DONE
    - Uncertainty of F0 (5th Percentile) via Bootstrapping
    - FO SD - DONE
    
Exports as wide and long CSV (can be adjusted to parquet for security/compression reasons)
"""

def main(path):
    # Iterates through files in path and extracts features

    feature_dictionary = {
        "File Name": [],
        "Mean F0": [],
        "Median F0": [],
        "95th F0": [],
        "5th F0": [],
        "SD F0": []
    }

    for sound_file in os.listdir(path):
        if os.path.exists(path+sound_file):
            sound_object =  Features(path + sound_file)
            mean_F0 = sound_object.mean_F_zero(sound_object.sound_object)
            median_F0 = sound_object.median_F_Zero(sound_object.sound_object)
            ninety_fifth_F0 = sound_object.ninety_fifth_F_Zero(sound_object.sound_object)
            fifth_F0 = sound_object.fifth_F_Zero(sound_object.sound_object)
            SD_F0 = sound_object.standard_deviation_F_Zero(sound_object.sound_object)

            feature_dictionary["File Name"].append(sound_file)
            feature_dictionary["Mean F0"].append(mean_F0)
            feature_dictionary["Median F0"].append(median_F0)
            feature_dictionary["95th F0"].append(ninety_fifth_F0)
            feature_dictionary["5th F0"].append(fifth_F0)
            feature_dictionary["SD F0"].append(SD_F0)

            # making it a CSV

            Feature_Dict_DF = pd.DataFrame(feature_dictionary)
            Feature_Dict_DF.to_csv("Features.csv", index=False)

            print(feature_dictionary)

        else:
            print(f"ERROR: <{path + sound_file} is not a valid path.")

if __name__ == "__main__":
    main("Data/")



