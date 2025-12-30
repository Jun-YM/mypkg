mypkg
ロボットシステム学課題

Wi‑Fi モニタリングシステム

本パッケージは、ROS 2 を用いて Wi‑Fi の受信信号強度（RSSI）を取得し、
その値を監視・通知するシステムです。

WSL 環境では Windows 側の Wi‑Fi 情報を取得し、
Ubuntu ネイティブ環境では nmcli を用いて Wi‑Fi 強度を取得します。

取得した RSSI は /wifi_signal トピックとして publish され、
閾値（デフォルト：-70 dBm）を下回ると警告を出します。

機能概要
✔ Wi‑Fi 強度の取得
Windows（WSL）では netsh wlan show interfaces を利用

Ubuntu では nmcli device wifi を利用

RSSI（dBm）を Int32 型で publish

✔ Wi‑Fi アラート
/wifi_signal を subscribe

RSSI が閾値より弱い場合に警告を出力

✔ launch ファイルで 2 ノード同時起動
wifi_signal_publisher

wifi_alert_node

準備
リポジトリのクローン
コード
git clone https://github.com/Jun-YM/mypkg.git
ワークスペースへ配置
コード
cd ~/ros2_ws/src
mv ~/mypkg .
ビルド
コード
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
使い方
ノードをまとめて起動
コード
ros2 launch mypkg wifi_monitor.launch.py
出力例
コード
Published Wi-Fi signal: -43 dBm
Wi-Fi signal is strong.
閾値（-70 dBm）を下回ると：

コード
Warning: Wi-Fi signal is weak! (-82 dBm)
必要なソフトウェア
ROS 2 Humble

Python 3.10

Windows（WSL）または Ubuntu 22.04

nmcli（Ubuntu の場合）

テスト環境
本パッケージは、ローカル環境および GitHub Actions による
リモート環境の両方でテスト済みです。

ローカル環境:

Ubuntu 22.04.5 LTS

Windows 11 + WSL2（Wi‑Fi 情報取得確認済み）

リモート環境:

GitHub Actions

ライセンス
このソフトウェアパッケージは、3 条項 BSD ライセンスの下、再頒布および使用が許可されます。

このパッケージのコードの一部は、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）を参考に作成しています。

ryuichiueda/my_slides robosys_2025

© 2025 Yamamoto Junpei
