import os


#PATH = r'E:/projects/data'
PATH = r'D:\mapillary-data/data2'

class DataGenerator:
    def __init__(self):
        self.path = PATH
        self.fnames = [os.path.join(root, fname) for root, _, files in os.walk(self.path) for fname in files]

    def __getitem__(self, item):
        return self.fnames[item]
