def binSearch(n, target, inf, sup):

    if inf > sup:
        return False

    med = (inf + sup)//2

    if n[med] == target:
        return True

    if n[med] < target:
        return binSearch(n, target, med+1, sup)
    else:
        return binSearch(n, target, inf, med-1)


n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binSearch(n, 7, 0, 10))
