# Números são importantes dentro da programação, e quase sempre você tera que lidar com
# cálculos matemáticos na programação, como a soma de vários valores, a multiplicação de uma possível pontuação,
# uma subtração de pontos de vida, dentre outros.

# A matemática básica na programação compõe 5 símbolos,
# + (adição), - (subtração), * (multiplicação), / (divisão) e % (restos)
# Você pode efetuar expressões matemáticas de diversas formas, confira algumas delas.

frutas = 5
cesta_frutas = 10

# Quando criamos uma váriavel, dizemos que declaramos elas, e quando atribuímos um valor, dizemos que inicializamos ela.
# Ou seja, eu declarei duas varíaveis, e cada uma delas foram inicializadas com um valor pré-definido

cesta_frutas = cesta_frutas + frutas
# Aqui eu declarei uma terceira variável, e inicializei ela com um cálculo, que somava o valor das duas variáveis acima.
# Afinal, a cesta de frutas tinham 10 frutas, e eu acrescentei + 5 frutas. Dessa forma:
# cesta_frutas = cesta_frutas + frutas
# "O valor da cesta de frutas, é o valor da mesma 'cesta de frutas' + 'frutas', ou seja, 10 + 5

# O mesmo caso vai se aplicar nos cálculos abaixo:

vida_heroi = 25
dano_inimigo = 6
vida_heroi = vida_heroi - dano_inimigo

score = 50
bonus_score = 2
score = score * bonus_score

seus_doces = 20
criancas = 4
seus_doces = seus_doces / criancas

# Ou você pode fazer assim:
x = 10 + 4
y = x / 2
z = y - 6