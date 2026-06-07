#2. Из предложенного текстового файла (text18-23.txt) вывести
#на экран его содержимое, количество букв в нижнем регистре.
#Сформировать новый файл, в который поместить текст в стихотворной
#форме предварительно поставив последнюю строку между второй и третьей."""

print('\n')
try:
    
    with open("text18-23.txt", "r", encoding="utf-8") as f:
        list = f.readlines()
    

    if len(list) < 7:
        text_borodino = (
            "И только небо засветилось,\n"
            "Все шумно вдруг зашевелилось,\n"
            "Сверкнул за строем строй.\n"
            "Полковник наш рожден был хватом:\n"
            "Слуга царю, отец солдатам…\n"
            "Да, жаль его: сражен булатом,\n"
            "Он спит в земле сырой."
        )
        
        with open("text18-23.txt", "w", encoding="utf-8") as f:
            f.write(text_borodino)
       
        with open("text18-23.txt", "r", encoding="utf-8") as f:
            list = f.readlines()

   
    for line in list:
        print(line, end="")
    print()

 
    t = 0
    for i in list:
        for _ in i:
            if _.islower():
                t += 1
    print(f"\nколичество букв в нижнем регистре: {t}\n")

   
    last_line = list[6].strip() + "\n"
    list.insert(2, last_line)
    list.pop() 
    
    
    with open("text2_2.txt", "w", encoding="utf-8") as f:
        f.writelines(list)
            
except TypeError as e:
    print(f"Произошла ошибка - {e}")
