# def suma(*args):
#     resultado = 0
#     print(args)
#     for valor in args:
#         resultado = resultado + valor
#     return resultado
#
# print(suma(1, 2, 3, 4, 5))  # HASTA MAS ARGUMENTOS SI GUSTAS

def suma(**kwargs):
	print(kwargs['name'])

suma(name = 'Eduardo', z = 20 , x=2.0) #HASTA MAS ARGUMENTOS SI GUSTAS