totalPRs=input("Podaj ilosc wszystkich PRek: ")
APR=input("Podaj ilosc PRek A: ")
BPR=input("Podaj ilosc PRek B: ")
SPR=input("Podaj ilosc PRek S: ")
print "Failed S: %0.0f%%" % (float(SPR) / totalPRs * 100.0)
print "Failed B: %0.0f%%" % (float(BPR) / totalPRs * 100.0)
print "Failed A: %0.0f%%" % (float(APR) / totalPRs * 100.0)
