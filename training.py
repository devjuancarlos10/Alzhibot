import openai
import json
import mysql.connector

# Establecer la clave de la API
openai.api_key = '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'

# Obtener los ID de archivo de los archivos JSONL
with open('data_train_copy.jsonl') as f:
    datos_train = json.load(f)
file_id_data_train = datos_train['archivo']['id']

with open('data_val_copy.jsonl') as f:
    datos_val = json.load(f)
file_id_data_val = datos_val['archivo']['id']

# Crear trabajo de ajuste fino
client = openai.Client()
client.fine_tuning.jobs.create(
  training_file=file_id_data_train, 
  validation_file=file_id_data_val,
  model="gpt-3.5-turbo-1106" #Puedes cambiar el modelo base según lo necesites.
)