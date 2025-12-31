# mypkg
ロボットシステム学課題2

# Wi‑Fiモニタリングシステム
![test](https://github.com/Jun-YM/mypkg/actions/workflows/test.yml/badge.svg)

本パッケージは、ROS2を用いてWi‑Fiの受信信号強度（RSSI）を取得し、
その値を監視・通知するシステムです。

取得したRSSIは/wifi_signalトピックとしてpublishされ、
-70dBmを下回ると警告を出します。

## 準備
- このリポジトリをターミナルで下記のようにクローンし、ワークスペース上に配置、ビルドを行ってください
```
git clone https://github.com/Jun-YM/mypkg.git
cd ~/ros2_ws/src
mv ~/mypkg .
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
```

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
- ROS_2

- Python 3.10

## テスト環境
本パッケージは、ローカル環境および GitHub Actions による
リモート環境の両方でテスト済みです。

* ローカル環境:

Ubuntu 22.04.5 LTS


* リモート環境:

Ubuntu 24.04

## ライセンス
このソフトウェアパッケージは、3 条項 BSD ライセンスの下、再頒布および使用が許可されます。

このパッケージのコードの一部は、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）を参考に作成しています。

 - [ryuichiueda/my_slides robosys_2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)

© 2025 Junpei Yamamoto
