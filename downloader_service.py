# downloader_service.py
import os
import platform
import subprocess
from pytubefix import YouTube

class YouTubeDownloaderService:
    @staticmethod
    def get_base_path():
        """Retorna a raiz da pasta do aplicativo."""
        home_dir = os.path.expanduser("~")
        return os.path.join(home_dir, "Videos", "YouTubeDownloader")

    @staticmethod
    def get_download_path(format_type):
        """
        Roteia o destino dinamicamente:
        Se for áudio, salva na subpasta 'Audios'. Senão, salva em 'Videos'.
        """
        base_dir = YouTubeDownloaderService.get_base_path()
        
        if "Áudio" in format_type:
            target_dir = os.path.join(base_dir, "Audios")
        else:
            target_dir = os.path.join(base_dir, "Videos")
            
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            
        return target_dir

    @staticmethod
    def open_download_folder():
        """Abre a pasta raiz do aplicativo nativamente de acordo com o Sistema Operacional."""
        path = YouTubeDownloaderService.get_base_path()
        
        # Se a pasta não existe (o usuário clicou antes de baixar algo), cria ela.
        if not os.path.exists(path):
            os.makedirs(path)
            
        system = platform.system()
        if system == "Windows":
            os.startfile(path)
        elif system == "Darwin":  # macOS
            subprocess.Popen(["open", path])
        else:  # Linux
            subprocess.Popen(["xdg-open", path])

    @staticmethod
    def download_media(url, format_type, progress_callback=None):
        # Pega a pasta específica (Audios ou Videos) baseada na escolha
        output_path = YouTubeDownloaderService.get_download_path(format_type)

        yt = YouTube(url, on_progress_callback=progress_callback)
        
        # Filtros de Qualidade e Som
        if format_type == "Áudio (Melhor Qualidade - MP3)":
            stream = yt.streams.get_audio_only()
            file_extension = ".mp3"
            
        elif format_type == "Vídeo - Máx. Qualidade (Com Som)":
            stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
            file_extension = ".mp4"
            
        elif format_type == "Vídeo - Baixa Qualidade (Com Som)":
            stream = yt.streams.filter(progressive=True).order_by('resolution').asc().first()
            file_extension = ".mp4"
            
        elif format_type == "Vídeo - 1080p ou Alta (Sem Som)":
            stream = yt.streams.filter(only_video=True).order_by('resolution').desc().first()
            file_extension = ".mp4"
            
        elif format_type == "Vídeo - 720p (Sem Som)":
            stream = yt.streams.filter(only_video=True, resolution="720p").first()
            if not stream:
                stream = yt.streams.filter(only_video=True).order_by('resolution').desc().first()
            file_extension = ".mp4"
            
        else:
            stream = yt.streams.get_highest_resolution()
            file_extension = ".mp4"

        if not stream:
            raise ValueError("Não foi possível encontrar um stream válido para esta opção.")

        # Download
        downloaded_file_path = stream.download(output_path=output_path)
        
        # Renomeação segura para MP3
        if format_type == "Áudio (Melhor Qualidade - MP3)":
            base, _ = os.path.splitext(downloaded_file_path)
            new_file = base + file_extension
            if os.path.exists(new_file):
                os.remove(new_file)
            os.rename(downloaded_file_path, new_file)
        
        return yt.title, output_path