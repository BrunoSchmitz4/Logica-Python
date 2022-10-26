# Aqui vamos usar estruturas condicionais para trazer exemplos de uso do AND
# Lembrando: condicionais são verificadores de condições que realizam determinadas ações
# caso uma ou mais condições forem atendidas.
# Nesta situação, vamos usar uma estrutura condicional com AND

battery = 20.0
wifi = True
memory = 1600

# Você nota que precisa baixar a mais nova atualização do seu jogo favorito,
# afinal, desenvolvedores de jogos costumam atualizar com frequência seus projetos,
# e seu jogo favorito não é diferente! Mas... tem um pequeno detalhe:
# O jogo pede que a atualização (instável) seja feita com celulares:
# Com a bateria (battery neste caso) acima de 50%;
# Conexão ao wifi (meio óbvio...rsrsrs);
# E um espaço de armazenamento de 500mb livre.
# Será que seu dispositivo terá o que é preciso para atualizar seu game?

print("Verificando 'Seu jogo favorito', por favor aguarde...")
question = str(input("Tudo pronto?(S/N): "))

if question == 'S' or question == 's': # Aqui usei or para tornar menor o código :)
    # Verifica:
    # Se o question tem como texto 'S', ou 's';
    if(wifi == True) and (memory > 500) and (battery >= 50.0):
        # Verifica:
        # Se o wifi(bool) é true;
        # Se o free_memory(int) é maior ou igual à 500;
        # Se o batter(float) é maior ou igual à 50.0;
        print("Começando download!")
    else:
        print("Algo deu errado...verifique se todos os requisitos atendem")
else:
    print("Ok, cancelando download")