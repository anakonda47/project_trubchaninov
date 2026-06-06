import re

def main():
    try:
        # читаем исходный файл
        with open("ip_address.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        file1_lines = []
        file2_lines = []
        in_section = False

        for line in lines:
            # включаем фильтр, как только дошли до нужного раздела
            if "Зарезервированные адреса" in line:
                in_section = True
                continue
            
            if in_section:
                # ищем регуляркой подсеть/ip (например, 10.0.0.0/8 или 192.168.0.0/16)
                match = re.search(r'\b(\d{1,3})\.(\d{1,3})\.\d{1,3}\.\d{1,3}(?:/\d{1,2})?\b', line)
                if match:
                    # вытаскиваем первый и второй октеты
                    first_octet = int(match.group(1))
                    second_octet = int(match.group(2))
                    
                    # если оба октета ненулевые
                    if first_octet != 0 and second_octet != 0:
                        file1_lines.append(line)
                    else:
                        file2_lines.append(line)

        # записываем результаты в два новых файла
        with open("file1.txt", "w", encoding="utf-8") as f:
            f.writelines(file1_lines)

        with open("file2.txt", "w", encoding="utf-8") as f:
            f.writelines(file2_lines)

        # вывод количества полученных строк
        print(f"Количество строк в первом файле (ненулевые октеты): {len(file1_lines)}")
        print(f"Количество строк во втором файле (остальные): {len(file2_lines)}")

    except FileNotFoundError as e:
        print(f"Ошибка: не найден файл {e.filename}")

main()
