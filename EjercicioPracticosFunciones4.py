def contar_primos(a):
    primos = [2];
    iteraciones = 3;

    if a < 2:
        return 0


    while iteraciones <= a:
        for n in range(3,iteraciones,2):
            if iteraciones % n == 0:
                iteraciones +=2;
                break;
        else:
            primos.append(iteraciones);
            iteraciones += 2;

    print(primos);
    return len(primos);

print(contar_primos(50))