def auto_shotdown_pc() -> None:
    import os
    import psutil as ps
    import time as t

    cls = lambda: os.system("cls")

    def bytes_to_mb(bytes: int) -> int:
                while bytes > 1024:
                    bytes /= 1024
                
                return round(bytes * 1000, 2)

    while True:
        print("Введите команду '/start' после того как начнете загрузку файла.\n")

        choice = input("Ввод: ")
        
        if choice.lower() == "/start":

            cls()
            size_file = float(input("Введите размер скачиваемого файла в гигабайтах: "))
            
            cls()

            print("Ожидание завершения скачивания файла...")

            temp_send_bytes = 0

            while True:
                net_io = ps.net_io_counters()
                send_bytes = bytes_to_mb(net_io.bytes_recv)

                if abs(send_bytes - temp_send_bytes) == 0:
                    
                    cls()
                    print("Ожидание завершения записи файла на диск...")

                    t.sleep((size_file * 1000) // 70)

                    cls()
                    print("Выключение компьютера.")

                    # os.system("shutdown -s -t 10")
                    break
                
                temp_send_bytes = bytes_to_mb(net_io.bytes_recv)
                t.sleep(5)
        else:
            os.system("cls")

            print("Неизвестная команда.\n")
            continue

def main():
    auto_shotdown_pc()

if __name__ == "__main__":
    main()


# если темп и текущее количество скаченных мегабайтов == 0
# прибавлем в счетчик += 1
# если счетчик == 120, то выключаем пк