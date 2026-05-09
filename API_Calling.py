import os
import io
from google import genai
from dotenv import load_dotenv
from gtts import gTTS



load_dotenv()
my_api_key = os.getenv("GEMINI_API_KEY")

cilent = genai.Client(api_key=my_api_key)

# note generate
def note_generate(images):
    prompt = """Summerize the images in note format in language bangla at max 100 words, 
    make sure necessary markdown to differntiate different section."""
    notes = cilent.models.generate_content(
        model = "gemini-2.5-flash",
        contents = [*images,prompt]
    )

    return notes.text

def audio_transcription(notes):
    speech = gTTS(notes,lang = 'bn',slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer

def quiz_generation(image,difficulty):
    prompt = f"""Generate 3 quizes in language bangla based on the {difficulty}. 
    make sure to add markdown to differtiate the options."""
    notes = cilent.models.generate_content(
        model = "gemini-2.5-flash",
        contents = [*image,prompt]
    )
    return notes.text