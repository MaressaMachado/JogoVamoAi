def limpa_tela():
    print("\x1b[2J")

def player(): 
    nome = input('Qual é o seu nome?')
    pergunta3 = int(input("Numa escala de 0 a 10 quanto você se interessa pela natureza e pelos povos indígenas?"))
    pergunta1 = int(input("Numa escala de 0 a 10 quanto você gosta de tecnologia?"))
    pergunta2 = int(input("Numa escala de 0 a 10 quanto você conhece/já ouviu falar sobre a linguagem Python?"))
    soma = (pergunta1 + pergunta2 + pergunta3)/3
    if soma >= 7:
        print (f"{nome}, muito bem-vinde a Jornada de Keretxu, prepare-se para embarcar nessa aventura. Vamos agora para a próxima fase dessa jornada!")
    else:
        print (f"{nome}, pela sua resposta nas perguntas, de antemão te avisamos que esse jogo muito provavelmente não vai te agradar... Deseja continuar mesmo assim?")
        resposta= int(input ("Digite o número de sua escolha: 1. Sim 2. Não"))
        if resposta == 1:
            print (f"Ok, {nome} vamos ver até onde você vai ")
            limpa_tela()
        else: 
            print ("\n")
            print ("Aperte para sair do jogo")
            limpa_tela()


    return player

def menu (): 
    while True:
        print("Menu:")
        print("Digite 1 para continuar na Jornada.")
        print("Digite 2 para sair.")
        opcao = int(input("Digite sua opção: "))
        if opcao == 1:
            print("-#"*16) 
            print("VAMOS CONTINUAR NA JORNADA")
            print("-#"*16)
            break
        
        elif opcao == 2:
            print("Tudo bem, sinta-se a vontade para voltar quando quiser!")
            exit ()
            break

   
    return menu

def boasvindas(): 
    print("-#"*16)
    print("BEM-VINDE A JORNADA KERETXU")
    print("-#"*16)
    print()
    print("Esse jogo é um convite para acompanhar a jornada da programadora Guarani Keretxu \n" 
          "Aqui, o que realmente importa é o retorno a raiz ancestral Ameríndia para que o novo aconteça \n" 
          "Por mais tecnodiversidade no mundo!\n")
    print("\n") 
    print('='*24)
    print('O INICIO DA JORNADA')
    print('='*24)
    print("\n"
          " O pensamento lógico dos juruá foi muito importante para a jornada de programadora de Keretxu,"
          "  e quem quiser acompanhá-la precisa ter essa nocão. Vamos lá? \n")

def ler_historia (opcao): 
    if opcao == "sim":
        print("-#"*16) 
        print("CONTINUACÃO DA HISTÓRIA")
        print("-#"*16)
        print("\n")
        print("- Onca-rei! Onça-rei! Que bom que o Senhor apareceu! Vamos logo! Pegue aquele cipó e me amarre no pé da árvore, mas tem de ser agora! É por isso que estou limpando o tronco e os galhos…\n"
              "- Calma lá! Não estou entendendo nada! O que é que está acontecendo? -perguntou a onça-rei, surpresa com a atitude do jabuti.\n"
              "É que está chegando o maior vendaval de todos os tempos! O maior vendaval de todos os séculos! O gavião passou por aqui e falou que é quase um furacão! " 
              " Está chegando, onça-rei!!! E eu tive uma ideia: Se eu ficar amarrado na árvore, não serei arrastado. Por favor, me ajude… o senhor sabe que eu sou lento!\n"
               "- Vendaval?!\n"
               "- Sim.\n"
               "- E você quer se salvar sozinha?! Alto lá! Quem é o rei da floresta?\n"
               "- O senhor onça-rei.\n"
               "- Então primeiro eu. Onde já se viu? Quem manda sou eu- disse a onça bufando.\n"
               "- Mas, senhor… \n" 
               "- Nada de mas, nada de mas… Vamos lá, que o tempo está passando. Você que vai me amarrar. Se alguém tem de se salvar aqui na floresta, sou eu.\n"
               "- Tá bem- disse o jabuti, fingindo-se transtornado.\n"
               " E assim fez.Amarrou a onça bem amarradinha. Ainda dirigiu-se à sua montanha de frutos, colocou-os em um cestinho e saiu tranquilamente, provando as deliciosas Jabuticabas." 
               "- Tchau, “seu” onca! Quando passar o vendavam eu volto para soltar o senhor."
               " Dizem os outros animais que a onça-rei está amarrada no pé de jabuticaba até hoje, e que aquelas pintas que ela tem são de tanta raiva por ter sido enganada por um simples jabuti.") 


    elif opcao == "não":
        print("ok")
    
    return ler_historia

def resolucao (resposta):
    if resposta == 1:
        print("\n"
              "Veja que 100 dividido por 7 leva ao quociente 14 e resto 2. Isto significa que os 100 dias correspondem a 14 semanas" 
              "inteiras e mais 2 dias. Cada uma das 14 semanas começa em uma terça-feira, dia seguinte ao que estava marcado"
              "a colheita, e terminam na próxima segunda-feira. Após essas 14 semanas, chegamos a uma segunda-feira, " 
              "e precisamos ainda contabilizar os 02 dias que faltam para totalizar 100 dias."
              "Assim, chegamos a uma quarta-feira de lua cheia.") 
    else: 
        print("Ok, que pena. ")

    return resolucao

def perguntas_teste():
    print("-#"*16)
    print("TESTE DE LÓGICA E PROGRAMACÃO")
    print("-#"*16)
    print("PERGUNTA 1. Iauaretê e o Jabuti\n"
      "A seguir leia o trecho de uma história antiga contada pelos nossos avôs:\n "
      "Estava lá o Jabuti cutucando com uma vara de bambu uma jabuticabeira para colher alguns frutos para o seu almoço,\n" 
      "quando sentiu um bafo faminto de onça no seu cangote.\n"
      "-Isso! Come suas frutinhas que eu sou uma onca que adora jabutis com sabor de frutos!\n"
      "Disse a onça-rei lambendo os beiços.\n"
      "Pronto! Estava indo tudo tão bem! Jabuti já tinha uma montanha de jabuticabas prontas para serem saboreadas uma a uma.\n" 
      "Agora, de repente, estava prestes a ser almoçado! Jabuti percebeu a presença faminta da onça, mas como tartaruga,\n"   
      "apesar de lenta no andar era muito rápido no pensar,\n"
      "Jabuti logo teve uma ideia quando viu um cipoal que se estendia até o chão.\n")

    resposta = input("O que você acha que o Jabuti fez? \n" 

        "a) Agarrou o cipó e pulou para outra árvore para fugir da onca. Afinal, como disse o texto, jabutis também são rápidos\n"
        "b)Enganou a onca e conseguiu convence-la  a se amarrar na árvore\n"
        "c) Se escondeu entre as folhas e o cipó e saiu rolando longe da vista da onca. \n Digite a letra da resposta:  ").lower

    if resposta == "b": 
        print("Muito bem você acertou!\n")
    else: 
        print("Que pena, você não pensou com cuidado numa questão tão simples... infelizmente SUA JORNADA ACABOU AQUI.  \n"
          "FIM DE JOGO\n")
        menu()

    print("PERGUNTA 2. Se Keretxu tivesse três coelhos a mais, o quadrado desse número seria 64. Quantos coelhos ela tem?\n"
      "a) 7\n b) 6 \n c) 5\n d) 8\n")
    resposta = input("Digite a alternativa correta: ")

    if resposta == "c": 
        print("Muito bem você acertou!\n")
    else: 
        print("Que pena, você errou \n")
        
    pergunta3 = input("PERGUNTA 3: Considere a série de números: 51, 9, 51, 12, 51, 15, 51,… Qual é o próximo número?\n "
                      " a) 14 \n b) 18 \n c) 21 \n d) 24 \n Digite aqui a alternativa: ") 

    if pergunta3 == "b": 
        print("Muito bem você acertou!\n")
    else: 
        print("Que pena, você errou \n")
    
    pergunta4 = input("PERGUNTA 4: A colheita da mandioca de Iracema estava marcada para uma Segunda-feira de lua cheia."
                  "Como ela ainda não estava no ponto de colheita como Iracema havia imaginado, ela achou melhor remarcar sua colheita" 
                  "para exatos 100 dias após a data original, na mesma lua cheia. A nova data de colheita de Iracema cairá em uma:\n"
                  "(a) Segunda-feira\n (b) terça-feira.\n (c) sexta-feira.\n (d) quarta-feira.\n (e) segunda-feira.\n"
                  "Digite a letra da alternativa correta: ") 

    if pergunta4 == "d":
        print("Parabéns, você acertou a pergunta mais difícil! ")
    else: 
        print("Poxa, a resposta não está correta...")

    resposta = int(input("Deseja visualizar como Keretxu resolveu desse problema? \n 1. Sim \n 2. Não \n Digite o número:"))
    if resposta == 1:
        print("\n"
              "Veja que 100 dividido por 7 leva ao quociente 14 e resto 2. Isto significa que os 100 dias correspondem a 14 semanas" 
              "inteiras e mais 2 dias. Cada uma das 14 semanas começa em uma terça-feira, dia seguinte ao que estava marcado"
              "a colheita, e terminam na próxima segunda-feira. Após essas 14 semanas, chegamos a uma segunda-feira, " 
              "e precisamos ainda contabilizar os 02 dias que faltam para totalizar 100 dias."
              "Assim, chegamos a uma quarta-feira de lua cheia.") 
    else: 
        print("Ok, que pena. ")


    print("PERGUNTA 5: Qual será o resultado desta sequência de comandos?\n"
          "x = 10\n"
          "y = 15\n"
          "x + y\n")

    print("A) 10 + 15\n"
          "B) True\n"
          "C) 25\n"
          "D) Syntax error\n") 

    resposta = input("Digite a letra correspondente a resposta correta: ").lower
    if resposta == "C":
        print("Resposta correta! ")
    else:
        print("A resposta não está correta, a alternativa correta era a letra C ")

        print("PERGUNTA 6: Qual a saída gerada pelo trecho de programa abaixo?\n"
            "x = 10\n"
            "y = 15\n"
            "z = 25\n"
            "print(x == z - y and z != y - x or not y != z - x)\n"

           "A) SyntaxError\n"
           "B) False\n"
           "C) Undefined \n"
           "D) True \n")

    resposta = input("Digite a letra correspondente a resposta correta: ").lower
    if resposta == "D":
        print("Resposta correta! ")
    else:
        print("A resposta não está correta, a alternativa correta era a letra D ")



        print("PERGUNTA 7: Quais os valores finais das variáveis a e b, se o usuário digitar 1 e 2, respectivamente?\n"
              "a = int(input('Qual o valor de a? '))\n"
              "b = int(input('Qual o valor de b? '))\n"
              "aux = a\n"
              "a = b\n"
              "b = aux\n"
              "print(a)\n"
              "print(b)\n"

             "A) a e b serão 1\n"
             "B) a e b serão 2\n"
             "C) a será 1 e b será 2\n"
             "D) a será 2 e b será 1\n")

    resposta = input("Digite a letra correspondente a resposta correta: ").lower
    if resposta == "D":
         print("Resposta correta! ")
    else:
        print("A resposta não está correta, a alternativa correta era a letra D ")

def minha_calculadora (calculo):
    if calculo % 2 == 0:
        return ("Par: Banana nanica")
    else:
        return ("Impar: Banana prata")

def ciclo ():
    print("\nAgora que você já demonstrou conhecimento em lógica vamos para a próxima etapa da nossa jornada: ")
    #PERSONAGEM2
    print("\n") 
    print('='*24)
    print('CICLO LUNAR')
    print('='*24)
    print("\n")
    print("Para os guarani, tudo é regido pelos ciclos lunares... desde plantar até fazer festas"
          "costuma-se fazer festas e celebrações para honrar os animais. Cada aldeia possui o seu animal-totem, que são aqueles mais reverenciados" 
          " e se tornam espíritos protetores do povo."
          "Pois bem, VOCÊ AGORA É A ONCA Iauaretê e está agora na aldeia Kamaiurá  da Lagoa do" 
          "Morená.\n" 
          "Hoje é dia de certa lua, e vai ter uma grande festa para você com muita danca, frutos e"
          "muito peixe! Todos cantam até quase o amanhecer.\n" 
          "PARA ESTA MISSÃO, MOSTRE QUE VOCÊ CONHECE O MÍNIMO DE CICLOS LUNARES! " 
          "Esse é um conhecimento essencial e muito básico para os indígenas. Por isso sua missão vai ser bem simples:\n"
          "    A) Os números a seguir estão em ordem decrescente, insira cada ciclo lunar do final para o início do mês\n" 
          "(cuidado para não se confundir! Insira tudo em uma única linha, não precisa usar vírgula para separar os ciclos)\n")

    #SEGUNDO RISCO DE DERROTA
    ciclos = input("Luas: ") 
    if ciclos == "minguante cheia crescente nova": 
        print("Muito bem, você acertou! <3 ")
    else:
        print("Que pena você errou! \n")
    menu()


    print("B) Descubra em qual lua acontece a grande festa: \n")
    lua = input("Escreva aqui sua resposta: \n")
    if lua == "cheia":
        print("Muito bem, você acertou! <3 ")
    else: 
        print("Você errou! ")

def escolha_caminho():
    print("-#"*16) 
    print("ESCOLHA SEU CAMINHO")
    print("-#"*16)

    escolha= int(input("Para onde você quer ir? \n"
                       "1. Descanso na beira do rio Igarapé \n2. Encontro com o pajé. " 
                       "Digite o número da sua escolha"))

    if escolha == 1:
        print("\n") 
        print('='*24)
        print('Descanso na beira do rio Igarapé')
        print('='*24)
        print("\n")

        print("Você tomou a decisão errada, era essencial você ter escolhido o encontro com o pajé! Para ir até o final da jornada você"
             " precisa saber priorizar o que realmente importa, portanto, sua jornada por aqui terminou!"
             "\nFIM DE JOGO \n")
        limpa_tela()
        menu()

    #TERCEIRO PERSONAGEM- JOVEM GUERREIRO
    else: 
        print("\n") 
        print('='*24)
        print('ENCONTRO COM A PAJÉ')
        print('='*24)
        print("\n") 

        print("Chegamos a clareira da floresta, esse momento será muito especial. Você agora é um JOVEM GUERREIRO GUARANI a pajé irá te dar")
        print("um conselho muito importante para a última etapa da jornada. Sente-se nesse tronco de árvore, o pajé já vai chegar ao")
        print ("seu encontro. Mas antes, vamos nos certificar se você realmente tem certeza que quer continuar na jornada: ") 
     #Printando a opcão: 
        menu()
        print("Aí vem a grande pajé da aldeia!"
              "-Mba'éichapa ndeka'aru? Jovem guerreiro, para você se encontrar com Jacy Tata, detentora dos segredos, você precisa se lembrar da palavra Coragem …"
              " Não esqueca isso: Todos nós vamos ser aquela a que o" 
              " nosso pensamento oferecer alimento. "
             " Agora você pode seguir esta coruja... Ela te levará as margens do rio igarapé e lá você vai poder descansar. ")

def hora_rango ():
    print("\n") 
    print('='*24)
    print('Dia seguinte: Hora do rango!')
    print('='*24)
    print("\n") 

    com_fome = input("A jovem guerreira acordou de uma noite tranquila e agora está com muita fome."
                 "Você está indo agora ao encontro de Kerû, um macaco muito brincalhão" 
                 "que também iniciou seus estudos na programacão agora e quer testar seu programa de números impar e par\n." 
                 "Kerû também é guardião do pomar da floresta e vai te dar a oportunidade de comer a fruta que quiser desde que você acerte o seu desafio, vamos lá! \n"
                 "Kerû quer que você acerte o seu tipo de banana preferido. Para isso, você deve inserir um número impar ou par de 1 à 5 e o programa devolverá"
                 "O tipo de banana e se você acertou ou não: \n")



    num = int(input("Insira um número: "))
    num2 = int(input("Insira um número: "))
    
    print(f"O primeiro número é {minha_calculadora(num)}"
      f"\nO segundo número é {minha_calculadora(num2)}"
      " \nVocê deu sorte! Kerû gosta de todos os tipos de banana! <3")

   #Escolhendo o premio
    fruta_preferida = input(f"Escolha a sua fruta favorita:\n banana, manga, abacaxi ou melancia? ")

    print(f"Muito bem, aguarde... Em instantes Kerû irá trazer sua {fruta_preferida}"
            " \nAqui está!")

def pai_onca ():
    print("Muito bem, agora que você está alimentado vamos continuar nossa jornada caminhando" 
      "agora por essa trilha de cutia.\n")
    input('Escreva "ok" para continuar: ')
    input("Espere um pouco, tem um buraco, escreva “parar”: ")
    print("O que será que tem nesse buraco? Espere, é Iauaretê, seu pai onca que caiu" 
      "em uma armadilha, vamos tira-lo de lá, ")
    input ("escreva 'ok' para dar o comando: ")
    print ("- Minha filha, muito obrigado! Foi Tupã que mandou você aqui! ")
    input ('Aperte o comando “andar” e depois “parar” embaixo do pé de jatobá:\n'
           'Comando 1:\n' 
           'Comando 2:\n') 

    print ('- Filha, está chegando a hora de saber se você realmente está preparada para receber' 
           'o segredo de Jacy- Tatá. Até aqui você teve alguns erros em algumas etapas,' 
           'mas agora, na última etapa você não poderá mais errar. Para chegar até Jacy ainda' 
           'você ainda deve percorrer alguns desafios. E para isso você irá precisar pegar uma'
           'pena do Acauã, o gavião branco. Com somente uma pena dele você poderá voar até Jacy-Tatá.')

    input ('- Onde eu encontro o Acauã? escreva "ok" para dar o comando perguntar' )

    print ("- Você terá de atravessar o cerrado. Depois subir a montanha da Pedra Furada." 
           "Mas há perigos. No cerrado moram catorze lobos-guará e eles vão tentar te impedir." 
            "Você vai precisar de amigos auxiliares. O ninho de Acauã fica na montanha. Espero que" 
            "você tenha guardado com muito carinho o conselho do grande Pajé, pois sem ele você não"
            "irá chegar até Jacy Tatá. ")

    input ('Pai, não sei se lembro quais foram exatamente as palavras do pajé. O que fazer agora?\n'
        'Aperte "ok" para dar o comando perguntar\n')

    print ('- Primeiro escolha os animais auxiliares, depois encontre novamente Kerû no pomar e ' 
       'acerte sua pergunta.  Com isso, ele irá te lembrar o conselho do grande pajé. '
       'Iauaretê deu um rugido e pouco a pouco foram surgindo vários animais: cutia,' 
       ' anta, o jabuti, o tamanduá, a preguiça, o macaco, o beija-flor, a coruja, o tucano,' 
       ' o mico-leão-dourado. ')

    input ("Escolha três animais protetores: ")

    print ("- Filho, eu te abencoo, e não se esqueca, quando precisar eu também posso te ajudar. ")
    input ("Escreva “andar” para ir embora.  ")

def final ():
    print("-#"*16)
    print("FINAL DA JORNADA")
    print("-#"*16)

    resposta = input("Agora você já voltou a ser SEU AVATAR estamos numa via de mão dupla, você precisa lembrar" 
                 " o conselho do pajé novamente?\n Digite sim ou não: ")
    #Escolhendo o caminho de pegar conselho com Keru ou continuar
    resposta = input("Agora você já voltou a ser SEU AVATAR estamos numa via de mão dupla, você precisa lembrar" 
                 " o conselho do pajé novamente?\n Digite sim ou não: ")
    if resposta == "sim":
        print ("Prepare-se para encontrar novamente o macaco Kerû. Desta vez ele está testando" 
               "seu mais novo conhecimento em Python, laços de repetição com while." 
               "Responda a pergunta do programa para conseguir o que precisa:\n"
               "Ok, vamos para o pomar, ao encontro de Kerû. Aqui está ele, sua pergunta é a seguinte:\n"
              "Olá, para que eu consiga te lembrar as palavras do grande pajé, você precisa usar"
              "meu primeiro programa com uso de while no Python <3. Além. disso você também"
              "vai precisar se lembrar sobre o primeiro personagem de uma história que você"
              "viu no comeco da jornada, vamos lá, não há tempo para perder!\n")

        animal = input("Qual era o animal que enganou a onca no primeiro teste que você fez? ")
        escolha = "jabuti"
        while animal != escolha:
            animal = input("Você já esqueceu?? Tente novamente: ")
        else: 
            print("Você conseguiu lembrar, muito bem!")
            print("A palavra é: Nós não somos guardiãs da natureza. Somos a natureza.")
    else: 
        print ("Vamos continuar a caminhada ruma ao cerrado. Nossa última e mais difícil etapa." 
               "Você ainda pode desistir se preferir: ")

def final_jornada ():
    print("Keretxu caminhou nesse caminho por um bom tempo antes de chegar ao encontro de Jacy-Tatá… Assim como você está nela agora."
      " Estamos indo em direção ao ninho de Acauã.\n Espere, seu auxiliar beija-flor está tentando lhe dizer algo:\n "
      "- Vem vindo um lobo-guará aí, ele já sentiu seu cheiro.\n"
      "O jabuti, acaba de sair do samburá (sacola grande indígena) para te dizer alguma coisa:\n "
      "- Amigue, faz o seguinte, fica debaixo daquela árvore e me ponha bem em cima do galho. " 
      " Não saia dali, deixe ele se aproximar bem. O resto deixe comigo. ")
    input (" Hora de ir para debaixo da árvore, aperte ir: ")
    resposta= input("Deseja aproveitar para descansar uns minutinhos? Sem problemas descansar dessa vez rss " 
                    " Digite sim ou não: ")
    if resposta == "sim": 
        print("\nzZzzzzzZ")
    else:
        print("Tudo bem então...")

    print("Depois de alguns minutos. \n - Pronto, disse o jabuti. Já dei um jeito no lobo," 
          "esperei o momento certo e consegui pular em cima dele, com meu casco ele desmaiou. ")
    input("Escreva “ir” para continuar a jornada: ")

    print("Agora o dia já escureceu. Espere, sua auxiliar coruja acaba de te avisar que tem mais" 
          "um lobo-guará se aproximando. Pense rápido, o que deseja fazer?") 

    escolha = input("1. Se esconder atrás de uma moita e ficar bem quieto esperando o lobo ir embora \n"
          "2. Se fingir de isca para o lobo e fazer uma armadilha com um cipó \n Digite o número"
          "de sua preferência: ")

    if escolha == "1":
        input("Ok, escreva “esconder” para ir atrás da moita\n")
        print("Essa não, o lobo guará sentiu o seu cheiro e VOCÊ MORREU!!!\n" 
              "infelizmente você tomou uma péssima decisão de se esconder, ao invés de encarar seu medo..." 
              "uma pena... você estava indo bem… FIM DE JORNADA")
        menu()
    else: 
        print("Ok. Para conseguir fazer sua armadilha você irá precisar:\n" 
          "1.pegar o cipó\n 2. fazer um nó escondido no chão")
        input("Digite os números do comando acima e depois escrava “ok”: ")
        print("Agora deite-se no chão e se faca de isca, não tenha medo, apenas confie." 
          "Agora espere o lobo se aproxima… ")
        input("Escreva os números de um a três: \n")
        input("Escreva ok para puxar o laço da armadilha: \n")
        print("Que ótimo, você conseguiu prender o lobo, parabéns pela coragem de se fazer de isca! "
          "Estamos chegando muito próximo a montanha da Pedra Furada. Espere um pouco," 
          "vem aí mais quatro lobos-guará ao mesmo tempo! Eles estão vindo na sua direção," 
          "está na hora de mostrar o seu lado onça e guerreiro que você já presenciou! ")
        input('Escreva o comando "ir" para dar o primeiro impulso e ++ para saltar. Digite: ')

        print("Parabéns você conseguiu se livrar dos lobos e de quebra chegou até o ninho do pássaro Acauã " 
          "e olha que surpresa boa: O ninho está vazio e há muitas penas." 
          "Escolha a mais bonita e se prepare para o fim dessa jornada <3 Escolher: ")

        input(' Escreva "ok" para pegar a pena escolhida: ')

        print("UAU! Parece que mal deu tempo para você escolher e agora você está no ombro do pássaro Acauã" 
          "Que velocidade hein?! Aproveite e relaxe um pouco, você merece, olhe para o céu!" 
          "Você passou por tantas provas e conseguiu chegar até o fim da sua jornada, assim como Keretxu"
          "Se você chegou até aqui você carregou com muito cuidado a palavra chave do grande pajé: CORAGEM - imóiámpápa "

          "Chegamos ao portão da casa cósmica de Jacy-Tatá, a mulher estrela, aquela  que revelou o grande segredo para Keretxu." 
          "Agora desfrute desse momento de sabedoria, em breve retornaremos para mais um capítulo da jornada") 


#Conhecendo o Jogador- PERSONAGEM1
player ()
#BOAS VINDAS- inicio do jogo
boasvindas()

#Printando a opcão menu: 
menu ()

#TESTE DE LÓGICA E PROGRAMACAO - RISCO DE DERROTA1
perguntas_teste()

#ETAPA 3: CICLO LUNAR
ciclo()

#ETAPA 4: TERCEIRO RISCO DE DERROTA
escolha_caminho()

#HORA DO RANGO- ENCONTRO COM KERU E DICA DA PAJÉ
hora_rango ()

#ENCONTRO DO GUERREIRO COM O PAI ONCA

pai_onca ()

#Encontro Keru para etapa final
final()

#Printando a funcão opcão para desistencia: 
menu()

#Etapafinal + última possibilidade de derrota ou vitória
final_jornada()