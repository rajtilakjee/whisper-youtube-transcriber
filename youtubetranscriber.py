import whisper
import pytube
import requests

def whisperMagic(url):
	r = requests.get(url)
	status = "Video unavailable" in r.text
	if status == False:
		data = pytube.YouTube(url)
		audio = data.streams.get_audio_only()
		audio = audio.download()

		model = whisper.load_model('medium')

		text = model.transcribe(audio)
		text = text['text']
		return text

print("Please enter the URL of the video: ", url)
print(whisperMagic(url))
