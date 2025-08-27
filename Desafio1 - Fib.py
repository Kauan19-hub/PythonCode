def fibonacci(n, sequencia = None):
  
  if sequencia is None:
    sequencia = [0, 1]
    
  if len(sequencia) >= n:
    print(sequencia)
    return(sequencia)
  
  sequencia.append(sequencia[-1] + sequencia[-2])
  return fibonacci(n, sequencia)

n = int(input("Digite quantos termos da sequência de Fibonacci deseja: "))

fibonacci(n)