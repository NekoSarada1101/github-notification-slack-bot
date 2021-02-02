# github-notification-slack-bot

<img width="415" src="https://user-images.githubusercontent.com/46714670/106553550-eea32d00-655c-11eb-9d6f-149bbd28a15d.png">

### 概要

GitHubの芝を生やしていなかったらSlackに通知するbot

### 開発環境

* Python 3.8
* [Cloud Functions](https://cloud.google.com/functions?hl=ja)
* [Cloud Pub/Sub](https://cloud.google.com/pubsub?hl=ja)
* [Cloud Scheduler](https://cloud.google.com/scheduler?hl=ja)

### 使用方法
[settings.py](https://github.com/NekoSarada1101/github-notification-slack-bot/blob/main/settings.py)
の`SLACK_WEBHOOK_URL`と`SLACK_USER_ID`を自分のSlackのWebhook URLとユーザーIDに書き換える。

### ライセンス

[MIT](https://github.com/NekoSarada1101/github-notification-slack-bot/blob/main/LICENSE)
