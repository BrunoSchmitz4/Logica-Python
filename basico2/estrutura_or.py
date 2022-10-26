# Aqui vamos usar estruturas condicionais para trazer exemplos de uso do OR
# Lembrando: condicionais são verificadores de condições que realizam determinadas ações
# caso uma ou mais condições forem atendidas.
# Nesta situação, vamos usar uma estrutura condicional com OR


# Desta vez, vamos fazer um café da tarde perfeito!
# Precisamos que alguns itens estejam de acordo, para que seja perfeito...ou quase
# Não precisa necessáriamente estarem todos, contudo se um ou mais estiverem corretos,
# O café da tarde será um sucesso (queria um café agora...)

cafe = True
leite = 4.0
cookies = 0
sanduiches = 10
playlist = 'best of \'80'
xicaras = 4
casa_limpa = False
cadeiras = 5
print(playlist)

if xicaras >= 4 or cadeiras >= 4:
    print("Ai sim! Vamos aos essenciais!")
    if casa_limpa == True or playlist == 'classics':
        print("Perfeito~~Último passo")
        if leite >= 5.0 or sanduiches >= 12 or cafe == True:
            print("Hora de chamar os convidados(as)! :)")
        else:
            print("Ah...será que é o suficiente?")
    else:
        print("Puts...e agora?!")
else:
    print("Hmm...Quantas mais faltam?")