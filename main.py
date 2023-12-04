import os

directory = "data/"

def get_files(directory):
    files = []
    for file in os.listdir(directory):
        print(file.split('_'))
        files.append(file)
    return files


if  __name__ == "__main__":
    get_files(directory)

