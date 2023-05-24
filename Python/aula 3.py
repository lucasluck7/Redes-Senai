#aula de média e condição 
#if e else - (se) e (ou algum)
#operadores relacionais

"""">  : maior 
<  : menor 
== : igual
>=: maior ou igual 
<= : menor ou igual 
!= : diferente 
< >: diferente 
"""


nota1=float(input('Informe a nota 1: '))
nota2=float(input('Informe a nota 2: '))
nota3=float(input('Informe a nota 3: '))

#se usa o float para trabalhar com números quebrados

media=(nota1+nota2+nota3)/3
if media >= 6:
    print('APROVADO PARABÉNS!!') 

elif media >= 5:
    print('Conselho de classe')
else:
    print('REPROVADO, ESTUDE MAIS!!')    


'''Dentro do else consigo colocar
          mais condições'''
        
    #elif é utilizado para ter uma nova condição
 

print('A sua média foi: ', media)  
#ideal sempre fazer boas práticas na programação




