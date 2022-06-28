import streamlit as st
st.set_page_config(page_title="Plottin")
strr = '孔维康组项目展示'
st.title(strr)
name = st.sidebar.selectbox(
    "小组成员",
    ("孔维康", "丁子明", "洪飞阳", "白文杰", "段宏伟", "张鑫鹏", "孙亚茹", "李碧拓")
)
job = st.sidebar.selectbox(
    "项目展示",
    ("数据处理", "模型训练", "模型评估", "模型预测")
)
if name=="丁子明" and job =='数据处理':
    st.header('丁子明项目展示')
