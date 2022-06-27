# docker benchmark
## これは何？
Docker DesktopのファイルIOが遅いことを確認するためのもの

## 必要なもの
- docker
- docker-compose
ローカル環境で試す場合
- Pythonのプログラムを実行できる環境
- pip install numpy tqdm

## 使い方
簡単に試すためにMakefileを使用する。
```bash
make init # コンテナの立ち上げ
make bash # コンテナ内に入る
python check_spped_test.py
```