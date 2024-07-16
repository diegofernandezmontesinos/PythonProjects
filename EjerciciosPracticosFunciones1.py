def devolver_distintos(a,b,c):
    suma=a+b+c;
    lista=[a,b,c];
    if suma <10:
        return min(lista);
    elif suma >15:
        return max(lista);
    else:
        return lista[1];

print(devolver_distintos(20,10,5))

