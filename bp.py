decisao = input('Você deseja saber a área de um trapézio (1), triângulo (2) ou círculo (3)?')
match decisao:
    case '1':
        def calcular_trapezio(base_maior, base_menor, altura):
            area = (base_maior + base_menor) * altura / 2
            return area 
        base_maior = float(input('Informe a base maior do trapézio: '))
        base_menor = float(input('Informe a base menor do trapézio: '))
        altura = float(input('Informe a altura do trapézio: '))
        print(f'A área do trapézio é {calcular_trapezio(base_maior, base_menor, altura)}')
    case '2':
        def calcular_triangulo(base, altura):
            area_2 = base * altura / 2
            return area_2
        base = float(input('Informe a base do triângulo: '))
        altura = float(input('Informe a altura do triângulo: '))
        print(f'A área do triângulo é {calcular_triangulo(base, altura)}')
    case '3':
        def calcular_circulo(r):
            area_3 = 3.14 * r ** 2
            return area_3
        r = float(input('Informe o raio do círculo: '))
        print(f'A área do círculo é {calcular_circulo(r)}')












