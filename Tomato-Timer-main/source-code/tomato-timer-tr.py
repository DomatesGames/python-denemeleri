  
import time
author = "DomatesGames from Github"
saat = int(input("Kaç saat? "))
saat = saat*60*60
dakika = int(input("Kaç dakika? "))
dakika = dakika*60
saniye = int(input("Kaç saniye? "))
saniye = saniye
time.sleep(saat + dakika + saniye)
print("Süre doldu!")
