# Check GPU availability
import torch
torch.cuda.is_available()

!pip install git+https://github.com/openai/whisper.git
!pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
!pip install transformers diffusers accelerate

from google.colab import files

uploaded = files.upload()
# Make sure to upload a file like "audio.m4a"
audio_file = list(uploaded.keys())[0]
print(f"Uploaded: {audio_file}")

import whisper

model = whisper.load_model("base")  # use "small" or "medium" for better accuracy
result = model.transcribe("physics.m4a")
translated_text = result["text"]
print("🔤 Translated Text:\n", translated_text)

# You can modify the system prompt below to make the image more fantasy, real-world, sci-fi, etc.
visual_prompt = f"""You are a creative visual designer. Given the following educational concept:
\"{translated_text}\"

Describe a vivid and artistic scene that best illustrates the core idea. Be imaginative, clear, and precise.
"""
print("🧠 Image Prompt:\n", visual_prompt)

from diffusers import StableDiffusionPipeline
import torch

# Load Stable Diffusion
pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1", 
    torch_dtype=torch.float16
).to("cuda")

# Generate image
image = pipe(visual_prompt).images[0]

# Save and display image
image.save("output_image.png")
image.show()

from google.colab import files
files.download("output_image.png")

