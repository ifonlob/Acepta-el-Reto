# test_manias.py
# -*- coding: utf-8 -*-

import pytest
# Importa la función correcta desde solucion.py
from manias_tenemos_todos import procesar_caso

@pytest.mark.parametrize(
    "lineas_caso, esperado",
    [
        # --- Casos del Enunciado ---
        (
            ["4", "*******", "*--*--*", "*-*-*-*", "--*---*"], 
            "M 2"
        ),
        (
            ["3", "-------", "*****-*", "*******"], 
            "S 2"
        ),

        # --- Casos Adicionales ---

        # Caso 3: Se acaban el primer día (Lunes, Semana 1)
        (
            ["2", "----*--", "*******"], # No hay pastillas para el Lunes
            "L 2"
        ),
        # Caso 4: Se acaban el primer día (si hay 0 semanas)
        (
            ["0"], 
            "L 1"
        ),
        # Caso 5: Se acaban el primer día (ninguna pastilla)
        (
            ["3", "-------", "-------", "-------"], 
            "L 1"
        ),
        # Caso 6: Dura exactamente una semana
        (
            ["1", "*******"], # 1 pastilla de cada
            "L 2" # Se acaban el Lunes de la Semana 2
        ),
        # Caso 7: Dura 3 semanas completas
        (
            ["3", "*******", "*******", "*******"], 
            "L 4" # Se acaban el Lunes de la Semana 4
        ),
        # Caso 8: Se acaban el Martes de la semana 2
        (
            ["2", "*******", "*------"], # L(2), M(1), X(1), J(1), V(1), S(1), D(1)
            "M 2" # Se acaban el Martes de la semana 2
        ),
        # Caso 9: Se acaban el Lunes de la semana 4
        (
            ["5", "*******", "*******", "*******", "------*", "------*"],
            # L(3), M(3), X(3), J(3), V(3), S(3), D(5)
            # W1: L(2), M(2), X(2), J(2), V(2), S(2), D(4)
            # W2: L(1), M(1), X(1), J(1), V(1), S(1), D(3)
            # W3: L(0), M(0), X(0), J(0), V(0), S(0), D(2)
            # W4 Lunes: Se acaban.
            "L 4" 
        ),
        # Caso 10: Se acaban el Jueves de la semana 5
        (
            ["5", "*******", "*******", "*******", "*******", "***----"],
            # L(5), M(5), X(5), J(4), V(4), S(4), D(4)
            # W1-W4 OK. Quedan: L(1), M(1), X(1), J(0), V(0), S(0), D(0)
            # W5 Lunes: OK (L: 0)
            # W5 Martes: OK (M: 0)
            # W5 Miércoles: OK (X: 0)
            # W5 Jueves: RUNS OUT!
            "J 5"
        ),
    ]
)
def test_procesar_caso(lineas_caso, esperado):
    """
    Esta función de test llama a la función del alumno 'procesar_caso'
    y comprueba que el resultado que devuelve es igual al 'esperado'.
    """
    assert procesar_caso(lineas_caso) == esperado