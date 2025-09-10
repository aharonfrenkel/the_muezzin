import io

import speech_recognition as sr
from speech_recognition import AudioData


class AudioTranscriber:
    def __init__(self):
        """Initializes the speech_recognition.recognizer object"""
        self._recognizer = sr.Recognizer()

    def transcribe(self, audio_file: bytes) -> str:
        """
        Transcribes the audio file to text

        Args:
            audio_file: The audio file to transcribe in bytes format

        Returns:
            The transcribed text
        """
        with sr.AudioFile(io.BytesIO(audio_file)) as source:
            audio_data: AudioData = self._recognizer.record(source)
            audio_text: str = self._recognizer.recognize_google(audio_data)
            return audio_text