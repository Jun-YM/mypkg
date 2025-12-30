#mypkg
ロボットシステム学課題2

#Wi‑Fiモニタリングシステム
![test](https://github.com/Jun-YM/mypkg/actions/workflows/test.yml/badge.svg)

本パッケージは、ROS2を用いてWi‑Fiの受信信号強度（RSSI）を取得し、
その値を監視・通知するシステムです。

WSL環境ではWindows側のWi‑Fi情報を取得し、
Ubuntuネイティブ環境ではnmcliを用いてWi‑Fi 強度を取得します。

取得したRSSIは/wifi_signal トピックとしてpublishされ、
-70dBmを下回ると警告を出します。

##準備
- このリポジトリをターミナルで下記のようにクローンして>ください。
```
git clone https://github.com/Jun-YM/mypkg.git
```
## 使い方
- 実行方法、実行結果の例
```
ros2 launch mypkg wifi_monitor.launch.py
Published Wi-Fi signal: -43 dBm
Wi-Fi signal is strong.
```
-70dBmを下回ると
```
Warning: Wi-Fi signal is weak! (-82 dBm)
```
##必要なソフトウェア
- ROS 2 Humble

- Python 3.10

##テスト環境
本パッケージは、ローカル環境および GitHub Actions による
リモート環境の両方でテスト済みです。

* ローカル環境:

Ubuntu 22.04.5 LTS


リモート環境:

Ubuntu 24.04

##ライセンス
このソフトウェアパッケージは、3 条項 BSD ライセンスの下、再頒布および使用が許可されます。

このパッケージのコードの一部は、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）を参考に作成しています。

ryuichiueda/my_slides robosys_2025

© 2025 Yamamoto Junpei
