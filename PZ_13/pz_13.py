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
          
            cleaned_line = line.strip()
            
            
            if "Зарезервированные адреса" in cleaned_line:
                in_section = True
                continue
            
            
            if in_section:
                
                match = re.match(r'^(\d{1,3})\.(\d{1,3})\.\d{1,3}\.\d{1,3}(?:/\d{1,2})?', cleaned_line)
                
                if match:
                    
                    ip_address = match.group(0)
                    
                    
                    first_octet = int(match.group(1))
                    second_octet = int(match.group(2))
                    
                    
                    output_line = ip_address + "\n"
                    
                    
                    if first_octet != 0 and second_octet != 0:
                        file1_lines.append(output_line)
                    else:
                        file2_lines.append(output_line)

      
        with open("file1.txt", "w", encoding="utf-8") as f:
            f.writelines(file1_lines)

        
        with open("file2.txt", "w", encoding="utf-8") as f:
            f.writelines(file2_lines)

        
        print(f"Количество строк в первом файле (оба октета ненулевые): {len(file1_lines)}")
        print(f"Количество строк во втором файле (остальные): {len(file2_lines)}")

    except FileNotFoundError:
        print("Ошибка: Исходный файл 'ip_address.txt' не найден.")

if __name__ == "__main__":
    main()
