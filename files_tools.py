import os,json 
from dotenv import load_dotenv

load_dotenv(os.path.join("C:\Program Files\ScriptX",".env"))





path_scripts = os.getenv("path_scripts")
assets_path = os.getenv("assets_path")


def show_files(exts =[".txt"],all =False):
    files_temp = []
    
    if all == True:
        items = os.listdir(path_scripts)
        for i in items:
            if os.path.isdir(os.path.join(f"{path_scripts}/{i}")):
                i_ = f"{i} || DIR"
                items[items.index(i)] = i_
        return items
    else:
        for i in exts:
            for j in os.listdir(path_scripts):
                if j.endswith(i):
                    files_temp.append(j)
        
        return files_temp


       
def read_file(file_path):
    with open(file_path,"r",encoding="utf-8") as f:
        data = f.read()
    
    return data

def write_file(file_path,data):
    with open(file_path,"w",encoding="utf-8") as f:
        f.write(data)
    f.close()
    
    
def write_json(file_name,data):
    with open(file_name,"w") as f:
        f.write(str(json.dumps(data,indent=4)))


def load_json(file_name):
    data = json.load(open(file_name,"r"))
    return data
    

