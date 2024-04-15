# Exercícios

## 2.1
Para implementar uma aplicativo de tarefas que lida com muitas inserções é melhor utilizar uma lista encadeada, pois o tempo de execução para inserção é menor do que o de um array.

## 2.2
Para implementar uma lista de pedidos de um restaurante é melhor utilizar uma lista encadeado, pois haverá muitas inserções e deleções nessa lista. Além disso, o chef sempre fará a leitura do primeiro item da lista e não de um item aleatório.

## 2.3
Para implementar uma lista de usuários do Facebook é melhor utilizar um array, pois haverá muitas buscas por usuários. Os arrays são melhores para fazer leitura, pois permitem o acesso aleatório.

## 2.4
Primeiramente, o tempo de execução para inserção em um array é O(n) enquanto que em uma lista encadeada é O(1). Para adicionar um novo usuário na lista, você terá de mover a posição de outros usuários. Caso não tiver mais espaço para adicionar um novo usuário, você terá que mover toda a lista para outra região da memória.

## 2.5
A estrutura híbrida é mais rápida do que os arrays e as listas encadeadas. Para encontrar um usuário em um array ou em uma lista encadeada é preciso, no pior cenário, percorrer toda a lista. Nessa nova estrutura, no entanto, reduzimos muito o tempo de busca ao agrupar os usuários pela primeira letra de seus nomes. Dessa forma, basta percorrer uma lista com usuários cuja primeira letra do nome seja a mesma para todos.
