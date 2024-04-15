def regressiva(i):
    print(i)
    if i <= 1:
        return
    regressiva(i-1)

regressiva(3)