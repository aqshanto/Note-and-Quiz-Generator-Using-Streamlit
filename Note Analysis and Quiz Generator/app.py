import streamlit as st
from API_Calling import note_generate, audio_transcription,quiz_generation
from PIL import Image

st.title("Note Summery and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizzes")
st.divider()

with st.sidebar:
    st.header("Controls")
    images = st.file_uploader("Upload the photos of your notes.",
                     type=['jpg','jpeg','png'],
                     accept_multiple_files=True,
                     )
    pil_images = []
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)

    if images:
        if len(images)>3:
            st.error("You can upload at max 3 images.")
        else:
            st.subheader("Your Uplaoded images")
            col = st.columns(len(images))
            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)


    selected_options = st.selectbox("Choose the difficulty of your quiz",
                                    ('Easy','Medium','Hard'),
                                    index = None
                                    )

    button = st.button("Click the button to initiate the AI",type ="primary")


if(button):
    if not images:
        st.error("You Must Upload 1 image.")
    elif not (selected_options):
        st.error("You must select a dificulty")
    else:

    #note
        with st.container(border=True):
            st.subheader("Your note",anchor = False)
            with st.spinner("AI is generating note for you..."):
                generated_notes = note_generate(pil_images)
                st.markdown(generated_notes)
        
        # Audio Transcriipt
        with st.container(border=True):
            st.subheader("Audio transciption",anchor = False)

            with st.spinner("AI is generating audio for you..."):                
                # clearing the markdown
                for char in "#*-_`":
                    generated_notes = generated_notes.replace(char," ")

                audio_file = audio_transcription(generated_notes)
                st.audio(audio_file)    


        # quiz        
        with st.container(border=True):
            st.subheader(f"Quiz ({selected_options}) Level",anchor = False)
            # the below portion will be replaced by api call

            with st.spinner("AI is generating quiz for you..."):
                quizss = quiz_generation(pil_images,selected_options)
                st.markdown(quizss)


