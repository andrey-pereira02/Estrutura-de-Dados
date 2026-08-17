def eVogal(s, v=0, c=0):

    if len(s) == 0:
        if v > c:
            return True
        else:
            return False

    if s[0] in "aeiouAEIOU":
        v += 1
    else:
        c += 1

    return eVogal(s[1:], v, c)


print(eVogal("boatarde"))
