def quicksort(array):
  if len(array) < 2:
    return array
  pivo = array[0]
  menores = [i for i in array[1:] if i <= pivo]
  maiores = [i for i in array[1:] if i > pivo]
  return quicksort(menores) + [pivo] + quicksort(maiores)

lista_ordenada = quicksort([33, 10, 33, 15, 7])
print(lista_ordenada)