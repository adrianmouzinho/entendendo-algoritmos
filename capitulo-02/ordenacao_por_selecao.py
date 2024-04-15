def busca_menor(arr):
  menor = arr[0]
  menor_indice = 0
  for i in range(1, len(arr)):
    if arr[i] < menor:
      menor = arr[i]
      menor_indice = i
  return menor_indice

def ordenacao_por_selecao(arr):
  novo_arr = []
  for i in range(len(arr)):
    menor_indice = busca_menor(arr)
    novo_arr.append(arr[menor_indice])
    arr.pop(menor_indice)
  return novo_arr

lista = [5, 3, 6, 2, 10]
print(lista)
print(ordenacao_por_selecao(lista))