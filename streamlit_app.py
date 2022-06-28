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
    st.header('丁子明数据处理')
    st.markdown('![图片alt](https://gss0.baidu.com/9vo3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/7af40ad162d9f2d36e8ff4cba1ec8a136327cc7c.jpg)')
