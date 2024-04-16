def soma(lista):
  if len(lista) == 0:
    return 0
  if len(lista) == 1:
    return lista[0]
  primeiro = lista.pop()
  return primeiro + soma(lista)

print(soma([2, 4, 6]))