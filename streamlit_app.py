import streamlit as st
import pandas as pd

# 页面配置
st.set_page_config(page_title="网点存款付息看板", layout="wide")

# 模拟数据准备
branch_data = {
    "网点名称": ["朝阳支行", "海淀支行", "西城支行"],
    "一般性存款付息率": [2.35, 2.28, 2.41],
    "对公存款付息率": [2.15, 2.08, 2.22],
    "个人存款付息率": [2.55, 2.48, 2.61]
}

# 侧边栏筛选模块
with st.sidebar:
    st.subheader("网点筛选")
    selected_branch = st.selectbox(
        "选择网点",
        options=branch_data["网点名称"],
        index=0,
        help="请从下拉菜单中选择要查看的网点"
    )

# 主显示区
st.header(f"{selected_branch}存款付息表看板")

print(selected_branch)

# 构建数据表格
table_data = {
    "序号": [1, 2, 3],
    "指标项目": ["一般性存款付息率", "对公存款付息率", "个人存款付息率"],
    "栏位": ["金额类", "金额类", "金额类"],
    "指标": [
        f"{branch_data[branch_data['网点名称'] == selected_branch]['一般性存款付息率'].values[0]}%",
        f"{branch_data[branch_data['网点名称'] == selected_branch]['对公存款付息率'].values[0]}%",
        f"{branch_data[branch_data['网点名称'] == selected_branch]['个人存款付息率'].values[0]}%"
    ]
}

df = pd.DataFrame(table_data)

# 表格显示配置
st.dataframe(
    df,
    column_config={
        "序号": st.column_config.NumberColumn(width="small"),
        "指标项目": st.column_config.TextColumn(width="medium"),
        "栏位": st.column_config.TextColumn(width="medium"),
        "指标": st.column_config.ProgressColumn(
            "完成率",
            format="%f%%",
            min_value=0,
            max_value=3,
            width="large"
        )
    },
    hide_index=True,
    use_container_width=True
)

# 数据说明
st.caption("数据说明：付息率指标为年化利率，更新周期为T+1")