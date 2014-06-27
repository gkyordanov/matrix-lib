class Matrix:
    def __init__(self, n, m, numbers):
        if n < 1:
            raise ValueError("The number of rows is less than 1!")
        if m < 1:
            raise ValueError("The number of columns is less than 1!")
        if len(numbers) != (n * m):
            raise ValueError("numbers is not of required length!")
        self._n = n
        self._m = m
        self.matrix = self.create_matrix(numbers)

    def __add__(self, other):
        numbers = []
        if self._n != other._n or self._m != other._m:
            raise ValueError("Cannot add! Different dimensions.")

        for i in range(0, other._n):
            for j in range(0, other._m):
                numbers.append(self.matrix[i][j] + other.matrix[i][j])

        return Matrix(self._n, self._m, numbers)

    def __sub__(self, other):
        numbers = []
        if self._n != other._n or self._m != other._m:
            raise ValueError("Cannot add! Different dimensions.")

        for i in range(0, other._n):
            for j in range(0, other._m):
                numbers.append(self.matrix[i][j] - other.matrix[i][j])

        return Matrix(self._n, self._m, numbers)

    def __mul__(self, other):
        if self._m != other._n:
            raise ValueError("Cannot multiplicate! Different dimensions!")

        transposed = list(zip(*other.matrix))
        numbers = []
        for row in self.matrix:
            for column in transposed:
                sum = 0
                for i in range(0, self._m):
                    sum += row[i] * column[i]
                numbers.append(sum)

        return Matrix(self._n, other._m, numbers)

    def mul_with_scalar(self, scalar):
        numbers = []
        for row in self.matrix:
            for number in row:
                numbers.append(number * scalar)

        return Matrix(self._n, self._m, numbers)

    def get(self, i, j):
        if i < 0 or i >= self._n:
            raise ValueError("Index i is out of bounds!")
        if j < 0 or j >= self._m:
            raise ValueError("Index j is out of bounds!")
        return self.matrix[i][j]

    def set(self, i, j, value):
        if i < 0 or i >= self._n:
            raise ValueError("Index i is out of bounds!")
        if j < 0 or j >= self._m:
            raise ValueError("Index j is out of bounds!")
        self.matrix[i][j] = value

    def __eq__(self, other):
        if self._n != other._n or self._m != other._m:
            return False
        for i in range(0, self._n):
            for j in range(0, self._m):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False

        return True

    def __str__(self):
        representation = ""
        for i in range(0, self._n):
            for j in range(0, self._m):
                if j == self._m - 1:
                    representation += str(self.matrix[i][j]) + '\n'
                else:
                    representation += str(self.matrix[i][j]) + '\t'
        return representation

    def __repr__(self):
        return self.__str__()

    def inverse(self):
        determinant = self.determinant()
        if determinant == 0:
            raise ValueError("Cannot inverse! determinant = 0.")
        adjugate_quantities = self.get_adjugate_quantities()
        adjugate_quantities = [number * (1 / determinant)
                               for number in adjugate_quantities]
        self.matrix = self.create_matrix(adjugate_quantities)

    def inversed(self):
        determinant = self.determinant()
        if determinant == 0:
            raise ValueError("Cannot inverse! determinant = 0.")
        adjugate_quantities = self.get_adjugate_quantities()
        adjugate_quantities = [round(number * (1/determinant), 6)
                               for number in adjugate_quantities]

        matrix = Matrix(self._n, self._n, adjugate_quantities)
        return matrix.transposed()

    def transpose(self):
        self.matrix = [list(l) for l in list(zip(*self.matrix))]
        self._n, self._m = self._m, self._n

    def transposed(self):
        numbers = [number for l in list(zip(*self.matrix)) for number in l]
        return Matrix(self._m, self._n, numbers)

    def determinant(self):
        return self.det(self.matrix)

    def det(self, matrix):
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

        i = 1
        column_to_miss = 0
        sum = 0
        while column_to_miss <= n-1:
            d = {}
            row = 1
            while row <= n-1:
                column = 0
                d[row] = []
                while column <= n-1:
                    if column != column_to_miss:
                        d[row].append(matrix[row][column])
                    column += 1
                row += 1
            sub_det = [d[x] for x in d]
            sum = sum + i*(matrix[0][column_to_miss])*(self.det(sub_det))
            i = i * (-1)
            column_to_miss += 1
        return sum

    def get_adjugate_quantities(self):
        adjugate_quantities = []
        for i in range(0, self._n):
            for j in range(0, self._n):
                adjugate_quantity = pow(-1, i + j) * self.get_sub_det(i, j)
                adjugate_quantities.append(adjugate_quantity)

        return adjugate_quantities

    def get_sub_det(self, row_to_miss, column_to_miss):
        sub_det = []
        for i in range(0, self._n):
            if i == row_to_miss:
                continue
            row = []
            for j in range(0, self._n):
                if j == column_to_miss:
                    continue
                row.append(self.matrix[i][j])
            sub_det.append(row)

        return self.det(sub_det)

    @property
    def m(self):
        return self._m

    @property
    def n(self):
        return self._n

    @property
    def is_symmetric(self):
        if self._n != self._m:
            return False

        for i in range(0, self._n):
            for j in range(i + 1, self._m):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    @property
    def is_orthogonal(self):
        if self._n != self._m:
            return False

        for i in range(0, self._n - 1):
            for j in range(i + 1, self._n):
                if self.scalar_mul(self.matrix[i], self.matrix[j]) != 0:
                    return False
        return True

    @property
    def is_diagonal(self):
        if self._n != self._m:
            return False

        for i in range(0, self._n):
            for j in range(i + 1, self._m):
                if self.matrix[i][j] != 0 or self.matrix[j][i] != 0:
                    return False
        return True

    def scalar_mul(self, vector1, vector2):
        sum = 0
        for i in range(0, len(vector1)):
            sum += vector1[i] * vector2[i]
        return sum

    def create_matrix(self, numbers):
        matrix = []
        row = []
        c = 0
        for number in numbers:
            if c < self.m:
                row.append(number)
                c = c + 1
            else:
                matrix.append(row[:])
                row.clear()
                row.append(number)
                c = 1
        matrix.append(row[:])
        return matrix


class SymmetricMatrix(Matrix):
    pass


class OrthogonalMatrix(Matrix):
    pass


class DiagonalMatrix(Matrix):
    pass
