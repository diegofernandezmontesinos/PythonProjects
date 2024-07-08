frase = input("Ingrese una frase una oración ").lower();
letras = [];

letras.append(input("Ingrese una letra: ").lower());
letras.append(input("Ingrese una letra: ").lower());
letras.append(input("Ingrese una letra: ").lower());

cantidadDeLetras1= frase.count(letras[0])
cantidadDeLetras2= frase.count(letras[1])
cantidadDeLetras3= frase.count(letras[2])
### empezamos aqi las respuestas

print("\n");
print("CANTIDAD DE LETRAS");
###1
print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidadDeLetras1} veces");
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidadDeLetras2} veces");
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidadDeLetras3} veces");
###2
print("\n");
print("CANTIDAD DE PALABRAS");
palabras = frase.split();
print(f"hemos encontrado {len(palabras)} palabras en tu texto.");

###3
print("\n");
print("LETRAS INICIO A FIN");

letra_inicio = frase[0];
letra_final = frase[-1];
print(f"la letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'.");
###4
print("\n");
print("TEXTO INVERTIDO");

palabras.reverse()
texto_invertido = ' '.join(palabras);

print(f"La frase invertida sería as: '{texto_invertido}'.")

###5
print("\n");
print("BUSCANDO LA PALABRA PYTHON");

buscarPalabra = 'python' in frase;
dic = {True : 'si', False: 'no'}
print(f"La palabra python {dic[buscarPalabra]} se encuentra en la frase.")