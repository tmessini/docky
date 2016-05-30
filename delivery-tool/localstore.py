import pickle
import sys


def save_object(obj, filename):
    try:
        with open(filename, 'wb') as output:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
    except IOError:
        print("Cannot open: ", filename)
    except:
        print("Unexpected error:", sys.exc_info()[0])


def load_object(filename):
    try:
        with open(filename, 'rb') as localstore:
            return pickle.load(localstore)
    except IOError:
        print("Cannot open: ", filename)
    except:
        print("Unexpected error:", sys.exc_info()[0])
