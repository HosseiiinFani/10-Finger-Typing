import pickle
import os

if os.path.isfile("../context.pickle"):
    print("IS")
    with open('../context.pickle', 'rb') as f:
        loaded_obj = pickle.load(f)
        print(loaded_obj)
        if loaded_obj:
            difficulty = loaded_obj['difficulty']
            level_score = loaded_obj['score']
            raw_data = loaded_obj['phrases']
