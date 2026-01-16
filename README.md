# mypkg
ロボットシステム学課題2

# Wi‑Fiモニタリングシステム
![test](https://github.com/Jun-YM/mypkg/actions/workflows/test.yml/badge.svg)

本パッケージは、ROS2を用いてWi‑Fiの受信信号強度（RSSI）を取得し、
その値を監視・通知するシステムです。

取得したRSSIは/wifi_signalトピックとしてpublishされ、
-70dBmを下回ると警告を出します。

# 使用しているトピック
ノード名:wifi_signal_publisher
トピック名:wifi_signal
型:std_msgs/msg/Int32

ノード名:wifi_alert_node
トピック名:wifi_signal	
型:std_msgs/msg/Int32

## 使い方
- 実行方法、実行結果の例
```
ros2 launch mypkg wifi_monitor.launch.py
[wifi_signal_publisher-1] [INFO] [1767121170.899404514] [wifi_signal_publisher]: Published Wi-Fi signal: -48 dBm
```
-70dBmを下回ると
```
[wifi_signal_publisher-1] [INFO] [1767121170.899404514] [wifi_signal_publisher]: Published Wi-Fi signal: -100 dBm
[wifi_alert_node-2] [WARN] [1767121170.900465406] [wifi_alert_node]: Warning: Wi-Fi signal is weak (-100 dBm)
```

## 必要なソフトウェア
- ROS2

- Python 3.10

## テスト環境
本パッケージは、ローカル環境および GitHub Actions による
リモート環境の両方でテスト済みです。

* ローカル環境:

Ubuntu 22.04.5 LTS


* リモート環境:

Ubuntu 24.04

## ライセンス
このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。

このパッケージのコードの一部は、下記のスライドを参考に作成しています。
(https://ryuichiueda.github.io/slides_marp/robosys2025/lesson10.html)

© 2025 Junpei Yamamoto
