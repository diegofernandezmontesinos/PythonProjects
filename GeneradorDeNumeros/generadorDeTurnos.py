'''crear funcion comestica, farmacia y perfumeria
crear funcion iniciadora
crear funciones internas que tenga el yield
'''


def perfumeria():
    for n in range(1,10000):
        yield f'P - {n}';

def cosmetica():
    for n in range(1,10000):
        yield f'C - {n}';

def farmacia():
    for n in range(1, 10000):
        yield f'F - {n}';



f = farmacia();
p = perfumeria();
c = cosmetica();

def decorador(rubro):
    print('\n' + '*'*20);
    print("Su número es:");
    if rubro == 'P':
        print(next(p));
    elif rubro == 'F':
        print(next(f));
    else:
        print(next(c));
    print("Espere y será atendido");
    print("*"*20 + "\n");

