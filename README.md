# chatGPT, langchain, streamlitを使用してchatbotを作成・公開する。

## ゴール
langchainで過去の質問内容を連鎖しながらchatGPTに質問を行うアプリをstreamlitで構築しstreamlit cloudで公開する。

## 学習
* langchainのchat message連鎖により過去の会話を引き継いだチャット
* streamlitでの簡易的なアプリ作成
* streamlit cloudでアプリ公開
![過去の会話を引き継いだチャット](https://github.com/akiyamah/langchain_streamlit_chatbot/blob/main/images/test.png)
これは以前Line botと連携したchatGPTを作成した際の問題点、過去のチャット内容を含めたチャットが行えなかった問題を解消。

## 前提
* ChatGPTのAPI key取得(https://platform.openai.com/)
* streamlitアカウント登録(https://streamlit.io/)
* langchainの確認(https://js.langchain.com/docs/)

## 外部ライブラリのインストール
```
pip3 install streamlit 
pip3 install streamlit-chat 
pip3 install langchain 
pip3 install openai 
```
## streamlit cloudでアプリ公開
* サインイン https://streamlit.io/
* New appでアプリ作成(githubアカウント連携)
* 設定- secret- 環境変数にOPENAI_API_KEY = "sk-XXX"を登録
