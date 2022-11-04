# Continuando o material de estudos, vamos falar sobre loops de repetição.
# Loops de repetição são extremamente importantes para seus projetos,
# afinal, é com eles que você consegue com maior facilidade manter uma interface em operação,
# ou então, realizar diversas ações até que a condição do while seja atendida,
# seja de forma automática ou manula, ou seja,
# exigindo condições se concretizando pelo usuário ou pelo próprio software.

# Abaixo, um exemplo

w = 0
x = 10
y = 46
z = y - x

# Aqui estamos dizendo que:
# ENQUANTO w for menor que z, ele vai:
# 'printar' o texto e o valor de w;
# adicionar 1 no valor de w

while w < z:
    print("O valor de 'w' é", w)
    w = w + 1

# Neste exemplo a pessoa precisa digitar sua conta e senha para entrar
conta = str(input("Digite sua conta: "))
senha = str(input("Digite sua senha: "))

if conta != 'batatinha' and senha != 'quandonasce':
    perguntar = 0

# Aqui estamos dizendo que:

# SE conta for diferente de 'batatinha';
# E senha for diferente ('!' e '=' juntos formam o símbolo !=) de 'quandonasce';

# ENQUANTO a conta for diferente de 'batatinha';
# E a senha for diferente ('!' e '=' juntos formam o símbolo !=) de 'quandonasce';

# Continuará no loop de pergunta
if perguntar == 0:
    while conta != 'batatinha' and senha != 'quandonasce':
        print("Senha ou conta incorreta, tente novamente")
        conta = str(input("Digite sua conta: "))
        senha = str(input("Digite sua senha: "))
        perguntar = 0
else:
    print("Espalha a rama pelo chão! :)")
    print("Bem vindo agente potato123.")