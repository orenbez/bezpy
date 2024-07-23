import os
import requests
import subprocess
from bs4 import BeautifulSoup
import m3u8

# watched this: https://www.youtube.com/watch?v=p07ZZZVL72E
# required to download ffmpeg: https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/

PATH = r'D:\D\video_downloads'


def get_video_links(archive_url):
    r = requests.get(archive_url)  # create response object
    soup = BeautifulSoup(r.content, 'html5lib')  # create beautiful-soup object
    links = soup.findAll('a')  # find all links on web-page
    video_links = [archive_url + link['href'] for link in links if link['href'].endswith('mp4')]  # filter the link ending with .mp4
    return video_links


def download_video_series(video_links):
    for link in video_links:

        # iterate through all links in video_links
        # and download them one by one
        # obtain filename by splitting url and getting last string
        file_name = link.split('/')[-1]

        print("Downloading file:%s" % file_name)

        # create response object
        r = requests.get(link, stream=True)

        # download started
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

        print("%s downloaded!\n" % file_name)

    print("All videos downloaded!")
    return


def download_mp4_series():
    archive_url = "https://ww1.m4uhd.tv/watch-movie-the-weekend-2018-232718.html"
    video_links = get_video_links(archive_url)     # getting all video links
    download_video_series(video_links)  # download all videos


def download_m3u8_series(url, convert):
    r = requests.get(url)
    if not r.ok:
        print('Bad response!')
    else:
        source = rf'{PATH}\video.ts'
        source_complete = rf'{PATH}\{movie_name}.ts'    # renamed source file

        dest = rf'{PATH}\{movie_name}.mp4'    # converted file

        m3u8_master = m3u8.loads(r.text)
        segments = m3u8_master.data['segments']
        total_segments = len(segments)
        with open(source, 'wb') as f:    # Downloading as MPEG transport stream format
            for part, segment in enumerate(segments, start=1):
                uri = segment['uri']
                duration = f"{segment['duration']}s"
                print(f'downloading part:{part}/{total_segments}, {duration=}')
                r = requests.get(uri)
                f.write(r.content)
        print('converting to mp4 ...')
        if convert:
            subprocess.run([r'C:\ffmpeg\bin\ffmpeg.exe', '-i', source, dest])
        os.rename(source, source_complete)
        print(f'download for {movie_name} is complete!!!')


def check_url(url):
    r = requests.get(url)
    if r.ok:
        m3u8_master = m3u8.loads(r.text)
        playlists = m3u8_master.data['playlists']
        if playlists:
            uri = playlists[0].get('uri')
            print(f'{uri=}')
            return False
        else:
            segments = m3u8_master.data['segments']
            print(f'There are {len(segments)} segments, this is the correct url')
            return True


if __name__ == "__main__":

    movie_name = 'Mediterraneo (1991)'
    m3u8_url = 'https://vdnm.v4507fb3559.site/_v2-ewdl/9a701df349a7e4ae16c25b01dd7fefae231920c4561f9eea8c9f78fe4fcd06741ae3e719f0ef63837c6cf62e8daaecb28d7ff9aa0d734593957b6ac8d304036c2ba572c63dc0f2a87391fa2e8655928300de2bf9e0ec895b97205eb6ff80e3a32b369acd5daf0ea77774ddace3/h/beaaabae4/fbfedeee;9d705ee448b4e4e553dc06568f6feda3345b239e1c12c0.m3u8'


    if check_url(m3u8_url):
        download_m3u8_series(m3u8_url, True)
