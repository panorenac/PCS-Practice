class RelojInteligente:
  def __init__ (self, codigo, referencia, marca, ip):
        self.CODIGO = codigo
        self.REFERENCIA= referencia
        self.MARCA = marca
        self.IP=ip

LISTA_RELOJES = []

re1 = RelojInteligente("M1", "GEAR S3", "Samsung", "216.58.152.97")
re2 = RelojInteligente("M2", "GEAR S5", "Samsung", "216.58.152.98")
LISTA_RELOJES = [re1, re2]

def imprimirRelojInteligente():
  for reloj in LISTA_RELOJES:
    print ("Código: ", reloj.CODIGO)
    print ("Referencia: ", reloj.REFERENCIA)
    print ("Marca: ", reloj.MARCA)
    print ("IP: ", reloj.MARCA)
    print ("")