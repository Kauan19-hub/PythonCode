habitantes = []

def coleta_dados():
  for i in range(4):
    print(f"\nHabitante: ")
    
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))
    genero = input("Genero M/F: ")
    esporte = input(("Esporte favorito: "))
    
    habitantes.append ({
      'nome': nome,
      'idade': idade,
      'altura': altura,
      'genero': genero,
      'esporte': esporte,
      
    })
    
def sem_homem_natacao():
  print("Infelizmente, não há homens que gostam de natação...")
  
def media_idade_homens_natacao(pessoas):
  homens = [p['idade'] for p in pessoas if p['genero'] == 'M' and p['esporte'] == 'natação']
  
  if homens:
    media = sum(homens) / len(homens)
    print(F"A idade média dos homens que curtem natação, é {media}.")
  
  else:
    sem_homem_natacao()
    
coleta_dados()
media_idade_homens_natacao(habitantes)    
    
    
