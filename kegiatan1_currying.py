def currying(func):
    def curried(*args):
        return func(*args)
    return curried

def perkalian(a, b):
    return a * b

perkalian_curry = currying(perkalian)

hasil = perkalian_curry(10, 2)
print(hasil)