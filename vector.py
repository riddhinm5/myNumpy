import math

class Vector():
    
    CANNOT_NORMALIZE_ZERO_VECTOR = 'Cannot normalize a zero vector'

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
        try:
            if isinstance(v, (int, float)):
                expand = []
                for _ in range(self.dimension):
                    expand.append(v)
                v = Vector(expand)
            if isinstance(v, Vector):
                mul_vec = Vector([self.coordinates[i] * v.coordinates[i] for i in range(self.dimension)])
                return mul_vec
            else:
                raise TypeError
        except TypeError:
            raise TypeError('Can only perform multiplication with a scalar with this function. To multiply 2 vectors use Vector.matmul()')
    
    __rmul__ = __mul__

    def getMagnitude(self):
        '''
        Magnitude of a vector is the measure of it's length
        rtype: Class 'vector'
        '''
        magnitude = math.sqrt(sum([i**2 for i in self.coordinates]))
        return magnitude

    def normalize(self):
        '''
        Normalizing a vector is the process of finding a unit vector i.e. 
        a vector with magnitude 1 in the same direction as a given vector
        rtype: vector
        '''
        magnitude = self.getMagnitude()
        try:
            unit_vecor = self * (1/magnitude)
            return unit_vecor
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR)

    def dot(self, v):
        '''
        Calculating the dot product of  2 vectors i.e. 
        v . w = v1*w1 + v2*w2 + ... + vn*wn
        '''
        dot = sum([u*v for u, v in zip(self.coordinates, v.coordinates)])
        return dot
    
    def angle(self, v, unit='radian'):
        try:
            v1 = self.normalize()
            w1 = v.normalize()
            angle = math.acos(v1.dot(w1))
            if unit == 'degree':
                angle *= 180/math.pi
            return angle

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR:
                raise Exception('Cannot comput an angle with a zero vector')
            else:
                raise e