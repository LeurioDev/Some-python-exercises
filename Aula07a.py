n1 = int(input('O valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
sub = n1 - n2
div = n1 / n2
mult = n1 * n2
div_int = n1//n2
div_resto = n1 % n2
expo = n1**n2
print('A soma vale: {:->16}\nA subtração vale: {:->11}\nA divisão vale: {:->13}\nA multiplicação vale: {:->7}\nA divisão inteira vale: {:->5}\n'
      'O resto da divisão vale: {:->4}\nA potência vale: {:->12}\n'.format(s,sub,div,mult,div_int,div_resto,expo))