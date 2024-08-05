
def cantidadLetras(frase, letras):
    cantidad_letras1 = frase.count(letras[0]);
    cantidad_letras2 = frase.count(letras[1]);
    cantidad_letras3 = frase.count(letras[2]);
    print('*' * 23);
    print('CANTIDAD DE LETRAS');
    print(f'Hemos encontrado la letra {letras[0]} repetida en {cantidad_letras1} veces en la frase ingresada');
    print(f'Hemos encontrado la letra {letras[1]} repetida en {cantidad_letras2} veces en la frase ingresada');
    print(f'Hemos encontrado la letra {letras[2]} repetida en {cantidad_letras3} veces en la frase ingresada');

def cantidadPalabras(frase):
    print('*' * 23);
    print('CANTIDAD DE PALABRAS ');
    palabras = frase.split();
    print(f'Hemos encontrado {len(palabras)} palabras en la frase');

def primera_ultima(frase):
    primera = frase[0];
    ultima = frase[-1];
    print('*' * 23);
    print('PRIMERA Y ÚLTIMA ');
    print(f'La primera letra de la frase es {primera} y la última es {ultima}');

def invertirTexto(frase):
    palabra = frase.split;
    revertido = palabra.reverse();
    texto_invertido = ' '.join(revertido);
    print('*' * 23);
    print('TEXTO INVERTIDO');
    print(f'{texto_invertido}');

def busca_python(frase):
    buscar = 'python' in frase
    dic = {True: 'si', False: 'no'};
    print(f'La palabra python {dic[buscar]} se encuentra en la frase')

def inicio():
    frase = input('ingrese una frase: ')
    letras = [];

    letras.append(input('Ingrese ahora una letra: '));
    letras.append(input('Ingrese ahora otra una letra: '));
    letras.append(input('Ingrese ahora una última una letra: '));

    opcion = input('Ingrese:\n[1] para contar la cantidad de letras: \n[2] Para la cantidad de palabras en la frase: \n[3] Primera y última letra de la frase: \n [4] Invertir el texto: \n[5] Buscar la palabra python: ')

    if opcion == '1':
        cantidadLetras(frase, letras);
    elif opcion == '2':
        cantidadPalabras(frase);
    elif opcion =='3':
        primera_ultima(frase);
    elif opcion == '4':
        invertirTexto(frase);
    else:
        busca_python(frase);



inicio()