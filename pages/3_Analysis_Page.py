import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Analysis")

st.title("Analytics")

new_df = pd.read_csv('Datasets/data_viz1.csv')
feature_text = pickle.load(open('Datasets/feature_text.pkl','rb'))

group_df = new_df.groupby('sector')[['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']].mean()


# Figure 1 -- Scatter Mapbox -->>
st.header("Sector Price per Sqft Geomap")
fig1 = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map", width=1200, height=700, hover_name=group_df.index)
st.plotly_chart(fig1, use_container_width=True)


# Figure 2 -- Wordcloud -->>
st.header("Features Wordcloud")
plt.rcParams["font.family"] = "Arial"
# Set the dark theme
plt.style.use('dark_background')
wordcloud = WordCloud(width=600, height=600, 
                      background_color='black', 
                      stopwords=set(['s']), 
                      min_font_size=10).generate(feature_text)

fig2, ax = plt.subplots(figsize=(5, 5), facecolor=None)
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
plt.tight_layout(pad=0)
st.pyplot(fig2)


# Figure 3 -- Scater Plot -->>
st.header("Area vs Price Scatter Plot")

property_type = st.selectbox("Select Property Type", ['flat', 'house'])

if property_type == 'house':
    fig3 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")
    # fig3.update_xaxes(range=[0, 13000])
    st.plotly_chart(fig3, use_container_width=True)
else:
    fig3 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")
    # fig3.update_xaxes(range=[0, 13000])
    st.plotly_chart(fig3, use_container_width=True)


# Figure 4 -- Pie Chart -->>
st.header("BHK Pie Chart")

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0, 'overall')

selected_sector = st.selectbox("Select Sector", sector_options)

if selected_sector == 'overall':
    fig4 = px.pie(new_df, names="bedRoom")
    st.plotly_chart(fig4, use_container_width=True)
else:
    fig4 = px.pie(new_df[new_df['sector'] == selected_sector], names="bedRoom")
    st.plotly_chart(fig4, use_container_width=True)


# Figure 5 -- Box Plot -->>
st.header("Side by Side BHK price comparison")
fig5 = px.box(new_df[new_df['bedRoom'] <= 4], x="bedRoom", y="price")
st.plotly_chart(fig5, use_container_width=True)


# Figure 6 -- Side by Side Distplot for property type -->>
st.header("Side by Side Distplot for property type")

fig6 = plt.figure(figsize=(10, 4))
sns.kdeplot(data=new_df, x="price", hue="property_type", fill=True)
st.pyplot(fig6)



