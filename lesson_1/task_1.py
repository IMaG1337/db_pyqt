import platform
from ipaddress import IPv4Address, ip_address
from subprocess import PIPE, Popen
from threading import Thread

NODES = [
    "192.168.8.1",
    "8.8.8.8",
    "yandex.ru",
    "google.com",
    "0.0.0.1",
    "0.0.0.2",
    "0.0.0.3",
    "0.0.0.4",
    "0.0.0.5",
    "0.0.0.6",
    "0.0.0.7",
    "0.0.0.8",
    "0.0.0.9",
    "0.0.1.0",
]


def check_host_or_ip(ip_or_host: str) -> IPv4Address:
    try:
        ipv4 = ip_address(ip_or_host)
    except ValueError:
        raise Exception("Не корректный ip")
    return ipv4


def popen_command(command: str, node: str) -> None:
    process = Popen(command, stdout=PIPE)
    if process.wait():
        print(f"Узел {node} доступен")
    else:
        print(f"Узел {node} недоступен")


def host_ping(nodes: list) -> None:
    for node in nodes:
        try:
            ipv4 = check_host_or_ip(node)
        except Exception:
            print(f"Узел {node} не ip")
            ipv4 = node
        param = "-n" if platform.system().lower() == "windows" else "-c"
        command = ["ping", param, "1", "-w", "1", str(ipv4)]
        Thread(target=popen_command, args=(command, node)).start()


def main():
    host_ping(NODES)


if __name__ == "__main__":
    main()
