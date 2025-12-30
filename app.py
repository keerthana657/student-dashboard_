import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="🎓 Student Dashboard", page_icon="🎓", layout="wide")

st.markdown("# 🎓 **Student Performance Dashboard** - REAL WEB DATA!")
st.markdown("--- *Powered by Kaggle/GitHub datasets* ---")

@st.cache_data
def load_data():
    return pd.read_csv('student_data.csv')

df = load_data()

# 🎯 BIG NUMBERS (KPIs)
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("👥 Students", len(df))
col2.metric("📊 Avg Score", f"{df['Average'].mean():.1f}%")
col3.metric("🥇 Top Score", f"{df['Average'].max():.1f}%")
col4.metric("⚠️ Failures", len(df[df['Grade']=='F']))
col5.metric("🎖️ A Grades", len(df[df['Grade']=='A']))

# 📈 COOL CHARTS
col1, col2 = st.columns(2)
with col1:
    # Top 10 Students Bar
    top10 = df.nlargest(10, 'Average')
    fig1 = px.bar(top10, x=top10.index, y='Average', 
                  title="🏆 Top 10 Students",
                  color='Average', color_continuous_scale='viridis')
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    # Grade Pie Chart
    fig2 = px.pie(df, names='Grade', title="📊 Grade Distribution",
                  color_discrete_sequence=['#FF6B6B','#4ECDC4','#45B7D1','#96CEB4','#FFEAA7'])
    st.plotly_chart(fig2, use_container_width=True)

# 📋 DATA TABLE
st.markdown("## 📋 All Student Data")
st.dataframe(df, use_container_width=True, height=400)

# 💡 SMART INSIGHTS
st.markdown("## 💡 **Key Insights** (Auto-generated!)")
col1, col2, col3 = st.columns(3)
col1.metric("📈 Pass Rate", f"{len(df[df['Grade']!='F'])/len(df)*100:.1f}%")
col2.metric("⭐ Excellence Rate", f"{len(df[df['Average']>=90])/len(df)*100:.1f}%")
col3.metric("⚠️ At-Risk Students", len(df[df['Average']<70]))

st.markdown("---")
st.markdown("*Data sourced from real educational datasets* 🌟")
