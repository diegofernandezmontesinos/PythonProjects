from pathlib import Path;
import os;

ruta_recetas = Path('/home/diego/Documentos/pythonProject/Recetas');

ruta_carnes = Path('/home/diego/Documentos/pythonProject/Recetas/Carnes');
carne_entrecot = Path(ruta_carnes, 'Entrecot al Malbec.txt');
carne_matambre = Path(ruta_carnes, 'Matambre a la Pizza.txt');

ruta_ensaladas = Path('/home/diego/Documentos/pythonProject/Recetas/Ensaladas');
ensalada_griega = Path(ruta_ensaladas, 'Ensalada Griega.txt');
ensalada_mediterranea = Path(ruta_ensaladas, 'Ensalada Mediterranea.txt');

ruta_pastas = Path('/home/diego/Documentos/pythonProject/Recetas/Pastas');
pasta_canelones = Path(ruta_pastas, 'Canelones de Espinaca.txt');
pasta_ravioles = Path(ruta_ensaladas, 'Ravioles de Ricotta.txt');

ruta_postres = Path('/home/diego/Documentos/pythonProject/Recetas/Postres');
postre_compota = Path(ruta_pastas, 'Compota de Manzana.txt');
postre_tarta = Path(ruta_ensaladas, 'Tarta de Frambuesa.txt');
def seleccionar_opcion():
    return input(f'''Hola, bienvenido al recetario de Negruras Master, el directorio de recetas se encuentra en {ruta_recetas} y dentro hay 4 tipos de recetas.
    Escoge 1 si quieres leer una receta\n. 2 si quieres crear un receta\n. 3 si quieres crear una categoría nueva\n. 4 si quieres eliminar una receta\n.5 si quieres eliminar una categoría\n. 6 si quieres finalizar la ejecución:  ''')

def pregunta_opcion(opcion_usuario):
    while opcion_usuario != '6':
        if opcion_usuario == '1':
            opcion_carpeta = input('Escoja entre carne, ensalada, pasta o postre: ');
            if opcion_carpeta.lower() == 'carne':
                opcion_receta_usuario = input(f'Escoja entre "Entrecot" o "Matambre a la Pizza": ');
                if opcion_receta_usuario .lower() == 'entrecot':
                    print('Haz escogido el entrecot');
                    receta = open(Path(carne_entrecot))
                    print(receta.read());
                    receta.close();
                    break;
                elif opcion_receta_usuario .lower() == 'matambre':
                    print('Haz escogido el matambre');
                    receta = open(Path(carne_matambre))
                    print(receta.read());
                    receta.close();
                else:
                    print('Opción no valida');
            elif opcion_carpeta.lower() == 'ensalada':
                opcion_receta_usuario = input(f'Escoga entre "Griega" o "Mediterranea": ');
                if opcion_receta_usuario.lower() == 'griega':
                    print('Haz escogido la ensalada griega');
                    receta = open(Path(ensalada_griega))
                    print(receta.read());
                    receta.close();
                elif opcion_receta_usuario.lower() == 'mediterranea':
                    print('Haz escogido la ensalada mediterranea');
                    receta = open(Path(ensalada_mediterranea))
                    print(receta.read());
                    receta.close();
                else:
                    print('Opción no valida');

            elif opcion_carpeta.lower() == 'pasta':
                opcion_receta_usuario  = input(f'Escoja entre "Canelones de Espinaca" o "Ravioles de Ricotta": ');
                if opcion_receta_usuario .lower() == 'canelones de espinaca':
                    print('Haz escogido los canelones de espinaca');
                    receta = open(Path(pasta_canelones))
                    print(receta.read());
                    receta.close();
                elif opcion_receta_usuario .lower() == 'ravioles de ricotta':
                    print('Haz escogido los Ravioles de Ricotta');
                    receta = open(Path(pasta_ravioles))
                    print(receta.read());
                    receta.close();
                else:
                    print('Opción no valida');

            elif opcion_carpeta.lower() == 'postre':
                opcion_receta_usuario = input(f'Escoja entre "Compota de manzana" o "Tarta de Frambuesa": ');
                if opcion_receta_usuario .lower() == 'compota de manzana':
                    print('Haz escogido La Compota de Manzana');
                    receta = open(Path(postre_compota))
                    print(receta.read());
                    receta.close();
                elif opcion_receta_usuario .lower() == 'tarta de frambuesa':
                    print('Haz escogido la tarta de frambuesa');
                    receta = open(Path(postre_tarta))
                    print(receta.read());
                    receta.close();
                else:
                    print('Opción no valida');
        elif opcion_usuario == '2':
            opcion_carpeta = input('Escoja entre carne, ensalada, pasta o postre: ');
            if opcion_carpeta.lower() == 'carne':
                opcion_crear = input('Perfecto, vamos a crear una nueva receta, ¿Cómo se va a llamar? ')
                recetaNueva = opcion_crear + '.txt';
                nueva_receta = open(Path(ruta_carnes, recetaNueva), 'w');
                nueva_receta.write(input('Ingrese la receta: '));
                nueva_receta.close();
            elif opcion_carpeta.lower() == 'ensalada':
                opcion_crear = input('Perfecto, vamos a crear una nueva receta, ¿Cómo se va a llamar? ')
                recetaNueva = opcion_crear + '.txt';
                nueva_receta = open(Path(ruta_ensaladas, recetaNueva), 'w');
                nueva_receta.write(input('Ingrese la receta: '));
                nueva_receta.close();
            elif opcion_carpeta.lower() == 'pasta':
                opcion_crear = input('Perfecto, vamos a crear una nueva receta, ¿Cómo se va a llamar? ')
                recetaNueva = opcion_crear + '.txt';
                nueva_receta = open(Path(ruta_pastas, recetaNueva), 'w');
                nueva_receta.write(input('Ingrese la receta: '));
                nueva_receta.close();
            elif opcion_carpeta.lower() == 'postre':
                opcion_crear = input('Perfecto, vamos a crear una nueva receta, ¿Cómo se va a llamar? ')
                recetaNueva = opcion_crear + '.txt';
                nueva_receta = open(Path(ruta_postres, recetaNueva), 'w');
                nueva_receta.write(input('Ingrese la receta: '));
                nueva_receta.close();
        elif opcion_usuario == '3':
            opcion_carpeta = input('Vamos a crear una categoría nueva, ¿cómo se va a llamar?: ');
            nueva_carpeta = Path(ruta_recetas, opcion_carpeta)
            if not os.path.exists(nueva_carpeta):
                os.mkdir(nueva_carpeta)
            else:
                print("Ya existe la carpeta");
        elif opcion_usuario == '4':
            opcion_carpeta = input('Vamos a eliminar una receta, escoja entre carne, ensalada, pasta o postre: ');
            if opcion_carpeta.lower() == 'carne':
                opcion_receta_usuario = input(f'Escoja entre "Entrecot" o "Matambre a la Pizza": ');
                if opcion_receta_usuario.lower() == 'entrecot':
                    os.remove(Path(carne_entrecot));
                elif opcion_receta_usuario.lower() == 'matambre':
                    os.remove(Path(carne_matambre));
                else:
                    print('Opción no valida');
            elif opcion_carpeta.lower() == 'ensalada':
                opcion_receta_usuario = input(f'Escoga entre "Griega" o "Mediterranea": ');
                if opcion_receta_usuario.lower() == 'griega':
                    os.remove(Path(ensalada_griega));
                elif opcion_receta_usuario.lower() == 'mediterranea':
                    os.remove(Path(ensalada_mediterranea));
                else:
                    print('Opción no valida');
            elif opcion_carpeta.lower() == 'pasta':
                opcion_receta_usuario = input(f'Escoja entre "Canelones de Espinaca" o "Ravioles de Ricotta": ');
                if opcion_receta_usuario.lower() == 'canelones de espinaca':
                    os.remove(Path(pasta_canelones));
                elif opcion_receta_usuario.lower() == 'ravioles de ricotta':
                    os.remove(Path(pasta_ravioles));
                else:
                    print('Opción no valida');
                pass;
            elif opcion_carpeta.lower() == 'postre':
                opcion_receta_usuario = input(f'Escoja entre "Compota de manzana" o "Tarta de Frambuesa": ');
                if opcion_receta_usuario.lower() == 'compota de manzana':
                    os.remove(Path(postre_compota));
                elif opcion_receta_usuario.lower() == 'tarta de frambuesa':
                    os.remove(Path(postre_tarta));
                else:
                    print('Opción no valida');
                pass;
        elif opcion_usuario == '5':
            opcion_categoria_usuario = input(f'¿Qué categoría quieres eliminar?": ');
            if opcion_categoria_usuario.lower() == 'carne':
                os.remove(ruta_carnes);
            elif opcion_categoria_usuario.lower() == 'ensalada':
                os.remove(ruta_ensaladas);
            elif opcion_categoria_usuario.lower() == 'pasta':
                os.remove(ruta_pastas);
            elif opcion_categoria_usuario.lower() == 'postre':
                os.remove(ruta_postres);
            pass;
    else :
        print('Fin del recetario, gracias');




pregunta_opcion(seleccionar_opcion())