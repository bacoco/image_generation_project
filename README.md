
# Image Generation Project

## Project Structure

- `streamlit_app.py`: Streamlit application code.
- `fastapi_server_complete.py`: FastAPI server code.
- `Dockerfile`: Dockerfile for the FastAPI server.
- `Dockerfile_Streamlit`: Dockerfile for the Streamlit application.
- `docker-compose.yml`: Docker Compose file to orchestrate the containers.

## Deployment Instructions

1. **Build and Run with Docker Compose**: 
   ```
   docker-compose up --build
   ```
   This will start the FastAPI server and Streamlit app.

2. **Access the Applications**: 
   - FastAPI server: `http://localhost:8000`
   - Streamlit app: `http://localhost:8501`

3. **Stopping the Services**: 
   ```
   docker-compose down
   ```

## Using the Applications

### FastAPI Server

Send POST requests to `/generate-image/` with the following parameters:

- `prompt`: Primary text prompt for image generation.
- `negative_prompt`: Text to specify what should not be in the image.
- `image_style`: Style of the image.
- `prompt2`: Secondary text prompt.
- `negative_prompt2`: Secondary negative prompt.
- `use_negative_prompt`: Flag to use or ignore the negative prompt.
- `use_prompt2`: Flag to use or ignore `prompt2`.
- `use_negative_prompt2`: Flag to use or ignore `negative_prompt2`.
- `seed`: Seed for randomness.
- `width`: Width of the generated image (256 to 1024 pixels).
- `height`: Height of the generated image (256 to 1024 pixels).
- `guidance_scale_base`: Guidance scale for base (1 to 20).
- `guidance_scale_refiner`: Guidance scale for refiner (1 to 20).
- `num_inference_steps_base`: Number of inference steps for base (10 to 150 steps).
- `num_inference_steps_refiner`: Number of inference steps for refiner (21 to 51 steps).
- `apply_refiner`: Flag to apply refiner.
- `randomize_seed`: Flag to randomize seed.

Example POST request in Python:
```python
import requests
url = 'http://localhost:8000/generate-image/'
data = {'prompt': 'A beautiful landscape', ...}
response = requests.post(url, json=data)
```

### Streamlit Application

- Access the app at `http://localhost:8501`.
- Enter prompts and adjust settings as needed.
- Click 'Generate Image' to view results.

## License

This project is open source and available under the [MIT License](LICENSE).
