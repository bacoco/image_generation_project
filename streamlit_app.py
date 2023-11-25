
import streamlit as st
import requests

st.title('Image Generation with FastAPI')

# Define the FastAPI endpoint
url = "http://localhost:8000/generate-image/"

# Create form for user input
with st.form(key='image_form'):
    prompt = st.text_input("Enter a prompt for image generation")
    negative_prompt = st.text_input("Enter a negative prompt (optional)", "")
    image_style = st.selectbox("Select Image Style", ["(No style)", "Other styles..."])
    use_negative_prompt = st.checkbox("Use negative prompt", value=False)
    use_prompt2 = st.checkbox("Use second prompt", value=False)
    prompt2 = st.text_input("Enter second prompt (optional)", "")
    negative_prompt2 = st.text_input("Enter second negative prompt (optional)", "")
    use_negative_prompt2 = st.checkbox("Use second negative prompt", value=False)
    seed = st.number_input("Seed", min_value=0, max_value=2147483647, value=0)
    width = st.slider("Width", min_value=256, max_value=1024, value=512)
    height = st.slider("Height", min_value=256, max_value=1024, value=512)
    guidance_scale_base = st.slider("Guidance scale for base", min_value=1, max_value=20, value=7)
    guidance_scale_refiner = st.slider("Guidance scale for refiner", min_value=1, max_value=20, value=7)
    num_inference_steps_base = st.slider("Number of inference steps for base", min_value=10, max_value=150, value=25)
    num_inference_steps_refiner = st.slider("Number of inference steps for refiner", min_value=21, max_value=51, value=30)
    apply_refiner = st.checkbox("Apply refiner", value=False)
    randomize_seed = st.checkbox("Randomize seed", value=True)
    submit_button = st.form_submit_button(label='Generate Image')

# On form submission, call the FastAPI server
if submit_button:
    data = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "image_style": image_style,
        "prompt2": prompt2,
        "negative_prompt2": negative_prompt2,
        "use_negative_prompt": use_negative_prompt,
        "use_prompt2": use_prompt2,
        "use_negative_prompt2": use_negative_prompt2,
        "seed": seed,
        "width": width,
        "height": height,
        "guidance_scale_base": guidance_scale_base,
        "guidance_scale_refiner": guidance_scale_refiner,
        "num_inference_steps_base": num_inference_steps_base,
        "num_inference_steps_refiner": num_inference_steps_refiner,
        "apply_refiner": apply_refiner,
        "randomize_seed": randomize_seed
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.image(response.json()['image'], use_column_width=True)
    else:
        st.error("Error in image generation")
