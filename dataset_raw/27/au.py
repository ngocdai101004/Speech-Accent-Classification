from moviepy.editor import VideoFileClip
from pytube import YouTube
from pytube.innertube import _default_clients
import datetime
import os


_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]


def convert_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(":"))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds


url = input()  # Nhập url
yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)

stream = yt.streams.get_lowest_resolution()
stream.download(filename="youtube.mp4")


cvt_video = VideoFileClip("youtube.mp4")
ext_audio = cvt_video.audio
while True:
    start_time = input()  # định dạng hh:mm:ss
    end_time = input()
    if (
        start_time == end_time and start_time == "00:00:00"
    ):  # nhập start_time = end_time = 00:00:00
        with open("youtube.mp4", "r") as f:
            if not f.closed:
                f.close()
        break
    start_seconds = convert_to_seconds(start_time)
    end_seconds = convert_to_seconds(end_time)
    video_segment = cvt_video.subclip(start_seconds, end_seconds)

    audio_segment = video_segment.audio  # Trích xuất âm thanh từ phần video đã cắt

    current_time = datetime.datetime.now()

    formatted_time = current_time.strftime("%Y_%m_%d_%H_%M_%S")

    file_name = f"{formatted_time}.mp3"
    audio_segment.write_audiofile(
        file_name
    )  # Ghi âm thanh ra file .mp3, file này có dạng yyyy_mm_dd_hh_mm_ss.mp3 để không trùng nhau
os.remove("youtube.mp4")
