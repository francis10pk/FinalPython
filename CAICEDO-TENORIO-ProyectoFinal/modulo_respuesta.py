# Autor:
#   Nombre1 Apellido1
#   Nombre1 Apellido1

# Esta función booleana retorna
#       True - en caso de contener etiquetas
#       False - en caso de no contener etiquetas
# Argumentos:
#       tweet
def contieneEtiquetas(tweet):

    entidades = tweet['entities']
    etiquetas = entidades['hashtags']

    if (len(etiquetas) > 0):
        return True
    else:
        return False

# Esta función devuelve una lista de etiquetas en el tweet
#       lst - lista de etiquetas
# Argumentos:
#       tweet
def extraerEtiquetas(tweet):
    entidades = tweet['entities']
    etiquetas = entidades['hashtags']

    lst = []
    for etiqueta in etiquetas:
        lst.append(etiqueta["text"])
    return lst

def extraerEtiquetasPorFechas(tweet):
    entidades = tweet['entities']
    etiquetas = entidades['hashtags']
    fecha = tweet["created_at"]
    infoFecha=fecha.split(" ")

    lst = []
    for etiqueta in etiquetas:
        lst.append([etiqueta["text"],infoFecha[5],infoFecha[1],infoFecha[0]])
    return lst

# Esta función elimina los elementos repetidos en la lista
#       lst - lista con elementos únicos
# Argumentos:
#       lista
def eliminarRepetidos(lista):

    lst = []
    for elemento in lista:
        if elemento not in lst:
            lst.append(elemento)
    return lst

# Este módulo muestra los candidatos a seleccionar
# Argumentos:
#       candidatos - lista de candidatos
def menuOpciones(candidatos):
    print("Candidatos Presidenciales de Ecuador - 2017".center(60,'*'))
    print("Pulso DigitalEC".center(60,'*'))
    for indice, candidato in enumerate(candidatos):
        print("{}.- {}".format(indice+1, candidato))

# Esta función devuelve el índice del candidato seleccionado [0, len(candidatos)-1]
#       indice - indice del candidato seleccionado
# Argumentos:
#       candidtos - lista de candidatos
def opcionCandidatos(candidatos):
    indice = int(input("Ingrese el número del candidato a mostrar los datos: "))
    while (indice < 1 or indice > len(candidatos)):
        indice = int(input("Ingrese el número del candidato a mostrar los datos: "))

    return indice-1