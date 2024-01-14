import json
import zipfile
import os
api_token = {"username":"diegoriosrios","key":"8b20c8cfa5e1d1a7bcc2213c0bcf3e4c"} ##contenido de archivo kaggle.json

##conectar a kaggle
with open("C:/Users/DIEGO/.kaggle/kaggle.json","w") as file:
    json.dump(api_token, file)

location = "C:/Users/DIEGO/Documents/proyecto_parcial/dataset"

##validar que la carpeta existe 
if not os.path.exists(location):
      ##si no existe la carpeta dataset entonces la creo
    os.mkdir(location)
else:
    ##si la carpeta existe, entonces voy a borrar su contenido
    for root, dirs, files in os.walk(location, topdown=False):
        for name in files:
            os.remove(os.path.join(root,name)) ##elimina todos los archivos 
        for name in dirs: 
            os.rmdir(os.path.join(root,name)) ##elimina todas las carpetas

##descargar dataset de kaggle
os.system("kaggle datasets download -d henryshan/starbucks -p C:/Users/DIEGO/Documents/proyecto_parcial/dataset")      

##descomprimir el archivo de kaggle
os.chdir(location)
for file in os.listdir():
    zip_ref = zipfile.ZipFile(file,"r") ##lee archivo .zip
    zip_ref.extractall() ##extrae el contenido de archivo .zip
    zip_ref.close() ##cierra archivo