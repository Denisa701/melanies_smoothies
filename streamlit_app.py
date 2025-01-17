from snowflake.snowpark.functions import col
# Import python packages
import streamlit as st


# Write directly to the app
st.title(":cup_with_straw: Customize  your smoothies :cup_with_straw:")
st.write(
    """choose the fruits you want 
    """
)


# option = st.selectbox(
#     "What is your favourite fruit?",
#     ("Banana", "Strawberry", "Peaches"))

# st.write("Your favourite fruit is:", option)
cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    'Choose up to 5 ingredients:',
    my_dataframe
)

if ingredients_list:
    st.write(ingredients_list)
    st.text(ingredients_list)

    ingredients_string = ''
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen

    st.write(ingredients_string)


    my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """')"""

    st.write(my_insert_stmt)

    if ingredients_string:
        session.sql(my_insert_stmt).collect()
    st.success('Your Smoothie is ordered!', icon="✅")
     
