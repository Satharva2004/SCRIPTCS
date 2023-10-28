import assemblyai as aai

aai.settings.api_key = "9d957a8be0f047e1a374431c34112f1f"

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(r"C:\\Users\\sawan\\Downloads\\videoplayback.mp4")
print("Transcribed Text:")
print(transcript.text)
print("Subtitles (SRT format):")
print(transcript.export_subtitles_srt())
summary = transcript.text[:100]
print("Summary:")
print(summary)

