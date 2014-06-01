class matrix:
    def __init__(self, n, m, *nums):
        self.n = n
        self.m = m
        if len(nums) == 0:
            self.__matrix = self.create_single_matrix()
        elif len(nums) != (n * m):
            raise ValueError("nums is not of required length!")
        else:
            self.__matrix = self.create_matrix(nums)

    def __add__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __str__(self, other):
        pass

    def inverse(self):
        pass

    def inversed(self):
        pass

    def transpose(self):
        pass

    def transposed(self):
        pass

    def determinant(self):
        pass
        
    def create_single_matrix(self):
        matrix = []
        if self._n != self._m:
            raise ValueError("Cannot create a single matrix!")
        return matrix
        
    @property
    def m(self):
        return self.m
    
    @m.setter
    def m(self, m):
        if m < 1:
            raise ValueError("The number of columns is less than 1!")
        self._m = m
        
    @property
    def n(self):
        return self.n
    
    @n.setter
    def n(self, n):
        if n < 1:
            raise ValueError("The number of rows is less than 1!")
        self._n = n


    def create_matrix(self, nums):
        matrix = []
        row = []
        c = 0
        for i in nums:
            if c < self._m:
                row.append(i)
                c = c + 1
            else:
                matrix.append(row[:])
                row.clear()
                row.append(i)
                c = 1
        matrix.append(row[:])
        return matrix

    def is_symmetric(self):
        return isinstance(self, symmetric_matrix)

    def is_orthogonal(self):
        return isinstance(self, orthogonal_matrix)

    def is_diagonal(self):
        return isinstance(self, diagonal_matrix)


class symmetric_matrix(matrix):
    pass


class orthogonal_matrix(matrix):
    pass


class diagonal_matrix(matrix):
    pass

