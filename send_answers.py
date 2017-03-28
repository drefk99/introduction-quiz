import json
import pandas as pd
import requests

with open('introduction_quiz.json') as data_file:

	data=json.load(data_file)

df = pd.DataFrame(data)

url='localhost'
r=requests.post(url, params=data_file)

print(df)
