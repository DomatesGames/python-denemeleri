import os
nelervar = os.listdir()
desktoplen = len(nelervar)
kackere = 0
while(True):
    if kackere != desktoplen:
        print(kackere)
        print(nelervar[kackere])
        kackere = kackere + 1

    else:
        acmakistedigi = input("Açmak istediğin programın ismini yaz (Uzantıyı da yazmayı unutma.): ")
        os.startfile(acmakistedigi)
