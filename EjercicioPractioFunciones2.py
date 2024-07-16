def devuelve_palabra(palabra):
    palabraDevuelta = set();
    for l in palabra:
        palabraDevuelta.add(l);
        miLista = list(palabraDevuelta)
        miLista.sort();
    return miLista

print(devuelve_palabra('entretenido'));