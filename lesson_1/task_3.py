"""
3. Написать функцию host_range_ping_tab(), возможности которой основаны 
на функции из примера 2. Но в данном случае результат должен быть итоговым 
по всем ip-адресам, представленным в табличном формате (использовать модуль tabulate). 
Таблица должна состоять из двух колонок и выглядеть примерно так:
"""
from ipaddress import IPv4Address, ip_address
from subprocess import Popen, PIPE
from typing import List
import platform
from tabulate import tabulate


def host_ping(nodes: List[IPv4Address, ]) -> list:
    result = []
    for node in nodes:
        param = "-n" if platform.system().lower() == "windows" else "-c"
        command = ["ping", param, "1", "-w", "1", str(node)]
        process = Popen(command, stdout=PIPE)
        if process.wait():
            result.append((node, None))
        else:
            result.append((None, node))
    return result


def host_range_ping(ip: str, diapason: int) -> None:
    lst_ip = [ip_address(ip)+i for i in range(diapason)]
    return host_ping(lst_ip)


def host_range_ping_tab(result: list):
    columns = ["Reachable", "Unreachable"]
    print(tabulate(result, headers=columns, tablefmt='plain'))


def main():
    ip = input('Введите ваш ip: ')
    while True:
        diapason = int(input('Введите диапазон ip: '))
        last = int(ip.split('.')[-1])
        if last + diapason > 255:
            ms = 255 - last
            print(f'Введите другой диапазон, максимальный диапазон: {ms}')
        else:
            break
    result = host_range_ping(ip, diapason)
    host_range_ping_tab(result)


if __name__ == '__main__':
    main()
