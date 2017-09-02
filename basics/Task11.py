def dec_to_bin(dec):
    bin = ""
    while dec != 0:
        if(dec % 2 == 0):
            bin = "0" + bin
        else:
            bin = "1" + bin
        dec = dec // 2
    return bin
print(dec_to_bin(127))