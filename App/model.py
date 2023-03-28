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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos




def new_data_structs(type):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {
        "data": None,
    }

    data_structs["data"] = lt.newList(datastructure=type,
                                     cmpfunction=compare)

    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    d = new_data(data["Año"], data["Código actividad económica"], data["Nombre actividad económica"],
                data["Código sector económico"],data["Nombre sector económico"],data["Código subsector económico"],
                data["Nombre subsector económico"],data["Costos y gastos nómina"], data["Aportes seguridad"], data["Aportes a entidades"], data["Efectivo y equivalentes"],
                data["Inversiones e instrumentos"], data["Cuentas y otros por cobrar"], data["Inventarios"], data["Propiedades"], data["Otros activos"], 
                data["Total patrimonio bruto"],data["Pasivos"], data["Total patrimonio líquido"], data["Ingresos ordinarios"], data["Ingresos financieros"], data["Otros ingresos"],
                data["Total ingresos brutos"], data["Devoluciones, rebajas"], data["Ingresos no renta"], data["Total ingresos netos"],data["Costos"],
                data["Gastos administración"], data["Gastos distribución"], data["Gastos financieros"], data["Otros gastos"], data["Total costos y gastos"], 
                data["Renta líquida ordinaria"], data["Pérdida líquida"], data["Compensaciones"], data["Renta líquida"], data["Renta presuntiva"], data["Renta exenta"], 
                data["Rentas gravables"], data["Renta líquida gravable"], data["Ingresos ganancias ocasionales"], data["Costos ganancias ocasionales"],
                data["Ganancias ocasionales no gravadas"], data["Ganancias ocasionales gravables"], data["Impuesto RLG"], data["Descuentos tributarios"], 
                data["Impuesto neto de renta"], data["Impuesto ganancias ocasionales"], data["Total Impuesto a cargo"], data["Anticipo renta año anterior"],
                data["Saldo a favor año anterior"], data["Autorretenciones"], data["Otras retenciones"], data["Total retenciones"], data["Anticipo renta siguiente año"],
                data["Saldo a pagar por impuesto"], data["Sanciones"], data["Total saldo a pagar"],data['Total saldo a favor'])
    lt.addLast(data_structs["data"], d)

    return data_structs


# Funciones para creacion de datos

def new_data(anio, cod_acti, nom_acti, cod_sector, nom_sector, cod_subsec, nom_subsec, costos_gastos_nom, apor_seguridad, apor_entidades, efec_equivalentes,inv_instru, 
             cuentas_cob, inventario, propiedades, otros_act, total_patrim_bruto, pasivos, total_patrim_liquido, ingresos_ordin, ingresos_finan, ingresos_otr, total_ingresos_brut,
             devoluciones_rebaj, ingresos_no_renta, total_netos, costos, gastos_ad, gastos_dist, gastos_finan, gastos_otr, total_c_g, renta_liq_ord, perdida_liq, compensaciones, 
             renta_liq, renta_presu, renta_exen, renta_grava, renta_liq_grava, ingreso_ganan_oca, costos_ganan_oca, ganan_oca_no_grava, ganan_oca_grava, impuesto_rlg, 
             descuentos_trib, imp_net_rent, imp_ganan_oca, total_imp_carg, antic_anio_ant, saldo_afav_ant, autoreten, otras_reten, total_reten, anti_rent_sig, 
             saldo_paga_imp, sanciones, total_s_pagar, total_favor):
    
    data = {'Año': 0, "Código actividad económica": "","Nombre actividad económica": "","Código sector económico": "","Nombre sector económico": "",
    "Código subsector económico": "","Nombre subsector económico": "", "Costos y gastos nómina": "", "Aportes seguridad": "", "Aportes a entidades": "", "Efectivo y equivalentes": "",
    "Inversiones e instrumentos":"", "Cuentas y otros por cobrar":"", "Inventarios": "", "Propiedades": "", "Otros activos":"", "Total patrimonio bruto":"", "Pasivos":"", 
    "Total patrimonio líquido":"", "Ingresos ordinarios":"", "Ingresos financieros":"", "Otros ingresos": "", "Total ingresos brutos":"", "Devoluciones, rebajas":"", 
    "Ingresos no renta":"","Total ingresos netos": "",  "Costos":"", "Gastos administración":"", "Gastos distribución":"", "Gastos financieros":"", "Otros gastos":"",
    "Total costos y gastos": "", "Renta líquida ordinaria":"","Pérdida líquida":"",  "Compensaciones":"", "Renta líquida":"","Renta presuntiva":"",  "Renta exenta":"",
    "Rentas gravables":"", "Renta líquida gravable":"", "Ingresos ganancias ocasionales":"", "Costos ganancias ocasionales":"", "Ganancias ocasionales no gravadas":"", 
    "Ganancias ocasionales gravables":"", "Impuesto RLG":"", "Descuentos tributarios":"", "Impuesto neto de renta":"", "Impuesto ganancias ocasionales":"", 
    "Total Impuesto a cargo":"", "Anticipo renta año anterior":"", "Saldo a favor año anterior":"", "Autorretenciones":"", "Otras retenciones":"", "Total retenciones":"",
    "Anticipo renta siguiente año":"", "Saldo a pagar por impuesto":"", "Sanciones":"", "Total saldo a pagar": "","Total saldo a favor": ''}

    data["Año"] = anio
    data["Código actividad económica"] = cod_acti
    data["Nombre actividad económica"] = nom_acti
    data["Código sector económico"] = cod_sector
    data["Nombre sector económico"] = nom_sector
    data["Código subsector económico"] = cod_subsec
    data["Nombre subsector económico"] = nom_subsec
    data["Costos y gastos nómina"] = costos_gastos_nom
    data["Aportes seguridad"] = apor_seguridad
    data["Aportes a entidades"] = apor_entidades
    data["Efectivo y equivalentes"] = efec_equivalentes
    data["Inversiones e instrumentos"] = inv_instru
    data["Cuentas y otros por cobrar"] = cuentas_cob
    data["Inventarios"] = inventario
    data["Propiedades"] = propiedades
    data["Otros activos"] = otros_act
    data["Total patrimonio bruto"] = total_patrim_bruto
    data["Pasivos"] = pasivos
    data["Total patrimonio líquido"] = total_patrim_liquido
    data["Ingresos ordinarios"] = ingresos_ordin
    data["Ingresos financieros"] = ingresos_finan
    data["Otros ingresos"] = ingresos_otr
    data["Total ingresos brutos"] = total_ingresos_brut
    data["Devoluciones, rebajas"] =devoluciones_rebaj
    data["Ingresos no renta"] = ingresos_no_renta
    data["Total ingresos netos"] = total_netos
    data["Costos"] = costos
    data["Gastos administración"] = gastos_ad
    data["Gastos distribución"] = gastos_dist
    data["Gastos financieros"] = gastos_finan
    data["Otros gastos"] = gastos_otr
    data["Total costos y gastos"] = total_c_g
    data["Renta líquida ordinaria"] = renta_liq_ord
    data["Pérdida líquida"] = perdida_liq
    data["Compensaciones"] = compensaciones
    data["Renta líquida"] = renta_liq
    data["Renta presuntiva"] = renta_presu
    data["Renta exenta"] = renta_exen
    data["Rentas gravables"] = renta_grava
    data["Renta líquida gravable"] = renta_liq_grava
    data["Ingresos ganancias ocasionales"] = ingreso_ganan_oca
    data["Costos ganancias ocasionales"] = costos_ganan_oca
    data["Ganancias ocasionales no gravadas"] = ganan_oca_no_grava
    data["Ganancias ocasionales gravables"] = ganan_oca_grava
    data["Impuesto RLG"] = impuesto_rlg
    data["Descuentos tributarios"] = descuentos_trib
    data["Impuesto neto de renta"]= imp_net_rent
    data["Impuesto ganancias ocasionales"] = imp_ganan_oca
    data["Total Impuesto a cargo"] = total_imp_carg
    data["Anticipo renta año anterior"] = antic_anio_ant
    data["Saldo a favor año anterior"] = saldo_afav_ant
    data["Autorretenciones"] = autoreten
    data["Otras retenciones"] = otras_reten
    data["Total retenciones"] = total_reten
    data["Anticipo renta siguiente año"] = anti_rent_sig
    data["Saldo a pagar por impuesto"] = saldo_paga_imp
    data["Sanciones"] = sanciones
    data["Total saldo a pagar"] = total_s_pagar
    data["Total saldo a favor"] = total_favor

    return data


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pos_data = lt.isPresent(data_structs["data"], id)
    if pos_data > 0:
        data = lt.getElement(data_structs["data"], pos_data)
        return data
    return None


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs["data"])


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    tamanio = data_size(data_structs)
    anios = crear_diccionario(data_structs, "data","Año", tamanio)
    #anios_filtrado = dict_filtrado(anios)
    #Crea un diccionario con los los años en sus llaves
    busca = "Total saldo a pagar"
    mayor = lt.newList(datastructure="ARRAY_LIST")
    for fecha in anios.keys():
        alto = encontrar_mayor(anios[fecha], busca)
        lt.addLast(mayor, alto)
    
    repeticiones = lt.size(mayor)
    respuesta = ordenar(mayor, "Año", repeticiones, 0)

    return (respuesta)
                
"""def dict_filtrado(diccionario_anios):
    dict_filtrado = {}
    for anio in diccionario_anios:
        parametros_filtrados = lt.newList(datastructure="ARRAY_LIST")
        parametros_og = lt.newList(datastructure="ARRAY_LIST")
        parametros_og = diccionario_anios[anio]
        lt.addLast(parametros_filtrados, parametros_og["Año"])
        lt.addLast(parametros_filtrados, parametros_og["Código actividad económica"])
        lt.addLast(parametros_filtrados, parametros_og["Nombre actividad económica"])
        lt.addLast(parametros_filtrados, parametros_og["Código sector económico"])
        lt.addLast(parametros_filtrados, parametros_og["Nombre sector económico"])
        lt.addLast(parametros_filtrados, parametros_og["Código subsector económico"])
        lt.addLast(parametros_filtrados, parametros_og["Nombre subsector económico"])
        lt.addLast(parametros_filtrados, parametros_og["Total ingresos netos"])
        lt.addLast(parametros_filtrados, parametros_og["Total costos y gastos"])
        lt.addLast(parametros_filtrados, parametros_og["Total saldo para pagar"])
        lt.addLast(parametros_filtrados, parametros_og["Total saldo a favor"])
        dict_filtrado[anio] = parametros_filtrados
    return dict_filtrado"""

def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    tamanio = data_size(data_structs)
    anios = crear_diccionario(data_structs, "data","Año", tamanio)
    
   
    # crea una lista con el mayor de cada año
    busca = "Total saldo a favor"

    mayor = lt.newList(datastructure="ARRAY_LIST")
    for fecha in anios.keys():
        alto = encontrar_mayor(anios[fecha], busca)
        lt.addLast(mayor, alto)
    
    repeticiones = lt.size(mayor)
    respuesta = ordenar(mayor, "Año", repeticiones, 0)
    
    
    return (respuesta)

 
    

    # TODO: Realizar el requerimiento 2
    
     ### Crea lista TAD ARRAY de subsectores por año
def crear_lista_subsectores_por_anio(lista_actividades):
   
    dic_subsecs ={}
    ## primero crea diccionario
    lista_actividades = lt.iterator(lista_actividades)
    
    for impuesto in lista_actividades:
        llave_subsector_dado =impuesto['Código subsector económico']
        if llave_subsector_dado not in dic_subsecs.keys():
            
            dict_subsector_dado = {}
            dict_subsector_dado['Año']=impuesto['Año']
            dict_subsector_dado['Código sector económico']=impuesto['Código sector económico']
            dict_subsector_dado['Nombre sector económico']=impuesto['Nombre sector económico']
            dict_subsector_dado['Código subsector económico']=impuesto['Código subsector económico']
            dict_subsector_dado['Nombre subsector económico']=impuesto['Nombre subsector económico']
            dict_subsector_dado['Total retenciones']=float(impuesto['Total retenciones'])
            dict_subsector_dado['Total ingresos netos']=float(impuesto['Total ingresos netos'])
            dict_subsector_dado['Total costos y gastos']=float(impuesto['Total costos y gastos'])
            dict_subsector_dado['Total saldo a pagar']=float(impuesto['Total saldo a pagar'])
            dict_subsector_dado['Total saldo a favor']=float(impuesto['Total saldo a favor'])
            dict_subsector_dado['Primeras y últimas 3 actividades en contribuir'] = 0

            dic_subsecs[llave_subsector_dado]=dict_subsector_dado
        else:
            ## Va contando los totales
            dict_subsector_dado =dic_subsecs[llave_subsector_dado]
            dict_subsector_dado['Total retenciones']+=float(impuesto['Total retenciones'])
            dict_subsector_dado['Total ingresos netos']+=float(impuesto['Total ingresos netos'])
            dict_subsector_dado['Total costos y gastos']+=float(impuesto['Total costos y gastos'])
            dict_subsector_dado['Total saldo a pagar']+=float(impuesto['Total saldo a pagar'])
            dict_subsector_dado['Total saldo a favor']+=float(impuesto['Total saldo a favor'])
    
     ### Lista Tad       
    lista_subsects=lt.newList(datastructure="ARRAY_LIST")
    for llave in dic_subsecs.keys():
        lt.addLast(lista_subsects,dic_subsecs[llave])

    return lista_subsects

def agregar_lista_de_6_a_subsector(subsector, lista_de_actividades_un_anio):
        
        ### vuelve array en objeto iterable
        lista_de_actividades_un_anio_1 = lt.iterator(lista_de_actividades_un_anio)
        codigo_subsect = subsector['Código subsector económico']
       
       
       
        #### Crear sublista del año solo de 1 subsecto Array
        lista_acotada_de_ACTIVIDADES_anio_y_subsector = lt.newList('ARRAY_LIST')
        #print(lt.size(lista_de_actividades_un_anio))
        #print(codigo_subsect)
       
       
       
       
        ### Agrega a la lista acotada los elementos filtrados por subsector
        for actividad in lista_de_actividades_un_anio_1:
           # print(type(actividad))
           # print(actividad['Código subsector económico'])

           ##Compara que sea del subsector dado
            if codigo_subsect == actividad['Código subsector económico']:
                lt.addLast(lista_acotada_de_ACTIVIDADES_anio_y_subsector,actividad)
                
        ### Ordena lista acotada por RETENCION
        quk.sort(lista_acotada_de_ACTIVIDADES_anio_y_subsector,sort_criteria_retenciones)
        #print(lista_acotada_de_ACTIVIDADES_anio_y_subsector)
        tamanio = lt.size(lista_acotada_de_ACTIVIDADES_anio_y_subsector)
        #print(tamanio)
        #### Crea lista PYTHON de 6 actividades relevantes 
        lista_6_activ_por_anio = []

        ### Condición para prevenir error out of range
        if tamanio>=6:
        
        
            
        
            lista_6_activ_por_anio.append(lt.getElement(lista_acotada_de_ACTIVIDADES_anio_y_subsector,1))
            lista_6_activ_por_anio.append(lt.getElement(lista_acotada_de_ACTIVIDADES_anio_y_subsector,2))
            lista_6_activ_por_anio.append(lt.getElement(lista_acotada_de_ACTIVIDADES_anio_y_subsector,3))
            lista_6_activ_por_anio.append(lt.getElement(lista_acotada_de_ACTIVIDADES_anio_y_subsector,tamanio-2))
            lista_6_activ_por_anio.append(lt.getElement(lista_acotada_de_ACTIVIDADES_anio_y_subsector,tamanio-1))
            lista_6_activ_por_anio.append(lt.getElement(lista_acotada_de_ACTIVIDADES_anio_y_subsector,tamanio))
        else:
            i =1
            while i<=tamanio:
                lista_6_activ_por_anio.append(lt.getElement(lista_acotada_de_ACTIVIDADES_anio_y_subsector,i))
                i+=1
        ### Añade la lista como elemento al dict subsect
        subsector['Primeras y últimas 3 actividades en contribuir']= lista_6_activ_por_anio
        #print(len(lista_6_activ_por_anio))
        return subsector



            

            






def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    lista_dicts_menores_anios = lt.newList('ARRAY_LIST')
    tamanio_data_structs = data_size(data_structs)
    dic_anios = crear_diccionario(data_structs, "data","Año", tamanio_data_structs)
    for lista_actividades_un_anio_dado in dic_anios.values():

      

        ####crea lista subsectkores patra el año dado
        lista_subsects_un_anio_dado = crear_lista_subsectores_por_anio(lista_actividades_un_anio_dado)

        ##encuentra menor subsect por retenciones
        menor = encontrar_menor(lista_subsects_un_anio_dado, 'Total retenciones')
        agregar_lista_de_6_a_subsector(menor,lista_actividades_un_anio_dado)
        lt.addLast(lista_dicts_menores_anios,menor)

    quk.sort(lista_dicts_menores_anios,sort_criteria)
    return lista_dicts_menores_anios
        



   
    
    
def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    tamanio = data_size(data_structs)
    anios = crear_diccionario(data_structs, "data","Año", tamanio)
    #Crea un diccionario con los los años en sus llaves
    busca = "Costos y gastos de nomina"
    sumatoria = lt.newList(datastructure="ARRAY_LIST")
    #Se crea una lista donde se almacena la sumatoria de cada año
    for fecha in anios.keys():
        for sector in fecha["Nombre sector económico"]:
            sumatoria = sector
        alto = encontrar_mayor(anios[fecha], busca)
        lt.addLast(mayor, alto)
        
    
    repeticiones = lt.size(mayor)
    respuesta = ordenar(mayor, "Año", repeticiones, 0)
    respuesta_filtrada = respuesta_filtrada_req4
    
    final = lt.iterator(respuesta_filtrada)
    return (final)
                
def respuesta_filtrada_req4(respuesta):
    respuesta_filtrada = lt.newList(datastructure="ARRAY_LIST")
    for elem in lt.iterator(respuesta):
        dic = {
            "Año": elem["Año"],
            "Código sector económico": elem["Código Sector Económico"],
            "Nombre sector económico": elem["Nombre Sector Económico"],
            "Código subsector económico": elem["Código Subsector Económico"],
            "Nombre subsector económico": elem["Nombre Subsector Económico"],
            """• Año.
• Código sector económico.
• Nombre sector económico.
• Código subsector económico.
• Nombre subsector económico.
• El total de costos y gastos nómina del subsector económico.
• El total ingresos netos del subsector económico.
• El total costos y gastos del subsector económico.
• El total saldo por pagar del subsector económico.
• El total saldo a favor del subsector económico.
• Las tres actividades económicas que menos aportaron y las tres actividades económicas que más
aportaron al valor total de costos y gastos de nómina en cada año, en donde cada elemento contendrá
la siguiente información:
o Código actividad económica.
o Nombre actividad económica.
o El total costos y gastos nómina.
o El total ingresos netos.
o El total costos y gastos.
o El total saldo por pagar.
o El Total saldo a favor."""
            "Total ingresos netos": elem["Total Ingresos Netos"],
            "Total costos y gastos": elem["Total Costos y Gastos"],
            "Total saldo para pagar": elem["Total Saldo a Pagar"],
            "Total saldo a favor": elem["Total Saldo a Favor"]
        }
        lt.addLast(respuesta_filtrada, dic)
    return respuesta_filtrada



def req_5(data_struct):
    """
    Función que soluciona el requerimiento 5
    """
    codigos= ["Descuentos tributarios", "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor" ]
    tamanio = data_size(data_struct)
    
    anios = crear_diccionario(data_struct,"data", "Año", tamanio)
    orden_anios = ordenar_dic(anios)
    organizado = {}
    extremos = {}
    respuesta = {}
    
    x = []
   
    
    for fecha in orden_anios.keys():
        orden = []
        repeticiones = lt.size(anios[fecha])
        if repeticiones <=6:
            orden.append(ordenar(orden_anios[fecha], "Descuentos tributarios", repeticiones, 0 ))

        else:
            
            orden.append(ordenar(orden_anios[fecha], "Descuentos tributarios", 3, 0 ))
            comienza = lt.size(anios[fecha])-3
            orden.append(ordenar(orden_anios[fecha], "Descuentos tributarios", 3, comienza ))


        extremos[fecha] = orden

        size = lt.size(orden_anios[fecha])

        sub_sector = crear_diccionario(orden_anios,fecha, "Código subsector económico", size )
        
        organizado[fecha] = sub_sector
        zona = lt.newList()
        for sector in organizado[fecha].keys():
            
            respuesta = {"Código sector económico": organizado[fecha][sector]["elements"][0]["Código sector económico"],
                         "Nombre sector económico": organizado[fecha][sector]["elements"][0]["Nombre sector económico"],
                         "Nombre subsector económico": organizado[fecha][sector]["elements"][0]["Nombre subsector económico"]}
            

            for codigo in codigos:
            
                suma = suma_variable(organizado[fecha][sector],codigo )
                
                respuesta[codigo] = suma
            
            organizado[fecha][sector] = respuesta
            
            final = dic(fecha,organizado[fecha][sector]["Código sector económico"], organizado[fecha][sector]["Nombre sector económico"],
                        
                        sector, organizado[fecha][sector]["Nombre subsector económico"],organizado[fecha][sector]["Descuentos tributarios"],
                        organizado[fecha][sector]["Total ingresos netos"],organizado[fecha][sector]["Total costos y gastos"],
                        organizado[fecha][sector]["Total saldo a pagar"],organizado[fecha][sector]["Total saldo a favor"] )
            lt.addLast(zona,final)
        x.append(zona)
    i = 0
    es = []
    while i < len(x):
        toca = encontrar_mayor(x[i],"Total descuentos tributarios del subsector economico" )
        es.append(toca)
        i+=1

    
    
    return(es, extremos)

def dic(anio, cod_sec, nom_sec, cod_subsec, nom_subsec, des, ing_net, cos_gas, pag, fav):
    dic ={"Año":anio,"Nombre sector económico": nom_sec, "Código subsector económico": cod_sec, "Código subsector económico": cod_subsec,
           "Nombre subsector económico": nom_subsec, "Total descuentos tributarios del subsector economico":des,
            "Total ingresos netos del subsector económico": ing_net,"Total costos y gastos del subsector ecnomico": cos_gas, 
            "Total saldo a pagar del subsector económico": pag, "Total saldo a favor subsector económico" : fav}

    # TODO: Realizar el requerimiento 5
    return dic

### Crea TAD ARRAY de 

    



def crear_lista_subsectores_totalizados_6(dic_subsects):
    
    ### Primero crear diccionario

    dic_totalizado_subsect = {}

    for llave_subsector in dic_subsects.keys():

        array_subsec = dic_subsects[llave_subsector]
        
        tamanio_array = lt.size(array_subsec)

        i =1
        while i<=tamanio_array:


                ###Accede diccionario de actividad
            actividad = lt.getElement(i)




            if actividad['Código subsector económico'] not in dic_totalizado_subsect.keys():

                dic_totalizado_subsect['Código subsector económico'] =  actividad['Código subsector económico']
                dic_totalizado_subsect['Nombre subsector económico'] =  actividad['Nombre subsector económico']
                dic_totalizado_subsect['Total ingresos netos'] =  float(actividad['Total ingresos netos'])
                dic_totalizado_subsect['Total costos y gastos'] =  float(actividad['Total costos y gastos'])
                dic_totalizado_subsect['Total saldo a favor'] =  float(actividad['Total saldo a favor'])
                dic_totalizado_subsect['Total saldo a pagar'] =  float(actividad['Total saldo a pagar'])

            else:
                dic_totalizado_subsect['Total ingresos netos'] +=  float(actividad['Total ingresos netos'])
                dic_totalizado_subsect['Total costos y gastos'] +=  float(actividad['Total costos y gastos'])
                dic_totalizado_subsect['Total saldo a favor'] +=  float(actividad['Total saldo a favor'])
                dic_totalizado_subsect['Total saldo a pagar'] +=  float(actividad['Total saldo a pagar'])

            
    lista_subsects=lt.newList(datastructure="ARRAY_LIST")
    for llave in dic_totalizado_subsect.keys():
        lt.addLast(dic_subsects[llave])

    return lista_subsects

                



def crear_lista_sectores_totalizados_por_anio(lista_subsects):
   
    dic_secs ={}
    ## primero crea diccionario
    lista_subsects = lt.iterator(lista_subsects)
    
    for subsector in lista_subsects:
        llave_sector_dado =subsector['Código sector económico']
        
        if subsector not in dic_secs.values():
            
            dict_sector_dado = {}

            dict_sector_dado['Nombre sector económico']=subsector['Nombre sector económico']
            dict_sector_dado['Código sector económico']=subsector['Código sector económico']


            dict_sector_dado['Total ingresos netos']=float(subsector['Total ingresos netos'])
            dict_sector_dado['Total costos y gastos']=float(subsector['Total costos y gastos'])
            dict_sector_dado['Total saldo a pagar']=float(subsector['Total saldo a pagar'])
            dict_sector_dado['Total saldo a favor']=float(subsector['Total saldo a favor'])
           
            ### Añade llave y valor primo a dic sector dado
            dic_secs[llave_sector_dado]=dict_sector_dado
        else:
            ## Va contando los totales
            dict_sector_dado =dic_secs[llave_sector_dado]
            dict_sector_dado['Total retenciones']+=float(subsector['Total retenciones'])
            dict_sector_dado['Total ingresos netos']+=float(subsector['Total ingresos netos'])
            dict_sector_dado['Total costos y gastos']+=float(subsector['Total costos y gastos'])
            dict_sector_dado['Total saldo a pagar']+=float(subsector['Total saldo a pagar'])
            dict_sector_dado['Total saldo a favor']+=float(subsector['Total saldo a favor'])
    
     ### Lista Tad       
    lista_sects=lt.newList(datastructure="ARRAY_LIST")
    for llave in dic_secs.keys():
        lt.addLast(lista_sects,dic_secs[llave])

    return lista_sects
         

       

       





def req_6(data_structs, anio):
    """
    Función que soluciona el requerimiento 6
    """
    tamanio_data_struct = data_size(data_structs)
    dic_anios = crear_diccionario (data_structs, 'data' ,'Año',tamanio_data_struct)
    array_del_anio = dic_anios[anio]
    tamanio_array_anio = lt.size(array_del_anio)


    #### Crear dic de actividades por subsector (llave subsector, valor array de actividades)
    dic_subsectores = crear_diccionario_de_TAD(array_del_anio, 'Código subsector económico', tamanio_array_anio )

    ### crea lista totalizada de subsectores

    lista_subsectores = crear_lista_subsectores_por_anio(array_del_anio)


    ### Crea lista de sectores más general

    lista_sectores = crear_lista_sectores_totalizados_por_anio(lista_subsectores)

    
    
    ### Encontray y añadir mayor y menos
    for sector in lt.iterator(lista_sectores):
        
        codigo_sector_dado = sector['Código sector económico']

        ###Proceso con mayor

        mayor_subsector_para_sector_dado = encontrar_mayor_con_condicion(lista_subsectores,'Total ingresos netos',codigo_sector_dado)

        codigo_mayor_subsector = mayor_subsector_para_sector_dado['Código subsector económico']

        lista_actividades_subsector_MAY_dado = dic_subsectores[codigo_mayor_subsector]

        mayor_actividad_mayor_subsector = encontrar_mayor(lista_actividades_subsector_MAY_dado,'Total ingresos netos')

        menor_actividad_mayor_subsector = encontrar_menor(lista_actividades_subsector_MAY_dado, 'Total ingresos netos')

        ## añadir mayor y menor actividad a mayor subsector

        mayor_subsector_para_sector_dado['Actividad que más contribuyó']= mayor_actividad_mayor_subsector

        mayor_subsector_para_sector_dado['Actividad que menos contribuyó']=menor_actividad_mayor_subsector

        ### añadir mayor subsector a sector dado

        sector['Subsector que más contribuyó'] = mayor_subsector_para_sector_dado




    ##### Proceso con menor

        menor_subsector_para_sector_dado = encontrar_menor_con_condicion(lista_subsectores, 'Total ingresos netos', codigo_sector_dado)
        
        codigo_menor_subsector = menor_subsector_para_sector_dado['Código subsector económico']

        lista_actividades_subsector_menor = dic_subsectores[codigo_menor_subsector]

        mayor_actividad_menor_subsector = encontrar_mayor(lista_actividades_subsector_menor,'Total ingresos netos')

        menor_actividad_menor_subsector = encontrar_menor(lista_actividades_subsector_menor,'Total ingresos netos')

        ## Añadir mayor y menor actividad a menor subsector

        menor_subsector_para_sector_dado['Actividad que más contribuyó']=mayor_actividad_menor_subsector

        menor_subsector_para_sector_dado['Actividad que menos contribuyó']= menor_actividad_menor_subsector



        ### Añadir menor subsector a sector dado
        sector['subsector que menos aportó'] = menor_subsector_para_sector_dado


    return lista_sectores

    










    
    


def req_7(data_structs, numero, anio_inicial, anio_final):
    """
    Función que soluciona el requerimiento 7
    """
    tamanio = data_size(data_structs)
    anios = crear_diccionario(data_structs,"data", "Año", tamanio)
    orden_anios = ordenar_dic(anios)
    
    por_anio = lt.newList()
    for fecha in orden_anios.keys():
        
        if int(fecha) >= int(anio_inicial) and int(fecha)<= int(anio_final):
            
            lt.addLast(por_anio, orden_anios[fecha])
    

    
    
    
    i = 1
    
                
                 

            
    
    listas_org = lt.newList(datastructure="ARRAY_LIST")
    while i<lt.size(por_anio)+1:
        inicial = lt.getElement(por_anio,i)

        merg.sort(inicial, sort_criteria_total_costos)
        lt.addLast(listas_org, inicial)

        i +=1
    e = 0
     

    final = lt.newList("SINGLE_LINKED")
    while e < int(numero):
        menor_primer = lt.newList(datastructure="ARRAY_LIST")
    
        for pos_lista in lt.iterator(listas_org):
            prim = lt.firstElement(pos_lista)
            lt.addLast(menor_primer, prim)
        
        men = encontrar_menor_pos(menor_primer, "Total costos y gastos")
        lt.addLast(final, men[0])
        elim = lt.getElement(listas_org, men[1])
        lt.removeFirst(elim)
        e+=1
        
    return final





               





    
   
    

def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if data_1["id"] > data_2["id"]:
        return 1
    elif data_1["id"] < data_2["id"]:
        return -1
    else:
        return 0

# Funciones de ordenamiento


def sort_criteria(impuesto_1, impuesto_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    if impuesto_1['Año']!= impuesto_2['Año']:
        cod_1 = impuesto_1['Año'].split()[0]
        cod_2 = impuesto_2['Año'].split()[0]
        return(float(impuesto_1['Año'])> float(impuesto_2['Año']))
    
    else:
        cod_1 = impuesto_1['Código actividad económica'].split()[0].split('/')[0]
        cod_2 = impuesto_2['Código actividad económica'].split()[0].split('/')[0]
        return(float(cod_1)>float(cod_2))
    


##### sort criteria para req 3
def sort_criteria_retenciones(a,b):

        cod_1 = a['Total retenciones'].split()[0].split('/')[0]
        cod_2 = b['Total retenciones'].split()[0].split('/')[0]
        return(float(cod_1)<float(cod_2))

def sort_criteria_total_ingresos_netos(a,b):

        cod_1 = a['Total ingresos netos'].split()[0].split('/')[0]
        cod_2 = b['Total ingresos'].split()[0].split('/')[0]
        return(float(cod_1)<float(cod_2))

def sort_criteria_total_costos(a,b):

        cod_1 = a["Total costos y gastos"].split()[0].split('/')[0]
        cod_2 = b["Total costos y gastos"].split()[0].split('/')[0]
        return(float(cod_1)<float(cod_2))

def sort(data_structs, tipo):
    if tipo == 1:
        sub_list = lt.subList(data_structs['data'],1,data_size(data_structs))
        lista =ins.sort(sub_list, sort_criteria)

    elif tipo == 2:

        sub_list = lt.subList(data_structs['data'],1,data_size(data_structs))
        lista =se.sort(sub_list, sort_criteria)
    elif tipo == 3:
        sub_list = lt.subList(data_structs['data'],1,data_size(data_structs))
        lista =sa.sort(sub_list, sort_criteria)
    
    elif tipo == 4:
        sub_list = lt.subList(data_structs['data'],1,data_size(data_structs))
        lista =quk.sort(sub_list, sort_criteria)
    
    elif tipo == 5:
        sub_list = lt.subList(data_structs['data'],1,data_size(data_structs))
        lista =merg.sort(sub_list, sort_criteria)
    
    return lista

#encontrar el mayor en una lista 
def encontrar_mayor(lista, criterio):
    
    i =0
    tamanio = lt.size(lista)
    mayor = 0
    respuesta ={}
    while i < tamanio:
        exacto = lt.getElement(lista,i)
        if float(exacto[criterio])>float(mayor):
            mayor = exacto[criterio]
            respuesta = exacto
        i+=1
    return respuesta

def encontrar_mayor_con_condicion(lista, criterio, condicion):
    
    i =0
    tamanio = lt.size(lista)
    mayor = 0
    respuesta ={}
    while i < tamanio:
        exacto = lt.getElement(lista,i)

        if exacto['Código sector económico'] ==  condicion:
        
             if float(exacto[criterio])>float(mayor):
                mayor = exacto[criterio]
                respuesta = exacto
        i+=1
    return respuesta

def encontrar_mayor_con_condicion(lista, criterio, condicion):
    
    i =0
    tamanio = lt.size(lista)
    mayor = 0
    respuesta ={}
    while i < tamanio:
        exacto = lt.getElement(lista,i)

        if exacto['Código sector económico'] ==  condicion:
        
             if float(exacto[criterio])>float(mayor):
                mayor = exacto[criterio]
                respuesta = exacto
        i+=1
    return respuesta

def encontrar_menor_con_condicion(lista, criterio, condicion):
    
    i =0
    tamanio = lt.size(lista)
    menor = 9999999999999
    respuesta ={}
    while i < tamanio:
        exacto = lt.getElement(lista,i)

        if exacto['Código sector económico'] ==  condicion:
        
             if float(exacto[criterio])<float(menor):
                menor = exacto[criterio]
                respuesta = exacto
        i+=1
    return respuesta

#### encontrar menor en TAD lista de diccionarios
def encontrar_menor(lista, criterio):
    
    i =0
    tamanio = lt.size(lista)
    respuesta ={}
    menor = 9999999999999
    while i <= tamanio:
        exacto = lt.getElement(lista,i)
        if float(exacto[criterio])<float(menor):
            respuesta = exacto
            menor = exacto[criterio]
        i+=1
    return respuesta

def encontrar_menor_pos(lista, criterio):
    
    i =0
    tamanio = lt.size(lista)
    respuesta ={}
    pos = 0
    menor = 9999999999999
    while i <= tamanio:
        exacto = lt.getElement(lista,i)
        if float(exacto[criterio])<float(menor):
            respuesta = exacto
            menor = exacto[criterio]
            pos = i
        i+=1
    return respuesta, pos

#organiza la informacion en diccionarios con la llave como el año
def crear_diccionario (data_structs, tipo ,categoria,tamanio):
    
    i =0
    dic = {}
    
    while i < tamanio:
        variable = lt.getElement(data_structs[tipo],i)
        momento = variable[categoria]
        if variable[categoria] not in dic.keys():
            dic[momento] = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(dic[momento], variable )
        elif variable[categoria] in dic.keys():
            lt.addLast(dic[momento], variable  )
        
        i +=1
    return dic

### Crea diccionario a partir de TAD lista(ARRAY o LINKED), no DataStructs:
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


#ordenar la lista en orden
def ordenar(lista, criterio, repeticiones, donde ):
    #organiza por años de menor a mayor
    respuesta = lt.newList("SINGLE_LINKED")
    
    for x in range( repeticiones):
        inicio = lt.getElement(lista,donde)
        superior = int(inicio[criterio])
        dict = inicio
        a = 0
        elim = 0
        while a < lt.size(lista):
            pos = lt.getElement(lista,a)
            if  int(pos[criterio])>int(superior) and int(pos[criterio]) != int(superior):
                superior = int(pos[criterio])
                elim = a
                dict = pos
            a+=1
            
        lt.addFirst(respuesta, dict)
        lt.deleteElement(lista, elim)

    return respuesta 
def ordenar_dic(dic):
    dic_keys = dic.keys()
    keys = sorted(dic_keys)
    orden_keys = {}
    for key in keys:
        orden_keys[key] = dic[key]
    return orden_keys
#suma la variable dentro de una lista con un criterio expecifico
def suma_variable(dic, suma):
    tamanio = lt.size(dic)
    i = 0
    valor = 0

    while i < tamanio:
        pos = lt.getElement(dic, i)
        valor += int(pos[suma])
        i+=1
    
    
    
    return valor