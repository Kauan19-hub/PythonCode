def contar_palavras(lista):
  
  contador = 0
  
  for palavra in lista:
    if palavra[0] == 'A' or palavra[0] == 'a': #Se a palavra for 'A' maiúsculo ou minúsculo, retorna a quantidade
    
        contador += 1
    
  return contador