"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
from ADT import list as lt
from ADT import orderedmap as map
from DataStructures import listiterator as it


"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo y retorna el catalogo inicializado.
    """
    catalog = {'booksTree':None,'booksList':None}
    catalog['booksTree'] = map.newMap ("BST")
    catalog['booksList'] = lt.newList("ARRAY_LIST")
    catalog['AccidentsTree'] = map.newMap ("BST")
    catalog['AccidentsList'] = lt.newList("ARRAY_LIST")

    return catalog


def newBook (row):
    """
    Crea una nueva estructura para almacenar un libro 
    """
    book = {"book_id": row['book_id'], "title":row['title'], "average_rating":row['average_rating'], "ratings_count":row['ratings_count']}
    return book
def newAccident (row):
    """
    Crea una nueva estructura para almacenar un libro 
    """
    accident = {"id": row['ID'], "Time": {}, "Country":row['Country']}
    accident["Time"]["DateI"]= row['Start_Time'].split(" ")[0]
    accident["Time"]["DateF"]= row['End_Time'].split(" ")[0]
    accident["Time"]["HourI"]= row['Start_Time'].split(" ")[1]
    accident["Time"]["HourF"]= row['End_Time'].split(" ")[1]
    accident["Time"]["DateHI"]= lt.newList("ARRAY_LIST")
    accident["Time"]["DateHF"]= lt.newList("ARRAY_LIST")
    return accident

def newAccidentDate(catalog, row):
    accident = {"id": None, "Date": row["Start_Time"].split(" ")[0]}
    accident["id"]= lt.newList("ARRAY_LIST")
    lt.addLast(accident['id'],row['ID'])

    return accident 

def addBookList (catalog, row):
    """
    Adiciona libro a la lista
    """
    books = catalog['booksList']
    book = newBook(row)
    lt.addLast(books, book)
def addAccidentList (catalog, row):
    """
    Adiciona libro a la lista
    """
    accidents = catalog['AccidentsList']
    accident = newAccident(row)
    lt.addLast(accidents, accident)

def addAccidentDate (catalog, row):
    """
    Adiciona libro al map con key=title
    """
    #catalog['booksTree'] = map.put(catalog['booksTree'], int(book['book_id']), book, greater)
    Accidents= catalog['AccidentsTree']
    Exist=map.get(Accidents,row["Start_Time"].split(" ")[0], greater)
    if Exist:
        lt.addLast(Exist['id'],row['ID'])
        map.put(catalog['AccidentsTree'],row["Start_Time"].split(" ")[0],Exist, greater)
        #director['sum_average_rating'] += float(row['vote_average'])
    else:
        Accident= newAccidentDate(catalog, row)
        map.put(Accidents, Accident['Date'], Accident, greater)
        

def addAccidentMap1 (catalog, row):
    """
    Adiciona libro al map con key=title
    """
    accident= newAccident(row)
    #catalog['booksTree'] = map.put(catalog['booksTree'], int(book['book_id']), book, greater)
    catalog['AccidentsTree']  = map.put(catalog['AccidentsTree'] , accident['Time']["DateHI"] , accident, greater)



# Funciones de consulta


def getBookMap (catalog, bookTitle):
    """
    Retorna el libro desde el mapa a partir del titulo (key)
    """
    return map.get(catalog['booksTree'], bookTitle, greater)

def rankBookMap (catalog, bookTitle):
    """
    Retorna la cantidad de llaves menores (titulos) dentro del arbol
    """
    return map.rank(catalog['booksTree'], bookTitle, greater)

def selectBookMap (catalog, pos):
    """
    Retorna la operación select (titulos) dentro del arbol
    """
    return map.select(catalog['booksTree'], pos) 


# Funciones de comparacion

def compareByKey (key, element):
    return  (key == element["key"] )  

def compareByTitle(bookTitle, element):
    return  (bookTitle == element['title'] )

def greater (key1, key2):
    if ( key1 == key2):
        return 0
    elif (key1 < key2):
        return -1
    else:
        return 1