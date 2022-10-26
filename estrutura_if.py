# Olá! Tendo em mente que você já deu uma analisada, e brincando com a pasta basico1,
# vamos começar a praticar estruturas if, as estruturas de condicionais.
# Uma condicional é uma ou mais coisas que ocorrem, caso um determinado pré-requisito aconteça.
# Ex: Você quer dar uma passeada no parque.
# SE estiver ensolarado, PASSEAR;
# SE NÃO SE estiver nublado, PASSEAR e LEVAR GUARDA-CHUVA;
# SE NÃO, FICAR EM CASA.

# Basicamente, para uma ação ocorrer (no caso, passear),
# é preciso que esteja ensolarado ou nublado, levando a sombrinha.
# Basicamente, ocorre da mesma forma na estrutura IF
# Traduzindo do inglês para o português fica:
# If: Se
# Else if: Senão se
# Else: Senão

# Vou usar o exemplo na prática

ensolarado = False
nublado = False
chuvoso = True


# Basicament, o IF está nos dizendo:
# SE, ensolarado for verdadeiro E nublado for falso E chuvoso for falso, ele vai executar
if(ensolarado == True) and (nublado == False) and (chuvoso == False):{
    print("Bom passeio!")
}
# O elif ocorre somente se o IF acima não atender, nem se houver outros ELIFs
# (sim, podem haver mais de 1)
# Ou seja, fica assim:
# SE NÃO SE ensolarado for falso E nublado for verdadeiro E chuvoso for verdadeiro, ele vai executar
elif(ensolarado == False) and (nublado == True) and (chuvoso == False):{
    print("Leve um guarda-chuva e bom passeio!")
}
# O else é um pouco diferente, pois como vemos abaixo, ele não faz verificação de booleanos (como acima)
# Isso ocorre pois o else é usado, para todas as possibilidades de condições que não foram constadas
# no IF ou no(s) ELIF(s).
# Então, fica:
# SENÃO todo o resto, ele vai executar
else:{
     print("Melhor ficar em casa pra não pegar resfriado.")
    }


# O AND significa "E", ou seja, para tal condição ser atendida,
# Ao menos duas ou mais variáveis precisam estar com o valor constado, seja bool ou não.

# O OR significa "OU", ou seja, para tal condição ser atendida,
# Ao menos uma das variáveis precisam estar com o valor constado, seja bool ou não.

#Exemplos nos próximos arquivos! :)