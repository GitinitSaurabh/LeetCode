def permutation(s: str, t: str):
    return sorted(s) == sorted(t)

print(permutation("ABC", "CBA"))