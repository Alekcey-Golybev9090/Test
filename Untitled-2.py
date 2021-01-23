def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def solve(p, q):
    d = discriminant(1, p, q)
    x1 = (-p + d ** 0.5) / 2
    x2 = (-p - d ** 0.5) / 2
    return [x2, x1]


def larger_root(p, q):
    ans = solve(p, q)
    return ans[1]


def smaller_root(p, q):
    ans = solve(p, q)
    return ans[0]


def main():
    p = float(input())
    q = float(input())
    print(discriminant(1, p, q))
    print(smaller_root(p, q), larger_root(p, q))
