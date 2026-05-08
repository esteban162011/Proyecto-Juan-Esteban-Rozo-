"""
Agenda de peliculas.
Modulo de interaccion por consola.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.

"""
import modulo_peliculas as mod


def mostrar_informacion_pelicula(pelicula: dict) -> None:
    """Imprime los detalles de la pelicula.
    Parametros:
        pelicula (dict): La pelicula de la cual se van a mostrar los detalles.
    """
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]

    print("Nombre: " + nombre + " - Anio: " + str(anio) + " - Duracion: " + str(duracion) + " mins")
    print("Genero: " + genero + " - Clasificacion: " + clasificacion)

    if hora // 100 < 10:
        hora_formato = "0" + str(hora // 100)
    else:
        hora_formato = str(hora // 100)

    if hora % 100 < 10:
        min_formato = "0" + str(hora % 100)
    else:
        min_formato = str(hora % 100)

    print("Dia: " + dia + " - Hora: " + hora_formato + ":" + min_formato)


def ejecutar_encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict,
                                           p5: dict, p6: dict, p7: dict, p8: dict) -> None:
    """Ejecuta la opcion de encontrar la pelicula mas larga."""
    mas_larga = mod.encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5, p6, p7, p8)
    print("La pelicula mas larga es:")
    mostrar_informacion_pelicula(mas_larga)


def ejecutar_consultar_duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict,
                                                    p5: dict, p6: dict, p7: dict, p8: dict) -> None:
    """Ejecuta la opcion de consultar la duracion promedio de las peliculas."""
    promedio = mod.duracion_promedio_peliculas(p1, p2, p3, p4, p5, p6, p7, p8)
    print("La duracion promedio de las peliculas es: " + promedio + " (HH:MM)")


def ejecutar_encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict,
                                 p5: dict, p6: dict, p7: dict, p8: dict) -> None:
    """Ejecuta la opcion de buscar peliculas de estreno (mas recientes que un anio dado)."""
    anio_str = input("Ingrese el anio limite para buscar estrenos: ")
    anio = int(anio_str)
    estrenos = mod.encontrar_estrenos(p1, p2, p3, p4, p5, p6, p7, p8, anio)
    print("Peliculas estrenadas despues de " + str(anio) + ": " + estrenos)


def ejecutar_cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict,
                                       p5: dict, p6: dict, p7: dict, p8: dict) -> None:
    """Ejecuta la opcion de consultar cuantas peliculas tienen clasificacion 18+."""
    cantidad = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5, p6, p7, p8)
    print("Cantidad de peliculas con clasificacion 18+: " + str(cantidad))


def ejecutar_buscar_pelicula(p1: dict, p2: dict, p3: dict, p4: dict,
                              p5: dict, p6: dict, p7: dict, p8: dict) -> None:
    """Ejecuta la opcion de buscar una pelicula por nombre y mostrar su informacion."""
    nombre = input("Ingrese el nombre de la pelicula que desea buscar: ")
    pelicula = mod.encontrar_pelicula(nombre, p1, p2, p3, p4, p5, p6, p7, p8)

    if pelicula is None:
        print("No hay ninguna pelicula con el nombre '" + nombre + "' en la agenda.")
    else:
        print("Informacion de la pelicula encontrada:")
        mostrar_informacion_pelicula(pelicula)


def ejecutar_reagendar_pelicula(p1: dict, p2: dict, p3: dict, p4: dict,
                                 p5: dict, p6: dict, p7: dict, p8: dict) -> None:
    """Ejecuta la opcion de reagendar una pelicula."""
    print("Reagendar una pelicula de la agenda")

    nombre = input("Ingrese el nombre de la pelicula que desea reagendar: ")
    pelicula = mod.encontrar_pelicula(nombre, p1, p2, p3, p4, p5, p6, p7, p8)

    if pelicula is None:
        print("No hay ninguna pelicula con el nombre '" + nombre + "' en la agenda.")
    else:
        nueva_hora = int(input("Ingrese la nueva hora (formato HHMM,): "))
        nuevo_dia = input("Ingrese el nuevo dia de la semana: ")
        control_str = input("¿Desea aplicar control horario? (s/n): ")
        control_horario = control_str.lower() == "s"

        resultado = mod.reagendar_pelicula(pelicula, nueva_hora, nuevo_dia, control_horario,
                                           p1, p2, p3, p4, p5, p6, p7, p8)

        if resultado:
            print("La pelicula fue reagendada exitosamente.")
            mostrar_informacion_pelicula(pelicula)
        else:
            print("No fue posible reagendar la pelicula.")
            print("Verifique que no exista conflicto de horario con otra pelicula")
            print("o que el nuevo horario cumpla las reglas de control horario.")


def ejecutar_decidir_invitar(p1: dict, p2: dict, p3: dict, p4: dict,
                              p5: dict, p6: dict, p7: dict, p8: dict) -> None:
    """Ejecuta la opcion de decidir si se puede invitar a alguien a ver una pelicula."""
    print("Decidir si se puede invitar a alguien a ver una pelicula")

    nom_peli = input("Ingrese el nombre de la pelicula: ")
    pelicula = mod.encontrar_pelicula(nom_peli, p1, p2, p3, p4, p5, p6, p7, p8)

    if pelicula is None:
        print("No hay ninguna pelicula con el nombre '" + nom_peli + "' en la agenda.")
    else:
        edad = int(input("Ingrese la edad del invitado: "))
        autorizacion_str = input("¿El invitado tiene autorizacion de sus padres? (s/n): ")
        autorizacion = autorizacion_str.lower() == "s"

        puede_invitar = mod.decidir_invitar(pelicula, edad, autorizacion)

        if puede_invitar:
            print("Si se puede invitar a esta persona a ver '" + nom_peli + "'.")
        else:
            print("No se puede invitar a esta persona a ver '" + nom_peli + "'.")
            print("Puede ser por restriccion de edad, genero de la pelicula o falta de autorizacion.")


def iniciar_aplicacion():
    """Inicia la ejecucion de la aplicacion por consola."""
    pelicula1 = mod.crear_pelicula("Shrek", "Familiar, Comedia", 0, 2001, "Todos", 1700, "Viernes")
    pelicula2 = mod.crear_pelicula("Get Out", "Suspenso, Terror", 0, 2017, "18+", 2330, "Sábado")
    pelicula3 = mod.crear_pelicula("Icarus", "Documental, Suspenso", 0, 2017, "18+", 800, "Domingo")
    pelicula4 = mod.crear_pelicula("Inception", "Acción, Drama", 0, 2010, "13+", 1300, "Lunes")
    pelicula5 = mod.crear_pelicula("The Empire Strikes Back", "Familiar, Ciencia-Ficción", 124, 1980, "7+", 1415, "Miércoles")
    pelicula6 = mod.crear_pelicula("Mario Bros", "Familiar", 0, 2023, "Todos", 1300, "Martes")
    pelicula7 = mod.crear_pelicula("Mufasa", "Familiar", 0, 2024, "Todos", 1300, "Viernes")
    pelicula8 = mod.crear_pelicula("El Exorcista", "Terror", 0, 1973, "18+", 2100, "Miércoles")

    ejecutando = True
    while ejecutando:
        print("\n\nMi agenda de peliculas para la semana de receso")
        print("-" * 50)

        print("Pelicula 1")
        mostrar_informacion_pelicula(pelicula1)
        print("-" * 50)

        print("Pelicula 2")
        mostrar_informacion_pelicula(pelicula2)
        print("-" * 50)

        print("Pelicula 3")
        mostrar_informacion_pelicula(pelicula3)
        print("-" * 50)

        print("Pelicula 4")
        mostrar_informacion_pelicula(pelicula4)
        print("-" * 50)

        print("Pelicula 5")
        mostrar_informacion_pelicula(pelicula5)
        print("-" * 50)

        print("Pelicula 6")
        mostrar_informacion_pelicula(pelicula6)
        print("-" * 50)

        print("Pelicula 7")
        mostrar_informacion_pelicula(pelicula7)
        print("-" * 50)

        print("Pelicula 8")
        mostrar_informacion_pelicula(pelicula8)
        print("-" * 50)

        ejecutando = mostrar_menu_aplicacion(pelicula1, pelicula2, pelicula3, pelicula4,
                                             pelicula5, pelicula6, pelicula7, pelicula8)

        if ejecutando:
            input("\nPresione Enter para continuar ... ")


def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4: dict,
                             p5: dict, p6: dict, p7: dict, p8: dict) -> bool:
    """Le muestra al usuario las opciones de ejecucion disponibles.
    Retorno:
        True si el usuario eligio una opcion diferente a salir.
        False si el usuario eligio salir.
    """
    print("\nMenu de opciones")
    print(" 1 - Buscar pelicula por nombre")
    print(" 2 - Consultar pelicula mas larga")
    print(" 3 - Consultar duracion promedio de las peliculas")
    print(" 4 - Consultar peliculas de estreno")
    print(" 5 - Consultar cuantas peliculas tienen clasificacion 18+")
    print(" 6 - Reagendar pelicula")
    print(" 7 - Verificar si se puede invitar a alguien")
    print(" 8 - Salir de la aplicacion")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_buscar_pelicula(p1, p2, p3, p4, p5, p6, p7, p8)
    elif opcion_elegida == "2":
        ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5, p6, p7, p8)
    elif opcion_elegida == "3":
        ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5, p6, p7, p8)
    elif opcion_elegida == "4":
        ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5, p6, p7, p8)
    elif opcion_elegida == "5":
        ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5, p6, p7, p8)
    elif opcion_elegida == "6":
        ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5, p6, p7, p8)
    elif opcion_elegida == "7":
        ejecutar_decidir_invitar(p1, p2, p3, p4, p5, p6, p7, p8)
    elif opcion_elegida == "8":
        continuar_ejecutando = False
        print("Hasta luego. ¡Disfruta tus peliculas!")
    else:
        print("La opcion '" + opcion_elegida + "' no es valida. Por favor elija entre 1 y 8.")

    return continuar_ejecutando


iniciar_aplicacion()
