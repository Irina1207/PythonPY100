#mes1 = b
#mes2 = mes1 + (mez1*0.03)
#mes3 = mes2 + ()
def rashod10 (aa, bb):
    doxod = aa * 10
    ras = 0
    for i in range(1, 11):
        ras = ras + bb
        bb = bb + bb * 0.03
    symma = ras - doxod
    return symma



if __name__ == "__main__":
    stip = 100
    rashod = 200
    print(rashod10(stip, rashod))

