from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import streamlit as st

#llmからの回答を生成する関数
load_dotenv()
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

def get_response(query, system_message):
    messages = [SystemMessage(content=system_message),HumanMessage(content=query)]
    answer = llm(messages)
    result = answer.content
    return result

#画面表示
st.title("サンプルアプリ: llmからの応答")

st.write("##### 動作モード1: 料理関連のコメントに回答")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで料理に関する回答が生成されます")
st.write("##### 動作モード2: 生成AI関連へのコメントに回答")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで生成AIに関する回答が生成されます")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["料理関連のコメント", "生成AI関連のコメント"]
)

st.divider()

if selected_item == "料理関連のコメント":
    input_message = st.text_input(label="料理関連のコメントを入力してください")

else:
    input_message = st.text_input(label="生成AI関連のコメントを入力してください")

if st.button("実行"):
    st.divider()

    if selected_item == "料理関連のコメント":
        if input_message:
            system_message = "あなたは料理の専門家です。ユーザーからの質問に対して、中学生でもわかるように回答してください。料理以外の質問に対しては、回答できないと返答してください"
            answer = get_response(input_message, system_message)
            st.write(f"回答:{answer}")

        else:
            st.error("テキストを入力してから「実行」ボタンを押してください。")

    else:
        if input_message:
            system_message = "あなたは生成AIの専門家です。ユーザーからの質問に対して、中学生でもわかるように回答してください。生成AI以外の質問に対しては、回答できないと返答してください"
            answer = get_response(input_message, system_message)
            st.write(f"回答:{answer}")

        else:
            st.error("テキストを入力してから「実行」ボタンを押してください。")