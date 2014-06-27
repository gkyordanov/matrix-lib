import unittest

from matrix import Matrix


class TestAddition(unittest.TestCase):
    def test_addition1(self):
        matrix1 = Matrix(2, 2, [1, 2,
                                3, 4])
        matrix2 = Matrix(2, 2, [5, 6,
                                7, 8])
        matrix3 = matrix1 + matrix2
        self.assertEqual(matrix3, Matrix(2, 2, [6, 8,
                                                10, 12]))

    def test_addition2(self):
        matrix1 = Matrix(3, 3, [1, 2, 3,
                                4, 5, 6,
                                7, 8, 9])
        matrix2 = Matrix(3, 3, [2, 2, 2,
                                2, 2, 2,
                                2, 2, 2])
        matrix3 = matrix1 + matrix2
        self.assertEqual(matrix3, Matrix(3, 3, [3, 4, 5,
                                                6, 7, 8, 9,
                                                10, 11]))

    def test_addition3(self):
        matrix1 = Matrix(4, 4, [2, 4, 16, 32,
                                64, 128, 256, 512,
                                1024, 2048, 4096, 8192,
                                2, 2, 2, 2])

        matrix2 = Matrix(4, 4, [2, 4, 8, 10,
                                12, 14, 16, 18,
                                20, 22, 24, 26,
                                28, 30, 32, 34])

        matrix4 = Matrix(4, 4, [4, 8, 24, 42,
                                76, 142, 272, 530,
                                1044, 2070, 4120, 8218,
                                30, 32, 34, 36])

        matrix3 = matrix1 + matrix2
        self.assertEqual(matrix3, matrix4)

    def test_addition4(self):
        matrix1 = Matrix(2, 2, [1, 2,
                                3, 4])
        matrix2 = Matrix(2, 2, [3, 3,
                                3, 3])
        matrix2 = matrix1 + matrix2 + matrix1
        self.assertEqual(matrix2, Matrix(2, 2, [5, 7,
                                                9, 11]))


class TestSubtraction(unittest.TestCase):
    def test_subtraction1(self):
        matrix1 = Matrix(2, 2, [1, 2,
                                3, 4])
        matrix2 = Matrix(2, 2, [5, 6,
                                7, 8])
        matrix3 = matrix2 - matrix1
        self.assertEqual(matrix3, Matrix(2, 2, [4, 4,
                                                4, 4]))

    def test_subtraction2(self):
        matrix1 = Matrix(3, 3, [1, 2, 3,
                                4, 5, 6,
                                7, 8, 9])
        matrix2 = Matrix(3, 3, [2, 2, 2,
                                2, 2, 2,
                                2, 2, 2])
        matrix3 = matrix1 - matrix2
        self.assertEqual(matrix3, Matrix(3, 3, [-1, 0, 1,
                                                2, 3, 4,
                                                5, 6, 7]))

    def test_subtraction3(self):
        matrix1 = Matrix(4, 4, [2, 4, 16, 32,
                                64, 128, 256, 512,
                                1024, 2048, 4096, 8192,
                                2, 2, 2, 2])

        matrix2 = Matrix(4, 4, [2, 4, 8, 10,
                                12, 14, 16, 18,
                                20, 22, 24, 26,
                                28, 30, 32, 34])

        matrix4 = Matrix(4, 4, [0, 0, 8, 22,
                                52, 114, 240, 494,
                                1004, 2026, 4072, 8166,
                                -26, -28, -30, -32])

        matrix3 = matrix1 - matrix2
        self.assertEqual(matrix3, matrix4)

    def test_subtraction4(self):
        matrix1 = Matrix(3, 2, [1, 2,
                                3, 4,
                                5, 6])
        matrix2 = Matrix(3, 2, [3, 3,
                                3, 3,
                                3, 3])
        matrix3 = matrix1 - matrix2
        self.assertEqual(matrix3, Matrix(3, 2, [-2, -1,
                                                0, 1,
                                                2, 3]))


class TestMultiplication(unittest.TestCase):
    def test_multiplication1(self):
        matrix1 = Matrix(2, 2, [1, 2,
                                3, 4])

        matrix2 = Matrix(2, 4, [1, 0, 3, 4,
                                9, 3, 1, 9])

        matrix3 = Matrix(2, 4, [19, 6, 5, 22,
                                39, 12, 13, 48])
        self.assertEqual(matrix1 * matrix2, matrix3)

    def test_multiplication2(self):
        matrix1 = Matrix(3, 3, [1, 0, 0,
                                0, 1, 0,
                                0, 0, 1])
        self.assertEqual(matrix1 * matrix1, matrix1)

    def test_multiplication3(self):
        matrix1 = Matrix(2, 3, [1, 0, 3,
                                5, 1, 7])
        matrix2 = Matrix(3, 2, [2, 6,
                                1, 0,
                                4, 5])
        matrix3 = Matrix(2, 2, [14, 21,
                                39, 65])
        self.assertEqual(matrix1 * matrix2, matrix3)

    def test_multiplicate4(self):
        matrix1 = Matrix(3, 3, [5, 2, 0,
                                0, 3, 1,
                                6, 7, 8])

        matrix2 = Matrix(3, 3, [2, 0, 1,
                                4, 0, 5,
                                0, 6, 1])

        matrix3 = Matrix(3, 3, [18, 0, 15,
                                12, 6, 16,
                                40, 48, 49])
        self.assertEqual(matrix1 * matrix2, matrix3)


class TestMultiplicationWithScalar(unittest.TestCase):
    def test_multiplicate_with_scalar1(self):
        matrix1 = Matrix(2, 2, [2, 2,
                                2, 2])

        matrix2 = Matrix(2, 2, [4, 4,
                                4, 4])
        self.assertEqual(matrix1.mul_with_scalar(2), matrix2)

    def test_multiplicate_with_scalar2(self):
        matrix1 = Matrix(3, 4, [10, 1, 4, 5,
                                1, 0, 2, 8,
                                3, 5, 10, 4])

        matrix2 = Matrix(3, 4, [30, 3, 12, 15,
                                3, 0, 6, 24,
                                9, 15, 30, 12])
        self.assertEqual(matrix1.mul_with_scalar(3), matrix2)


class TestTranspose(unittest.TestCase):
    def test_transpose1(self):
        matrix1 = Matrix(2, 4, [1, 0, 3, 4,
                                9, 3, 1, 9])

        matrix2 = Matrix(4, 2, [1, 9,
                                0, 3,
                                3, 1,
                                4, 9])
        matrix1.transpose()
        self.assertEqual(matrix1, matrix2)

    def test_transpose2(self):
        matrix1 = Matrix(3, 3, [1, 2, 3,
                                4, 5, 6,
                                7, 8, 9])

        matrix2 = Matrix(3, 3, [1, 4, 7,
                                2, 5, 8,
                                3, 6, 9])
        matrix1.transpose()
        self.assertEqual(matrix1, matrix2)

    def test_transposed1(self):
        matrix1 = Matrix(4, 4, [2, 4, 8, 10,
                                12, 14, 16, 18,
                                20, 22, 24, 26,
                                28, 30, 32, 34])

        matrix2 = Matrix(4, 4, [2, 12, 20, 28,
                                4, 14, 22, 30,
                                8, 16, 24, 32,
                                10, 18, 26, 34])
        matrix3 = matrix1.transposed()
        self.assertEqual(matrix2, matrix3)

    def test_transposed2(self):
        matrix1 = Matrix(3, 4, [10, 11, 12, 13,
                                14, 15, 16, 17,
                                18, 19, 20, 21])

        matrix2 = Matrix(4, 3, [10, 14, 18,
                                11, 15, 19,
                                12, 16, 20,
                                13, 17, 21])
        matrix3 = matrix1.transposed()
        self.assertEqual(matrix2, matrix3)


class TestDeterminant(unittest.TestCase):
    def test_determinant1(self):
        matrix = Matrix(3, 3, [1, 2, 3,
                               4, 5, 6,
                               7, 8, 9])
        self.assertEqual(matrix.determinant(), 0)

    def test_determinant2(self):
        matrix = Matrix(4, 4, [1, 0, 0, 0,
                               0, 1, 0, 0,
                               0, 0, 1, 0,
                               0, 0, 0, 5])
        self.assertEqual(matrix.determinant(), 5)

    def test_determinant3(self):
        matrix = Matrix(2, 2, [4, 3,
                               0, 1])
        self.assertEqual(matrix.determinant(), 4)

    def test_determinant4(self):
        matrix = Matrix(3, 3, [5, 2, 0,
                               0, 3, 1,
                               6, 7, 8])
        self.assertEqual(matrix.determinant(), 97)

    def test_determinant5(self):
        matrix = Matrix(6, 6, [10, 3, 0, 1, 32, 5,
                               3, 7, 8, 1, 10, 0,
                               2, 34, 5, 3, 0, 0,
                               0, 2, 6, 2, 8, 2,
                               0, 0, 12, 6, 1, 7,
                               9, 0, 3, 9, 2, 4])
        self.assertEqual(matrix.determinant(), -1230138)

    def test_determinant4(self):
        matrix = Matrix(1, 1, [5])
        self.assertEqual(matrix.determinant(), 5)


class TestInverse(unittest.TestCase):
    def test_inversed1(self):
        matrix = Matrix(3, 3, [5, 2, 0,
                               0, 3, 1,
                               6, 7, 8])

        matrix2 = Matrix(3, 3, [0.175258, -0.164948, 0.020619,
                                0.061856, 0.412371, -0.051546,
                                -0.1855670, -0.237113, 0.154639])

        self.assertEqual(matrix.inversed(), matrix2)


class TestGetAndSet(unittest.TestCase):
    matrix = Matrix(4, 4, [2, 4, 8, 10,
                           12, 14, 16, 18,
                           20, 22, 24, 26,
                           28, 30, 32, 34])

    def test_get1(self):
        self.assertEqual(self.matrix.get(1, 1), 14)

    def test_get2(self):
        self.assertEqual(self.matrix.get(2, 3), 26)

    def test_set1(self):
        self.matrix.set(1, 2, 200)
        self.assertEqual(self.matrix.get(1, 2), 200)

    def test_set2(self):
        self.matrix.set(3, 0, 100)
        self.assertEqual(self.matrix.get(3, 0), 100)

if __name__ == '__main__':
    unittest.main()
