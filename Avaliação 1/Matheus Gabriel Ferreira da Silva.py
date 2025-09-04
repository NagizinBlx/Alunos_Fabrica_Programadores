# CALCULADORA DE IMC COM CATEGORIZAÇÃO
# ENTREGA ATÉ 04/09/2025

# FAZER UM FORK E UM PULL REQUEST PARA ENTREGAR

# Nome: Matheus Gabriel Ferreira da Silva

print('Insira sua altura:')
altura = input()
print('insira seu peso:')
peso = input()

altura = float(altura)
peso = float(peso)

resultado = altura * altura
imc = peso / resultado

if imc >= 40:
    print('Obesidade Grau III (morbida)')    
elif imc > 34.9:
    print('Obesidade Grau II')
elif imc > 29.9:
    print('Obesidade Grau I')
elif imc > 24.9:
    print('Sobrepeso')
elif imc > 18.5:
    print('Peso normal')
else:
    print('Abaixo do peso') 
