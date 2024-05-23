from modulo_datos import *
from modulo_respuesta import *


#Ejemplo de procesamiento de datos del candidato según el índice indicado.
#revisen la lista candidatos en modulo_datos


menuOpciones(candidatos)
indice = opcionCandidatos(candidatos)
candidato = candidatos[indice]

tweets = cargarTweets(idCandidato=candidato, cargarTodos=False)
etiquetas = []

for tweet in tweets:
    diccionario={}
    if contieneEtiquetas(tweet) :
        etiquetas = etiquetas + extraerEtiquetas(tweet)

etiquetas = eliminarRepetidos(etiquetas)
print("\nHashtags utilizados en los tweets por {}: ".format(candidato))

for i,etiqueta in enumerate(etiquetas):
    print("{}.- {}".format(i+1, etiqueta))