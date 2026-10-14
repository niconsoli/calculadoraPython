import math

print("""Calculadora em Python!
As operações serão realizadas conforme sua requisição. """)
repetir = True
while repetir:
    print("""
Por favor, escolha uma das opções abaixo:
1. Soma;
2. Subtração;
3. Multiplicação;
4. Divisão;
5. Média aritmética;
6. Potenciação;
7. Radiciação;
8. Fatorial;
9. Logaritmo;
10. Teorema de Pitágoras;
11. MMC (Mínimo Múltiplo Comum);
12. MDC (Máximo Divisor Comum);
13. Seno;
14. Cosseno;
15. Tangente;
16. Porcentagem;
0. Sair.""")
    opc = input()

    match opc:
        case "0":
            print("Certo, encerrando...")
            repetir = False
        case "1":
            print("Perfeito, quantos números iremos somar?")
            n = int(input())
            if  n > 1:
                numbers = []
                for i in range(n):
                    print(f"Qual o {i + 1}º número?")
                    numbers.append(input())
                soma = 0
                for i in range(len(numbers)):
                    soma += float(numbers[i])
                print(f"O resultado da sua soma de {numbers} é igual a {soma}!")
            else:
                print("Por favor, inserir um número maior do que 1.")
 
        case "2":
            print("Perfeito, quantos números iremos subtrair?")
            n = int(input())
            if n > 1:
                numbers = []
                for i in range(n):
                    print(f"Qual o {i + 1}º número?")
                    numbers.append(input())
                subtracao = float(numbers[0])
                for i in range(1, len(numbers)):
                    subtracao -= float(numbers[i])
                print(f"O resultado da sua subtração de {numbers} é igual a {subtracao}!")
            else:
                print("Por favor, inserir um número maior do que 1.")

        case "3":
            print("Perfeito, quantos números iremos multiplicar?")
            n = int(input())
            if n > 1:
                numbers = []
                for i in range(n):
                    print(f"Qual o {i + 1}º número?")
                    numbers.append(input())
                multiplicacao = float(numbers[0])
                for i in range(1, len(numbers)):
                    multiplicacao *= float(numbers[i])
                print(f"O resultado da sua multiplicação de {numbers} é igual a {multiplicacao}!")
            else:
                print("Por favor, inserir um número maior do que 1.")

        case "4":
            print("""
Na divisão temos o dividendo e o divisor
Ou também, numerador e denominador!
Por exemplo, para ½: 
O dividendo, ou numerador, seria 1
Consequentemente, o divisor, ou o denominador, seria 2!
E a divisão, quando efetuada, geraria o resultado 0,5.
Compreendendo isso, me diga, qual o dividendo/numerador da sua divisão?""")
            numerador = float(input())
            print("Certo, e o divisor/denominador?")
            denominador = float(input())
            if denominador != 0:
                divisao = numerador / denominador
                print(f"O resultado de {numerador} dividido por {denominador} é equivalente a {divisao}!")
            else:
                print("Não é possível dividir nenhum número por zero. Por favor, escolha outro número como seu denominador!")

        case "5":
            print("""
Para média aritmética, o cálculo será feito desta forma:
Suponha que realizaremos o cálculo de três números, o 1, o 2 e o 3.
Primeiro, efetuaremos a soma entre os três. No nosso caso, 1 + 2 + 3 seria igual a 6.
Em seguida, dividiremos este número pela quantia de números que foi somada.
No nosso caso, escolhemos três números (1, 2 e 3). Então a soma destes, 6, seria dividido por 3
Assim, encontraríamos a média aritmética com o valor de 2.0!
Vamos experimentar? Calcularemos a média aritmética de quantos números?""")
            n = int(input())
            if n > 1:
                numbers = []
                for i in range(n):
                    print(f"Qual é o {i + 1}º número?")
                    numbers.append(input())
                soma = 0
                for i in range(len(numbers)):
                    soma += float(numbers[i])
                mediaAritmetica = float(soma / len(numbers))
                print(f"O resultado da média aritmética dos números {numbers} é igual a {mediaAritmetica}!")
            else: 
                print("Por favor, inserir um número maior do que 1.")

        case "6": 
            print("""
Potenciação representa multiplicar um número n vezes por ele mesmo.
Por exemplo, vamos supor que você quer descobrir quanto vale 2³ (ou, interpretando, base 2 sobre o expoente 3!).
Isto é, nada mais do que, 2 multiplicado por 2, mais uma vez multiplicado por 2.
Sabemos que 2 multiplicado por 2 é quatro, que, por sua vez, quando multiplicado por 2, retorna o nosso valor final: oito
Entretanto, 2 * 2 * 2, ou 2³ é igual a 8.
Vamos experimentar? Qual será a base da sua potenciação?
Para fins educativos, a base da continha que fizemos de explicação é o dois (2)!""")
            base = int(input())
            print(f"Perfeito! E quantas vezes iremos multiplicar {base} por ele mesmo?")
            expoente = int(input())
            if expoente > 0:
                potenciacao = base
                for i in range(abs(expoente - 1)):
                    potenciacao *= base
                print(f"O resultado da potenciação de {base} pelo expoente {expoente} é igual a {potenciacao}!")
            elif expoente == 0:
                print(f"""
Para potências de zero, todo número elevado a zero é igual a um.
Ou seja, no seu caso: {base} elevada a zero, também é igual a 1.""")
            elif expoente < 0:
                potenciacao = base
                for i in range(abs(expoente + 1)):
                    potenciacao *= base
                potenciacao_negativo = 1 / potenciacao
                print(f"O resultado da potenciação de {base} pelo expoente {expoente} é igual a {potenciacao_negativo}!")
            elif base == 0 and expoente < 0:
                print("Ao realizar a potenciação para zero com um expoente negativo, estaremos invertendo o cálculo para uma divisão de denominador zero, e não é possível calcular uma divisão com denominador zero! Por favor, escolha outro número.")

        case "7":
            print("""
Radiciação é o processo oposto à potenciação!
Isto é, se considerarmos que 2², ou 2 * 2 é igual a quatro.
Logo saberemos a raiz quadrada de quatro é igual a dois!
A raiz ser quadrada significa que o índice buscado é igual a 2. É o índice padrão, quando não determinado.
Isso nada mais significa que o número que estamos buscando precisa ter como expoente 2, ou seja, multiplicar-se por si mesmo duas vezes para chegar no nosso número-base!
Por causa disso, a resposta funciona dos dois lados:
Tanto 2² é igual a 4, quanto 2√4 é igual a 2!
A raiz pode ter outros índices, por exemplo 3√8.
Neste caso, estamos buscando um número que multiplicado por ele mesmo \033[1mtrês\033[0m vezes, retorne oito.
Ou seja, o número dois! 2 * 2 * 2 é igual a oito! Portanto 3√8 = 2.
Quer entender um pouco melhor na prática? Qual vai ser o índice da nossa raiz?""")
            indice = int(input())
            if indice > 1:
                print("Perfeito! E qual será o nosso radicando (o número cuja raiz iremos encontrar)?")
                radicando = int(input())
                if radicando < 0:
                    print("O cálculo da radiciação para radicandos negativos com índices ímpares e pares não tem respostas reais! Por favor, insira outro número como seu radicando.")
                else:
                    radiciacao = math.pow(radicando, 1 / indice)
                    print(f"O resultado da radiciação de {radicando} pelo índice {indice} é igual a {radiciacao}!")
            else:
                print("Por favor, insira um valor para índice maior do que 1.")  

        case "8":
            print("""
Para calcularmos o fatorial de um número, multiplicaremos ele por todos os números que vem antes dele, com exceção do zero.
Para entendermos melhor, eis um exemplo!
O fatorial de 3 é calculado por multiplicar este por todos os números que o antecedem, ou seja:
3 multiplicado por 2 e multiplicado por 1: resultando em seis!
Vamos calcular um fatorial? Qual número você quer calcular o fatorial?""")
            base = int(input())
            if base > 0:
                fatorial = base
                for i in range(base, 1, -1):
                    fatorial *= (i - 1)
                print(f"O resultado do fatorial de {base} é igual a {fatorial}!")
            elif base == 0:
                print("Para o caso específico de 0!: todos os números multiplicados por zero são iguais a um. Sendo assim, 0! = 1.")
            elif base < 0:
                print("Não é possível calcular o fatorial de números negativos! Por favor, escolha outro número.")

        case "9":
            print("""
O logaritmo fecha o nosso trio, com a radiciação e a potenciação.
Para entendermos melhor, vamos analisar a estrutura do logaritmo!
Para a estrutura logₐb = x, esse "a"zinho pequeno é o que chamamos de base. Caso não determinado, o padrão é a base 10.
Já esse b, colado com a nossa base, é o logaritmando, o valor que estamos tentando encontrar! Por fim, x representa, claro, o logaritmo.
O que estamos procurando é um processo análogo à radiciação e à potenciação: queremos um expoente que, quando eleve nossa base, resulte no logaritmando!
No nosso exemplo, seria um valor b que equivale a aˣ. Por isso, logₐb = x é equivalente a aˣ = b.
Esse é um pouquinho mais complicado de entender! Talvez possamos entender melhor praticando!
Qual será a base do nosso logaritmo? log\033[1mₐ\033[0m b = x""")
            base = int(input())
            if base > 1:
                print("Perfeito! E agora, qual será o nosso logaritmando? logₐ\033[1mb\033[0m = x")
                logaritmando = int(input())
                if logaritmando > 0:
                    logaritmo = math.log(logaritmando, base)
                    print(f"O resultado do logaritmo de {logaritmando} pela base {base} é igual a {logaritmo}!")
                else:
                    print("O valor do logaritmando não pode ser menor do que zero! Por favor, escolha outro número.")
            else:
                print("O valor da base do seu logaritmo precisa ser maior do que um! Por favor, escolha outro número.")

        case "10":
            print("""
Um dos mais populares e emblemáticos conceitos matemáticos do mundo, o Teorema de Pitágoras, consiste em uma das principais fórmulas da trigonometria!
Para entendermos, precisamos pensar em um triângulo retângulo. Pense em um triângulo fatiado ao meio! A ideia é essa mesmo, a metade de um triângulo, com um ângulo reto de 90º.
Agora, precisaremos entender os conceitos de catetos e da hipotenusa, que utilizaremos neste cálculo.
A hipotenusa é o lado mais longo do nosso triângulo retângulo, a nossa grande linha diagonal!
Os outros dois lados do nosso triângulo retângulo chamaremos de catetos!
O Teorema diz que, quando multiplicarmos ambos os catetos elevados ao quadrado, o valor também deve ser equivalente à hipotenusa elevada ao quadrado!
É o que diz hip² = cateto_um² + cateto_dois²!
Este é o básico que precisaremos saber! Vamos praticar?
Primeiro, me diga. Qual valor você tem? Você quer encontrar a hipotenusa com o cálculo dos dois catetos, ou algum dos dois catetos com a hipotenusa?
1. Calcular a hipotenusa;
2. Calcular um cateto.""")
            opcPitg = input()
            match opcPitg:
                case "1":
                    print("Perfeito! Então me fala o valor do nosso primeiro cateto, por favor!")
                    cat1 = int(input())
                    if cat1 > 0:
                        print("Certo! E o segundo cateto, equivale a quanto?")
                        cat2 = int(input())
                        if cat2 > 0:
                            hipotenusa = math.sqrt((math.pow(cat1, 2) + math.pow(cat2, 2)))
                            print(f"O resultado da hipotenusa do nosso triângulo retângulo, de catetos {cat1} e {cat2}, equivale a {hipotenusa}!")
                        else:
                            print("O valor do cateto não pode ser negativo! Por favor, escolha outro número.")
                    else:
                        print("O valor do cateto não pode ser negativo! Por favor, escolha outro número.")
                case "2":
                    print("Perfeito! Então me fala o valor da hipotenusa do nosso triângulo retângulo!")
                    hipotenusa = int(input())
                    if hipotenusa > 0:
                        print("Certo! Agora, preciso do valor do cateto que você já conhece, para determinarmos o outro!")
                        cat1 = int(input())
                        if cat2 > 0:
                            cat2 = math.sqrt((math.pow(cat1, 2) - math.pow(hipotenusa, 2)))
                            print(f"O cateto do nosso triângulo retângulo, de cateto {cat1} e hipotenusa {hipotenusa}, equivale a {cat2}!")
                        else:
                            print("O valor da hipotenusa não pode ser negativo! Por favor, escolha outro número.")
                    else:
                        print("O valor da hipotenusa não pode ser negativo! Por favor, escolha outro número.")

        case "11": # MMC (Mínimo Múltiplo Comum);
            print("""
O Mínimo Múltiplo Comum é o menor número inteiro positivo, diferente de zero, múltiplo comum dentre uma série de números.
Para entendermos melhor, vou dar um exemplo. O MMC de 5, 10 e 20 é igual a vinte; Como todos os números são múltiplos de cinco, o 20 é o primeiro a ser encontrado em comum, dentre seus valores!
Outro exemplo é o MMC de 3, 5 e 7, que é igual a 105; uma vez que os três números são divisíveis por 105, e este é o menor número inteiro positivo múltiplo deles.
Dinâmico, não é mesmo? Vamos calcular o MMC de quantos números?""")
            n = int(input())
            numeros = []
            mmc = 1
            for i in range(n):
                print(f"Qual o {i + 1}º número?")
                numeros.append(int(input()))
            for i in range(len(numeros)):
                mmc = math.lcm(*numeros)
            print(f"O valor do Mínimo Múltiplo Comum entre os números {numeros} é igual a {mmc}!")

        case "12":
            print("""
O Máximo Divisor Comum é o maior número inteiro capaz de dividir uma série de números e retornar um valor exato, sem restos.
Para entendermos melhor, vou dar um exemplo. O MDC de 5, 10 e 20 é igual a cinco; uma vez que os três números são divisíveis por cinco, o maior número inteiro capaz de dividir todos eles.
Outro exemplo é o MDC de 3, 6 e 9, que é igual a três; uma vez que os três números são divisíveis por três, e este é o maior número inteiro capaz de dividir todos eles.
Dinâmico, não é mesmo? Vamos calcular o MDC de quantos números?""")
            n = int(input())
            numeros = []
            mdc = 1
            for i in range(n):
                print(f"Qual o {i + 1}º número?")
                numeros.append(int(input()))
            for i in range(len(numeros)):
                mdc = math.gcd(*numeros)
            print(f"O valor do Máximo Divisor Comum entre os números {numeros} é igual a {mdc}!")

        case "13":
            print("""
Parte do trio de razões trigonométricas, o Seno se trata da divisão do cateto oposto de um triângulo retângulo pela hipotenusa do mesmo.
Para entendê-lo melhor, precisamos entender um triângulo retângulo!
Este, nada mais é do que um triângulo fatiado ao meio! Isto é, teremos metade de um triângulo, com um dos lados possuindo um ângulo reto!
O lado mais longo do nosso triângulo retângulo chamaremos de hipotenusa! Esta, que usaremos no cálculo do nosso seno.
Agora, para entendermos como identificar os catetos adjacente e oposto, precisaremos verificar o ângulo de referência, que é um dos ângulos agudos do nosso triângulo retângulo.
Desta forma, fica didático: O cateto que estiver oposto ao nosso ângulo de referência, será o nosso cateto oposto. O cateto que estiver adjacente ao nosso ângulo de referência, será o nosso cateto adjacente!
Assim, usaremos o valor do cateto oposto dividido pela hipotenusa para calcularmos nosso seno!
Vamos nessa? Qual o valor do ângulo você gostaria de descobrir o seno?""")
            valor = int(input())
            seno = math.sin(math.radians(valor))
            print(f"O seno do nosso ângulo de {valor}º equivale a {seno}!")

        case "14":
            print("""
O Cosseno é um dos valores mais importantes do mundo da Trigonometria! 
Se trata da divisão do cateto adjacente de um triângulo retângulo pela hipotenusa do mesmo.
Para entendê-lo melhor, precisamos entender um triângulo retângulo!
Este, nada mais é do que um triângulo fatiado ao meio! Isto é, teremos metade de um triângulo, com um dos lados possuindo um ângulo reto!
O lado mais longo do nosso triângulo retângulo chamaremos de hipotenusa! Esta, que usaremos no cálculo do nosso cosseno!
Agora, para entendermos como identificar os catetos adjacente e oposto, precisaremos verificar o ângulo de referência, que é um dos ângulos agudos do nosso triângulo retângulo!
Desta forma, fica didático: O cateto que estiver oposto ao nosso ângulo de referência, será o nosso cateto oposto. O cateto que estiver adjacente ao nosso ângulo de referência, será o nosso cateto adjacente!
Assim, usaremos o valor do cateto adjacente dividido pela hipotenusa para calcularmos nosso cosseno!
Vamos nessa? Qual o valor do ângulo você gostaria de descobrir o cosseno?""")
            valor = int(input())
            cosseno = math.cos(math.radians(valor))
            print(f"O cosseno do nosso ângulo de {valor}º equivale a {cosseno}!")

        case "15":
            print("""
A tangente se trata da divisão dos dois catetos que compõem um triângulo retângulo.
Para entender melhor do que estou falando, precisamos entender o que é um triângulo retângulo!
O que, resumidamente, nada mais é do que um triângulo fatiado ao meio! Isto é, teremos metade de um triângulo, com um dos lados possuindo um ângulo reto!
O lado mais longo do nosso triângulo retângulo chamaremos de hipotenusa.
Mas, para entendermos como identificar os catetos adjacente e oposto, precisaremos antes verificar o ângulo de referência, que será um dos ângulos agudos do nosso triângulo retângulo.
Desta forma, fica didático: O cateto que estiver oposto ao nosso ângulo de referência, será o nosso cateto oposto. O cateto que estiver adjacente ao nosso ângulo de referência, será o nosso cateto adjacente!
Assim, simplesmente precisaremos dividir esses valores, o \033[1mcateto oposto\033[0m dividido pelo \033[1mcateto adjacente\033[0m!
Vamos nessa? Qual o valor do ângulo você gostaria de descobrir a' tangente?""")
            valor = int(input())
            tangente = math.tan(math.radians(valor))
            print(f"A tangente do nosso ângulo de {valor}º equivale a {tangente}!")

        case "16":
            print("""
A porcentagem é um dos mais comuns e populares usos cotidianos da matemática nos tempos modernos!
Entendê-la é simples, também! Imagine que estamos tentando descobrir quanto é 50% de 10.
A ideia é como se dividíssemos 10 em 100 pedacinhos separados. Dessa forma, queremos saber quanto valem 50 desses bloquinhos juntos!
É por isso que se chama porCENtagem! Do número cem!
O valor de uma única unidade desse bloquinho seria igual a 1% do nosso valor total.
Vamos lá! Qual o número que calcularemos uma porcentagem hoje?""")
            base = int(input())
            print("E quantos porcento (ou quantos bloquinhos) calcularemos deste número hoje?")
            fator = int(input())
            fatorCem = fator / 100
            porcentagem = base * fatorCem
            print(f"{fator}% de {base} equivale a {porcentagem}!")

        case _:
            print("A opção que você escolheu é inválida. Por favor, tente novamente!")