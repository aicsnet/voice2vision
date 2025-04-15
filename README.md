# voice2vision

# 🎤voice2vision(CLI)

This is a lightweight CLI app powered by OpenAI's Whisper model that transcribes audio files into text. It is designed to run in Hugging Face Spaces directly from GitHub, without requiring any web interface.

Features

- Transcribes `.wav`, `.mp3`, `.m4a`, and other audio formats
- Powered by [openai/whisper](https://github.com/openai/whisper)
- Simple command-line interface
- Deployed using Hugging Face Spaces

File Structure
voice2vision-cli ├── app.py # Main script that runs transcription ├── requirements.txt # Dependencies ├── README.md # Project documentation

How to Use (Locally or in HF Logs Tab)

1. Add your audio file as `example.wav` (or update the filename in `app.py`)
2. Run the following command:

bash
python app.py
You’ll get the transcribed text printed in your console.

Requirements
Python 3.8+

ffmpeg (for audio preprocessing)

Install Locally
bash
Copy
Edit
pip install -r requirements.txt
Make sure ffmpeg is installed in your environment.


Example Output
arduino
Transcription:
"Quantum mechanics is a fundamental theory in physics that..."
🧠 Credits
OpenAI Whisper

