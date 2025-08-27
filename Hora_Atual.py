import datetime 

def mostrar_hora():
  now = datetime.datetime.now()
  formatar = now.strftime("%H:%M:%S")
  
  print(formatar)
  
mostrar_hora()