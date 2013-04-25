#! /usr/bin/python
import random, sys 
from math import exp, sin, cos, log, tan, sinh

# Constantes
A = 1.0
B = 100.0
n = 500
u = 1e-20

def error(expr1, expr2, valor_min, valor_max, nro_test, umbral):
  i = 0
  fallos = 0
  while (i < nro_test): 
   a = random.uniform(valor_min, valor_max)
   b = random.uniform(valor_min, valor_max)
   if (abs(eval(expr1) - eval(expr2)) > umbral):
     fallos += 1
   i += 1
  return (fallos*100/float(nro_test))
  
if __name__ == '__main__':
  if (len(sys.argv) == 7):
    expr1 = sys.argv[1]
    expr2 = sys.argv[2]
    min_value = float(sys.argv[3])
    max_value = float(sys.argv[4])
    numero_test = int(sys.argv[5]) 
    umbral = float(sys.argv[6])
    print "{0} {1} {2} {3} {4} {5}".format(expr1, expr2, min_value, max_value, numero_test, umbral)
    print "Porcentaje de fallos: {0}%".format(error(expr1, expr2, min_value, max_value, numero_test, umbral))
  else: 
    print "La forma de uso es: {0} expr1 expr2 min_value max_value numero_test umbral".format(sys.argv[0])
    print "Se usan los valores por defecto:"
    print "{0} expr1    expr2         min_value  max_value numero_test umbral fallos".format(sys.argv[0])
    print "{0} (a*b)**3 (a**3)*(b**3) 1.0        100.0     500         1e-20  {1}".format(sys.argv[0], error('(a*b)**3', '(a**3)*(b**3)', A, B, n, u))
    print "{0} (a/b)    1/(b/a)       1.0        100.0     500         1e-20  {1}".format(sys.argv[0], error('(a/b)', '1/(b/a)', A, B, n, u))
