votaram = {}

def verifica_eleitor(eleitor):
  votou = votaram.get(eleitor)
  if votou == None:
    votaram[eleitor] = True
    print('Deixe votar!')
    return
  print('Mande embora!')

verifica_eleitor('tom')
verifica_eleitor('mike')
verifica_eleitor('mike')