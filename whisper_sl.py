import streamlit as st
import whisper

# Load the Whisper model
model = whisper.load_model("medium")

# Streamlit UI
st.title("Whisper Audio Transcription")

uploaded_file = st.file_uploader("Choose an audio file...", type=["m4a", "mp3", "wav", "ogg"])

if uploaded_file is not None:
    file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
    st.write(file_details)

    # Save the uploaded file temporarily
    temp_file_name = f"temp_audio.{file_details['FileType'].split('/')[-1]}"
    with open(temp_file_name, "wb") as f:
        f.write(uploaded_file.read())

    # Transcribe the audio
    st.write("Transcribing audio...")
    try:
        result = model.transcribe(temp_file_name, verbose=True)
        st.write("Transcription:")
        st.write(result["text"])
    except Exception as e:
        st.write("An error occurred during transcription.")
        st.write(e)
