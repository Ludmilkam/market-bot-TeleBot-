import os

def find_path():
    path_abs = os.path.abspath(__file__ + "/..")
    path_abs = path_abs.split("/")
    del path_abs[-1]
    path_abs = "/".join(path_abs)
    return path_abs