import pandas as pd
import streamlit as st
import streamlit.components.v1 as stc
from pygwalker.api.streamlit import StreamlitRenderer
import openpyxl
import pygwalker as pyg
import tempfile
import os
import time
import traceback





# st.set_page_config(page_title='CSVプレビュー', layout='wide')
# st.title('CSVファイルの読み込み')

# # エンコーディングの選択
# selected_encoding = st.selectbox(
#     'エンコーディングを選択', 
#     ['utf-8', 'shift_jis', 'cp932'],
#     key='encoding'
# )

# # ファイルアップローダー
# uploaded_file = st.file_uploader('CSVファイルをアップロード', type='csv')

# if uploaded_file:
#     try:
#         # CSVファイルをDataFrameとして読み込む
#         df = pd.read_csv(uploaded_file, encoding=selected_encoding)
#         st.success("CSVファイルを正常に読み込みました。")

#         # データのプレビュー表示（先頭5行）
#         st.subheader("データの先頭5行")
#         st.dataframe(df.head())
#     except Exception as e:
#         st.error(f"CSVの読み込みに失敗しました: {e}")



# st.set_page_config(page_title='PyGWalker', layout='wide')
# st.title('PyGWalker 可視化')

# selected_encoding = st.selectbox(
#     'encodingを選択',
#     ['utf-8', 'shift_jis', 'cp932'],
#     key='encoding'
# )

# uploaded_file = st.file_uploader('CSVファイルをアップロード', type='csv')

# if uploaded_file:
#     try:
#         # CSV読み込み
#         df = pd.read_csv(uploaded_file, encoding=selected_encoding)
#         st.success("✅ CSVファイルを正常に読み込みました。")

#         # DataFrameの構造を確認（トラブル時の分析に役立つ）
#         st.subheader("データプレビュー")
#         st.dataframe(df.head())
#         st.write("データ型:")
#         st.write(df.dtypes)
#         st.write("サイズ:", df.shape)

#         with st.spinner("PyGWalkerで可視化を生成中..."):
#             progress_bar = st.progress(0, text="進捗: 初期化中...")
#             time.sleep(0.3)

#             progress_bar.progress(20, text="進捗: 一時ファイルを作成中...")
#             with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmpfile:
#                 tmp_path = tmpfile.name

#             try:
#                 progress_bar.progress(50, text="進捗: 可視化のHTMLを生成中...")

#                 # PyGWalkerでHTML生成（envは小文字の 'streamlit'）
#                 pyg.walk(df, env="streamlit", output_file=tmp_path)
#                 st.success("✅ HTMLファイルの生成に成功しました。")

#             except Exception as e:
#                 st.error("❌ pyg.walk() の実行に失敗しました")
#                 st.code(traceback.format_exc(), language="python")
#                 raise

#             time.sleep(0.3)
#             progress_bar.progress(80, text="進捗: HTMLを読み込み中...")

#             with open(tmp_path, "r", encoding="utf-8") as f:
#                 html = f.read()

#             os.unlink(tmp_path)
#             progress_bar.progress(100, text="進捗: 完了！")

#             # HTMLが空かチェック
#             st.write(f"HTMLの長さ: {len(html)} 文字")
#             if len(html.strip()) == 0:
#                 st.error("⚠️ HTMLが空です。pyg.walk の生成に失敗している可能性があります。")
#             else:
#                 # HTML内容表示とダウンロード
#                 st.subheader("HTMLソース（先頭1000文字）")
#                 st.code(html[:1000], language="html")

#                 st.download_button(
#                     label="生成されたHTMLをダウンロード",
#                     data=html,
#                     file_name="pygwalker_output.html",
#                     mime="text/html"
#                 )

#                 # 可視化ビュー表示
#                 st.subheader("PyGWalker 可視化ビュー")
#                 stc.html(html, scrolling=True, height=1600)
#                 st.success("✅ PyGWalkerによる可視化が完了しました")

#     except Exception as e:
#         st.error("❌ 処理中にエラーが発生しました")
#         st.code(traceback.format_exc(), language="python")


st.set_page_config(page_title='PyGWalker', layout='wide')
st.title('PyGWalker 可視化')

selected_encoding = st.selectbox(
    'エンコーディングを選択',
    ['utf-8', 'shift_jis', 'cp932'],
    key='encoding'
)

uploaded_file = st.file_uploader('CSVファイルをアップロード', type='csv')

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file, encoding=selected_encoding)
        st.success("✅ CSVファイルを正常に読み込みました。")

        st.subheader("データプレビュー")
        st.dataframe(df.head())
        st.write("データ型:")
        st.write(df.dtypes)
        st.write("サイズ:", df.shape)

        # ✅ PyGWalker可視化（公式推奨方式）
        st.subheader("PyGWalker 可視化ビュー")
        renderer = StreamlitRenderer(df)
        renderer.explorer()

    except Exception as e:
        st.error("❌ データ処理中にエラーが発生しました")
        st.code(traceback.format_exc())