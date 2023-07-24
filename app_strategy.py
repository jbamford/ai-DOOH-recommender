import streamlit as st
import strategy_openAI as strategy_openAI
import pandas as pd

stateless_table = strategy_openAI.OPEN_AI_STATELESS()

st.title("AI DOOH Media Planner")
st.header("Experimental DOOH media planner that uses AI to build your media plan from text prompts and audience descriptions")

industry_vertical = st.text_input("Industry Vertical")
media_goals = st.text_area("Campaign Goals")
generate_media_plan = st.button("Generate a brand new DOOH strategy")
# st.text("Good edit keywords include: 'add', 'update', 'combine', 'delete'")
# edit_media_plan_button = st.button("Edit Media Plan")    

if generate_media_plan:
    media_plan = stateless_table.get_media_strategy(media_goals,industry_vertical)
    # st.dataframe(media_plan)
# if edit_media_plan_button:
#     media_plan = stateless_table.edit_table(media_plan_description)
#     # st.dataframe(media_plan_edit)
try:
    st.write(media_plan)   
    st.markdown("Want an official media plan? Drop us a [note](https://www.goldfishads.com/contact-us) and our planning team will convert this strategy into a media plan for you. \n At a minium we're sure you will love the maps and mockups.")
except:
    pass 