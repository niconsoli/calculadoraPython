import numbers
import math
from numpy import append

print("""Calculadora em Python!
As operações serão realizadas conforme sua requisição!""")
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
Perfeito! Na divisão temos o dividendo e o divisor
Ou também, numerador e denominador!
Por exemplo, para ½: 
O dividendo, ou numerador, seria 1
Consequentemente, o divisor, ou o denominador, seria 2!
E a divisão, quando efetuada, geraria o resultado 0,5.
Compreendendo isso, me dia, qual o dividendo/numerador da sua divisão?""")
            numerador = float(input())
            print("Certo, e o divisor/denominador?")
            denominador = float(input())
            divisao = float(numerador / denominador)
            print(f"O resultado de {numerador} dividido por {denominador} é equivalente a {divisao}!")

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

        case "7":
            print("""
Radiciação é o processo oposto à potenciação!
Isto é, se considerarmos que 2², ou 2 * 2 é igual a quatro.
Logo saberemos a raiz quadrada de quatro é igual a dois!
A raiz ser quadrada significa que o índice buscado é igual a 2.
Isso nada mais significa que o número que estamos buscando precisa ter como expoente 2, ou seja, multiplicar-se por si mesmo duas vezes para chegar no nosso número-base!
Por causa disso, a resposta funciona dos dois lados:
Tanto 2² é igual a 4, quanto 2√4 é igual a 2!
A raiz pode ter outros índices, por exemplo 3√8.
Neste caso, estamos buscando um número que multiplicado por ele mesmo \033[1mtrês\033[0m vezes, retorne oito.
Ou seja, o número dois! 2 * 2 * 2 é igual a oito! Portanto 3√8 = 2.
Quer entender um pouco melhor na prática? Qual vai ser o índice da nossa raiz?""")
            indice = int(input())
            print("Perfeito! E qual será o nosso radicando (o número cuja raiz iremos encontrar)?")
            radicando = int(input())

            
# 7. Radiciação;
# 8. Fatorial;
# 9. Logaritmo;
# 10. Teorema de Pitágoras;
# 11. MMC (Mínimo Múltiplo Comum);
# 12. MDC (Máximo Divisor Comum);
# 13. Seno;
# 14. Cosseno;
# 15. Tangente;
# 16. Porcentagem;