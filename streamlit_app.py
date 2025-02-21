import streamlit as st
from datetime import datetime

# 页面配置
st.set_page_config(page_title="财务报表分析平台", layout="wide")

# 初始化session状态
if 'report_type' not in st.st.session_state:
    st.session_state.report_type = "月表"

# 模拟数据
org_list = ["总行营业部", "朝阳支行", "海淀支行", "西城支行"]
quoter_mapping = {1:"上旬", 2:"中旬", 3:"下旬"}

# 顶部筛选栏布局
col1, col2, col3 = st.columns([2, 2, 3])
with col1:
    selected_org = st.selectbox(
        "🏢 机构选择",
        options=org_list,
        index=0,
        help="请选择要查询的分支机构"
    )

with col2:
    report_type = st.selectbox(
        "📊 报表类型",
        options=["旬表", "月表", "季度表", "年表"],
        index=1,
        key="report_type_selector",
        help="选择需要的报表时间维度"
    )

with col3:
    # 动态时间选择器
    current_year = datetime.now().year
    if report_type == "旬表":
        year = st.number_input("年份", min_value=2010, max_value=current_year, value=current_year)
        quarter = st.selectbox("旬别", options=list(quoter_mapping.values()))
    elif report_type == "月表":
        month_col1, month_col2 = st.columns([3, 7])
        with month_col1:
            year = st.number_input("年份", min_value=2010, max_value=current_year, value=current_year)
        with month_col2:
            month = st.slider("月份", 1, 12, datetime.now().month)
    elif report_type == "季度表":
        year = st.number_input("年份", min_value=2010, max_value=current_year, value=current_year)
        quarter = st.radio("季度", [1, 2, 3, 4], horizontal=True)
    else:  # 年表
        year_range = st.slider(
            "统计周期",
            min_value=2010,
            max_value=current_year,
            value=(current_year-1, current_year)
        )

# 动态生成查询参数
query_params = {
    "机构": selected_org,
    "报表类型": report_type,
    "时间范围": ""
}

if report_type == "旬表":
    query_params["时间范围"] = f"{year}年{quarter}"
elif report_type == "月表":
    query_params["时间范围"] = f"{year}年{month}月"
elif report_type == "季度表":
    query_params["时间范围"] = f"{year}年第{quarter}季度"
else:
    query_params["时间范围"] = f"{year_range[0]}~{year_range[1]}年度"

# 显示查询参数（实际应用替换为数据查询）
st.divider()
st.subheader("📈 当前查询参数")
st.json(query_params)