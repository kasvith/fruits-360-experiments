import pickle

def load_pickle(path):
    with open(path, mode='rb') as file:
        # note the encoding type is 'latin1'
        data = pickle.load(file, encoding='latin1')
    
    features = data['features']
    labels = data['labels']
    names = data['names']
    
    return features, labels, names
