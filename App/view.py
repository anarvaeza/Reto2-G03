"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
import traceback
from tabulate import tabulate
import pandas as pd


def crear_diccionario_de_TAD (TAD ,categoria,tamanio):
    
    i =0
    dic = {}
    
    while i < tamanio:
        variable = lt.getElement(TAD,i)
        momento = variable[categoria]
        if variable[categoria] not in dic.keys():
            dic[momento] = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(dic[momento], variable )
        elif variable[categoria] in dic.keys():
            lt.addLast(dic[momento], variable  )
        
        i +=1
    return dic
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

######Filtra diccionarios por columnas a mostrar
def filtrar_dic_con_por_llaves(dic, lista_de_columnas_aMostrar):
    dic_filt ={}
    for llave in lista_de_columnas_aMostrar:
        dic_filt[llave]=dic[llave]

    return dic_filt

def filtrar_lista_dics_por_columnas(lista_dics,lista_columnas):
    lista_filt = []

    tamanio_lista = len(lista_dics)
    i = 0

    while i<tamanio_lista:
        dic_filt_dado = filtrar_dic_con_por_llaves(lista_dics[i],lista_columnas)
        lista_filt.append(dic_filt_dado)
        i+=1
    return lista_filt


def filtrar_lista_dics_por(lista_dics,lista_columnas):
    lista_filt = []

    tamanio_lista = lt.size(lista_dics)
    i = 0

    while i<tamanio_lista:
        a = lt.getElement(lista_dics,i)
        dic_filt_dado = filtrar_dic_con_por_llaves(a,lista_columnas)
        lista_filt.append(dic_filt_dado)
        i+=1
    return lista_filt
def new_controller(tipo):
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller(tipo)
    return control

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Listar las actividades económicas con mayor total saldo a pagar para todos los años")
    print("3- Listar las actividades económicas con mayor total saldo a favor para para todos los años")
    print("4- Encontrar el subsector económico con el menor total de retenciones para todos los años disponibles")
    print("5- Encontrar el subsector económico con los mayores costos y gastos de nómina para todos los años disponibles")
    print("6- Encontrar el subsector econmico con los mayores descuentos tributarios para todos los años disponibles")
    print("7- Encontrar la actividad económica con el mayor total de ingresos netos para cada sector económico en un año específico")
    print("8- Listar el TOP (N) de las actividades económicas con el menor total de costos y gastos para un periodo de tiempo")
    print("9-  Listar el TOP (N) de actividades económicas de cada subsector con los mayores totales de impuestos a cargo para un periodo de tiempo ")
    print("10- Obtener dato dado un ID")
    print("11- Carga, con tipo de ordenamientos")

    print("0- Salir")

def print_3_primeros_y_ultimos(lista, sample=3):

    size = lt.size(lista)
    lista_1 =lt.iterator(lista)
    losimp =[]
    
    if size<= sample*2:
        #print('Los',size,'primeros impuestos son:')
        for impuesto in lista_1:
            losimp.append(impuesto)

    else:
        #print('Los',sample, 'primeros y últimos impuestos son:')
        i=1
        while i <=sample:
            impuesto = lt.getElement(lista, i)
            losimp.append(impuesto)
            i+=1
        
        i= size- sample +1
        while i <=size:
            impuesto = lt.getElement(lista, i)
            losimp.append(impuesto)
            i+=1 
    return(losimp)

def menu_tipo_lista():
    print("Ahora que tipo de lista deseas ")
    print("1- ARRAY_LIST")
    print("2- SINGLE_LINKED")


def menu_tipo_ordenamiento():
    print("Ahora que tipo de ordenamiento deseas ")
    print("1- insertion sort")
    print("2- selection sort")
    print("3- shell sort")
    print("4- quick sort")
    print("5- merge sort")


def menu_nombre_archivo():
    print("Que porcentage de datos ")
    print("1-1%")
    print("2-5%")
    print("3-10%")
    print("4-20%")
    print("5-30%")
    print("6-50%")
    print("7-100%")

#los tipos de ordenamiento 
def menu_ordenamiento():
     menu_tipo_ordenamiento()
     ordenamiento = input('Seleccione una opción para continuar\n')
     try: 
        if int(ordenamiento) == 1:
            sort = "insertion"
            return sort
        elif int(ordenamiento) == 2:
            sort = "selection"
            return sort
        elif int(ordenamiento) == 3:
            sort = "shell"
            return sort
        elif int(ordenamiento) == 4:
            sort = "quick"
            return sort
        elif int(ordenamiento) == 5:
            sort = "merge"
            return sort
     except ValueError:
            print("Ingrese  opción válida.\n")
            traceback.print_exc()

    
     
# los nombres de los datos
def menu_archivo():
    menu_nombre_archivo()
    porcentaje = input('Seleccione una opción para continuar\n')
    try:
        if int(porcentaje) == 2:
            
            size ="Salida_agregados_renta_juridicos_AG-5pct.csv"
            return size
        elif int(porcentaje) == 3:
            size = "Salida_agregados_renta_juridicos_AG-10pct.csv"
            return size
        elif int(porcentaje) == 4:
            size = "Salida_agregados_renta_juridicos_AG-20pct.csv"
            return size
        elif int(porcentaje) == 5:
            size = "Salida_agregados_renta_juridicos_AG-30pct.csv"
            return size
        elif int(porcentaje) == 6:
            size = "Salida_agregados_renta_juridicos_AG-50pct.csv"
            return size
        elif int(porcentaje) == 1:
            size = "Salida_agregados_renta_juridicos_AG-small.csv"
            return size
        elif int(porcentaje) == 7:
            size = "Salida_agregados_renta_juridicos_AG-large.csv"
            return size
    except ValueError:
            print(" una opción válida.\n")
            traceback.print_exc()





def load_data(control, archivo):
    """
    Carga los datos
    """

    control_1 =controller.load_data(control, archivo)
    return control_1
def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    data = controller.get_data(control, id)
    print("El dato con el ID", id, "es:", data)


def print_req_1(control):
    """
    Función que imprime la solución del Requerimiento 1 en consola
    """
    respuesta = (controller.req_1(control))
    res = filtrar_lista_dics_por(respuesta[0],['Año',"Código actividad económica", "Nombre actividad económica", "Código sector económico","Nombre sector económico",
                 "Código subsector económico", 'Nombre subsector económico', "Total ingresos netos", "Total costos y gastos",
                 "Total saldo a pagar", "Total saldo a favor"] )
    print(tabulate(res, headers="keys", tablefmt= "grid", maxcolwidths=15, maxheadercolwidths=15  ))
    print(respuesta)

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    
    respuesta = (controller.req_2(control))
    res = filtrar_lista_dics_por(respuesta[0],['Año',"Código actividad económica", "Nombre actividad económica", "Código sector económico","Nombre sector económico",
                 "Código subsector económico", 'Nombre subsector económico', "Total ingresos netos", "Total costos y gastos",
                 "Total saldo a pagar", "Total saldo a favor"] )
    print(tabulate(res, headers="keys", tablefmt= "grid", maxcolwidths=15, maxheadercolwidths=15  ))
    print(respuesta[1])
   
    


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    req_3 = controller.req_3(control)

    respuesta = req_3[0]['elements']

    respuesta_filtrada =filtrar_lista_dics_por_columnas( respuesta,['Año','Código sector económico',
                                              'Nombre sector económico','Código subsector económico',
                                          'Nombre subsector económico', 'Total retenciones','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])

    #res_esp_2019 = respuesta[1]['Primeras y últimas 3 actividades en contribuir']

    tabulate_respuesta = tabulate(respuesta_filtrada, headers='keys', maxcolwidths =[10]*6, maxheadercolwidths=[10]*6)
    print(tabulate_respuesta)
    i=0
    tamanio_lista = len(respuesta)
    while i<tamanio_lista:

        anio_subsect = respuesta[i]['Año']
        lista_por_subsec = filtrar_lista_dics_por_columnas(respuesta[i]['Primeras y últimas 3 actividades en contribuir'],['Código actividad económica',
                                                            'Nombre actividad económica','Total retenciones','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
        
        lista_subsect_tabulete = tabulate(lista_por_subsec,headers='keys', maxcolwidths =[10]*7, maxheadercolwidths=[10]*7)
        print('Actividades que más y menos contribuyeron al subsector para ',anio_subsect)
        print(lista_subsect_tabulete)

        i+=1


    #print(type(res_esp_2016))
    #print(res_esp_2016)
    #df_2019 = pd.DataFrame(res_esp_2019)
    #df = pd.DataFrame(respuesta)
    #df_fil = df[['Año','Nombre subsector económico','Total retenciones']]
    #df_filt_2019 = df_2019[['Código actividad económica','Nombre actividad económica']]
    #print(df_fil)
    #print(df_filt_2019)
    print('TAMAÑO:  ',req_3[1])
    print('TIEMPO:  ',req_3[2])



def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    
    # TODO: Imprimir el resultado del requerimiento 4
    print(controller.req_4(control))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    respuesta = (controller.req_5(control))
    organizado = respuesta[0][0]
    extremos = (respuesta[0][1])
    
    print(tabulate(organizado, headers="keys", tablefmt="grid", maxcolwidths=15, maxheadercolwidths=15  ))




    heads = ['Año',"Código actividad económica", "Nombre actividad económica", "Código sector económico","Nombre sector económico",
                 "Código subsector económico", 'Nombre subsector económico', "Total ingresos netos", "Total costos y gastos",
                 "Total saldo a pagar", "Total saldo a favor"]
    for ext in extremos.keys():
        size = len(extremos[ext])
        if size != 1:
            fin = filtrar_lista_dics_por(extremos[ext][0], heads)
            print("The three economic activities that contributed the most in " + ext )
            print(tabulate(fin, headers="keys", tablefmt= "grid", maxcolwidths=15, maxheadercolwidths=15  ))
            

           
            print("The three economic activities that contributed the least in " + ext )
            fin = filtrar_lista_dics_por(extremos[ext][1], heads)
            
            print(tabulate(fin, headers="keys", tablefmt= "grid", maxcolwidths=15, maxheadercolwidths=15  ))
            

        else:
            tamanio = lt.size(extremos[ext][0])
            normal = lt.iterator(extremos[ext][0])
            print("There are only " + str(tamanio)+" economic activities in " + ext)
            fin = filtrar_lista_dics_por(extremos[ext][0], heads)
            print(tabulate(fin, headers="keys", tablefmt= "grid", maxcolwidths=15, maxheadercolwidths=15  ))
    print(respuesta[1])
def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    anio =input('Ingrse año a buscar  ')
    req_6 = controller.req_6(control,anio)
    req_6_lista = req_6[0]['elements']
    req_6_tamanio = req_6[1]
    req_6_time = req_6[2]

    respuesta_filtrada =filtrar_lista_dics_por_columnas( req_6_lista,['Código sector económico',
                                              'Nombre sector económico','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])


    tabulate_respuesta = tabulate(respuesta_filtrada, headers='keys', maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
    print(tabulate_respuesta)

    tamanio_lista = len(req_6_lista)

    i = 0
    while i< tamanio_lista:

        sector=req_6_lista[i]
        
        nombre_sector = sector['Nombre sector económico']

        print('Para el sector ',nombre_sector,' , el subsector económico que más aportó es:')
        subsector_mayor = sector['Subsector que más contribuyó']
        #print(subsector_mayor)
        subsector_mayor_filt = filtrar_dic_con_por_llaves(subsector_mayor,['Código subsector económico',
                                              'Nombre subsector económico','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
        
        #print(subsector_mayor_filt)
        
        subsect_mayor_tab = tabulate([subsector_mayor_filt], headers='keys', maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
        print(subsect_mayor_tab)
        
        print('Para el dicho subsector que más aporto, las actividades que más y menos aportaron respectivamente son:')

        actividad_mas_subsector_mayor = subsector_mayor['Actividad que más contribuyó']
        actividad_menos_subsector_mayor = subsector_mayor['Actividad que menos contribuyó']

        actividad_mas_subsector_mayor_filt = filtrar_dic_con_por_llaves(actividad_mas_subsector_mayor,['Código actividad económica',
                                              'Nombre actividad económica','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
        
        #print(actividad_mas_subsector_mayor_filt)
        
        actividad_menos_subsector_mayor_filt = filtrar_dic_con_por_llaves(actividad_menos_subsector_mayor,['Código actividad económica',
                                              'Nombre actividad económica','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
        

        tab_mayor_mayor = tabulate([actividad_mas_subsector_mayor_filt], headers='keys', maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
        tab_mayor_menor = tabulate([actividad_menos_subsector_mayor_filt], headers='keys', maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
        print(tab_mayor_mayor)
        print(tab_mayor_menor)



        ### Ahora con menor
        print('Para el sector ',nombre_sector,' , el subsector económico que MENOS aportó es:')
        subsector_menor = sector['subsector que menos aportó']
        #print(subsector_mayor)
        subsector_menor_filt = filtrar_dic_con_por_llaves(subsector_menor,['Código subsector económico',
                                              'Nombre subsector económico','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
        
        #print(subsector_mayor_filt)
        
        subsect_menor_tab = tabulate([subsector_menor_filt], headers='keys', maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
        print(subsect_menor_tab)
        
        print('Para el dicho subsector que MENOS aporto, las actividades que MÁS y MENOS aportaron respectivamente son:')

        actividad_mas_subsector_menor = subsector_menor['Actividad que más contribuyó']
        actividad_menos_subsector_menor = subsector_menor['Actividad que menos contribuyó']

        actividad_mas_subsector_menor_filt = filtrar_dic_con_por_llaves(actividad_mas_subsector_menor,['Código actividad económica',
                                              'Nombre actividad económica','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
        
        #print(actividad_mas_subsector_mayor_filt)
        
        actividad_menos_subsector_menor_filt = filtrar_dic_con_por_llaves(actividad_menos_subsector_menor,['Código actividad económica',
                                              'Nombre actividad económica','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
        

        tab_menor_mayor = tabulate([actividad_mas_subsector_menor_filt], headers='keys', maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
        tab_menor_menor = tabulate([actividad_menos_subsector_menor_filt], headers='keys', maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
        print(tab_menor_mayor)
        print(tab_menor_menor)

        i+=1


    
      

    #df_sectores = pd.DataFrame(req_6_lista)
    #df_sectores_imprimir = df_sectores[['Nombre sector económico','Total ingresos netos']]

    
    #print(df_sectores_imprimir)

    print('TAMAÑO: ',req_6_tamanio)
    print('TIEMPO: ', req_6_time)


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    anio_in = input("Ingrese el año inial " )
    anio_fin = input("Ingrese el año final ")
    numero = input("Numero de actividades a identificar ")
    respuesta = (controller.req_7(control, numero, anio_in, anio_fin))
    
    heads = ['Año',"Código actividad económica", "Nombre actividad económica", "Código sector económico","Nombre sector económico",
                 "Código subsector económico", 'Nombre subsector económico', "Total ingresos netos", "Total costos y gastos",
                 "Total saldo a pagar", "Total saldo a favor"]
    fin = filtrar_lista_dics_por(respuesta[0], heads)
    print(tabulate(fin, headers="keys", tablefmt= "grid", maxcolwidths=15, maxheadercolwidths=15  ))
    print(respuesta[1])


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    print (controller.req_8(control))
    
    


# Se crea el controlador asociado a la vista


# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                control = new_controller("ARRAY_LIST")
                archivo = menu_archivo()
                load_data(control,archivo)
                sort_data_result = controller.sort(control, 5)


                arraY_gen = control['model']['data']
                
                tamanio_arraygen = lt.size(arraY_gen)

                dic_anios =crear_diccionario_de_TAD(arraY_gen,'Año',tamanio_arraygen)

                i = 0

                for anio in dic_anios.keys():
                    array_por_anio = dic_anios[anio]
                    print('Para ',anio, ', los primeros y últimos impuestos son:')
                    lista_imprimir = print_3_primeros_y_ultimos(array_por_anio)
                    lista_imprimirfilt = filtrar_lista_dics_por_columnas(lista_imprimir,['Año','Código actividad económica','Nombre actividad económica',
                                                'Código sector económico','Nombre sector económico','Código subsector económico',
                                              'Nombre subsector económico','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
                    lkista_tab = tabulate(lista_imprimirfilt, headers='keys', maxcolwidths =[12]*11, maxheadercolwidths=[12]*11)
                    print(lkista_tab)
                    
                print(sort_data_result[1])
                
            
                
            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 10:
                id = input("Ingrese un id: ")
                print_data(control, id)
            
            elif int(inputs) == 11:
                menu_tipo_lista()
                opcion = input('Seleccione una opción para continuar\n')
                try:
                    if int(opcion) == 1:
                        tipo = 1
                        orden  = menu_ordenamiento()
                        tamaño = menu_archivo()
                        sort_data_result = controller.correr_todo(tipo,orden,tamaño)
                        ordenado =print_3_primeros_y_ultimos(sort_data_result[0])
                        print(tabulate(ordenado, headers="keys"))
                        print(sort_data_result[1])
                        print(sort_data_result[2])
                    elif int(opcion) == 2:
                        tipo = 2
                        orden  = menu_ordenamiento()
                        tamaño = menu_archivo()
                        sort_data_result = controller.correr_todo(tipo,orden,tamaño)
                        ordenado =print_3_primeros_y_ultimos(sort_data_result[0])
                        print(tabulate(ordenado, headers="keys"))
                        print(sort_data_result[1])
                        print(sort_data_result[2])
                    
                except ValueError:
                    print("Ingrese una opción válids.\n")
                    traceback.print_exc()






            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except ValueError:
            print("Ingrese una opción válida.\n")
            traceback.print_exc()
    sys.exit(0)
