modal = 100000000;
laba = 0;

for i in range (9):
    if i == 1 or i == 2:
        print("laba bulan ke-",i, "sebesar: ", 0);
    elif i > 2 and i < 5:
        temp = modal * 1 / 100;
        laba += temp;
        print("laba bulan ke-",i, "sebesar: ", temp);
    elif i > 4 and i < 8:
        temp = modal * 5 / 100;
        laba += temp;
        print("laba bulan ke-",i, "sebesar: ", temp);
    elif i == 8:
        # Mengikuti Output dengan 2% Laba, sementara disoal pada bulan ke 8 harusnya laba sebesar 3%.
        temp = modal * 2 / 100;
        laba += temp;
        print("laba bulan ke-",i, "sebesar: ", temp);
        print('Total Laba adalah', laba);
