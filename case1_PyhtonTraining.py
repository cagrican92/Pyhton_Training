#Görev 1:  Verilen değerlerin veri yapılarını inceleyiniz.
x = 8
y = 3.2
z = 8j + 12
a = "hello world"
b = True
c = 23 < 22
l = [1,2,3,4]
d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown" }
t = ("Machine Learning", "Data Science")
s = {"Pyhton", "Machine Learning", "Data Science"}

type(t)

#Görev 2:  Verilen string ifadenintümharflerinibüyükharfeçeviriniz. Virgülvenoktayerinespace koyunuz, kelimekelimeayırınız.
text = "The goal is to turn data into information, and information into insight."
text = text.upper()
list = text.replace("," , " ").replace(".", " ").split()
list

#Görev 3:  Verilenlisteyeaşağıdakiadımlarıuygulayınız.
# Adım1: Verilenlisteninelemansayısınabakınız.
# Adım2: Sıfırıncıveonuncuindekstekielemanlarıçağırınız.
# Adım3: Verilenlisteüzerinden["D", "A", "T", "A"] listesioluşturunuz.
# Adım4: Sekizinciindekstekielemanısiliniz.
# Adım5: Yeni birelemanekleyiniz.
# Adım6: Sekizinciindekse"N" elemanınıtekrarekleyiniz.

lst = ["D","A","T","A","S","C","I","E","N","C","E"]
len(lst)
lst[0]
lst[10]
lst[0:4]
del lst[8]
lst.append("CAN")
lst.insert(8,"N")
print(lst)

#Görev 4:  Verilensözlükyapısınaaşağıdakiadımlarıuygulayınız.
# Adım1: Key değerlerineerişiniz.
# Adım2: Value'laraerişiniz.
# Adım3: Daisy key'ineait12 değerini13 olarakgüncelleyiniz.
# Adım4: Key değeriAhmet value değeri[Turkey,24] olanyeni birdeğerekleyiniz.Adım5: Antonio'yudictionary'densiliniz.
dict = {'cristian': ['amerika',18],
       'daisy': ['england',12],
       'antonio':['Spain',22],
       'dante':['italy',25]}
dict.keys()
dict.values()
dict['daisy'][1]=13
dict["daisy"]
dict["Ahmet"]="[turkiye,24]"
dict.pop("antonio")
dict

# 5:Argümanolarakbirlistealan, listeniniçerisindekitekveçiftsayılarıayrılistelereatayanvebulistelerireturn edenfonksiyonyazınız.
# Liste elemanlarına tek tek erişmeniz gerekmektedir.Her bir elemanın çift veya tek olma durumunu kontrol etmekiçin  % yapısını kullanabilirsiniz.
def bul_cift_tek(liste):
    cift = []
    tek = []

    for eleman in liste:
        if eleman % 2 == 0:
            cift.append(eleman)
        else:
            tek.append(eleman)

    print(cift, tek)
    return cift, tek


l = [2, 3, 18, 93, 22]

bul_cift_tek(l)
