# Um programa na maioria das vezes interaje com o usuário, como fazemos isso? Com o input!
# o input pede para que o usuário insira algo,
# O que o usuário é um dado que possívelmente será adicionado à uma variável,
# mas não se limita nisso.

# input("Qual é o seu nome?")
# Este input recolhe dados do tipo any
# O tipo any (como já diz no inglês), é um tipo qualquer, ou seja, este input não se restringe a tipos.

# Na maioria das vezes os inpurs estão em variáveis que não tem uma inicialização, ou seja,
# Elas não tem um valor pré-definido, o usuário é quem irá definir, veja a seguir:

nome = str(input("Insira seu nome: "))
idade = int(input("Insira sua idade: "))
altura = float(input("Insira sua altura (troque vírgula por ponto. Ex:1.70): "))

print("Dados do usuário: ")
print("Nome do usuário: ",nome)
print("Idade do usuário: ",idade)
print("Altura do usuário: ",altura)

# Este programa acima, pega nome, idade e altura do usuário e armazena os dados nas variáveis.
# Ali, o str, int e o float que precendem o input, indicam que a variável pede um valor daquele tipo.

# Você também pode fazer cálculos em prints e inputs.
x = 2
print("Sua idade daqui à 2 anos será: ", idade + x) # Uma forma de calcular
print("Sua idade daqui à 4 anos será: ", idade + 4) # Outra forma
