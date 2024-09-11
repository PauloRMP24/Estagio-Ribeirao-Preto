# QUESTÃO 1

def seq_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False


# Solicita um número ao usuário
numero = int(input("Informe um número: "))

# Verifica se o número pertence à sequência de Fibonacci
if seq_fibonacci(numero):
    print(f"O número {numero} está na sequência de Fibonacci")
else:
    print(f"O número {numero} não está na sequência de Fibonacci")

#QUESTÃO 2
def verificar_string(string):
    #Converter a srting para minúscula e contar a quantidade de vezes que a letra "a" aparece
    aparencias = string.lower().count('a')

    if aparencias > 0:
        print(f"A letra 'a' aparece {aparencias} vezes na string")
    else:
        print("A letra 'a' não aparece na string")


frase = input("Digite qualquer coisa: ")

verificar_string(frase)

#QUESTÃO 3
indice = 12
soma = 0
k = 1

while k < indice:
    k = k + 1
    soma = soma + k

print(soma)
#QUESTÃO 4
#a)
seq_a = [1,3,5,7]
prox_a = seq_a[-1] + 2
print(f"O próximo elemento é {prox_a}")

print("\n\n")
#b)
seq_b = [2,4,8,16,32,64]
prox_b = seq_b[-1] * 2
print(f"O próximo elemento é {prox_b}")

print("\n\n")
#c)
seq_c = [0,1,4,9,16,25,36]
prox_c = (len(seq_c))**2
print(f"O próximo elemento é {prox_c}")

print("\n\n")
#d)
seq_d = [4,16,35,64]
prox_d = (2 * len(seq_d) + 2)**2
print(f"O próximo elemento é {prox_d}")

print("\n\n")
#e)
seq_e = [1,1,2,3,5,8]
prox_e = seq_e[-1] + seq_e[-2]
print(f"O próximo elemento é {prox_e}")

print("\n\n")
#f)
seq_f = [2,10,12,16,17,18,19]
prox_f = seq_f[-1] + 1
print(f"O próximo elemento é {prox_f}")

#QUESTÃO 5
import time

lamps = {
    "A": {"estado": "apagada", "temperatura": "fria"},
    "B": {"estado": "apagada", "temperatura": "fria"},
    "C": {"estado": "apagada", "temperatura": "fria"}
}

def ligar(lamp):
    lamps[lamp]["estado"] = "acesa"
    lamps[lamp]["temperatura"] = "quente"

def desligar(lamp):
    lamps[lamp]["estado"] = "apagada"

    if lamps[lamp]["estado"] == "acesa":
        lamps[lamp]["temperatura"] = "quente"

def verificar():
    for lamp, status in lamps.items():
        print(f"Lâmpada {lamp}: {status['estado']} e {status['temperatura']}")


ligar("A")
time.sleep(2)

desligar("A")
ligar("B")

print("Verificando: ")
verificar()