salario= float(input('Informe seu sálario: '))

if salario > 8250.00:
    aumento= salario * 1.10

else:
    
    aumento= salario * 1.15

print('Seu seu salario atual é:',aumento)

'''else não precisa de uma condiçao, se nenhum
if aconetcer ele excuta na sequêcia'''