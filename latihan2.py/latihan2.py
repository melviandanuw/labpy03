number = [];

while True:
    numberInput = int(input('Masukkan Bilangan: '));
    number.append(numberInput);

    if numberInput == 0:
        max2 = number[0];
        for b in range(0, len(number)):        
            if(number[b] > max2):    
                max2 = number[b];    
        print('Bilangan Terbesar adalah', max2);
        break;
