import streamlit as st
import numpy as np
import pandas as pd

st.title("Streamt 入門")

# st.write("DataFrame")

# df = pd.DataFrame({
#     "1列目":[1,2,3,4],
#     "2列目":[10,20,30,40]
# })

# # st.write(df)

# st.dataframe(df.style.highlight_max(axis=0))

# df.style.highlight_max(axis=0)

# # 静的な表（ソートなどはできない）
# st.table(df)

# """
# # 章
# ## 節
# ### 項

# """

# # Pythonのコードがマジックコマンドで書ける
# """
# ```python
# import streamlit as st 
# import numpy as np 
# import pandas as pd
# ```

# """


# df = pd.DataFrame(
#     np.random.rand(100,2) + [35.69,139.70],
#     columns=["lat","lon"]
# )
# df

# # 折れ線グラフ　インタラクティブ
# st.line_chart(df)

# st.area_chart(df)

# st.bar_chart(df)

# # 緯度・軽度を指定することでマップ上にマーカーを表示できる
# # st.map(df)

# st.write("Display image")
# from PIL import Image

# #チェックボックス（チェックを入れるとTrueになる）
# if st.checkbox("Show Image"):
#     img = Image.open("001_hiyoko.jpg")
#     st.image(img, caption="hiyoko",use_column_width=True)

# #セレクトボックス
# option = st.selectbox(
#     "あなたが好きな数字を教えてください",
#     list(range(1,11))
# )

# st.write('あなたの好きな数字は、', option ,'です。')




# text = st.text_input("あなたの趣味を教えてください")
# "あなたの趣味：",text,"です。"

# condition = st.slider("あなたの今の調子は？",0,100,50)
# "あなたの調子は",condition,"です。"

left_column, right_column = st.columns(2)
button = left_column.button("左からカラムに文字を表示")
if button:
    right_column.write("ここは右からむですえ")

expander = st.expander("")

import time

st.write("プログレスバーの表示")
"Start!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.1)