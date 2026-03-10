import streamlit as st
import google.generativeai as genai

# Cấu hình giao diện
st.set_page_config(page_title="AI Hành Chính Việt Nam", layout="wide")

# QUAN TRỌNG: Thay dãy chữ dưới đây bằng mã AIza... thật của bạn
API_KEY = "AIzaSyCUuIC53vrbfBH4oEcTbhjMwFnqcI1mIfU" 

try:
    genai.configure(api_key=API_KEY)
    # Sử dụng gemini-1.5-flash là bản ổn định nhất hiện nay
    model = genai.GenerativeModel('gemini-3-flash-preview')
except:
    st.error("Lỗi cấu hình API Key. Vui lòng kiểm tra lại mã AIza của bạn.")

st.title("🏛️ TRỢ LÝ SOẠN THẢO VĂN BẢN HÀNH CHÍNH")
st.markdown("---")

col_in, col_out = st.columns([1, 2])

with col_in:
    st.subheader("📌 Nhập thông tin")
    loai_vb = st.selectbox("Loại văn bản", ["Công văn", "Quyết định", "Tờ trình", "Thông báo"])
    co_quan = st.text_input("Cơ quan ban hành", "Tên cơ quan của bạn")
    noi_dung = st.text_area("Nội dung tóm tắt", height=200)
    btn = st.button("🚀 BẮT ĐẦU SOẠN THẢO", use_container_width=True)

with col_out:
    st.subheader("📄 Kết quả")
    if btn:
        if noi_dung:
            with st.spinner('AI đang soạn thảo...'):
                try:
                    prompt = f"Soạn thảo {loai_vb} đúng chuẩn Nghị định 30/2020/NĐ-CP cho {co_quan} về: {noi_dung}."
                    response = model.generate_content(prompt)
                    st.text_area("Văn bản hoàn thiện:", value=response.text, height=550)
                except Exception as e:
                    st.error(f"Lỗi AI: {e}")
        else:
            st.warning("Vui lòng nhập nội dung!")
