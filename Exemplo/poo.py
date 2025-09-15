### VARIÁVEIS ###
# nome = "Kauan"
# idade = 17
# edv = 92907217
# departamento = "ETS"
# planta = "CaP"

# nome2 = "Batman"
# idade2 = 37
# edv2 = 92907030
# departamento2 = "TET-LA"
# planta2 = "CtP"

class Colaborador():
  def __init__(self, nome, idade, edv, departamento, planta):
    self.__nome = nome 
    self.__idade = idade
    self.__edv = edv
    self.__departamento = departamento
    self.__planta = planta
    
  ### FUNÇÕES ###
  def imprimir_informacoes(self):
        msg = f"{self.__nome} é colaborador de {self.__planta}/{self.__departamento}, tem {self.__idade} anos e seu EDV é {self.__edv}"
        print(msg) 
    
  ### VERBO = FUNÇÃO = MÉTODO
  ### SUBSTANTIVO = VARIVÁVEL = ATRIBUTOS/PARÂMETROS 
  ### CRIAR OBJETOS = INSTANCIAR
  
kauan = Colaborador(nome = "Kauan", idade = 17, departamento = "ETS", planta = "CaP", edv = 92907217)
batman = Colaborador(nome = "Batman", idade = 37, departamento = "TET-LA", planta = "CtP", edv = 92907030)

kauan.imprimir_informacoes()
batman.imprimir_informacoes()
  
  


