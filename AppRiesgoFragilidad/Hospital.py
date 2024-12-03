class Hospital:
  def __init__ (self, nit, nombre, direccion):
        self.NIT = nit 
        self.NOMBRE = nombre 
        self.DIRECCION = direccion
      
  LISTA_HOSPITALES = []

h1 = Hospital(890901826-2, "Pablo Tobón Uribe", "Diagonal 80 #76-08, Robledo")
h2 = Hospital(890906347-9, "Manuel Uribe Ángel", "Diagonal 31 36ª sur 80, Envigado")
LISTA_HOSPITALES = [h1, h2]

def imprimirHospital():
  for hospital in LISTA_HOSPITALES:
    print ("Nit: ", hospital.NIT)
    print ("Nombre: ", hospital.NOMBRE)
    print ("Dirección: ", hospital.DIRECCION)
    print ("")