def devuelveCeros(*args):
    contador = 0;
    for n in args:
        if args[contador] == 0 and args[contador + 1] == 0:
            return True;
        else:
            contador += 1;

    return False;

print(devuelveCeros(1,2,5,98,1,0,2,5,0,0))