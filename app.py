import streamlit as st
import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.title("🎤 Taylor Swift Lyrics Visualizer")

song_title = st.text_input("Enter a Taylor Swift song title:", "")

if song_title:
    artist = "Taylor Swift"
    try:
        # Call the lyrics.ovh API
        response = requests.get(f"https://api.lyrics.ovh/v1/{artist}/{song_title}")
        data = response.json()

        if 'lyrics' in data:
            lyrics = data['lyrics']
            st.subheader("Lyrics Preview:")
            st.text(lyrics[:500] + "..." if len(lyrics) > 500 else lyrics)

            # Generate word cloud
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(lyrics)
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            st.pyplot(plt)
        else:
            st.error("Lyrics not found. Please try another song.")
    except Exception as e:
        st.error(f"Error: {e}")
