import yt_dlp

LINK="https://www.youtube.com/watch?v={ID_video}"

def download_youtube_video(url, output_path="."):
    try:
        ydl_opts = {
            'format': 'best',  # best quality
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Name saved
            'overwrites': True,
            'verbose': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            print(f"O arquivo será salvo em: {ydl.prepare_filename(info_dict)}")
            ydl.download([url])
        print("Download concluído!")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")

video_url = LINK
download_path = r"C:\downloads"  # Directori destination

download_youtube_video(video_url, download_path)
