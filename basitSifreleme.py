harfler="abcdefgğhıijklmnoöprsştuüvyz"

kelime="Hey"
kelime=kelime.lower()

#Mevcut şifrenin bir sonraki harflerini yazarak şifreleme yaptık
sifreliKelime=harfler[harfler.index(kelime[0])+1] +  harfler[harfler.index(kelime[1]) + 1 ] + harfler[harfler.index(kelime[2])+1]
print(sifreliKelime)

# kelime[0] şifrelenecek Kelimenin ilk harfini bulduk
# harfler.index(kelime[0])  Harfler'de şifrelenecek kelimenin indeks sayısını bulduk
# harfler.index(kelime[0]) + 1 Diyerek , şifrenin ilk kelimesinin indeks degerini bir arttirarak diger harfin gelmesini sagladik.

#Şifrelemedeki Amaç bir sonra ki harfleri getirmek
print(kelime[0]+"------->"+harfler[harfler.index(kelime[0])+1])
print(kelime[1]+"------->"+harfler[harfler.index(kelime[1])+1])
print(kelime[2]+"------->"+harfler[harfler.index(kelime[2])+1])
print(kelime+" '  Parolasının Şifrelenmiş Hali ==  "+sifreliKelime)



print("="*150)

sifresiKirilmisHali=harfler[harfler.index(sifreliKelime[0])-1 ] +  harfler[harfler.index(sifreliKelime[1])-1 ] + harfler[harfler.index(sifreliKelime[2])-1 ]

print(sifreliKelime[0]+"------->"+harfler[harfler.index(sifreliKelime[0])-1])
print(sifreliKelime[1]+"------->"+harfler[harfler.index(sifreliKelime[1])-1])
print(sifreliKelime[2]+"------->"+harfler[harfler.index(sifreliKelime[2])-1])
print(sifreliKelime + "'nin Şifresi Çözülmüş Hali " + sifresiKirilmisHali)



