#Jogo da Forca em Python
#Versão Portuguesa do código
#Feito por David Ericson
#03/06/2024

import random
import os

#Variaveis globais que serão usadas nas funções
chances = 6
tentativa = ''
restantes = False
letras_usadas = []
jogador = ''
pj1 = 0
pj2 = 0
nome_j1 = ''
nome_j2 = ''
reiniciar = ''



#------------------------------------------------------



def resetar(): #Função usada para resetar variáveis globais
    global chances
    global tentativa
    global restantes
    global letras_usadas
    global jogador
    
    chances = 6
    tentativa = ''
    restantes = False
    letras_usadas = []
    jogador = ''



#------------------------------------------------------



def forca(chance): #Função da interface da forca
    if chance == 6:
        print('  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========')
    elif chance == 5:
        print('  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========')
    elif chance == 4:
        print('  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========')
    elif chance == 3:
        print('  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========')
    elif chance == 2:
        print('  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========')
    elif chance == 1:
        print('  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========')
    else:
        print('  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========')



#------------------------------------------------------



def palavra_escondida (p): #Função da interfaçe da palavra que está sendo adivinhada
    descoberta = []
    for i in range (len(p)):
        descoberta.append('_')
    return descoberta



#------------------------------------------------------



def jvj(): #Função - Modo Jogador vs Jogador
    global chances
    global tentativa
    global restantes
    global letras_usadas
    global pj1
    global pj2
    global jogador
    global reiniciar
    global nome_j1
    global nome_j2

    #------------------------------------------------------
    while reiniciar != 'N': #Define quando a função será encerrada

        resetar()
        reiniciar = ''

        os.system('cls' if os.name == 'nt' else 'clear')
        print ('- Modo Jogador vs Jogador -')
        print('-------------------------------')

        if pj1 == 0 and pj2 == 0:
            print ('[Regras]: Um jogador deverá inserir a palavra misteriosa e o outro deve adivinha-la, se o jogador descobrir\n a palavra, ganhará um ponto, caso não consiga, o outro jogador que inseriu a palavra pontuará.')
            print('-------------------------------')
            nome_j1 = str(input('Insira o nome do Jogador 01: '))
            nome_j2 = str(input('Insira o nome do Jogador 02: '))
        else:
            print(f'[Placar]\n{nome_j1}: {pj1}\n{nome_j2}: {pj2}')
            print('-------------------------------')

        #------------------------------------------------------
        while jogador != nome_j1 and jogador != nome_j2:
            jogador = (input(f'> Qual jogador será responsável por adivinhar a palavra nesta rodada? [{nome_j1}/{nome_j2}]: '))
            if jogador != nome_j1 and jogador != nome_j2:
                print('Jogador Inválido!')

        palavra = str(input('> Insira a palavra que deve ser adivinhada (A palavra será escondida após ser inserida): ')).upper() 
        os.system('cls' if os.name == 'nt' else 'clear')
        descoberta = palavra_escondida(palavra)

        #------------------------------------------------------
        while restantes != True and chances >= 0: #Parte da adivinhação da palavra
            restantes = True
            acertou = False

            forca(chances)
            print(f'{descoberta}|Letars Usadas:{letras_usadas}')


            if chances > 0: #Área de inserir os caracteres para adivinhar a palavra escondida
                while len(tentativa) != 1:
                    tentativa = str(input('Insira apenas uma letra: ')).upper()
                    for i in range (len(letras_usadas)): #Verifica se a letra da tentativa ja foi usada alguma vez
                        if tentativa == letras_usadas[i]:
                            print ('Letra já utilizada')
                            tentativa = ''


                letras_usadas.append(tentativa) #Coloca a tentativa na matriz de letras já usadas


                for i in range (len(palavra)): #Verifica se a palavra contém a letra inserida na tentatica
                    if palavra[i] == tentativa:
                        descoberta[i] = tentativa
                        acertou = True


            if acertou == False: #Retira uma chance caso a palavra não contenha a letra inserida na tentativa
                chances -= 1


            for i in range (len(descoberta)): #Verifica se a palavra já foi totalmente descoberta
                if descoberta[i] == '_':
                    restantes = False
        

            tentativa = ''
            os.system('cls' if os.name == 'nt' else 'clear')

        #------------------------------------------------------
        print('-------------------------------')
        if chances <= 0: #Retira pontos caso o jogador tenha perdido
            forca(chances)
            if jogador == 'p1':
                print(f'Você perdeu, a palavra era {palavra}. [{nome_j2} Recebeu +1 Ponto]')
                pj2 += 1
            else:
                print(f'Você perdeu, a palavra era {palavra}. [{nome_j1} Recebeu +1 Ponto]')
                pj1 += 1

        else: #Adiciona pontos caso o jogador tenha ganhado
            forca(chances)
            print(f'{descoberta}')
            print(f'Parabéns você acertou! [{jogador} Recebeu +1 Ponto]')
            if jogador == 'p1':
                pj1 += 1
            else:
                pj2 += 1

        #------------------------------------------------------

        while reiniciar != 'S' and reiniciar != 'N': #Reinicio ou finalização do programa
            reiniciar = str(input('Deseja continuar jogando? [S/N]: ')).upper()

            if reiniciar == 'S' and reiniciar == 'N':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('-------------------------------')
            if reiniciar != 'S' and reiniciar != 'N':
                print('Operação Inválida')



#------------------------------------------------------



def jvm(): #Função - Modo Jogador vs Máquina
    global chances
    global tentativa
    global restantes
    global letras_usadas
    global reiniciar
    global pj1


    while reiniciar != 'N': #Define quando a função será encerrada
        resetar()
        
        lista_de_palavras = ["casa", "carro", "flor", "gato", "cachorro","mesa", "cadeira", "janela", "porta", "livro","caneta", "lapis", "papel", "bolsa", "sapato","sol", "lua", "estrela", "nuvem", "rio","mar", "peixe", "passaro", "telefone", "computador","teclado", "mouse", "camisa", "bicicleta", "bola","chave", "faca", "garfo", "colher", "prato","copo", "cavalo", "abacaxi", "leite", "amigo"]
        os.system('cls' if os.name == 'nt' else 'clear')
        print ('- Modo Jogador vs Máquina -')
        print('-------------------------------')

        if reiniciar != 'S':
            print ('[Regras]: Tente adivinhar o máximo de palavras possíveis para acumular pontos, caso erre uma vez você perde!')
            print('-------------------------------')
            a = str(input('Pressione qualquer botão para iniciar a partida...'))

        reiniciar = ''

        os.system('cls' if os.name == 'nt' else 'clear')

        palavra = (lista_de_palavras[random.randint(0,39)]).upper()
        descoberta = palavra_escondida(palavra)

        #------------------------------------------------------
        while restantes != True and chances >= 0: #Parte da adivinhação da palavra
            restantes = True
            acertou = False

            forca(chances)
            print(f'{descoberta}\nLetars Usadas:{letras_usadas}|Pontuação: {pj1}')


            if chances > 0: #Área de inserir os caracteres para adivinhar a palavra escondida
                while len(tentativa) != 1:
                    tentativa = str(input('Insira apenas uma letra: ')).upper()
                    for i in range (len(letras_usadas)):
                        if tentativa == letras_usadas[i]:
                            print ('Letra já utilizada')
                            tentativa = ''


                letras_usadas.append(tentativa) #Coloca a tentativa na matriz de letras já usadas


                for i in range (len(palavra)): #Verifica se a palavra contém a letra inserida na tentativa
                    if palavra[i] == tentativa:
                        descoberta[i] = tentativa
                        acertou = True


            if acertou == False: #Retira uma chance caso a palavra não contenha a letra inserida na tentativa
                chances -= 1


            for i in range (len(descoberta)): #Verifica se a palavra já foi totalmente descoberta
                if descoberta[i] == '_':
                    restantes = False
        
            tentativa = ''
            os.system('cls' if os.name == 'nt' else 'clear')

        #------------------------------------------------------

        print('-------------------------------')
        if chances <= 0:
            forca(chances)
            print(f'Você perdeu, a palavra era [{palavra}] | Sua pontuação final foi de {pj1} pontos.')
            pj1 = 0

        else:
            forca(chances)
            print(f'{descoberta}')
            pj1 += 1
            print(f'Parabéns você acertou e recebeu +1 ponto!!! [Total: {pj1}]')


#------------------------------------------------------

        while reiniciar != 'S' and reiniciar != 'N': #Reinicio ou finalização do programa
            reiniciar = str(input('Deseja continuar jogando? [S/N]: ')).upper()

            if reiniciar == 'S' and reiniciar == 'N':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('-------------------------------')
            if reiniciar != 'S' and reiniciar != 'N':
                print('Operação Inválida')



#------------------------------------------------------



def principal(): #Função principal para selecionar o modo de jogo
    print('-------------------------------')
    print('- Jogo da Forca -')
    print('-------------------------------')
    modo = str(input('Caso deseje sair digite [Sair] | Que modo de jogo você deseja jogar?[[Jogador vs Jogador][Jogador vs Máquina]]: ')).lower() #Seleção do modo
    while modo != 'sair':

        if modo == 'jogador vs jogador' or modo == 'jvj':
            print('-------------------------------')
            modo = 'sair'
            jvj()

        elif modo == 'jogador vs máquina' or modo == 'jvm':
            print('-------------------------------')
            modo = 'sair'
            jvm()

        else:
            print('Opção inválida, tente novamente.')
            print('-------------------------------')

            modo = str(input('Caso deseje sair digite [Sair] | Que modo de jogo você deseja jogar?[Jogador vs Jogador][Jogador vs Máquina]: ')).lower()

principal() #Inicia a função principal
print('-------------------------------')
print('Programa Encerrado....')