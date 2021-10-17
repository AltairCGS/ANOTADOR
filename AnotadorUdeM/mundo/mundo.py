from datetime import date

from AnotadorUdeM.mundo.errores import LibroExistenteError, SeccionExistenteError, PaginaExistenteError


class Nota:
    def __init__(self, contenido : str, etiqueta : str):
        self.contenido : str = contenido
        self.etiqueta : str = etiqueta
        self.fecha_creacion = date.today()
        self.destacada : int = 0
        #atributo que sirve para determinar si la nota es destacada o no (0 = no esta destacada, 1 = si es destacada), se manejara como propiedad para poder modificarla.


class Pagina:
    def __init__(self,titulo : str):
        self.titulo : str = titulo
        self.fecha_creacion = date.today()
        self.notas = []

    @property
    def _titulo(self):
        return self.titulo

    @_titulo.setter
    def _titulo(self, nuevo_titulo : str):
        self.titulo = nuevo_titulo

    def buscar_nota(self,etiqueta : str):
        #TODO: Este metodo en teoria deberia buscar todas las notas con la misma etiqueta y retornarlas
        pass

    def agregar_notas(self,contenido_nota : str, etiqueta_nota : str):
        #TODO: Agrega una nueva nota sin verificar que otras notas contengan la misma etiqueta
        pass


class Seccion:
    def __init__(self, titulo : str):
        self.titulo : str = titulo
        self.fecha_creacion = date.today()
        self.paginas = []

    @property
    def _titulo(self):
        return self.titulo

    @_titulo.setter
    def _titulo(self, nuevo_titulo : str):
        self.titulo = nuevo_titulo

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
                pagina._titulo = nuevo_titulo
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
            else:
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
                seccion._titulo = nuevo_titulo
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
        self.notas_destacadas = []

    def buscar_libro(self, titulo_libro: str):
        """
        Busca un libro con un titulo dado

        :param titulo_libro: un str con el titulo que se quiere buscar
        :return: Un objeto de la clase Libro o None si no existe ningun libro con el titulo dado
        """
        for libro in self.libros:
            if titulo_libro == libro.titulo:
                return libro
            else:
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