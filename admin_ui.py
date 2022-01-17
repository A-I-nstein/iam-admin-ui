#####-----importing neccessary libraries-----#####

import streamlit as st
from bokeh.layouts import row
from pre_process import get_users
from bokeh.plotting import figure

#####-----UI Elements-----#####

st.set_page_config(layout="wide")

hide_streamlit_style = """
                   <style>
                   #MainMenu {visibility: hidden;}
                   footer {visibility: hidden;}
                   </style>
                   """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown('<h1 style = " font-size: 50px; text-align:center; font-weight:bold">Identity and Access Management</h1>', unsafe_allow_html=True)
st.markdown('<h1 style = " font-size: 25px; text-align:center; font-weight:bold">Admin Monitoring Tool</h1>', unsafe_allow_html=True)
st.text("")

st.subheader("Click to expand")

users = get_users()
removed = []

users_detail_expanders = {}
suspicion_scores = {}
kickout_buttons = {}


col1, col2 = st.columns([4, 1])
users_col = col1.container()
ss_col = col2.container()

if 'removed' not in st.session_state:
    st.session_state.removed = []

for i in users:

    if i not in st.session_state.removed:

        with users_col:
            users_detail_expanders[i] = st.empty()
            with users_detail_expanders[i].expander(i):

                p1 = figure(title='Tracing Mouse Movements', x_axis_label='x', y_axis_label='y', plot_width=500, plot_height=400)
                p1.line(users[i][1][0], users[i][1][1], legend_label='Mouse Movements', line_width=2)

                p2 = figure(title='Keyboard Tracking', x_axis_label='number of key strokes', y_axis_label='Time', plot_width=500, plot_height=400)
                p2.line([i for i in range(1, len(users[i][2])+1)], users[i][2], legend_label='Key Speed', line_width=2)
                st.bokeh_chart(row(p1, p2), use_container_width=False)

        with ss_col:
            suspicion_scores[i] = st.empty()
            with suspicion_scores[i].expander("Suspicion Score: "+ str(users[i][0])):
                kickout_buttons[i] = st.empty()
                if kickout_buttons[i].button("Remove "+i):
                    st.session_state.removed.append(i)
                    users_detail_expanders[i].empty()
                    suspicion_scores[i].empty()
                    kickout_buttons[i].empty()
