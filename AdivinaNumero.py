from random import *;

print("Bueno,he pensado en un numero, adivina cuales")
intentosUsuario = 0;
intentosMax = 8;
numeroAleatorio = round(randint(1, 101))
while intentosMax > intentosUsuario:
    numeroUsuario = int(input('Ingrese un numero '));
    intentosUsuario += 1;
    if(numeroUsuario >  numeroAleatorio):
        print('Tu numero esta por encima del mio');
        continue;
    elif(numeroUsuario < numeroAleatorio):
        print('Tu numero esta por debajo del mio');
        continue;
    else:
        print(f'acertaste lo hiciste en  {intentosUsuario}')
        break;



