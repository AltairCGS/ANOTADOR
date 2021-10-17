class AnotadorError(Exception):
    pass


class LibroExistenteError(AnotadorError):
    """
    Representa una excepción que indica que el libro ya existe en el anotador

    Attributes:
        titulo: un str que indica el titulo del libro que ya existe
        msg: Un str que contiene el mensaje de error
    """

    def __init__(self, titulo: str, msg: str):
        self.titulo: str = titulo
        self.msg: str = msg


class LibroNoExistenteError(AnotadorError):
    """
    Representa una exepción que indica que no existe un libro con un titulo dado

    Attributes:
        titulo: Un str que indica el titulo del libro que se esta buscando
        msg: un str que contiene el mensaje de error
    """
    def __init__(self, titulo: str, msg: str):
        self.titulo: str = titulo
        self.msg: str = msg


class SeccionExistenteError(AnotadorError):
    """
    Representa una excepcion que indica que la seccion ya existe en el libro

    Attributes:
        titulo: Un str que indica que el titulo de la seccion que ya existe
        msg: Un str que contiene el mensaje de error
    """
    def __init__(self, titulo: str, msg: str):
        self.titulo: str = titulo
        self.msg: str = msg


class SeccionNoExistenteError(AnotadorError):
    """
    Representa una exepcion que indica que no existe una seccion con el titulo dado

    Attributes:
        titulo: Un str que indica el titulo de la seccion que se esta buscando
        msg: Un str que contiene el mensaje de error
    """
    def __init__(self, titulo: str, msg: str):
        self.titulo: str = titulo
        self.msg: str = msg


class PaginaExistenteError(AnotadorError):
    """
    Representa una excepcion que indica que la pagina ya existe en la seccion

    Attributes:
        titulo: Un str que indica que el titulo de la pagina que ya existe
        msg: Un str que contiene el mensaje de error
    """
    def __init__(self, titulo: str, msg: str):
        self.titulo: str = titulo
        self.msg: str = msg


class PaginaNoExistenteError(AnotadorError):
    """
    Representa una exepcion que indica que no existe una pagina con el titulo dado

    Attributes:
        titulo: Un str que indica el titulo de la pagina que se esta buscando
        msg: Un str que contiene el mensaje de error
    """
    def __init__(self, titulo: str, msg: str):
        self.titulo: str = titulo
        self.msg: str = msg
