# ui.py
import customtkinter as ctk
import threading
from downloader_service import YouTubeDownloaderService

class DownloaderApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("YouTube Downloader Avançado")
        self.geometry("650x450")
        self.resizable(False, False)
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.build_ui()

    def build_ui(self):
        self.title_label = ctk.CTkLabel(self, text="YouTube Downloader", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=(20, 10))

        self.url_entry = ctk.CTkEntry(self, width=500, placeholder_text="Cole o link do vídeo aqui...")
        self.url_entry.pack(pady=10)

        self.format_options = [
            "Vídeo - Máx. Qualidade (Com Som)",
            "Vídeo - Baixa Qualidade (Com Som)",
            "Vídeo - 1080p ou Alta (Sem Som)",
            "Vídeo - 720p (Sem Som)",
            "Áudio (Melhor Qualidade - MP3)"
        ]
        self.format_dropdown = ctk.CTkOptionMenu(self, values=self.format_options, width=500)
        self.format_dropdown.pack(pady=10)

        # ==========================================
        # FRAME PARA ORGANIZAR OS DOIS BOTÕES LADO A LADO
        # ==========================================
        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(pady=15)

        self.download_btn = ctk.CTkButton(self.buttons_frame, text="Baixar Agora", command=self.start_download_thread, width=200)
        self.download_btn.grid(row=0, column=0, padx=10)

        self.open_folder_btn = ctk.CTkButton(self.buttons_frame, text="Abrir Pasta de Destino", command=self.open_folder, width=200, fg_color="#4a4a4a", hover_color="#2b2b2b")
        self.open_folder_btn.grid(row=0, column=1, padx=10)
        # ==========================================

        # Barra de Progresso e Porcentagem
        self.progress_bar = ctk.CTkProgressBar(self, width=500)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=5)
        
        self.percent_label = ctk.CTkLabel(self, text="0%", font=ctk.CTkFont(size=12))
        self.percent_label.pack(pady=0)

        self.status_label = ctk.CTkLabel(self, text="Aguardando URL...", text_color="gray")
        self.status_label.pack(pady=10)

    def open_folder(self):
        """Dispara a abertura da pasta raiz sem travar a interface."""
        YouTubeDownloaderService.open_download_folder()

    def start_download_thread(self):
        url = self.url_entry.get().strip()
        format_type = self.format_dropdown.get()

        if not url:
            self.update_status("Erro: O campo de URL está vazio.", "red")
            return

        self.download_btn.configure(state="disabled")
        self.progress_bar.set(0)
        self.percent_label.configure(text="0%")
        self.update_status("Iniciando download... Por favor, aguarde.", "orange")

        thread = threading.Thread(target=self.process_download, args=(url, format_type))
        thread.start()

    def process_download(self, url, format_type):
        try:
            title, saved_path = YouTubeDownloaderService.download_media(
                url, format_type, progress_callback=self.on_progress_update
            )
            # Como o caminho salvo pode ser longo, nós omitimos parte dele se for necessário
            self.update_status(f"Concluído! Salvo com sucesso.", "green")
        except Exception as e:
            self.update_status(f"Erro ao baixar. Tente outra URL ou formato.", "red")
            print(f"[ERROR] Traceback: {e}")
        finally:
            self.download_btn.configure(state="normal")
            self.url_entry.delete(0, 'end')

    def on_progress_update(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = bytes_downloaded / total_size
        
        self.after(0, self.update_progress_ui, percentage)

    def update_progress_ui(self, percentage):
        self.progress_bar.set(percentage)
        self.percent_label.configure(text=f"{int(percentage * 100)}%")

    def update_status(self, message, color):
        self.after(0, lambda: self.status_label.configure(text=message, text_color=color))