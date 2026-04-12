import unittest
from tp1_1 import main as turnos
from tp1_3 import main as cajas

class TestTurnos(unittest.TestCase):
    def test_turnos_1(self):
        # Caso facil: no hay superposiciones, puedo atender primero al primer turno y luego al segundo
        orden, ganancia = turnos([(1, 10), (2, 10)])
        self.assertEqual([0, 1], orden)
        self.assertEqual(20, ganancia)

    # Tests hechos por el grupo. A partir de aca solo se testea la ganancia, ya que hay casos para los cuales hay más
    # de un orden posible a la maxima ganancia, diversos algoritmos pueden resultar en diferentes órdenes,
    # pero deben resultar en la misma ganancia

    def test_turnos_2(self):
        orden, ganancia = turnos([(3, 1), (1, 5), (2, 10)])
        # el unico orden que llega a la ganancia maxima es [1, 2, 0]
        print(orden)
        self.assertEqual(16, ganancia)

    def test_turnos_3(self):
        orden, ganancia = turnos([(1, 5), (1, 5), (2, 20), (2, 20)])
        # orden = [2, 3] o [3, 2] da ganancia = 40
        print(orden)
        self.assertEqual(40, ganancia)

    def test_turnos_4(self):
        orden, ganancia = turnos([(5, 100), (1, 99), (2, 99), (2, 200)])
        # orden = [1, 3, 0] o [2, 3, 0] da una ganancia de 399
        print(orden)
        self.assertEqual(399, ganancia)

    def test_turnos_5(self):
        orden, ganancia = turnos([(2, 5), (2, 20), (1, 10)])
        print(orden)
        self.assertEqual(30, ganancia)

class TestCajas(unittest.TestCase):
    def test_cajas_1(self):
        # Caso facil: una sola caja, tiene altura 1, el orden es la unica caja con base 1 y altura 1
        altura, orden = cajas([(1, 1, 1)])
        print(altura, orden)
        self.assertEqual(1, altura)
        self.assertEqual([(0, (1, 1))], orden)

    def test_cajas_2(self):
        altura, orden = cajas([(4, 2, 4), (3, 3, 3)])
        print(altura, orden)
        self.assertEqual(5, altura)
        self.assertEqual([(0, (4, 4)), (1, (3, 3))], orden)

    def test_cajas_3(self):
        altura, orden = cajas([(2, 2, 2), (2, 1, 1), (1.5, 3, 2)])
        print(altura, orden)
        self.assertEqual(3, altura)
        self.assertEqual([(2, (1.5, 2))], orden)

    def test_cajas_4(self):
        altura, orden = cajas([(1, 2, 3), (2, 1, 2), (3, 4, 1)])
        print(altura, orden)
        self.assertEqual(4, altura)
        self.assertEqual([(2, (3, 1))], orden)

    def test_cajas_5(self):
        altura, orden = cajas([
            (1, 1, 1),
            (3, 2, 1),
            (1, 2, 3),
            (2, 2, 1),
            (1, 3, 1),
            (4, 1, 5)])
        print(altura, orden)
        self.assertEqual(4, altura)
        self.assertEqual([(5, (4, 5)), (4, (1, 1))], orden)

    def test_cajas_6(self):
        altura, orden = cajas([
            (6, 6, 6),
            (2, 2, 2),
            (5, 5, 5),
            (1, 1, 1),
            (4, 4, 4),
            (3, 3, 3),
            (7, 7, 7)])
        print(altura, orden)
        self.assertEqual(28, altura)
        self.assertEqual([
            (6, (7, 7)),
            (0, (6, 6)),
            (2, (5, 5)),
            (4, (4, 4)),
            (5, (3, 3)),
            (1, (2, 2)),
            (3, (1, 1))], orden)

if __name__ == "__main__":
    unittest.main()
