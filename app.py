import streamlit as st
st.set_page_config(page_title="Survey Data Dashboard", layout="wide", initial_sidebar_state="expanded")
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

st.title('Data Engineering Visualization dashboard')
st.set_option('deprecation.showPyplotGlobalUse', False)

brain_stroke_data = pd.read_csv("brain_stroke.csv")

st.write(brain_stroke_data.head())
st.write("This page allows us to understand the distribution of our data")
Data_Total, Females, Males = st.columns(3)

with Data_Total:
    st.markdown("**Total**")
    total_rows = brain_stroke_data.shape[0] 
    st.markdown(f"<h4 style='text-align: center; color: yellow;'>{total_rows}</h4>", unsafe_allow_html=True)

with Females:
    st.markdown("**Female**")
    total_females = round((brain_stroke_data.loc[brain_stroke_data['gender'] == 'Female'].shape[0] / brain_stroke_data.shape[0]) * 100, 2)
    st.markdown(f"<h4 style='text-align: center; color: yellow;'>{total_females} % </h4>", unsafe_allow_html=True)

with Males:
    st.markdown("**Male**")
    total_males = round((brain_stroke_data.loc[brain_stroke_data['gender'] == 'Male'].shape[0] / brain_stroke_data.shape[0]) * 100, 2)
    st.markdown(f"<h4 style='text-align: center; color: yellow;'>{total_males} % </h4>", unsafe_allow_html=True)

    
col1, col2 = st.columns(2)
def plot_pie_chart(df, title):
    df_values = df.values.flatten()
    df_labels = df.index
    fig = go.Figure(
        go.Pie(
        labels = df_labels,
        values = df_values,
        hoverinfo = "label+percent+value",
        textinfo = "label+percent",
        hole =0.3, 
        direction ='clockwise',
        showlegend=False
    ))
    st.plotly_chart(fig)

def bar_chart(df, title):
    df_values = df.values.flatten()
    df_labels = df.index
    # fig = go.Figure(go.Bar(
    #         x=df_values,
    #         y=df_labels))
    fig = px.bar(y=df_values, x=df_labels)

    #fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    #fig.update_layout(barmode='stack', yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig)

def plot_cluster_features(clusters):
    polar=clusters.groupby("label").mean().reset_index()
    polar=pd.melt(polar,id_vars=["label"])
    fig5 = px.line_polar(polar, r="value", theta="variable", color="label", line_close=True,height=800,width=1000)
    st.plotly_chart(fig5)

def plot_clusters_pie_chart(clusters):
    pie=clusters.groupby('label').size().reset_index()
    pie.columns=['label','value']
    fig5 = px.pie(pie,values='value',names='label', hole=0.3, height=300, width=300)
    fig5.update_traces(textposition='inside', textinfo='label+percent', hoverinfo='label+value+percent')
    fig5.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig5)

features = ["age","hypertension","heart_disease", "avg_glucose_level","bmi"]
ml_data = brain_stroke_data[features]
#def k_means_clustering(data):


# fig1 = plt.figure(figsize=(10,10))
# brain_stroke_data.describe().T.sort_values(ascending = 0,by = "mean").style.background_gradient(cmap = "BuGn")\
# .bar(subset = ["std"], color ="red").bar(subset = ["mean"], color ="blue")
# st.pyplot(fig1)



# fig1 = plt.figure(figsize=(10,10))
# px.histogram(brain_stroke_data, x="age", y="bmi", color="stroke",
#                    marginal="box", # or violin, rug
#                    hover_data=brain_stroke_data.columns)
# st.pyplot(fig1)


fig = plt.figure(figsize=(10,10))
sns.heatmap(brain_stroke_data.corr(),annot = True,cmap = 'GnBu')
st.pyplot(fig)


with col1:
    gender = brain_stroke_data['gender'].value_counts().to_frame()
    plot_pie_chart(gender, "gender_visualization")

    #age = brain_stroke_data['age'].value_counts().to_frame()
    # fig = px.scatter(brain_stroke_data['age'])
    # st.plotly_chart(fig)
    # df1 = brain_stroke_data[['gender', 'age']]
    # fig = df1.groupby('gender').age.plot(kind='kde')
    fig = plt.figure(figsize=(10, 4))
    sns.violinplot(brain_stroke_data['age'])
    st.pyplot(fig)


with col2: 
    Residence_type = brain_stroke_data['Residence_type'].value_counts().to_frame()
    bar_chart(Residence_type, "Residence_type")

    sns.violinplot(data=brain_stroke_data, x="age", y="gender")
    st.pyplot()

# features = ['gender','work_type','smoking_status','hypertension','heart_disease','ever_married',
#            'Residence_type']
# for feature in features:
#     fig = plt.figure(figsize=(10, 10))
#     px.histogram(brain_stroke_data, x=feature,color="stroke")
#     st.pyplot(fig)
pca = PCA(2)
pca_data = pca.fit_transform(ml_data)
kmeans_clus = KMeans(n_clusters=2)
pca_data_labels = kmeans_clus.fit_predict(pca_data)
fig_clustering = px.scatter(x=pca_data[:,0], y=pca_data[:,1], color=pca_data_labels)
st.plotly_chart(fig_clustering)







