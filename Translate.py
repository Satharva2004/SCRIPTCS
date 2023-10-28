import assemblyai as aai
import streamlit as st
import os
import time
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

aai.settings.api_key = "9d957a8be0f047e1a374431c34112f1f"
st.title("😼 SCRIPTCS↩")
st.markdown("""**⏮ CREATE SUBTITLE OF YOUR FAVORITE MOVIES/TV-SHOWS/WEBSERIES....**""")
st.markdown("""**⏸ GET CUSTOMIZED SUMMARY....**""")
st.markdown("""**⏭ DETAIL TRANSCRIBING ETC....**""")
st.write("")
st.write("")
st.write("")
st.write("")
st.title("Enter the local file path 👇")
file_path = st.text_input("")

if file_path:
    if os.path.exists(file_path):
        st.write("Transcribing... Please wait.")
        progress_bar = st.progress(0)  # Initialize a progress bar

        # Simulate a loading delay
        for percent_complete in range(0, 101, 1):
            time.sleep(2)  # Simulate a 1-second delay
            progress_bar.progress(percent_complete)  # Update the progress

        # Transcribe the file at the provided file path
        transcriber = aai.Transcriber()
        st.write("# Subtitle: 📌")
        st.write("")
        transcript = transcriber.transcribe(file_path)
        srt_subtitles_button = st.download_button(
            label="Download Subtitles",
            data=transcript.export_subtitles_srt(),
            key="subtitles-srt",
        )
        # Display the transcribed text
        st.write("# Transcribed: 📌")
        st.write("")
        st.write(transcript.text)
        st.write("")
        transcript_button = st.download_button(
            label="Download Transcript",
            data=transcript.text,
            key="transcript-txt",
        )
        st.write("")
        st.write("")

        # Generate a summary using sumy
        LANGUAGE = "english"
        parser = PlaintextParser.from_string(transcript.text, Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)

        summarizer = LsaSummarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)

        summary = summarizer(
            parser.document, sentences_count=5
        )  # Adjust the number of sentences in the summary as needed
        summarized_text = " ".join([str(sentence) for sentence in summary])
        st.write("# Summary: 📌")
        st.write(summarized_text)
        st.write("")
        summary_button = st.download_button(
            label="Download Summary",
            data=summarized_text,
            key="summary-txt",
        )
        st.success("Success! ", icon="✅")
        st.balloons()
    else:
        st.write("The provided file path is not valid or the file does not exist.")
