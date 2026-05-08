"""
Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.


NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula en formato HHMM (ej: 1430)
            - dia (str): Indica que día de la semana se planea ver la película
"""

# Días considerados "entre semana" para el control horario
DIAS_ENTRE_SEMANA = ["Lunes", "Martes", "Miércoles", "Miercoles", "Jueves"]


def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int,
                   clasificacion: str, hora: int, dia: str) -> dict:
    """Construye y retorna el diccionario de una pelicula.
    Parametros:
        nombre (str): Nombre de la pelicula.
        genero (str): Genero(s) de la pelicula separados por comas.
        duracion (int): Duracion en minutos.
        anio (int): Anio de estreno.
        clasificacion (str): Clasificacion por edad ('Todos', '7+', '13+', '16+', '18+').
        hora (int): Hora de inicio en formato HHMM (ej: 1430 para 2:30 PM).
        dia (str): Dia de la semana en que se planea ver la pelicula.
    Retorna:
        dict: Diccionario con la informacion de la pelicula.
    """
    pelicula = {
        "nombre": nombre,
        "genero": genero,
        "duracion": duracion,
        "anio": anio,
        "clasificacion": clasificacion,
        "hora": hora,
        "dia": dia
    }
    return pelicula


def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,
                       p5: dict, p6: dict, p7: dict, p8: dict) -> dict:
    """Busca una pelicula por nombre entre las ocho registradas.
    Parametros:
        nombre_pelicula (str): Nombre de la pelicula a buscar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        p6 (dict): Diccionario que contiene la informacion de la pelicula 6.
        p7 (dict): Diccionario que contiene la informacion de la pelicula 7.
        p8 (dict): Diccionario que contiene la informacion de la pelicula 8.
    Retorna:
        dict: El diccionario de la pelicula encontrada, o None si no existe.
    """
    for pelicula in [p1, p2, p3, p4, p5, p6, p7, p8]:
        if pelicula["nombre"] == nombre_pelicula:
            return pelicula
    return None


def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict,
                                  p5: dict, p6: dict, p7: dict, p8: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las ocho peliculas recibidas.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        p6 (dict): Diccionario que contiene la informacion de la pelicula 6.
        p7 (dict): Diccionario que contiene la informacion de la pelicula 7.
        p8 (dict): Diccionario que contiene la informacion de la pelicula 8.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion.
    """
    mas_larga = p1
    if p2["duracion"] > mas_larga["duracion"]:
        mas_larga = p2
    if p3["duracion"] > mas_larga["duracion"]:
        mas_larga = p3
    if p4["duracion"] > mas_larga["duracion"]:
        mas_larga = p4
    if p5["duracion"] > mas_larga["duracion"]:
        mas_larga = p5
    if p6["duracion"] > mas_larga["duracion"]:
        mas_larga = p6
    if p7["duracion"] > mas_larga["duracion"]:
        mas_larga = p7
    if p8["duracion"] > mas_larga["duracion"]:
        mas_larga = p8
    return mas_larga


def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict,
                                 p5: dict, p6: dict, p7: dict, p8: dict) -> str:
    """Calcula la duracion promedio de las ocho peliculas que entran por parametro.
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        p6 (dict): Diccionario que contiene la informacion de la pelicula 6.
        p7 (dict): Diccionario que contiene la informacion de la pelicula 7.
        p8 (dict): Diccionario que contiene la informacion de la pelicula 8.
    Retorna:
        str: La duracion promedio de las peliculas en formato 'HH:MM'.
    """
    total_minutos = (p1["duracion"] + p2["duracion"] + p3["duracion"] + p4["duracion"] +
                     p5["duracion"] + p6["duracion"] + p7["duracion"] + p8["duracion"])
    promedio_minutos = total_minutos // 8

    horas = promedio_minutos // 60
    minutos = promedio_minutos % 60

    if horas < 10:
        horas_str = "0" + str(horas)
    else:
        horas_str = str(horas)

    if minutos < 10:
        minutos_str = "0" + str(minutos)
    else:
        minutos_str = str(minutos)

    return horas_str + ":" + minutos_str


def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict,
                       p5: dict, p6: dict, p7: dict, p8: dict, anio: int) -> str:
    """Busca entre las ocho peliculas cuales tienen como anio de estreno una fecha
       estrictamente posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        p6 (dict): Diccionario que contiene la informacion de la pelicula 6.
        p7 (dict): Diccionario que contiene la informacion de la pelicula 7.
        p8 (dict): Diccionario que contiene la informacion de la pelicula 8.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de las peliculas encontradas separadas por comas,
             o "Ninguna" si no hay coincidencias.
    """
    estrenos = ""

    if p1["anio"] > anio:
        estrenos = estrenos + p1["nombre"]

    if p2["anio"] > anio:
        if estrenos != "":
            estrenos = estrenos + ", "
        estrenos = estrenos + p2["nombre"]

    if p3["anio"] > anio:
        if estrenos != "":
            estrenos = estrenos + ", "
        estrenos = estrenos + p3["nombre"]

    if p4["anio"] > anio:
        if estrenos != "":
            estrenos = estrenos + ", "
        estrenos = estrenos + p4["nombre"]

    if p5["anio"] > anio:
        if estrenos != "":
            estrenos = estrenos + ", "
        estrenos = estrenos + p5["nombre"]

    if p6["anio"] > anio:
        if estrenos != "":
            estrenos = estrenos + ", "
        estrenos = estrenos + p6["nombre"]

    if p7["anio"] > anio:
        if estrenos != "":
            estrenos = estrenos + ", "
        estrenos = estrenos + p7["nombre"]

    if p8["anio"] > anio:
        if estrenos != "":
            estrenos = estrenos + ", "
        estrenos = estrenos + p8["nombre"]

    if estrenos == "":
        estrenos = "Ninguna"

    return estrenos


def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict,
                              p5: dict, p6: dict, p7: dict, p8: dict) -> int:
    """Indica cuantas peliculas de clasificacion '18+' hay entre los ocho diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        p6 (dict): Diccionario que contiene la informacion de la pelicula 6.
        p7 (dict): Diccionario que contiene la informacion de la pelicula 7.
        p8 (dict): Diccionario que contiene la informacion de la pelicula 8.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'.
    """
    contador = 0

    if p1["clasificacion"] == "18+":
        contador = contador + 1
    if p2["clasificacion"] == "18+":
        contador = contador + 1
    if p3["clasificacion"] == "18+":
        contador = contador + 1
    if p4["clasificacion"] == "18+":
        contador = contador + 1
    if p5["clasificacion"] == "18+":
        contador = contador + 1
    if p6["clasificacion"] == "18+":
        contador = contador + 1
    if p7["clasificacion"] == "18+":
        contador = contador + 1
    if p8["clasificacion"] == "18+":
        contador = contador + 1

    return contador


def reagendar_pelicula(peli: dict, nueva_hora: int, nuevo_dia: str,
                       control_horario: bool, p1: dict, p2: dict, p3: dict,
                       p4: dict, p5: dict, p6: dict, p7: dict, p8: dict) -> bool:
    """Verifica si es posible reagendar la pelicula. Comprueba que la nueva hora y dia no
       choquen con otra pelicula. Si hay control horario, aplica las siguientes reglas:
         - No se pueden programar documentales a las 22:00 (2200) o mas tarde.
         - No se pueden programar dramas los viernes.
         - Entre semana (lunes a jueves), no se pueden programar peliculas que inicien
           a las 23:00 (2300) o mas tarde, ni antes de las 6:00 (600).
    Parametros:
        peli (dict): Pelicula a reagendar.
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula (formato HHMM).
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula.
        control_horario (bool): Indica si se desea aplicar el control horario.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        p6 (dict): Diccionario que contiene la informacion de la pelicula 6.
        p7 (dict): Diccionario que contiene la informacion de la pelicula 7.
        p8 (dict): Diccionario que contiene la informacion de la pelicula 8.
    Retorna:
        bool: True si se pudo reagendar, False de lo contrario.
    """
    genero = peli["genero"].lower()

    if control_horario:
        # Regla 1: No programar documentales a las 22:00 o mas tarde
        if "documental" in genero and nueva_hora >= 2200:
            return False

        # Regla 2: No programar dramas los viernes
        if "drama" in genero and nuevo_dia.lower() == "viernes":
            return False

        # Regla 3: Entre semana, no antes de las 6:00 ni a las 23:00 o mas tarde
        dia_lower = nuevo_dia.lower()
        es_entre_semana = (dia_lower == "lunes" or dia_lower == "martes" or
                           dia_lower == "miércoles" or dia_lower == "miercoles" or
                           dia_lower == "jueves")

        if es_entre_semana:
            if nueva_hora < 600 or nueva_hora >= 2300:
                return False

    # Verificar que no haya conflicto de dia y hora con otra pelicula
    for otra in [p1, p2, p3, p4, p5, p6, p7, p8]:
        # No comparar la pelicula consigo misma
        if otra["nombre"] != peli["nombre"]:
            if otra["dia"] == nuevo_dia and otra["hora"] == nueva_hora:
                return False

    # Si paso todas las verificaciones, se reagenda
    peli["hora"] = nueva_hora
    peli["dia"] = nuevo_dia
    return True


def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool) -> bool:
    """Verifica si es posible invitar a la persona a ver la pelicula segun su edad,
       el genero de la pelicula y la autorizacion parental.
       Reglas:
         - Los mayores de edad (18 anos o mas) pueden ser invitados a cualquier pelicula.
         - Los menores de 15 anos no pueden ver peliculas de terror.
         - Los invitados de 10 anos o menos solo pueden ver peliculas de genero familiar.
         - Si la edad no cumple la clasificacion de la pelicula, se requiere autorizacion
           de los padres, excepto en documentales (en documentales no se acepta excepcion).
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado.
        edad_invitado (int): Edad del invitado.
        autorizacion_padres (bool): Indica si el invitado cuenta con autorizacion de sus padres.
    Retorna:
        bool: True si se puede invitar, False de lo contrario.
    """
    genero = peli["genero"].lower()
    clasificacion = peli["clasificacion"]

    # Regla 1: Los mayores de edad pueden ver cualquier pelicula
    if edad_invitado >= 18:
        return True

    # Regla 2: Menores de 15 anos no pueden ver peliculas de terror
    if edad_invitado < 15 and "terror" in genero:
        return False

    # Regla 3: Invitados de 10 anos o menos solo pueden ver peliculas de genero familiar
    if edad_invitado <= 10 and "familiar" not in genero:
        return False

    # Regla 4: Verificar clasificacion por edad
    # En documentales no aplica la excepcion de autorizacion de padres
    es_documental = "documental" in genero

    if clasificacion == "Todos":
        return True
    elif clasificacion == "7+":
        if edad_invitado >= 7:
            return True
        elif autorizacion_padres and not es_documental:
            return True
        else:
            return False
    elif clasificacion == "13+":
        if edad_invitado >= 13:
            return True
        elif autorizacion_padres and not es_documental:
            return True
        else:
            return False
    elif clasificacion == "16+":
        if edad_invitado >= 16:
            return True
        elif autorizacion_padres and not es_documental:
            return True
        else:
            return False
    elif clasificacion == "18+":
        # Ya verificamos edad >= 18 arriba, asi que aqui siempre es False
        return False
    else:
        return False
