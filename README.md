# 🎙️ Audio-to-Image Visualizer

Turn voice into stunning visuals using Whisper + Stable Diffusion!

## 🧠 What it does

- Transcribes educational audio using OpenAI Whisper
- Converts the text into a creative image prompt
- Generates a vivid image with Stable Diffusion 2.1

🛠️ How to Run

1. Clone the repository:
2. bash
git clone https://github.com/aicsnet/voice2vision.git
cd audio-to-image-visualizer
Install dependencies:

bash

pip install -r requirements.txt
Add your audio file (e.g., physics.m4a) to the root folder.

Run the script:

bash
python main.py
🔋 Requirements
Python 3.8+

NVIDIA GPU with at least 6GB VRAM

CUDA 11.8+

ffmpeg installed (needed by Whisper)

📷 Output
The script will generate and display an image and save it as output_image.png.
