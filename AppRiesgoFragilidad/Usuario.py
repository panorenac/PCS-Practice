
class Usuario:
    LISTA_USUARIOS = []  # lista global

    def __init__(self, id, nombre):
        self.ID = id
        self.NOMBRE = nombre
        # Cada vez que se crea un usuario o subclase, se añade a la lista global
        Usuario.LISTA_USUARIOS.append(self)

    @classmethod
    def imprimirUsuarios(cls):
        print("========= LISTA DE TODOS LOS USUARIOS =========")
        for usuario in cls.LISTA_USUARIOS:
            print(f"ID: {usuario.ID} - Nombre: {usuario.NOMBRE} - Tipo: {usuario.__class__.__name__}")
        print("")