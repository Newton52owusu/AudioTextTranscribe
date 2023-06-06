import whisper

model = whisper.load_model("base")
result = model.transcribe("your directory")

with open("transcription.txt", "w") as file:
    file.write(result("text"))




