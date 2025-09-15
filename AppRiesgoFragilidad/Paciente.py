from Usuario import Usuario

class Paciente(Usuario):
 def __init__(self, id, nombre, edad, celular, referencia, nit):
        super().__init__(id, nombre) 
        self.EDAD = edad
        self.CELULAR = celular
        self.REFERENCIA_RELOJINTELIGENTE = referencia
        self.NIT_HOSPITAL = nit

LISTA_PACIENTES = []
'''
  def ingresarPaciente():
      for i in range (0,2):
        id = int(input("Ingrese el ID del paciente: "))
        nombre = input("Ingrese el nombre del paciente: ")
        edad = int(input("Ingrese la edad del paciente: "))
        celular = int(input("Ingrese el celular del paciente: "))
        referencia = input("Ingrese el nit del paciente: ")
        nit = int(input("Ingrese el nit del paciente: "))
        print ("")
        paciente = PACIENTE(id, nombre, edad, celula, referencia, nit)
        LISTA_PACIENTES.append(paciente)
 '''

p1 = Paciente(1027, "Leticia Londoño", 75, 3102004534,"M1","890901826-2")
p2 = Paciente(1028, "Ottoniel Noreña", 68, 3156782399,"M1","890906347-9")
LISTA_PACIENTES = [p1, p2]

def imprimirPaciente():
    for paciente in LISTA_PACIENTES:
      print ("ID: ", paciente.ID)
      print ("Nombre: ", paciente.NOMBRE)
      print ("Edad: ", paciente.EDAD)
      print ("Celular: ", paciente.CELULAR)
      print ("RelojInteligente: ", paciente.REFERENCIA_RELOJINTELIGENTE)
      print ("Nit: ", paciente.NIT_HOSPITAL)
      print ("")