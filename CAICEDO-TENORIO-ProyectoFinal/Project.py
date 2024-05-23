from modulo_datos import *
from modulo_respuesta import *
import time
from datetime import date
import sys

print("""
        ********************************************************************************************************
        *  **************************************************************************************************  *
        *  *                                     ENCUESTAS                                                  *  *
        *  *                                                                                                *  *
        *  *   1. Imagen Social                                                                             *  *
        *  *        a.Lista de etiquetas utilizadas                                                         *  *
        *  *        b.Etiqueta mas utilizada y numero de veces que aparece                                  *  *
        *  *        c.Cantidad de tweets por cada mes (considere el anio) y por cada dia de la semana       *  *
        *  *        d.Mes con mayor numero de tweets creados                                                *  *
        *  *        e.Dia de la semana con mayor numero de tweets creados                                   *  *
        *  *        f.Fuentes mas utilizadas desde las que se hizo un tweet, p.e: Android, Mac,etc          *  *
        *  *   2. Analizar el comportamiento de todos los competidores                                      *  *
        *  *        a.Candidato presidencial con el mayor número de tweets en cada una de las tres franjas  *  *
        *  *        horarias:                                                                               *  *
        *  *                § Mañana (00:00 – 11:59)                                                       *  *
        *  *                § Tarde (12:00 – 17:59)                                                        *  *
        *  *                § Noche (18:00 – 23:59)                                                        *  *
        *  *        b.Para todos los candidatos se mostrará la lista de usuarios a los que han respondido,  *  *
        *  *        número de veces que interactuaron y la lista de fechas que haninteractuado              *  *
        *  *   3. Presencia en las redes                                                                    *  *
        *  *        a.Mes con el mayor número de tweets con “corazones”                                     *  *
        *  *        b.Día de la semana con mayor número de tweets con “corazones”                           *  *
        *  *   4. Salir                                                                                     *  *
        *  *                                                                                                *  *
        *  **************************************************************************************************  *
        ********************************************************************************************************
    """)
print("\n")

while True:
    while True:
        op=int(input("Ingrese una opcion:"))
        if op<5 and op>0:
            break
        else:
            print("OPCION NO VALIDA!!!".center(10, "-"))

    if op==1:
        menuOpciones(candidatos)
        indice = opcionCandidatos(candidatos)
        candidato = candidatos[indice]
        tweets = cargarTweets(idCandidato=candidato, cargarTodos=False)
        etiquetas = []

        op2=str(input("Ingrese su opcion:"))

        if op2.upper()=="A":
            for tweet in tweets:
                diccionario = {}
                if contieneEtiquetas(tweet):
                    etiquetas = etiquetas + extraerEtiquetas(tweet)
                for i in etiquetas:
                    if i not in diccionario:
                        diccionario[i] = 1
                    else:
                        diccionario[i] = diccionario[i] + 1
            has=""
            valorMax=0
            for i in diccionario:
                if diccionario[i]>=valorMax:
                    has=i
                    valorMax=diccionario[i]
            print(has + " numero de veces repetidos: " + str(valorMax)+"\n")

        if op2.upper()=="B":
            for tweet in tweets:
                if contieneEtiquetas(tweet):
                    etiquetas = etiquetas + extraerEtiquetas(tweet)
            etiquetas = eliminarRepetidos(etiquetas)
            print("\nHashtags utilizados en los tweets por {}: ".format(candidato))
            print("\n")
            for i, etiqueta in enumerate(etiquetas):
                print("{}.- {}".format(i + 1, etiqueta))
            print("\n")

        meses = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        if op2.upper()=="C":
            diccionario={}
            for tweet in tweets:
                if contieneEtiquetas(tweet):
                    etiquetas = etiquetas + extraerEtiquetasPorFechas(tweet)
            for i in range(len(etiquetas)):
                if etiquetas[i][1] not in diccionario:
                    diccionario[etiquetas[i][1]]={"Jan":[{},{},{},{},{},{},{}],"Feb":[{},{},{},{},{},{},{}],"Mar":[{},{},{},{},{},{},{}],"Apr":[{},{},{},{},{},{},{}],"May":[{},{},{},{},{},{},{}],"Jun":[{},{},{},{},{},{},{}],"Jul":[{},{},{},{},{},{},{}],"Aug":[{},{},{},{},{},{},{}],"Oct":[{},{},{},{},{},{},{}],"Nov":[{},{},{},{},{},{},{}],"Dec":[{},{},{},{},{},{},{}]}
                    if etiquetas[i][3]=="Mon":
                        (diccionario[etiquetas[i][1]][etiquetas[i][2]][0])[etiquetas[i][0]]=1
                    elif etiquetas[i][3]=="Tue":
                        (diccionario[etiquetas[i][1]][etiquetas[i][2]][1])[etiquetas[i][0]] = 1
                    elif etiquetas[i][3] == "Wed":
                        (diccionario[etiquetas[i][1]][etiquetas[i][2]][2])[etiquetas[i][0]] = 1
                    elif etiquetas[i][3] == "Thu":
                        (diccionario[etiquetas[i][1]][etiquetas[i][2]][3])[etiquetas[i][0]] = 1
                    elif etiquetas[i][3] == "Fri":
                        (diccionario[etiquetas[i][1]][etiquetas[i][2]][4])[etiquetas[i][0]] = 1
                    elif etiquetas[i][3] == "Sat":
                        (diccionario[etiquetas[i][1]][etiquetas[i][2]][5])[etiquetas[i][0]] = 1
                    elif etiquetas[i][3] == "Sun":
                        (diccionario[etiquetas[i][1]][etiquetas[i][2]][6])[etiquetas[i][0]] = 1
                else:
                    if etiquetas[i][3]=="Mon":
                        if etiquetas[i][0] not in (diccionario[etiquetas[i][1]][etiquetas[i][2]][0]):
                            (diccionario[etiquetas[i][1]][etiquetas[i][2]][0])[etiquetas[i][0]]=1
                        else:
                            (diccionario[etiquetas[i][1]][etiquetas[i][2]][0])[etiquetas[i][0]] = (diccionario[etiquetas[i][1]][etiquetas[i][2]][0])[etiquetas[i][0]]+1
                    elif etiquetas[i][3]=="Tue":
                        if etiquetas[i][0] not in (diccionario[etiquetas[i][1]][etiquetas[i][2]][1]):
                            (diccionario[etiquetas[i][1]][etiquetas[i][2]][1])[etiquetas[i][0]]=1
                        else:
                            (diccionario[etiquetas[i][1]][etiquetas[i][2]][1])[etiquetas[i][0]] = (diccionario[etiquetas[i][1]][etiquetas[i][2]][1])[etiquetas[i][0]]+1
                    elif etiquetas[i][3] == "Wed":
                        if etiquetas[i][0] not in (diccionario[etiquetas[i][1]][etiquetas[i][2]][2]):
                            (diccionario[etiquetas[i][1]][etiquetas[i][2]][2])[etiquetas[i][0]]=1
                        else:
                            (diccionario[etiquetas[i][1]][etiquetas[i][2]][2])[etiquetas[i][0]] = (diccionario[etiquetas[i][1]][etiquetas[i][2]][2])[etiquetas[i][0]]+1
                    elif etiquetas[i][3] == "Thu":
                        if etiquetas[i][0] not in (diccionario[etiquetas[i][1]][etiquetas[i][2]][3]):
                            (diccionario[etiquetas[i][1]][etiquetas[i][2]][3])[etiquetas[i][0]]=1
                        else:
                            (diccionario[etiquetas[i][1]][etiquetas[i][2]][3])[etiquetas[i][0]] = (diccionario[etiquetas[i][1]][etiquetas[i][2]][3])[etiquetas[i][0]]+1
                    elif etiquetas[i][3] == "Fri":
                        if etiquetas[i][0] not in (diccionario[etiquetas[i][1]][etiquetas[i][2]][4]):
                            (diccionario[etiquetas[i][1]][etiquetas[i][2]][4])[etiquetas[i][0]]=1
                        else:
                            (diccionario[etiquetas[i][1]][etiquetas[i][2]][4])[etiquetas[i][0]] = (diccionario[etiquetas[i][1]][etiquetas[i][2]][4])[etiquetas[i][0]]+1
                    elif etiquetas[i][3] == "Sat":
                        if etiquetas[i][0] not in (diccionario[etiquetas[i][1]][etiquetas[i][2]][5]):
                            (diccionario[etiquetas[i][1]][etiquetas[i][2]][5])[etiquetas[i][0]]=1
                        else:
                            (diccionario[etiquetas[i][1]][etiquetas[i][2]][5])[etiquetas[i][0]] = (diccionario[etiquetas[i][1]][etiquetas[i][2]][5])[etiquetas[i][0]]+1
                    elif etiquetas[i][3] == "Sun":
                        if etiquetas[i][0] not in (diccionario[etiquetas[i][1]][etiquetas[i][2]][6]):
                            (diccionario[etiquetas[i][1]][etiquetas[i][2]][6])[etiquetas[i][0]]=1
                        else:
                            (diccionario[etiquetas[i][1]][etiquetas[i][2]][6])[etiquetas[i][0]] = (diccionario[etiquetas[i][1]][etiquetas[i][2]][6])[etiquetas[i][0]]+1
            print(diccionario)
            for i in diccionario:
                print(i.center(25,"-"))
                for j in diccionario[i]:
                    print(j.ljust(10,"*"))
                    cont=0
                    for k in (diccionario.get(i)).get(j):
                        cont+=1
                        print("Dia" + str(cont))
                        for l in k:
                            print(l + " numero de veces: " + str((diccionario.get(i)).get(j)[cont-1].get(l)))
                        print("\n")

        if op2.upper()=="D":
            diccionario={}
            for tweet in tweets:
                fecha=tweet["created_at"]
                infoFecha=fecha.split(" ")
                if infoFecha[1] not in diccionario:
                    diccionario[infoFecha[1]]=1
                else:
                    diccionario[infoFecha[1]]+= 1
            mes=""
            valorMax=0
            for i in diccionario:
                if diccionario[i]>=valorMax:
                    mes=i
                    valorMax=diccionario[i]
            print(mes + " con un valor de " + str(valorMax) +" "+ "retweets")

        if op2.upper()=="E":
            diccionario={}
            for tweet in tweets:
                fecha=tweet["created_at"]
                infoFecha=fecha.split(" ")
                if infoFecha[0] not in diccionario:
                    diccionario[infoFecha[0]]=1
                else:
                    diccionario[infoFecha[0]]+= 1
            dia=""
            valorMax=0
            for i in diccionario:
                if diccionario[i]>=valorMax:
                    dia=i
                    valorMax=diccionario[i]
            print(dia + " con un valor de " + str(valorMax) +" "+ "retweets")

        if op2.upper()=="F":
            diccionario = {}
            for tweet in tweets:
                fuente = tweet["source"]
                infoFuente=fuente.split(">")
                if infoFuente[1] not in diccionario:
                    diccionario[infoFuente[1]] = 1
                else:
                    diccionario[infoFuente[1]] += 1
            for i in diccionario:
                print( i + " numero de veces: " + str(diccionario.get(i)))

    if op==2:
        op2=input("Ingrese su opcion:")

        if op2.upper()=="A":
            diccionario = {}
            for i in range(8):
                candidato = candidatos[i]
                nombreCandidato=obtenerCandidato(i)
                tweets = cargarTweets(idCandidato=candidato,cargarTodos=False)
                diccionario[nombreCandidato]={"Horario 1":0,"Horario 2":0,"Horario 3":0}
                for tweet in tweets:
                    fecha = tweet["created_at"]
                    infoFecha = fecha.split(" ")
                    tiempo = infoFecha[3].split(":")
                    horas = int(tiempo[0]) + (int(tiempo[1]) / 60) + (int(tiempo[2]) / 3600)
                    if horas>=0 and horas<12:
                        diccionario[nombreCandidato]["Horario 1"]+=1
                    elif horas>=12 and horas<18:
                        diccionario[nombreCandidato]["Horario 2"] += 1
                    elif horas>=18 and horas<24:
                        diccionario[nombreCandidato]["Horario 3"] += 1

            nombre1=""
            max1=0
            nombre2=""
            max2=0
            nombre3=""
            max3=0

            for i in diccionario:
                if diccionario[i]["Horario 1"]>max1:
                    max1=diccionario[i]["Horario 1"]
                    nombre1=i
                elif diccionario[i]["Horario 2"]>max2:
                    max2=diccionario[i]["Horario 2"]
                    nombre2=i
                elif diccionario[i]["Horario 3"]>max3:
                    max3=diccionario[i]["Horario 3"]
                    nombre3=i
            print("\n")
            print("Candidato con mayor numero de tweets horario 00:00 a 11:59".center(10,"-"))
            print(nombre1 + " " + str(max1))
            print("Candidato con mayor numero de tweets horario 12:00 a 17:59".center(10, "-"))
            print(nombre2 + " " + str(max2))
            print("Candidato con mayor numero de tweets horario 18:00 a 23:59".center(10, "-"))
            print(nombre3 + " " + str(max3))
            print("\n")

    if op==3:
        op2=input("Ingrese su opcion:")
        if op2.upper()=="A":
            menuOpciones(candidatos)
            indice = opcionCandidatos(candidatos)
            candidato = candidatos[indice]
            tweets = cargarTweets(idCandidato=candidato, cargarTodos=False)
            diccionario={}
            for tweet in tweets:
                fecha = tweet["created_at"]
                corazon = tweet["favorite_count"]
                infoFecha = fecha.split(" ")
                if (infoFecha[1] not in diccionario) and corazon>0:
                    diccionario[infoFecha[1]]=1
                elif corazon>0:
                    diccionario[infoFecha[1]]+=1
            mes=""
            valorMax=0
            for i in diccionario:
                if diccionario[i]>=valorMax:
                    valorMax=diccionario[i]
                    mes=i
            print("Mes con mayor numeros de tweets con corazones: "+ mes.center(5,"-"))

        if op2.upper() == "B":
            menuOpciones(candidatos)
            indice = opcionCandidatos(candidatos)
            candidato = candidatos[indice]
            tweets = cargarTweets(idCandidato=candidato, cargarTodos=False)
            diccionario = {}
            for tweet in tweets:
                fecha = tweet["created_at"]
                corazon = tweet["favorite_count"]
                infoFecha = fecha.split(" ")
                if (infoFecha[0] not in diccionario) and corazon > 0:
                    diccionario[infoFecha[0]] = 1
                elif corazon > 0:
                    diccionario[infoFecha[0]] += 1
            dia = ""
            valorMax = 0
            for i in diccionario:
                if diccionario[i] >= valorMax:
                    valorMax = diccionario[i]
                    dia = i
            print("Dia con mayor numeros de tweets con corazones: " + dia.center(5, "-"))


    if op==4:
        break