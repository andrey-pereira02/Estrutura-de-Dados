def towerHanoi(numberOfDisks, startPeg=1, endPeg=3):
    if numberOfDisks:
        towerHanoi(numberOfDisks - 1, startPeg, 6-startPeg-endPeg)
        print("Mova disco %d da torre %d para torre %d" %
              (numberOfDisks, startPeg, endPeg))
        towerHanoi(numberOfDisks-1, 6-startPeg-endPeg, endPeg)


print(towerHanoi(4))
