from pydub import AudioSegment


audio = AudioSegment.from_mp3("./static/musica.mp3")

audio2 = AudioSegment.from_mp3("./static/musica2.mp3")

#musicas = [audio,audio2]

audio.play()