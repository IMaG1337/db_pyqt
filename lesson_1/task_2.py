from ipaddress import ip_network
from task_1 import host_ping


def host_range_ping(ip: str, diapason: str) -> None:
    network = list(ip_network(f'{ip}/24'))
    host_ping(network[0:int(diapason)])


def main():
    ip = input('Введите ваш ip: ')
    diapason = input('Введите диапазон ip: ')
    host_range_ping(ip, diapason)


if __name__ == '__main__':
    main()
