import vector as v

def main():
    vec1 = v.Vector([8.218, -9.341])
    vec2 = v.Vector([-1.129, 2.111])
    vec3 = v.Vector([7.119, 8.215])
    vec4 = v.Vector([-8.223, 0.878])
    vec5 = v.Vector([1.671, -1.012, -0.318])
    print(vec1 + vec2)
    print(vec3 - vec4)
    print(vec5 * 7.41)

if __name__ == '__main__':
    main()