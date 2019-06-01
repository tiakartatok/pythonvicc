from kreta_api import *
import re


	

#login


username = input("Username: ")

#check user is me (xd)

if username == "bazsi":
	student = Student("klik035178001", "72456156732", "2005-01-09") # a tanuló adatait inicializáljuk
	student.refresh_bearer() # azonosító kód lekérése
	student.refresh_student() # tanuló adatainak lekérése
	jegyek = student.evaluation_list #összes osztályzat tárolása egy variableba
	#functions
	def get_weight():
		for x in jegyek:
			er = x.weight
			if er == "200%":
				return "Témazáró"
			else:
				return "Röpdolgozat"
	
	def get_theme():
		for x in jegyek:
			er = x.theme
			if not er:
				return "None"
			else:
				return x.theme
				
	text_file = open("jegyek.txt", "w")
	text_file.write("%s" % jegyek)
	text_file.close()
	#print(student) # tanulóhoz tartozó adatok kiírása
	text_file = open("alldata.txt", "w")
	text_file.write("%s" % student)
	text_file.close()
	
	#print("Név: ", student.name) # tanuló nevének kiírása
	#print("Legutóbbi osztályzat:", student.evaluation_list[0].subject, student.evaluation_list[0].value, "Téma:", student.evaluation_list[0].theme, "Dolgozat típusa:", get_weight(0)) # ebből a tantárgyból kapta a legújabb jegyet
	#print(student.evaluation_list.value)
	"""for x in jegyek:
		print("|", "Tantárgy:",x.subject,"|",
		"Osztályzat:", x.value,"|",
		"Téma:", x.theme,"|",
		"Súly:", x.weight,"|")
		#print(x.value)
		#print(x.theme)
		#print(x.weight)
		#print(get_weight())
	print("Töri")#Történelem
	print("Matek")#matematika
	print("Angol")
	print("Fizika")
	print("Kémia")
	print("Biológia")
	print("Földrajz")
	print("Fizika")
	print("Rajz")#Rajz és vizuális kultúra
	print("Irodalom")	#magyar irodalom
	print("Nyelvtan") #magyar nyelv
	"""
	def jegy_by_subj(sub):
		#print(sub0)
		for x in jegyek:
			q = []
			if x.subject == sub:
				r = int(''.join(filter(str.isdigit, x.value)))
				print(r)
		
				
	jegy_by_subj("Történelem")
	
	
else:
	password = input("Password: ")
	klik = input("Klik: ");

	student = Student(klik, username, password) # a tanuló adatait inicializáljuk
	student.refresh_bearer() # azonosító kód lekérése
	student.refresh_student() # tanuló adatainak lekérése
	print(student) # tanulóhoz tartozó adatok kiírása
	print(student.name) # tanuló nevének kiírása
	print(student.evaluation_list[0].subject) # ebből a tantárgyból kapta a legújabb jegyet
