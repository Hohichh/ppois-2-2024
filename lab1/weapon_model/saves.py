import pickle
import os

def save_state(player, gunshop, filename):
    with open(filename, 'wb') as f:
        pickle.dump((player, gunshop), f)

def load_state(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    else:
        print("File not found.")
        return None