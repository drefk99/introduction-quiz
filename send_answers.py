import json
import pandas as pd
import requests
import sys

##Cargar archivo json
with open('introduction_quiz.json') as data_file:

	datajs=json.load(data_file)
##Variable para obetener argumentos del usuario
args=sys.argv
##URL que ingresa usuario
url=args[1]
##ejemplo 'http://localhost:9200/examen/jorge/intro?pretty=true'
##Posteo del json en la dirección 
r=requests.post(url, data=json.dumps(datajs))
##Descarga información de la URL despues del posteo
impre=requests.get(url)
df = impre.text
##Impresión en la terminal
print(df)
