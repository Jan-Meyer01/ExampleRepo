#################################################################
## Script for leading .mat files and saving them as .npy files ##
#################################################################

# import function to load .mat data from scipy library
from scipy.io import loadmat
# import numpy for saving the data as a .npy file
import numpy as np
# import argument parser for command line use
import argparse
# import for joining paths and checking directories
from os.path import join, isdir
# import for creating directories
from os import mkdir

# parse folders for input and output 
parser = argparse.ArgumentParser()
parser.add_argument('-i','--input', default='data', help='folder for input')
parser.add_argument('-o','--output', default='data', help='folder for output')
args = parser.parse_args()

# create relative path to folders
path_input = join('.',args.input)
path_output = join('.',args.output)

# check if the input folder exists, else create error message
if not isdir(path_input):
    raise ValueError('The input directory does not exist!!')

# check if the output folder exists, else create it
if not isdir(path_output):
    mkdir(path_output)

# load .mat file
data = loadmat(join(path_input,'DummyData.mat'))

# save data as .npy file (add file extension automatically!)
np.save(join(path_output,'DummyData'), data)