# Text-to-Image Generator (Local CPU Version)

This folder contains a fully local text-to-image generator using Hugging Face's `diffusers` library and the **Stable Diffusion v1.5** model. 

## Features
- **Cost**: $0.00 (Completely Free)
- **Hardware**: Runs entirely on your CPU (No GPU required)
- **Privacy**: 100% Offline generation (after the initial model download)

## How to use
1. Double-click the `setup_and_run.bat` file.
2. The script will automatically:
   - Create a Python virtual environment.
   - Install all required libraries (like PyTorch and Diffusers). Check your internet connection as this downloads roughly 2.5GB of libraries.
   - Run the application.
3. The very **first time** you run the application, it will download the Stable Diffusion model weights (~4.2 GB). This will take a while depending on your internet speed.
4. Once loaded, type your text prompt and wait for the image to generate!
   - *Note: Because this runs on a CPU, generating an image can take anywhere from 3 to 15 minutes depending on your processor's speed.*

## Files Explanation
- `app.py`: The main Python script that contains the logic. You can edit the `num_inference_steps` in this file to make it faster (lower quality) or slower (higher quality).
- `requirements.txt`: The list of Python libraries needed to run the app.
- `setup_and_run.bat`: A helper script so that you don't even need to open the terminal to run the app.
