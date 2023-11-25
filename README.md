
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

- **FastAPI Server**: Send POST requests to `/generate-image/` with image generation parameters.
- **Streamlit Application**: Interactive frontend to send requests to the FastAPI server and display results.
