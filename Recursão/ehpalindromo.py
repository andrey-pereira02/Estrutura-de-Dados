def ehpalindromo(str, i, j):
    if i >= j:
        return True

    if str[i] != str[j]:
        return False

    return ehpalindromo(str, i + 1, j-1)


s = "arara"
print(ehpalindromo(s, 0, len(s) - 1))
