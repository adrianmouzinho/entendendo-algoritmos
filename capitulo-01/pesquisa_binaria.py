def pesquisa_binaria(lista, item):
  baixo = 0
  alto = len(lista) - 1

  while alto >= baixo:
    meio = int((alto + baixo) / 2)
    chute = lista[meio]
    if chute == item:
      return meio
    elif chute < item:
      baixo = meio + 1
    else:
      alto = meio - 1
    
  return None

lista = [1, 3, 5, 7, 9]
resultado = pesquisa_binaria(lista, -1)
if resultado != None:
  print(lista[resultado], 'foi encontrado na posição', resultado)
else:
  print('item não encontrado')