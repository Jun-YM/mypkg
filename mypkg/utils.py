import subprocess


def get_wifi_signal():
#Linuxのnmcliコマンドを使用しWi-FiのRSSIを取得（できない場合は-100を返す）
    try:
        result = subprocess.check_output(
            ["nmcli", "-t", "-f", "IN-USE,SIGNAL", "device", "wifi"],
            universal_newlines=True
        )

        for line in result.splitlines():
            if line.startswith("*"):
                parts = line.split(":")
                if len(parts) >= 2:
                    signal_percent = int(parts[1])
                    return -1 * (100 - signal_percent)
    except Exception:
        pass

    return -100

