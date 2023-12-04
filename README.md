# MailDev
ローカルネットワークで使えるメールサーバを構築する①<br>
<br>
ダミーのSMTPサーバ。飛ばしたメールをWebブラウザで確認出来る。<br>
メール送信サービスや、送信プログラム、スクリプトを作成した際のテストで活用するのが良さそう。。<br>
なお、ローカルのDocker/kubernetesでメールを送受信できる環境については、別プロジェクトで構築したい考え。

## 参考情報
　MailDev<br>
　　1. [本家（GitHub）](https://github.com/maildev/maildev/tree/master)<br>
　　2. [【初心者向け】ローカルでmaildevを立てて、ターミナル（telnet）からメール送信してみる（Qiita）](https://qiita.com/4EAE_Learner/items/4d06a1c76b8b8b23d41f)<br>
　　3. [maildev (SMTP mock server) を使ってハイパーメール開発（Qiita）](https://qiita.com/sotarok/items/ff5ca29f88d1f8069c98)<br>
　　4. [ISO-2022-JP に対応した maildev の dockerイメージ を作る（Qiita）](https://qiita.com/kanemu/items/1f2da063c7e5b5477502)

## ポート情報
| ポート　　  | 用途        | 備考        |
|:-----------:|:------------|:------------|
| 1080        | ウェブアプリ | http://localhost:1080 |
| 1025        | SMTP        | メール送受信プロトコル  |
<br>

## 構築と起動

### Dockerイメージ
本家のDovecotをパッケージからインストールした場合、ISO-2022-JPに対応しておらず、Webアプリ上で日本語が文字化けしてしまう。<br>
そこで、修正を試みたが、上手く解消できなかったため、こちらのDockerイメージを拝借し、日本語化したイメージで起動する。

### Windowsでの注意事項
docker-compose.yml及びDockerfileはLinux向けに設定されている。<br>
ホストがWindowsマシンの場合、ディレクトリはスラッシュ(/)ではなく、バックスラッシュ(円マーク)(\)になる事に注意すること。

例① ホストがLinux/MacOSの場合
```
maildev:
  build:./Dockerfile
```

例② ホストがWindowsの場合
```
maildev:
  build:.\Dockerfile
```


### 起動
`docker-compose.yml`が保存されているディレクトリにカレントを移してコマンドを実行。<br>
なお、WindowsやMacでDocker Desktopを使用しているのであれば、2回目以降はDocker Desktopで再生ボタンを押せば良い。(※)<br>

※ docker-compose.ymlを書き替えたときは、`docker-compose up -d`の再実行が必要。<br>

　 再実行すると、永続化していない情報は初期状態に戻るため、ある程度使用し続けた後に実行する際は、<br>
　 バックアップや永続化を行えるようにしてから実施することをオススメする。<br><br>

実行例① 挙動を理解するためにビルドと起動を分けて実行したいとき～2段階で実行
```
docker-compose build
docker-compose up -d
```

実行例② ビルドから起動まで一発で実行したいとき～Dockerイメージの作成に慣れたらこちらで充分
```
docker-compose up -d
```

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
