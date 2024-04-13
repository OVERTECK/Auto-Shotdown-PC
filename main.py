def auto_shotdown_pc() -> None:
    import os
    import psutil as ps
    import time as t

    cls = lambda: os.system("cls")

    def bytes_to_mb(bytes: int) -> int:
                while bytes > 1024:
                    bytes /= 1024
                
                return round(bytes * 1000, 2)

    disks = ps.disk_partitions()

    before_free_memories = []

    for disk in disks:
        partition_usage = ps.disk_usage(disk.mountpoint)

        before_free_memories.append(bytes_to_mb(partition_usage.free))

    after_free_memories = []
 
    while True: 

        print("Введите команду '/start' после того как начнете загрузку файла.\n")

        choice = input("Ввод: ")
        
        if choice.lower() == "/start":

            for disk in disks:
                partition_usage = ps.disk_usage(disk.mountpoint)

                after_free_memories.append(bytes_to_mb(partition_usage.free))

            difference = []

            
            
            for before, after in zip(before_free_memories, after_free_memories):
                difference.append(before - after)

            size_file = max(map(abs, difference))
            print(size_file)
            cls()

            print("Ожидание завершения скачивания файла...")

            temp_send_bytes = 0

            while True:
                net_io = ps.net_io_counters()
                send_bytes = bytes_to_mb(net_io.bytes_recv)

                if abs(send_bytes - temp_send_bytes) == 0:
                    
                    cls()
                    print("Ожидание завершения записи файла на диск...")

                    t.sleep(size_file // 70)

                    cls()
                    print("Выключение компьютера.")

                    os.system("shutdown -s -t 10")
                    
                    return
                
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