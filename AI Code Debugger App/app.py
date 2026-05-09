import streamlit as st
from api_calling import debug_genration
from PIL import Image

st.header("AI Code Debugger App")
st.divider()
image = st.file_uploader("Upload your Code screenshot down here⤵️",
                          type=['jpg','jpeg','png']
                          )

code_text = st.text_area("Paste your code down here ⤵️",placeholder="paste your entire code here")

if(image):
    pli_image = Image.open(image)

selected_option = st.selectbox("What do you want?",
                               ["Hints","Solution With Code"],
                               index= None
                               )

if image and code_text:
    st.error("⚠️ Please provide EITHER an image OR text code, not both.")
button = st.button("Debug Code",type = "primary")

if "error_explaination" not in st.session_state:
    st.session_state.error_explaination = None

if(button):
    if image and code_text:
        st.error("⚠️ Please provide EITHER an image OR text code, not both.")
    elif not image and not code_text:
        st.error("You must upload or paste the code")
    elif not selected_option:
        st.error("You have to select any one of the options.")
    elif image:
        with st.container(border=True):
            with st.spinner(f"Ai is working on your prompt and will give you {selected_option} of the problem."):
                st.session_state.error_explaination = debug_genration(pli_image)
    elif code_text:
        with st.container(border=True):
            with st.spinner(f"Ai is working on your prompt and will give you {selected_option} of the problem."):
                st.session_state.error_explaination = debug_genration(code_text)
        

if st.session_state.error_explaination:
    debug = st.session_state.error_explaination.split("---Solution With Code---")

    # error explaination and solution of the code
    if len(debug) > 1:
        if selected_option == "Hints":
            st.markdown(debug[0])
        else:
            st.markdown(debug[1])
    else:
        st.markdown(st.session_state.error_explaination)
