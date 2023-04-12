import pickle

# data = {
#     'username': "ABC",
#     'name': 'Ali'
# }

# with open('mypickle.pickle', 'wb') as f:
#     pickle.dump(data, f)

# with open('mypickle.pickle', 'rb') as f:
#     loaded_obj = pickle.load(f)
#     print(loaded_obj)

with open('data.pickle', 'wb') as f:
    pickle.dump(None, f)

# with open('mypickle.pickle', 'rb') as f:
#     loaded_obj = pickle.load(f)
#     print(loaded_obj)
#     if loaded_obj:
#         print("ASD")