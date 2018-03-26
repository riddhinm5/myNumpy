class Vector():
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        try:
            if isinstance(v, int):
                expand = []
                for _ in range(self.dimension):
                    expand.append(v)
                v = Vector(expand)
            if isinstance(v, Vector):
                if self.dimension != v.dimension:
                    raise ValueError
                sum_vec = Vector([self.coordinates[i] + v.coordinates[i] for i in range(self.dimension)])
                return sum_vec
            else:
                raise TypeError

        except ValueError:
            raise ValueError('The coordiantes have a length mis-match')
        
        except TypeError:
            raise TypeError('Can perform addition only with another vector or a scalar')
    
    def __sub__(self, v):
        try:
            if isinstance(v, int):
                expand = []
                for _ in range(self.dimension):
                    expand.append(v)
                v = Vector(expand)
            if isinstance(v, Vector):
                if self.dimension != v.dimension:
                    raise ValueError
                sub_vec = Vector([self.coordinates[i] - v.coordinates[i] for i in range(self.dimension)])
                return sub_vec
            else:
                raise TypeError

        except ValueError:
            raise ValueError('The coordiantes have a length mis-match')
        
        except TypeError:
            raise TypeError('Can perform addition only with another vector or a scalar')
    
    def __mul__(self, v):
        print(v)
        try:
            if isinstance(v, (int, float)):
                expand = []
                for _ in range(self.dimension):
                    expand.append(v)
                v = Vector(expand)
                mul_vec = Vector([self.coordinates[i] * v.coordinates[i] for i in range(self.dimension)])
                return mul_vec
            else:
                raise TypeError
        except TypeError:
            raise TypeError('Can only perform multiplication with a scalar with this function. To multiply 2 vectors use Vector.matmul()')
    
    __rmul__ = __mul__