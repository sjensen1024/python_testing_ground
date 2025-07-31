from chatterbox.tts import ChatterboxTTS
import sounddevice

model = ChatterboxTTS.from_pretrained(device="cuda")

first_line = "Hi there. What you're hearing right now was just generated using a pretrained model with Chatterbox. Isn't that cool?"
first_line_wav = model.generate(first_line)

second_line = "Whoa! Yeah! That's super cool!"
second_line_wav = model.generate(second_line, exaggeration=1.5)

third_line = "Uh... it's not THAT cool. It's just a simple script. Anyway. Gotta go. Bye!"
third_line_wav = model.generate(third_line, exaggeration=0.6)


sounddevice.play(first_line_wav.T, model.sr)
sounddevice.wait()

sounddevice.play(second_line_wav.T, model.sr)
sounddevice.wait()

sounddevice.play(third_line_wav.T, model.sr)
sounddevice.wait()
