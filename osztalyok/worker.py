class Worker:       #bevezetes modul neve is ugyanez kisbetuvel
    name = "Névtelen"
    city = "Ismeretlen"
    age = 0
    

print("Osztaly:")
print(Worker.name)
print(Worker.city)
print(Worker.age)
    
pali = Worker

pali.name = "Pál"
pali.city = "Vác"
pali.age = 34

print("Pali:")
print(pali.name)
print(pali.city)
print(pali.age)

jani = Worker

jani.name = "Janos"
jani.city = "Bugyi"
jani.age = 45

print("Janos:")
print(jani.name)
print(jani.city)
print(jani.age)
