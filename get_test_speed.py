import os


def get_test_speed():
    ret = os.system("python3 ./speedtest-cli.py")
    f = open("scan.txt", "r")
    ret_l = f.read().split("\n")
    return float(ret_l[0]), float(ret_l[1])


if __name__ == "__main__":
    print(get_test_speed())

