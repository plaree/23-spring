import numpy as np


x = input("x sayisini giriniz: ") # x sayısı için girdi alıyorum.
y = input("y sayisini giriniz: ") # y sayısı için girdi alıyorum.

x = int(x) # str olan x değişkenimi int'e döünüştürüyorum.
y = int(y) # str olan x değişkenimi int'e döünüştürüyorum.



print("x**y = ", x**y) # ekrana sonucumu yazdırıyorum.
print("log2(x) = ", int(np.log2(x))) # ekrana sonucumu yazdırıyorum (float olan logaritma sonucunu int'e çevirdim).

'''
ödev kağidindaki log(x) ifadesi 2 tabaninda değil de e tabanında çalıştığı için ifadeyi değiştirdim. 
'''