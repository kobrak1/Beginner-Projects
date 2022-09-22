from random import*
from time import*


class Dortislem:

	def __init__(self,soru_sayisi):
		self.soru_sayisi = soru_sayisi
	def soru_uretici(self):
		mac_1 = randint(1,20)
		mac_2 = randint(1,20)
		mac_3 = choice(["+","-","*","/"])
		if mac_3 == "+":
			cevap = mac_1 + mac_2
		if mac_3 == "-":
			cevap = mac_1 - mac_2
		if mac_3 == "*":
			cevap = mac_1 * mac_2
		if mac_3 == "/":
			cevap = mac_1 / mac_2
		
		soru = f"{mac_1} {mac_3} {mac_2}"
		return soru,cevap
	def oyun(self):
		dogru_cevap = 0
		baslama_zamani = time()
		
		for i in range(self.soru_sayisi):
			soru,cevap = self.soru_uretici()
			print(f"{i+1}. Soru = {soru} ")
			
			
			kullanıcı_cevabi = float(input("Senin Cevabin = "))
			cevap = round(cevap , 2)
			if kullanıcı_cevabi == cevap:
				dogru_cevap += 1
				print("DOGRU")
			else:
				print(f"YANLIS! Dogru cevap {cevap}.")
		bitirme_zamanı = time()
		oyun_suresi = bitirme_zamanı-baslama_zamani
		zaman = round(oyun_suresi,2)
		


		print(f"{zaman} saniyede 10 soru icerisinden {dogru_cevap} soruyu dogru cevapladiniz.")
oyunum = Dortislem(10)
oyunum.oyun()

