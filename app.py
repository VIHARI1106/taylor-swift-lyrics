import streamlit as st
import lyricsgenius
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load API token from secrets
GENIUS_ACCESS_TOKEN = st.secrets["GENIUS_ACCESS_TOKEN"]
genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)
genius.skip_non_songs = True
genius.excluded_terms = ["(Remix)", "(Live)"]

# Streamlit App UI
st.set_page_config(page_title="Taylor Swift Lyrics Visualizer", layout="centered")
st.title("🎤 Taylor Swift Lyrics Visualizer")

song_title = st.text_input("Enter a Taylor Swift song title:")

if song_title:
    with st.spinner("Fetching lyrics..."):
        try:
            song = genius.search_song(song_title, "Taylor Swift")
            if song and song.lyrics:
                st.subheader("🎶 Lyrics")
                st.text_area("Lyrics", song.lyrics, height=300)

                # Word Cloud
                st.subheader("☁️ Word Cloud")
                wc = WordCloud(width=800, height=400, background_color="white").generate(song.lyrics)
                fig, ax = plt.subplots()
                ax.imshow(wc, interpolation='bilinear')
                ax.axis("off")
                st.pyplot(fig)
            else:
                st.error("Lyrics not found. Try another song.")
        except Exception as e:
            st.error(f"Error: {e}")
