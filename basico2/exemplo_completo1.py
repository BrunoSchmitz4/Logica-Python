# Agora, por que não tentamos algo mais completo?
# Vamos unir o que aprendemos e desenvolver um pequeno projeto que reune tudo (ou quase tudo)
# visto nestes arquivos de auxílio no aprendizado python :)

screen1 = 0
screen2 = False
screen3 = False
perguntar = ''

nome = ''
idade = 0
altura = 0.0
peso = 0.0
entrar = 0

if entrar == 0:
    screen1 = 1
else:
    screen1 = 0
while screen1 == 1:
    nome = str(input("Insira seu nome: "))
    idade = int(input("Insira sua idade: "))
    if idade < 18:
        print("Desculpe, mas você precisa ter 18 anos ou mais para realizar este teste")
    elif idade >= 18:
        peso = float(input("Insira seu peso (em kg): "))
        altura = float(input("Insira sua altura (em metros): "))
        print("Estas foram as informações inseridas:", "\nNome:" ,nome,"\nIdade: ",idade,"\nPeso: ",peso,"\nAltura: ",altura)
        perguntar = str(input("Você deseja mudar?(S/N)"))
        if perguntar == 's' or perguntar == 'S':
            screen1 == 1
        elif perguntar == 'n' or perguntar == 'N':
            imc = peso / (altura * altura)
            print("Tudo bem,", nome, ".\nSeu IMC é: ", imc)
            if imc <= 18.5:
                print("Seu IMC mostra que você está abaixo do peso ideal.")
            elif imc >= 18.6 and imc <= 24.9:
                print("Seu IMC mostra que você está no peso ideal.")
            elif imc >= 25.0 and imc <= 29.9:
                print("Seu IMC mostra que você está um pouco acima do peso ideal.")
            elif imc >= 30.0 and imc <= 34.9:
                print("Seu IMC mostra que você está com obesidade no primeiro grau.")
            elif imc >= 35.0 and imc <= 39.9:
                print("Seu IMC mostra que você está com obesidade no segundo grau.")
            elif imc >= 40:
                print("Seu IMC mostra que você está com obesidade no terceiro grau.")
            else:
                print("Valor não condiz na classificação (resumida).")
                screen1 = 1
            print("Cálculo pronto")
        else:
            print("Opção inexistente")
    # peso / (altura*altura)