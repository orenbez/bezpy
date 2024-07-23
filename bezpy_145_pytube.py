# requires pip install pytube - downloads youtube videos
# https://pytube.io/en/latest/
# https://pypi.org/project/pytube/7.0.16/

import sys
from pytube import YouTube


def download_video(url, save_path, resolution):
    try:
        yt = YouTube(url)
    except Exception as e:
        print(e)
        sys.exit()

    streams = yt.streams.filter(progressive=True, file_extension="mp4")
    get_video = {resolution == 'high': streams.get_highest_resolution,
                 resolution == 'low': streams.get_lowest_resolution}.get(True)
    res_stream = get_video()
    print("Starting download ...")
    print('Title:', yt.title)
    print('Publish Date:', yt.publish_date)
    print('Author:', yt.author)
    print('Resolution:', resolution)
    res_stream.download(output_path=save_path)
    print("Video downloaded successfully!")


if __name__ == "__main__":

    _url = 'https://youtu.be/v5Hzv82KnQk?si=kQf_ihZiJhij2T_X'
    _save_path = r'C:\youtube'
    _resolution = 'high'  # high / low
    download_video(_url, _save_path, _resolution)
