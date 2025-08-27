def contagem_caractere(texto, caractere):
   
   #Contador que vai contar os caracteres
   contador = 0
   
   #Para cada letra dentro do texto
   for letra in texto:
     if letra == caractere:
       contador += 1
       
   return contador
  