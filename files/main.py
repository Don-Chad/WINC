__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
import zipfile
# import chardet

# def clean_cache():
#     try:
#         shutil.rmtree("cache")
        
#     except Exception as e:
#         os.mkdir("cache")
#     os.mkdir("cache")
path = "files/cache/"

def clean_cache():
    if os.path.isdir(path):
        # path = "cache/"
        for file_name in os.listdir(path):
            file = path + file_name
            print(file)
            if os.path.isfile(file):
                os.remove(file)
    else:
        os.mkdir(path)

# clean_cache()

# (os.path.isdir("cache"))

def cache_zip(path_to_file, cache):
    with zipfile.ZipFile(path_to_file, "r") as zip_ref:
        zip_ref.extractall(cache)

# cache_zip("/users/mark/WINC/files/data.zip", "/users/mark/WINC/files/cache")

# clean_cache()
dir_path = path

def cached_files():
    files = []
    for f in os.listdir(dir_path):
        file_with_path = os.getcwd()+ "/" + dir_path +f
        files.append(file_with_path)
    return files


files = (cached_files())

print(files)

def find_password(files):
    Everything_all_at_once = []
    for file in files:
        # f = read(open(file, "r"))
        with open(file, "r", encoding='utf-8') as f:
            # result = chardet.detect(f.read())
            content = f.read() 
            # for everything in content:
            if "password" in content: 
                password = content[(content.find("password")+10):136] 
                print(password)
                return str(password)
    # if "password" in content:
    #     print(f"Found 'pass' in {file}")
    # else:
    #     print("no password found")
    # return(Everything_all_at_once)

find_password(files)

# correct_horse_battery_staple

# G = open(P, 'r')
# print(G.read())