inport streamlit as st
sy.title("แอปพลิเคชั่นแปลงปี พ.ศ. เป็น ค.ศ.")
bh_year=st.number_input("กรอกปี พ.ศ. ท่ต้ิงการแปลง",velue=2569)
ce_year=bh_year-543
st.header(f"ปีค.ศ. คือ : {ce_year}")
