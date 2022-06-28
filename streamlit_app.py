import streamlit as st
import pandas as pd
import numpy as np
# markdown
st.markdown('Streamlit Demo')
import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")
# 设置网页标题
st.title('一个傻瓜式构建可视化 web的 Python 神器 -- streamlit')

# 展示一级标题
st.header('1. 安装')

st.text('和安装其他包一样，安装 streamlit 非常简单，一条命令即可')
code1 = '''pip3 install streamlit'''
st.code(code1, language='bash')


# 展示一级标题
st.header('2. 使用')

# 展示二级标题
st.subheader('2.1 生成 Markdown 文档')

# 纯文本
st.text('导入 streamlit 后，就可以直接使用 st.markdown() 初始化')

# 展示代码，有高亮效果
code2 = '''import streamlit as st
st.markdown('Streamlit Demo')'''
st.code(code2, language='python')
df = pd.DataFrame(
    np.random.randn(10,5),
    columns=('第%d列' % (i+1) for i in range(5))
)

st.dataframe(df.style.highlight_max(axis=0))
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns = ["a", "b", "c"])
st.bar_chart(chart_data)
