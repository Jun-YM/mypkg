# SPDX-FileCopyrightText: 2025 Junpei Yamamoto
# SPDX-License-Identifier: BSD-3-Clause

import subprocess
import platform
import re

def get_wifi_signal():

    #Windows、WSLの場合
    if platform.system() == "Windows" or "microsoft" in platform.uname().release.lower():
        try:
            result = subprocess.check_output(
                ["powershell.exe", "-Command", "netsh wlan show interfaces"],
                universal_newlines=True
            )

            #RSSI探す
            match_rssi = re.search(r"Rssi\s*:\s*(-?\d+)", result)
            if match_rssi:
                return int(match_rssi.group(1))

            #Signal探す
            match_signal = re.search(r"Signal\s*:\s*(\d+)%", result)
            if match_signal:
                percent = int(match_signal.group(1))
                #dBmに変換
                return int((percent / 2) - 100)

        except Exception:
            pass

        return -100  #失敗

    #Ubuntuの場合
    try:
        result = subprocess.check_output(
            ["nmcli", "-t", "-f", "IN-USE,SIGNAL", "device", "wifi"],
            universal_newlines=True
        )
        for line in result.splitlines():
            if line.startswith("*"):
                parts = line.split(":")
                if len(parts) >= 2:
                    percent = int(parts[1])
                    return int((percent / 2) - 100)
    except Exception:
        pass

    return -100

