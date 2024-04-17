cache = {}

def pega_pagina(url):
  paginaEstaEmCache = cache.get(url) != None
  if paginaEstaEmCache:
    print('dados do cache!')
    return cache.get(url)
  dados = 'pegando dados do servidor...' 
  cache[url] = dados
  return dados

print(pega_pagina('facebook.com'))
print(pega_pagina('facebook.com/about'))
print(pega_pagina('facebook.com'))