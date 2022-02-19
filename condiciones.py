# Condiciones

esMayorEdad = True

if esMayorEdad == True: # if not esMayorEdad  and or
   print('es mayor de edad')
   print('esto es del if')
else:
    print('no es mayor de edad')
    print('esto es parte del elfe')

print('mensaje de prueba') # Recordar tabulacion

# Ejercicion

"""
pedir: verbo en infinitivo(ar, er, ir) x 
despues: conjugar el verbo x
"""
prombres={
    'yo': {
        'ar': 'o',
        'er': 'o',
        'ir': 'o'
    },
    'el': {
        'ar': 'a',
        'er': 'e',
        'ir': 'e'
    },
    'ella':{
        'ar': 'a',
        'er': 'e',
        'ir': 'e'
    }
}

verbo= input()

x1=verbo[len(verbo)-1]
x2=verbo[len(verbo)-2]

if x1=='r' and (x2== 'a' or 'e' or 'i'):
  terminacion=x2+x1
  sinterminacion= verbo.replace(terminacion, "")
  for final in prombres:
      print(final, sinterminacion+prombres[final][terminacion])
  