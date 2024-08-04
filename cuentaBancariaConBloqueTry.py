class Persona():
    def __init__(self,nombre, apellido):
        self.nombre = nombre;
        self.apellido = apellido;

class Cliente(Persona):
    def __init__(self,nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido);
        self.numero_cuenta = numero_cuenta;
        self.balance = balance;

    def __str__(self):
        return f'El cliente {self.nombre} tiene un balance de {self.balance} en su numero de cuenta {self.numero_cuenta}'

    def depositar(self, monto_retirar):
        self.balance += monto_retirar;

    def retirar(self,monto_retirar):
        if self.balance >= monto_retirar:
            self.balance -=monto_retirar;
            print('Retiro realizado correctamente');
        else:
            print('Fondos insuficientes.');



def crear_cliente():
    nombre = input('Ingrese su nombre: ');
    apellido = input('Ingrese su apellido: ')
    numero_cuenta = input('Ingrese su número de cuenta: ')

    cliente = Cliente(nombre, apellido, numero_cuenta);
    return cliente;

def inicio():
    mi_cliente = crear_cliente();
    print(mi_cliente);
    opcion = 0;

    while opcion != 'S':
        print('Elige: Depositar [D], Retirar [R] o Salir [S]: ')


        try:
            opcion = input().upper();
            ['D', 'R', 'S'].index(opcion);
        except ValueError:
            print('Esa opcion no es válida');
        else:
            if opcion == 'D':
                monto_dep = int(input('Monto a Depositar: '));
                mi_cliente.depositar(monto_dep);
            elif opcion == 'R':
                monto_ret = int(input('Monto a Retirar: '));
                mi_cliente.depositar(monto_ret);
        print(mi_cliente);

    print('Gracias, buen día.');



inicio();