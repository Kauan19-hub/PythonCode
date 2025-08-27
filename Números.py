def media(numeros):
  
  if not numeros:
    return None #Lista vazia será retornada
  
  #Soma de números, e suas divisões
  soma = sum(numeros)
  media = soma / len(numeros)
  
  return media
