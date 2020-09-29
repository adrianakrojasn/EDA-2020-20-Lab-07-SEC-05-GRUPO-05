import config as cf
from App import model
import datetime
import csv
from DISClib.ADT import orderedmap as om
from DISClib.ADT import list as lt
"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(analyzer, crimesfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    crimesfile = cf.data_dir + crimesfile
    input_file = csv.DictReader(open(crimesfile, encoding="utf-8-sig"),
                                delimiter=",")
    for crime in input_file:
        model.addCrime(analyzer, crime)

    return analyzer
    
def loadOffenses(analyzer, offensesFile):
    crime=analyzer['crimes']
    offenses= lt.newList('SINGLE_LINKED', cmpfunction=None)
    offensesFile = cf.data_dir + offensesFile
    input_file = csv.DictReader(open(offensesFile, encoding="utf-8-sig"),
                                delimiter=",")
    for offense in input_file:
        model.newOffenseEntry(offense, crime)

    return analyzer

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________


def crimesSize(analyzer):
    """
    Numero de crimenes leidos
    """
    return model.crimesSize(analyzer)


def indexHeight(analyzer):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(analyzer)


def indexSize(analyzer):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(analyzer)


def minKey(analyzer):
    """
    La menor llave del arbol
    """
    return model.minKey(analyzer)


def maxKey(analyzer):
    """
    La mayor llave del arbol
    """
    return model.maxKey(analyzer)


def getCrimesByRange(analyzer, initialDate, finalDate):
    """
    Retorna el total de crimenes en un rango de fechas
    """
    initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
    finalDate = datetime.datetime.strptime(finalDate, '%Y-%m-%d')
    return model.getCrimesByRange(analyzer, initialDate.date(),
                                  finalDate.date())


def getCrimesByRangeCode(analyzer, initialDate,
                         offensecode):
    """
    Retorna el total de crimenes de un tipo especifico en una
    fecha determinada
    """
    initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
    return model.getCrimesByRangeCode(analyzer, initialDate.date(),
                                      offensecode)


def getCrimesByDate(analyzer, Date):
    """
    Retorna el total de crimenes en un rango de fechas
    """
    Date= datetime.datetime.strptime(Date, '%Y-%m-%d')
    return model.getCrimesByDate(analyzer, Date.date())
