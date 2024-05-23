import time
from datetime import date
import sys

candidatos = ["ZuquilandaDuque","IvanEspinelM","CynthiaViteri6","daloes10",
              "PacoMoncayo","pesanteztwof","LassoGuillermo","Lenin"]

def obtenerCandidato(indice):
    candidato=candidatos[indice]
    return candidato

def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    formatStr       = "{0:." + str(decimals) + "f}"
    percents        = formatStr.format(100 * (iteration / float(total)))
    filledLength    = int(round(barLength * iteration / float(total)))
    bar             = '█' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()

def cargarTweets(idCandidato="", cargarTodos=True):
    tweets = []
    lines = []
    prefix = 'Cargando '

    if cargarTodos:
        prefix = prefix + 'todos los tweets de todos los candidatos'
        for candidato in candidatos:

            fo = open("tweets-" + candidato + ".txt", "r", encoding="UTF-8")
            lines = lines + list(fo)
            fo.close()
    elif idCandidato in candidatos:
        prefix = prefix + 'todos los tweets de '+idCandidato
        fo = open("tweets-" + idCandidato + ".txt", "r", encoding="UTF-8")
        lines = lines + list(fo)
        fo.close()

    i = 0
    l = len(lines)
    printProgress(i, l, prefix='Cargando Tweets:', suffix='Completo', barLength=50)

    for line in lines:
        i += 1
        printProgress(i, l, prefix=prefix, suffix='Completo', barLength=50)
        tweets.append(eval(line))

    return tweets

def cargarTweetsTodos(idCandidato=""):
    tweets = []
    lines = []
    prefix = 'Cargando '


    prefix = prefix + 'todos los tweets de '+idCandidato
    fo = open("tweets-" + idCandidato + ".txt", "r", encoding="UTF-8")
    lines = lines + list(fo)
    fo.close()

    return tweets


def tweetsMasAntiguos():
    meses = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    for candidato in candidatos:

        fo = open("tweets-" + candidato + ".txt", "r")
        lines = list(fo)
        fo.close()

        today = date.fromtimestamp(time.time())

        for line in lines:

            tweet = eval(line)
            fecha = tweet['created_at']
            dia, mes, numerodia, hora, tmz, anio = fecha.split()

            ndate = date(int(anio), meses.index(mes) + 1, int(numerodia))

            if ndate < today:
                today = ndate


        print("Tweet más antiguo: {} de {}".format(today, candidato))
