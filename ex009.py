#ex009 - Faça um programa leia um numero inteiro qualquer e imprima a sua tabuada na tela.
n = int(input("Digite um número para a tabuada: "))
#t1 = n * 1
#t2 = n * 2
#t3 = n * 3
#t4 = n * 4
#t5 = n * 5
#t6 = n * 6
#t7 = n * 7
#t8 = n * 8
#t9 = n * 9
#t10 = n * 10 abaixo um caminho mais otimizado para fazer o exercicio.
print("-" * 12)
print("a tabuada do número {}".format(n))
print("{} x {:2} = {:2}".format(n, 1, n*1))
print("{} x {:2} = {:2}".format(n, 2, n*2))
print("{} x {:2} = {:2}".format(n, 3, n*3))
print("{} x {:2} = {:2}".format(n, 4, n*4))
print("{} x {:2} = {:2}".format(n, 5, n*5))
print("{} x {:2} = {:2}".format(n, 6, n*6))
print("{} x {:2} = {:2}".format(n, 7, n*7))
print("{} x {:2} = {:2}".format(n, 8, n*8))
print("{} x {:2} = {:2}".format(n, 9, n*9))
print("{} x {:2} = {:2}".format(n, 10, n*10))
print("-" * 12)