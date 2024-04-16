def tamanho_lista(lista):
  if len(lista) == 0:
    return 0
  if len(lista) == 1:
    return 1
  lista.pop()
  return 1 + tamanho_lista(lista)

print(tamanho_lista([2, 4, 6]))