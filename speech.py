import speech_recognition as sr
import webbrowser

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
    
    try:
        recognized_text = r.recognize_google(audio_text)
        print("Text: " + recognized_text)
        
        if 'play' in recognized_text.lower() and 'song' in recognized_text.lower():
            song_name = recognized_text.lower().replace("play", "").replace("song", "").strip()
            if song_name:
                search_query = song_name.replace(" ", "+")
                youtube_url = f"https://www.youtube.com/results?search_query={search_query}"
                webbrowser.open(youtube_url)
                
            else:
                print("Song name not recognized.")
        else:
            search_query = recognized_text.replace(" ", "+")
            google_url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(google_url)

    except Exception as e:
        print("Sorry, I did not get that", e)
