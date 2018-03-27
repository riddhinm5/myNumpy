import vector as v

def testcase1():
    print('#'*20)
    print('performing arithmetic operations on vectors')
    print('#'*20)
    vec1 = v.Vector([8.218, -9.341])
    vec2 = v.Vector([-1.129, 2.111])
    vec3 = v.Vector([7.119, 8.215])
    vec4 = v.Vector([-8.223, 0.878])
    vec5 = v.Vector([1.671, -1.012, -0.318])
    print(vec1 + vec2)
    print(vec3 - vec4)
    print(vec5 * 7.41)
    print('#'*20)

def testcase2():
    print('#'*20)
    print('getting magnitude and unit vectors for vectors provided')
    print('#'*20)
    # test vectors for magnitude test
    vec1 = v.Vector([-0.221, 7.437])
    vec2 = v.Vector([8.813, -1.331, -6.247])
    # print results
    print(vec1.getMagnitude())
    print(vec2.getMagnitude())
    # test vectors for unit vector test
    vec3 = v.Vector([5.581, -2.136])
    vec4 = v.Vector([1.996, 3.108, -4.554])
    # print results
    print(vec3.normalize())
    print(vec4.normalize())
    print('#'*20)

def testcase3():
    print('#'*20)
    print('getting the dot product the angle between 2 vectors')
    print('#'*20)
    # test for dot product
    v1 = v.Vector([7.887, 4.138])
    w1 = v.Vector([-8.802, 6.776])
    v2 = v.Vector([-5.955, -4.904, -1.874])
    w2 = v.Vector([-4.496, -8.755, 7.103])
    # print results
    print(v1.dot(w1))
    print(v2.dot(w2))
    # test for the angle between 2 vectors
    v3 = v.Vector([3.183, -7.627])
    w3 = v.Vector([-2.668, 5.319])
    v4 = v.Vector([7.35, 0.221, 5.188])
    w4 = v.Vector([2.751, 8.259, 3.985])
    # print results
    print(v3.angle(w3, unit='radian'))
    print(v4.angle(w4, unit='degree'))
    print('#'*20)


def main():
    testcase1()
    testcase2()
    testcase3()

if __name__ == '__main__':
    main()