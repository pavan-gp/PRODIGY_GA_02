import torch
from diffusers import StableDiffusionPipeline
import time
import os

def generate_image_on_cpu(prompt, output_filename="generated_image.png"):
    print(f"\nStarting image generation for prompt:\n'{prompt}'\n")
    print("Please be patient. Running on CPU can take several minutes (often 5-15 minutes).")
    
    # Using Stable Diffusion v1.5 as it's a solid baseline.
    model_id = "runwayml/stable-diffusion-v1-5"
    
    print(f"\nLoading model '{model_id}'...")
    print("Note: This will download ~4GB of data the VERY FIRST time you run it.")
    
    # Load pipeline
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id, 
        torch_dtype=torch.float32 # Use float32 for CPU
    )
    
    # We are using CPU, so we keep it on CPU.
    pipe = pipe.to("cpu")
    
    # Optional: reduce memory usage slightly (though mostly impacts GPU, good practice)
    pipe.enable_attention_slicing()
    
    print("\nModel loaded! Starting to draw the image...")
    start_time = time.time()
    
    # Generate image. We use fewer inference steps (e.g., 20) to make CPU generation faster.
    # The default is usually 50, but 20 gives decent results much quicker.
    try:
        image = pipe(prompt, num_inference_steps=20).images[0]
    except Exception as e:
        print(f"Error during generation: {e}")
        return
        
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"\nSuccess! Image generated in {execution_time:.2f} seconds!")
    
    # Save the image
    image.save(output_filename)
    print(f"Saved to {os.path.abspath(output_filename)}\n")

if __name__ == "__main__":
    print("===========================================")
    print("   LOCAL TEXT-TO-IMAGE GENERATOR (CPU)     ")
    print("===========================================")
    print("This script uses your computer's CPU to run.")
    print("No cloud APIs, completely free and private!\n")
    
    user_prompt = input("Enter a description of the image you want to generate:\n> ")
    if not user_prompt.strip():
        user_prompt = "A futuristic city skyline at sunset, cyberpunk style, high detail"
        print(f"\nNo prompt entered, using default:\n> {user_prompt}")
        
    generate_image_on_cpu(user_prompt)
