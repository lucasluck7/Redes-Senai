
num1=int(input('Informe um número para cáculo: '))

print('Tabuada do',':')

for i in range(1,11):
    resultado = num1 * i
    print(num1,'x', i,"=", resultado)