from datetime import date

from AnotadorUdeM.mundo.errores import LibroExistenteError, SeccionExistenteError, PaginaExistenteError


class Nota:
    def __init__(self, contenido : str, etiqueta : str):
        self._contenido : str = contenido
        self.etiqueta : str = etiqueta
        self.fecha_creacion = date.today()
        self._destacada : int = 0
        #atributo que sirve para determinar si la nota es destacada o no (0 = no esta destacada, 1 = si es destacada), se manejara como propiedad para poder modificarla.

    @property
    def contenido(self):
        return self._contenido

    @contenido.setter
    def contenido(self, nuevo_contenido : str):
        self._contenido = nuevo_contenido

    @property
    def destacada(self):
        return self._destacada

    @destacada.setter
    def destacada(self, actulizar):
        self._contenido = actulizar


class Pagina:
    def __init__(self,titulo : str):
        self._titulo : str = titulo
        self.fecha_creacion = date.today()
        self.notas = []

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, nuevo_titulo : str):
        self._titulo = nuevo_titulo

    def buscar_nota(self,etiqueta : str):
        notas_encontradas = []
        for nota in self.notas:
            if etiqueta == nota.etiqueta:
                notas_encontradas.append(nota)
        return notas_encontradas

    def buscar_notas_fecha(self,fecha):
        notas_encontradas_fecha = []
        for nota in self.notas:
            if fecha == nota.fecha_creacion:
                notas_encontradas_fecha.append(nota)
        return notas_encontradas_fecha

    def mostrar_destacadas(self):
        notas_destacadas = []
        for nota in self.notas:
            if nota.destacada == 1:
                notas_destacadas.append(nota)
        return notas_destacadas

    def agregar_notas_pagina(self,contenido_nota : str, etiqueta_nota : str):
        nota = Nota(contenido_nota,etiqueta_nota)
        self.notas.append(nota)
        #Anotador.agregar_notas(nota)

    def modificar_nota(self,contenido,nuevo_contenido):
        for nota in self.notas:
            if contenido == nota.contenido:
                nota.contenido = nuevo_contenido
                break

    def borra_nota(self,etiqueta):
        for nota in self.notas:
            if etiqueta == nota.etiqueta:
                self.notas.remove(nota)

    def marcar_nota_destacada(self,etiqueta):
        for nota in self.notas:
            if etiqueta == nota.etiqueta:
                nota.destacada = 1


class Seccion:
    def __init__(self, titulo : str):
        self._titulo : str = titulo
        self.fecha_creacion = date.today()
        self.paginas = []

    @property
    def titulo(self):
        return self.titulo

    @titulo.setter
    def titulo(self, nuevo_titulo : str):
        self._titulo = nuevo_titulo

    def buscar_pagina(self, titulo_pagina: str):
        """
        Busca una pagina con un titulo dado
        (metodo resiclado para ver pagina)

        :param titulo_pagina: str con el titulo que se quiere buscar
        :return: Un objeto de la clase Pagina o None si no existe ninguna pagina con el titulo dado
        """
        for pagina in self.paginas:
            if titulo_pagina == pagina.titulo:
                return pagina
            else:
                return None

    def agregar_pagina(self, titulo_pagina):
        """
        Agrega una nueva pagina a la lista de paginas de la seccion

        :param titulo_pagina: str con el titulo de la nueva pagina
        :return: Objeto de la clase Pagina que se agrego a la seccion
        :raises: PaginaExistenteError: Si ya existe una pagina con el titulo dado
        """
        pagina = self.buscar_pagina(titulo_pagina)
        if pagina is None:
            pagina = Pagina(titulo_pagina)
            self.paginas.append(pagina)
            return pagina
        else:
            raise PaginaExistenteError(titulo_pagina, f"Ya existe una pagina con el titulo {titulo_pagina}")

    def modificar_pagina(self, titulo, nuevo_titulo):
        """
        Modifica el titulo de la pagina
        :param titulo: str con el titulo de la pagina a buscar
        :param nuevo_titulo: str con el nuevo titulo de la pagina
        """
        for pagina in self.paginas:
            if titulo == pagina.titulo:
                pagina.titulo = nuevo_titulo
                break

    def borrar_pagina(self, titulo : str):
        """
        Elimina una pagina de la lista de paginas de una seccion

        :param titulo: str con el titulo de la pagina a buscar y eliminar
        """
        pagina = self.buscar_pagina(titulo)
        self.paginas.remove(pagina)


class Libro:
    def __init__(self, titulo : str):
        self.titulo : str = titulo
        self.fecha_creacion = date.today()
        self.secciones = []

    def buscar_seccion(self, titulo_seccion: str):
        """
        Busca una seccion con un titulo dado
        (metodo resiclado para ver seccion)

        :param titulo_seccion:  un str con el titulo que se quiere buscar
        :return: Un objeto de la clase Seccion o None si no existe ninguna seccion con el titulo dado
        """
        for seccion in self.secciones:
            if titulo_seccion == seccion.titulo:
                return seccion
        return None

    def agregar_seccion(self, titulo_seccion: str):
        """
        Agrega una nueva seccion a la lista de secciones del libro
        :param titulo_seccion: str con el titulo de la nueva seccion
        :return: Objeto de la clase Seccion que se agrego al libro
        :raises SeccionExistenteError: Si ya existe una seccion con el titulo dado
        """
        seccion = self.buscar_seccion(titulo_seccion)
        if seccion is None:
            seccion = Seccion(titulo_seccion)
            self.secciones.append(seccion)
            return seccion
        else:
            raise SeccionExistenteError(titulo_seccion, f"Ya axiste una seccion con el titulo {titulo_seccion}")

    def modificar_seccion(self, titulo: str, nuevo_titulo: str):
        """
        Modifica el titulo de la seccion

        :param titulo: str con el titulo de la seccion a buscar
        :param nuevo_titulo: str con el nuevo titulo de la seccion
        """
        for seccion in self.secciones:
            if titulo == seccion.titulo:
                seccion.titulo = nuevo_titulo
                break

    def borrar_seccion(self, titulo: str):
        """
        Elimina una seccion de la lista de secciones en el libro
        :param titulo: str con el titulo de la seccion a buscar y eliminar
        """
        seccion = self.buscar_seccion(titulo)
        self.secciones.remove(seccion)


class Anotador:
    def __init__(self):
        self.libros = []
        self.notas = []
        self.notas_destacadas = []

    def agregar_notas(self,nota):
        self.notas.append(nota)

    def ver_notas(self,etiqueta):
        notas_encontradas = []
        for nota in self.notas:
            if etiqueta == nota.etiqueta:
                notas_encontradas.append(nota)
        return notas_encontradas

    def buscar_libro(self, titulo_libro: str):
        """
        Busca un libro con un titulo dado

        :param titulo_libro: un str con el titulo que se quiere buscar
        :return: Un objeto de la clase Libro o None si no existe ningun libro con el titulo dado
        """
        for libro in self.libros:
            if titulo_libro == libro.titulo:
                return libro
        return None

    def agregar_libro(self,libro_titulo):
        """
        Agrega un nuevo libro a la lista de Libros del Anotador

        :param libro_titulo: str con el titulo del nuevo libro
        :return: Objeto de la clase Libro que se agrego al anoptador
        :raises LibroExistenteError: Si ya existe un libro con el titulo dado
        """
        libro = self.buscar_libro(libro_titulo)
        if libro is None:
            libro = Libro(libro_titulo)
            self.libros.append(libro)
            return libro
        else:
            raise LibroExistenteError(libro_titulo, f"Ya existe un libro con el titulo {libro_titulo}")