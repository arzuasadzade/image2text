import openai
import streamlit as st
from PIL import Image
import numpy as np

# Set your OpenAI API key
openai.api_key = "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"

# Title and subtitle
st.title("Generate Text from Images")
st.markdown("## Generative Text - Using `streamlit` - hosted on 🤗 Spaces")

# Image uploader
image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

if image is not None:
    input_image = Image.open(image)
    st.image(input_image)

    # OpenAI GPT-3.5 prompt generation
    prompt = f"Generate a description for the image:\n{np.array(input_image)}"

    with st.spinner("💨 AI is at Work! "):
        result = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100
        )

        generated_text = result['choices'][0]['text']

        st.write(generated_text)
    st.balloons()
else:
    st.write("Upload an Image")

st.caption("Made with ❤️ by arzy. Credits to 🤗 Spaces for Hosting this")

