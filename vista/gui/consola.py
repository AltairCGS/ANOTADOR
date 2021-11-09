from AnotadorUdeM.mundo.errores import LibroExistenteError, SeccionExistenteError, PaginaExistenteError, \
    NotaExistenteError
from AnotadorUdeM.mundo.mundo import Anotador, Libro, Seccion, Pagina


def menu():
    opt = 0
    while opt not in range(1,6):
        print(f"\n==== MENU DE OPCIONES ====")
        print("1. Agregar un libro")
        print("2. Agregar una seccion")
        print("3. Agregar una pagina")
        print("4. Agregar una nota")
        print("5. Salir")

        opt = int(input("\nIngrese una opcion: "))

        if opt not in range(1,6):
            print("\nERROR: OPCION NO VALIDA")

        return opt

if __name__ == "__main__":
    anotador = Anotador()
    libro = Libro()
    seccion = Seccion()
    pagina = Pagina()
    opcion = 0
    while opcion != 5:
        opcion = menu()

        if opcion == 1:
            print("\n>>>> AGREGAR UN LIBRO")
            titulo = input("Titulo del nuevo libro: ")
            try:
                anotador.agregar_libro(titulo)
            except LibroExistenteError as err:
                print(f"\nERROR: {err.msg}")
            else:
                print("\nINFO: El libro se agrego exitosamente")

        elif opcion == 2:
            print("\n>>>> AGREGAR UNA SECCION")
            titulo = input("Titulo de la nueva seccion")
            try:
                libro.agregar_seccion(titulo)
            except SeccionExistenteError as err:
                print(f"\nERROR: {err.msg}")
            else:
                print("\nINFO: La seccion se agrego exitosamente")

        elif opcion == 3:
            print("\n>>>> AGREGAR UNA PAGINA")
            titulo =  input("Titulo de la nueva pagina")
            try:
                seccion.agregar_pagina(titulo)
            except PaginaExistenteError as err:
                print(f"\nERROR: {err.msg}")
            else:
                print("\nINFO: La pagina se agrego exitosamente")

        elif opcion == 4:
            print("\n>>>> AGREGAR UNA NOTA")
            contenido = str(input("Contenido de la nota"))
            etiqueta = str(input("Etiqueta de la nota"))
            try:
                pagina.agregar_notas_pagina(contenido, etiqueta)
            except NotaExistenteError as err:
                print(f"\nERROR: {err.msg}")
            else:
                print("\nINFO: La nota se agrego exitosamente")
        elif opcion == 5:
            print("\n================")
            print("FIN DEL PROGRAMA")
            print("================")

