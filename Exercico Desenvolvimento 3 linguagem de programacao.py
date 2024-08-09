##Ranger Escreva um código que imprima todos os números exceto o número 13.
for andar in range (1, 21):
  if (andar == 13):
     continue
  print(andar)


## While Escreva um código que imprima todos os números exceto o número 13.
contador = 1 
while (contador <= 20):
  if (contador == 13):
     contador = contador + 1
     continue
  else:
      print (contador)
      contador += 1


#imprima eles em ordem decrescente (20, 19, 18...)
for andar in range (20, 0, -1):
  if (andar == 13):
     continue
  else:
   print (andar)