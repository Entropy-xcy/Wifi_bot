import subprocess


def get_replied_message():
    out = subprocess.Popen(["sudo", "iwlist", "wlan0", "scan"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()
    return str(stdout)


def get_ap_numbers():
    return get_replied_message().count("ESSID")


def get_ap_strength():
    strin = get_replied_message()
    ap_list = []
    while strin.find("ESSID") != -1:
        strin = strin[strin.find("Quality") + 8:]
        quality = strin[:strin.find(" ")]
        quality = int(quality[:quality.find("/")])
        strin = strin[strin.find("ESSID:\"") + 7:]
        ssid = strin[:strin.find("\"")]
        ap_list.append((ssid, quality))
    return ap_list


if __name__ == "__main__":
    print(get_ap_strength())

