from typing import List
import sys

def leer_casos_completos(ruta_fichero: str) -> List[List[str]]:
    """
    Lee un fichero donde la primera línea es el NÚMERO TOTAL de casos.
    Luego, cada caso empieza con un NÚMERO que indica cuántas
    líneas le pertenecen (ej: "4" semanas).
    """
    casos_completos = []
    try:
        with open(ruta_fichero, "r", encoding="utf-8") as f:
            num_total_casos = int(f.readline().strip())

            for _ in range(num_total_casos):
                linea_num_semanas = f.readline().strip()
                if not linea_num_semanas:
                    continue

                num_semanas = int(linea_num_semanas)

                # Esta lista guardará todas las líneas de ESTE caso
                lineas_del_caso = [linea_num_semanas] 

                for _ in range(num_semanas):
                    linea_semana = f.readline().strip()
                    lineas_del_caso.append(linea_semana)

                casos_completos.append(lineas_del_caso)

        return casos_completos

    except (FileNotFoundError, ValueError) as e:
        print(f"Error al leer el fichero de entrada: {e}")
        sys.exit(1)

def procesar_caso(lineas_caso: List[str]) -> str:
    """
    Recibe:
        lineas_caso (List[str]): Una lista con TODAS las líneas de un caso.
            - lineas_caso[0] es el número de semanas (ej: "4")
            - lineas_caso[1:] son las semanas (ej: "*******", "*--*--*", ...)
    
    Devuelve:
        (str): El resultado (ej: "M 2")
    """
    
    # 1. Aquí dentro debes crear tus contadores (Lunes=0, Martes=0, ...)
    
    # 2. Aquí recorres las líneas (desde lineas_caso[1] en adelante)
    #    y cuentas TODOS los asteriscos.
    
    # 3. Aquí haces la simulación (while True) para gastar
    #    los contadores hasta que uno llegue a 0.
    # Repre senta la cantidad de veces en las que no se ha tomado la pastilla dependiendo del día.
    
    lunes = 0
    martes = 0
    miercoles = 0
    jueves = 0
    viernes = 0
    sabado = 0
    domingo = 0
    semanas_guardadas = lineas_caso[1:]
    
    for semanas_str in semanas_guardadas:
        for i in range(len(semanas_str)):
            if semanas_str[i] == "*":
                match i:
                    case 0:
                        lunes += 1
                    case 1:
                        martes += 1
                    case 2:
                        miercoles += 1
                    case 3:
                        jueves += 1
                    case 4:
                        viernes += 1
                    case 5:
                        sabado += 1
                    case 6:
                        domingo += 1
    for semana_actual in range(1,100):
        for j in range (0,7):
            if j == 0: # Lunes
                if lunes > 0:
                    lunes -= 1
                else:
                    return f"L {semana_actual}"
            
            elif j == 1: # Martes
                if martes > 0:
                    martes -= 1
                else:
                    return f"M {semana_actual}"

            elif j == 2: # Miércoles
                if miercoles > 0:
                    miercoles -= 1
                else:
                    return f"X {semana_actual}"

            elif j == 3: # Jueves
                if jueves > 0:
                    jueves -= 1
                else:
                    return f"J {semana_actual}"
            
            elif j == 4: # Viernes
                if viernes > 0:
                    viernes -= 1
                else:
                    return f"V {semana_actual}"
            
            elif j == 5: # Sábado
                if sabado > 0:
                    sabado -= 1
                else:
                    return f"S {semana_actual}"
            
            elif j == 6: # Domingo
                if domingo > 0:
                    domingo -= 1
                else:
                    return f"D {semana_actual}"   

def main(argv: List[str]) -> None:
    if len(argv) < 2:
        print("Uso: python programa.py <ruta_fichero_entrada.txt>")
        sys.exit(1)

    ruta_entrada = argv[1]
    lista_de_casos = leer_casos_completos(ruta_entrada)

    for caso in lista_de_casos:
        # <- Llamada a la función del alumno con la lista de líneas
        resultado = procesar_caso(caso)
        print(resultado)

if __name__ == "__main__":
    main(sys.argv)