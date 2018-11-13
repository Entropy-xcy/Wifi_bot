from flask import Flask
import get_test_speed as test
import wifi_signal

app = Flask(__name__)

@app.route("/get_net_stat")
def get_net_stat():
    lag, band = test.get_test_speed()
    return str(lag) + "," + str(band)


@app.route("/get_ap_strength")
def get_ap_strength():
    ret = ""
    ap_list = wifi_signal.get_ap_strength()
    for i in ap_list:
        ret = ret + str(i[0]) + "," + str(i[1]) + "\n"
    return ret


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=5000)

