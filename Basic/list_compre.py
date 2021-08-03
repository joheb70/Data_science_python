
temps = [220, 293, 340, -1049 , 230]

new_temps = [temp/10 for temp in temps if temp != -1049]

print(new_temps)


def foo(num):
    return[i for i in num if isinstance(i,int)]




    