#Data
print("=====MASUKAN JUMLAH MAKANAN YANG DIPESAN=====")
I = int(input("IKAN BAKAR     Rp 25.000,00 : "))
E = int(input("ES DOGER       Rp 6.000,00  : "))
R = int(input("RUJAK CINGUR  Rp 8.000,00  : "))

#Total
TI = 25000*I
TE = 6000*E
TR = 8000*R

#Print
print("=====TOTAL=====")
print("Total IKAN Bakar     :Rp ",TI)
print("Total ES DOGER       :Rp ",TE)
print("Total RUJAK CINGUR   :Rp ",TI)

#Jumlah total bayar
JT=TI+TE+TR
print("Jumlah total biaya yang harus dibayar adalah Rp", JT)

