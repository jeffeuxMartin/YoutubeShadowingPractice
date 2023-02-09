import streamlit as st
import pandas as pd

st.title('YouTube transcription')
# uploaded_csv = st.file_uploader('選擇您要上傳的CSV檔')

# if uploaded_csv is not None:
#     df = pd.read_csv(uploaded_csv)
#     st.header('您所上傳的CSV檔內容：')
#     st.dataframe(df)

try:
    import os
    print('GPU?')
    os.system('nvidia-smi')
    print('GPU!')
except:
    pass

vid = st.text_input('Input Video ID:')

 
def ytvideo(vid):
    return f"https://www.youtube.com/watch?v={vid}" 
   
def videoTranscriptioin(vid):
    import logging
    with st.empty():

    
        placeholder = st
        placeholder.header("Downloading ...")
        from get_video_from_yt import download
        cache_video = f'{vid}.mp4'
        cache_audio = f'{vid}.mp3'
        cache_script = f'{vid}.json'
        download(ytvideo(vid), cache_video)
        
        placeholder.header("Converting ...")
        from mp4_to_mp3 import \
            convert_video_to_audio_ffmpeg
        convert_video_to_audio_ffmpeg(cache_video)
        
        placeholder.header("Generating Scripts ...")
        from video2script import split_video
        split_video(
            vid=cache_audio,
            model='base',  # FIXME
            output=cache_script,
            prune=True,
        )
        placeholder.empty()
    
import os
import sys
import time

if vid:
    st.text(vid)
    script_path = f"{vid}.json"
    with st.empty():
        if not os.path.exists(script_path):
            videoTranscriptioin(vid)
    if os.path.exists(script_path):
        from player_segbyseg import play_frontend
        audio_path = f"{vid}.mp3"
        st.audio(audio_path)
        play_frontend(
            mp3_path=audio_path,
            script_path=script_path,
            stop=0,     # FIXME
            n_words=5,  # FIXME
            speed=1.0,  # FIXME
        )
        st.video(
            # f"{vid}.mp4"
            f"https://www.youtube.com/watch?v={vid}" 
        )


# if vid:
#     st.header(vid[0])
#     os.system(f'say {vid[0]}')

#     time.sleep(1)
        
#     st.header(vid[1])
#     os.system(f'say {vid[1]}')

#     time.sleep(1)
        
#     st.header(vid[2])
#     os.system(f'say {vid[2]}')

#     time.sleep(1)
        
#     st.header(vid[3])
#     os.system(f'say {vid[3]}')
