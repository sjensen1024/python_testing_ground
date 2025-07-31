from chatterbox.tts import ChatterboxTTS
import sounddevice
import requests

response = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "text/plain"})
joke = response.text
print(joke)

model = ChatterboxTTS.from_pretrained(device="cuda")

joke_wav = model.generate("So, here's our newly generated joke: " + joke + "Well,  I hope you enjoyed this lovely joke.", exaggeration=0.05)

sounddevice.play(joke_wav.T, model.sr)
sounddevice.wait()
