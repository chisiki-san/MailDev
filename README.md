# MailDev
　ローカルネットワークで使えるメールサーバを構築する
 
  MailDevはSMTP（送信側）なので、対になるPOPをDovecot火何かで作成したいと思っている。<br>
  （ブランチ切って動作検証し、問題なければmainを更新）

## OS
　Rocky Linux 9.2<br>
　　[Dockerイメージ（本家）](https://hub.docker.com/_/rockylinux)

## メールサービス
　MailDev<br>
　　1. [本家（GitHub）](https://github.com/maildev/maildev/tree/master)<br>
　　2. [【初心者向け】ローカルでmaildevを立てて、ターミナル（telnet）からメール送信してみる（Qiita）](https://qiita.com/4EAE_Learner/items/4d06a1c76b8b8b23d41f)<br>
　　3. [maildev (SMTP mock server) を使ってハイパーメール開発（Qiita）](https://qiita.com/sotarok/items/ff5ca29f88d1f8069c98)

## ポート情報
| ポート　　  | 用途        | 備考        |
|:-----------:|:------------|:------------|
| 1080        | ウェブアプリ | http://localhost:1080 |
| 1025        | SMTP        | メール送受信プロトコル  |
<br>

## 構築と起動

### Dockerイメージのビルド
　本件ではMailDevそのもののDockerイメージではなく、OSにMailDevをインストールしてDockerイメージを作成する。<br>
　そのため、docker-compose up -d での起動の前に、MailDevのルート（docker-compose.ymlが配置されているフォルダ）で下記コマンドを実行する。

　　`docker-compose build`

### 起動
　初回はコマンドラインで下記コマンドを実行。2回目以降はDocker Desktopから起動可能。

　　`docker-compose up -d`

### 停止
　Docker Desktopで停止をクリックすればOK。<br>
　もちろん、下記コマンドラインで停止可能。ただし、stopでなくdownにするとコンテナが消えてしまうので注意。

　　`docker-compose stop`

### アンインストール
　Docker Desktopの場合<br>
　　1. Containers , 2. Imagesの順にゴミ箱をクリック

　コマンドラインの場合<br>
　　Docker Desktopと同様にコンテナ、イメージの順に削除。<br>

　　　コンテナの削除<br>
　　　　`docker rm [CONTAINER ID or NAMES]`

　　　イメージの削除<br>
　　　　`dokcer rmi [IMAGE ID]`

　　なお、コンテナとイメージのリストはそれぞれ下記のコマンドで出力できる。<br>
　　（`-a`を付与することで非起動状態のコンテナも含めて出力される）

　　　コンテナのリスト表示<br>
　　　　`docker ps -a`

 　　　イメージのリスト表示<br>
 　　　　`dokcer images -a`


---
## 参考：mdファイルの書き方
　1. [マークダウン記入法（Qiita）](https://qiita.com/oreo/items/82183bfbaac69971917f)<br>
　2. [About Mermaid（本家のサイト）](https://mermaid.js.org/intro/)
