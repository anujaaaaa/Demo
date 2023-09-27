import streamlit as st
import openai

api_key = "key"
openai.api_key = api_key

st.title("GPT-3.5-turbo Chatbot")

user_input = st.text_area("You:", "")
temperature = st.slider("Temperature", min_value=0.1, max_value=1.0, step=0.1, value=0.5)

if user_input:
    
    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo", # this is "ChatGPT" $0.002 per 1k tokens
                        messages=[{"role": "system", "content": "test"},
                                  {"role": "user", "content":  user_input} ],
                        temperature=temperature
                            )
 
    # Display the response
    st.text("ChatGPT (GPT-3.5-turbo):")
    st.write(response['choices'][0]['message']['content'])
   #  st.write(response)