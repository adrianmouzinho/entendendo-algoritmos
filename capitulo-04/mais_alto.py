def mais_alto(lista):
  if len(lista) == 0:
    return None
  if len(lista) == 1:
    return lista[0]
  atual = lista.pop()
  maior = mais_alto(lista)
  if atual > maior:
    return atual
  return maior

print(mais_alto([2, 4, 6]))