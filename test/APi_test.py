'''
Descargar una biblioteca python llamada requests
'pip install requests
Tenemos que usarlo en este archivo
'''
import requests

# hacer una solicitud a la API
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
# Mostrar la respuesta
if response.status_code == 200:
    print('Respuesta de la API!')
    print(response.json()) #convertir la respuesta a un diccionario JSON
else:
    print('Error en la respuesta de la API', response.status_code)
