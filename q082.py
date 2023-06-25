# -*- coding: utf-8 -*-

import geocoder
import pandas as pd
import plotly.express as px
import streamlit as st


def main():
    st.title("nightlife")
    tabe = st.radio(label="今日何食べた", options=["和食", "洋食", "中華"])
    st.write(tabe)

    hon = st.text_input("好きな本は")
    if hon:
        st.write(f"{hon}、ですね、nice")

    aso = st.text_input("遊びに行くならどこに行くの")
    if aso:
        geo = geocoder.osm(aso)
        # st.write(f"lat:{geo.latlng[0]}, lng:{geo.latlng[1]}")
        df = pd.DataFrame({
            "name": [aso],
            "lat": [geo.latlng[0]],
            "lon": [geo.latlng[1]]
        })
        fig = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="name", color_discrete_sequence=["fuchsia"],
                                zoom=15, height=400)
        fig.update_layout(
            mapbox_style="open-street-map",
            title="遊びに行くところ",
        )
        st.plotly_chart(fig)


if __name__ == '__main__':
    main()
