import streamlit as st
import google.generativeai as genai

# Cấu hình giao diện giống app.hanhchinh.ai.vn
st.set_page_config(page_title="AI Hành Chính Việt Nam", layout="wide")

# Nhập API Key (Bạn có thể dán cứng mã AIza... của bạn vào đây)
API_KEY = "AIzaSyCUuIC53vrbfBH4oEcTbhjMwFnqcI1mIfU"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Giao diện chính
st.title("🏛️ TRỢ LÝ SOẠN THẢO VĂN BẢN HÀNH CHÍNH")
st.markdown("---")

# Chia 2 cột: Trái nhập liệu - Phải kết quả
col_input, col_output = st.columns([1, 2])

with col_input:
    st.subheader("📌 Cấu hình văn bản")
    loai_vb = st.selectbox("Chọn loại văn bản", ["Công văn", "Quyết định", "Tờ trình", "Thông báo"])
    co_quan = st.text_input("Cơ quan ban hành", "Tên cơ quan của bạn")
    noi_dung = st.text_area("Nội dung tóm tắt", height=200, placeholder="Nhập yêu cầu soạn thảo...")
    
    btn = st.button("🚀 BẮT ĐẦU SOẠN THẢO", use_container_width=True)

with col_output:
    st.subheader("📄 Kết quả soạn thảo")
    if btn:
        if noi_dung:
            with st.spinner('AI đang xử lý...'):
                prompt = f"Soạn thảo {loai_vb} đúng chuẩn Nghị định 30/2020/NĐ-CP cho {co_quan} về: {noi_dung}."
                response = model.generate_content(prompt)
                st.text_area("Văn bản AI tạo ra:", value=response.text, height=500)
                st.success("Đã soạn xong! Bạn có thể copy nội dung trên.")
        else:
            st.error("Vui lòng nhập nội dung!")
