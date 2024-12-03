from Usuario import Usuario
class Recepcionista(Usuario):
    def __init__(self, id, nombre, nit):
        super().__init__(id, nombre)
        self.NIT_HOSPITAL = nit  

LISTA_RECEPCIONISTAS = []

r1 = Recepcionista("RE1", "Natalia Beltrán", "890901826-2")
r2 = Recepcionista("RE2", "Luz Elena Villa", "890906347-9")
LISTA_RECEPCIONISTAS = [r1, r2]

def imprimirRecepcionista():
  for recepcionista in LISTA_RECEPCIONISTAS:
    print ("ID: ", recepcionista.ID)
    print ("Nombre: ", recepcionista.NOMBRE)
    print ("Nit Hospital: ", recepcionista.NIT_HOSPITAL)
    print ("")