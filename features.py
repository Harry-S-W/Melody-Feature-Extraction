import parselmouth
from parselmouth.praat import call
from os import path

class Features:
    def __init__(self, file_path):
        self.file_path = file_path
        self.sound_object = ""
        if path.exists(file_path):
            self.sound_object = parselmouth.Sound(file_path)
        else:
            print(f"ERROR: <{file_path}> is not a valid path. \n\n Terminating")
            return

    def mean_F_zero(self, sound_object):
        pitch = sound_object.to_pitch()
        mean_pitch = call(pitch, "Get mean", 0, 0, "Hertz")

        print(f"Mean F0: {mean_pitch} Hz")
        return mean_pitch

    def standard_error_of_mean_F_Zero(self):
        print("placeholder")

    def median_F_Zero(self, sound_object):
        pitch = sound_object.to_pitch()
        median_pitch = call(pitch, "Get quantile", 0.0, 0.0, 0.5, "Hertz")

        print(f"Median F0: {median_pitch} Hz")
        return median_pitch

    def ninety_fifth_F_Zero(self, sound_object):
        pitch = sound_object.to_pitch()
        ninety_fifth_percentile = call(pitch, "Get quantile", 0.0, 0.0, 0.95, "Hertz")

        print(f"95th Percentile F0: {ninety_fifth_percentile} Hz")
        return ninety_fifth_percentile

    def fifth_F_Zero(self, sound_object):
        pitch = sound_object.to_pitch()
        fifth_percentile = call(pitch, "Get quantile", 0.0, 0.0, 0.05, "Hertz")

        print(f"5th Percentile F0: {fifth_percentile} Hz")
        return fifth_percentile

    def standard_deviation_F_Zero(self, sound_object):
        pitch = sound_object.to_pitch()
        SD = call(pitch, "Get standard deviation", 0.0, 0.0, "Hertz")

        print(f"Standard Deviation F0: {SD} Hz")
        return SD
