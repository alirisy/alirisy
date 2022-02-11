#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
st. header('simple web app')
st. write('''temp converter''')
f=st.number_input("temp")
st.write("far in celcius is",5/9*f+32)


# In[1]:


import streamlit as st
st. header('''simple web app''')
st. write('''*my app''')
pie=3.14
radius=4.8
volume=st. slider("radius")
st. write("volume ", radius *4/3*pie**3)


# In[ ]:




