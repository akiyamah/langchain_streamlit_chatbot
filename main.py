import os 

import streamlit as st
from streamlit_chat import message

from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.schema import HumanMessage, AIMessage


# 環境変数の読み込み
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# ChatGPTのインスタンス作成
chat_gpt = ChatOpenAI(model_name="gpt-3.5-turbo")

# セッション内に保存されたチェット履歴のメモリの取得
try:
    memory = st.session_state["memory"]
except:
    memory=ConversationBufferMemory(return_messages=True)

# チェーンのインスタンス作成
chain = ConversationChain(
    llm=chat_gpt, 
    memory=memory,
)

#チャット履歴（HumanMessageやAIMessageなど）を格納する配列の初期化
history = []

# Streamlit　タイトル部分のUIの作成
st.title("AI ChatBot")
st.subheader("はじめに")
st.markdown("##### 説明")
st.text(
    "このアプリはAIがあなたの質問に答えます。\n"
    "試しに質問して下さい。"
)
st.markdown("##### 質問例")
st.code("日本人の平均身長は？")

st.subheader("")


with st.form(key="message_form"):
    # form 送信後は空になる
    text_input = st.text_input("メッセージ")
    # ボタン
    send_button = st.form_submit_button("送信")
    
    if send_button: #・ボタンが押された時の処理        
        send_button = False
        
        # ChatGPTの実行
        chain(text_input)
        
        # セッションへのチャット履歴の保存
        st.session_state["memory"] = memory
        
        # チェット履歴(HumanMessage, AIMessage)の読み込み
        try:
            history = memory.load_memory_variables({})["history"]
        except Exception as e:
            st.error(e) 
    
    # チャット履歴の表示
    for index, chat_message in enumerate(reversed(history)):
        if type(chat_message) == HumanMessage:
            message(chat_message.content, is_user=True, key=2 * index) 
        elif type(chat_message) == AIMessage:
            message(chat_message.content, is_user=False, key=2 * index + 1)
    

