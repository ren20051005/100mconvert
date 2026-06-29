import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("AI搭載 🏃‍♂️ タイム予測アプリ")

# 1. AIに学習させる過去のデータ
data = [
    {"distance": 200, "time": 22.0, "actual_100m": 10.5},
    {"distance": 150, "time": 16.2, "actual_100m": 10.4},
    {"distance": 300, "time": 35.5, "actual_100m": 11.0},
    {"distance": 400, "time": 50.0, "actual_100m": 11.5},
    {"distance": 200, "time": 23.5, "actual_100m": 11.2},
    {"distance": 100, "time": 11.0, "actual_100m": 11.0}
]
df = pd.DataFrame(data)

# 2. AIの学習
X = df[["distance", "time"]]
y = df["actual_100m"]
ai_model = LinearRegression()
ai_model.fit(X, y)

# 3. Streamlitの画面表示
st.write("過去の先輩たちのデータを学習したAIが、あなたの100mのタイムを予測します。")

user_distance = st.number_input("走った距離(m)を入力してください", value=300)
user_time = st.number_input("タイム(秒)を入力してください", value=36.0)

if st.button("AIに予測してもらう！"):
    prediction = ai_model.predict([[user_distance, user_time]])
    st.success(f"🤖 AIの分析結果：あなたの100m予測タイムは 【{prediction[0]:.2f} 秒】 です！")
    
    st.write("---")
    st.subheader("💡 参考：近い距離の過去データ")
    v_df = df[df["distance"] == user_distance]
    if not v_df.empty:
        st.dataframe(v_df)
    else:
        st.write("同じ距離の過去データがないため、AIが全体の傾向から推測しました。")
