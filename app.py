import streamlit as st
import os

st.set_page_config(
    page_title="AI Music Generator",
    page_icon="🎵",
    layout="centered"
)

st.title("🎵 AI Music Generation")
st.write("Generate piano music using a trained LSTM model.")

if st.button("🎼 Generate Music"):

    with st.spinner("Generating music..."):

        os.system("python generate.py")

    st.success("Music generated successfully!")

    output_file = "output/generated.mid"

    if os.path.exists(output_file):

        with open(output_file, "rb") as file:
            st.download_button(
                label="⬇ Download Generated MIDI",
                data=file,
                file_name="generated.mid",
                mime="audio/midi"
            )

    else:
        st.error("Generated MIDI file not found.")