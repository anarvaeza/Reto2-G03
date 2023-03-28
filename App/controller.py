"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import time
import csv
from DISClib.ADT import list as lt
...
csv.field_size_limit(2147483647)


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(type):
    """
    Crea una instancia del modelo
    """

    control = {
        "model": None
    }
    control["model"] = model.new_data_structs(type)
    return control


# Funciones para la carga de datos

def datos_por_año(datos: list):
    dic_anios ={}  
    for dato in datos:
        if dato['Año'] not in dic_anios:
            dic_anios[dato['Año']]=[dato]

        else:
            dic_anios[dato['Año']].append(dato)

    return dic_anios




def load_data(control, filename):
    """
    Carga los datos del reto
    """
    file = cf.data_dir + filename
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    catalog = control['model']
    for line in input_file:
        model.add_data(catalog, line)

    
    
    return  catalog

def crear_list_iterable(catalog):
    lista = lt.iterator(catalog)
    return lista
    # TODO: Realizar la carga de datos

def data_size(control):
    return lt.size(control['model']["data"])
# Funciones de ordenamiento

def sort(control, tipo):
    """
    Ordena los datos del modelo
    """
    start_time = get_time()
    lista = model.sort(control["model"], tipo)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    tamano = data_size(control)
    return lista, delta_t, tamano

# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    data = model.get_data(control["model"], id)
    return data


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    start_time =get_time()
    req_1 = model.req_1(control["model"])
    end_time = get_time()
    delta_t = delta_time(start_time,end_time)
    return req_1, delta_t


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start_time =get_time()
    req_2 = model.req_2(control["model"])
    end_time = get_time()
    delta_t = delta_time(start_time,end_time)
    return req_2, delta_t


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start_time = get_time()
    req_3 = model.req_3(control["model"])
    end_time = get_time()
    delta_t = delta_time(start_time,end_time)
   
    tamanio = data_size(control)

    return req_3, tamanio, delta_t


def req_4(control,anio):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    req_4 = model.req_4(control["model"],anio)
    return req_4


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    start_time = get_time()
    req_5 = model.req_5(control["model"])
    end_time = get_time()
    delta_t = delta_time(start_time,end_time)
    return req_5, delta_t


def req_6(control,anio):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start_time = get_time()
    req_3 = model.req_6(control["model"],anio)
    end_time = get_time()
    delta_t = delta_time(start_time,end_time)
    tamanio = data_size(control)

    return req_3, tamanio, delta_t


def req_7(control, numero , anio_in, anio_fin):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start_time = get_time()
    req_7 = model.req_7(control["model"], numero, anio_in, anio_fin)
    end_time = get_time()
    delta_t = delta_time(start_time,end_time)
    return req_7, delta_t


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    req_8 = model.req_8(control["model"])
    return req_8


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def correr_todo(tipo, organizacion, tamaño):
    if tipo == 1:
        control = new_controller("ARRAY_LIST")
    elif tipo == 2:
        control = new_controller("SINGLE_LINKED")

    load_data(control, tamaño)
    if organizacion == "insertion":
        final = sort(control, 1)
         
 
    elif organizacion == "selection":
        final = sort(control, 2)

    elif organizacion == "shell":
        final = sort(control, 3)
    
    elif organizacion == "quick":
        final = sort(control, 4)
    
    elif organizacion == "merge":
        final = sort(control, 5)

    return final
