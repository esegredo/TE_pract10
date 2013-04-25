#! /usr/bin/python
import sys, math
from modulo_error import error

#constantes
A = 1.0
B = 100.0
numero_test = 500
umbral = 1e-20
lista_identidades = [ ('(a*b)**3', '(a**3)*(b**3)'), 
                      ('a/b','1/(b/a)'), 
                      ('exp(a+b)','exp(a)*exp(b)'),
                      ('log(a**b)','b*log(a)'),
                      ('a-b','-(b-a)'),
                      ('(a*b)**4','(a**4)*(b**4)'),
                      ('(a+b)**2','(a**2)+2*a*b+(b**2)'),
                      ('(a+b)*(a-b)','(a**2)-(b**2)'),
                      ('log(a*b)','log(a)+log(b)'),
                      ('a*b','exp(log(a)+log(b))'),
                      ('1/((1/a)+(1/b))','a*b/(a+b)'), 
                      ('a*(sin(b)**2+cos(b)**2)','a'), 
                      ('sinh(a+b)','(exp(a)*exp(b)-exp(-a)*exp(-b))/2'), 
                      ('tan(a+b)','sin(a+b)/cos(a+b)'), 
                      ('sin(a+b)','sin(a)*cos(b)+sin(b)*cos(a)') 
										]

if __name__ == '__main__':
  if (len(sys.argv) == 10):
    min_value = float(sys.argv[1])
    max_value = float(sys.argv[2])
    numero_test = int(sys.argv[3]) 
    nombre_fich = sys.argv[4]
    umbrales = map(float, sys.argv[5:])

    # Abrimos el fichero para escritura
    fich = open(nombre_fich, 'w')

    for ident in lista_identidades:
      fich.write("expr1: {0}\n".format(ident[0]))
      fich.write("expr2: {0}\n".format(ident[1]))
      for umb in umbrales:
        fich.write("% de fallos para el umbral {0}: {1}\n".format(umb, error(ident[0], ident[1], min_value, max_value, numero_test, umb)))
      fich.write("\n")

    # Cerramos el fichero
    fich.close()
  else: 
    print "La forma de uso es {0} min_value max_value numero_test nombre_fichero umbral_1 umbral_2 ... umbral_5".format(sys.argv[0])
    print "Se usan los valores por defecto:" 
    print " {0} expr1    expr2         min_value  max_value numero_test umbral % fallos".format(sys.argv[0])
    print " {0} (a*b)**3 (a**3)*(b**3) 1.0        100.0     500         1e-20  {1}".format(sys.argv[0], error('(a*b)**3', '(a**3)*(b**3)', A, B, numero_test, umbral))
    print " {0} (a/b)    1/(b/a)       1.0        100.0     500         1e-20  {1}".format(sys.argv[0], error('(a/b)', '1/(b/a)', A, B, numero_test, umbral))
