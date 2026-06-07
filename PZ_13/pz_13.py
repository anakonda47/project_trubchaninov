# Из исходного текстового файла (ip_address.txt) из раздела «Зарезервированные
#адреса» перенести в первый файл строки с ненулевыми первым и вторым октетами,
#а во второй – все остальные. Посчитать количество полученных строк в каждом
#файле.

import re

def main():
    try:
        
        with open("ip_address.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        file1_lines = []
        file2_lines = []
        in_section = False

        for line in lines:
            
            if "Зарезервированные адреса" in line:
                in_section = True
                continue
            
            if in_section:
               
                match = re.search(r'\b(\d{1,3})\.(\d{1,3})\.\d{1,3}\.\d{1,3}(?:/\d{1,2})?\b', line)
                if match:
                    
                    first_octet = int(match.group(1))
                    second_octet = int(match.group(2))
                    
                   
                    if first_octet != 0 and second_octet != 0:
                        file1_lines.append(line)
                    else:
                        file2_lines.append(line)

      
        with open("file1.txt", "w", encoding="utf-8") as f:
            f.writelines(file1_lines)

        with open("file2.txt", "w", encoding="utf-8") as f:
            f.writelines(file2_lines)

        
        print(f"Количество строк в первом файле (ненулевые октеты): {len(file1_lines)}")
        print(f"Количество строк во втором файле (остальные): {len(file2_lines)}")

    except FileNotFoundError as e:
        print(f"Ошибка: не найден файл {e.filename}")

main()
