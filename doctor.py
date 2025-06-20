import base64
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()
image_path = "pimple.jpg"
def doc(image_path, patient_statement):
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

    
    image_file= open(image_path, 'rb')
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    vision_llm = ChatGroq(
        model = "meta-llama/llama-4-maverick-17b-128e-instruct",
        api_key=GROQ_API_KEY
        ) 
    

    query = f"""You are a doctor. Your patient will ask you for help by expressing his condition through pictures and texts. 
    Analyze the pictures and the patient's statement. Replay in few lines according to patient statement.
    \\
    Patient's statement: {patient_statement}
    \\
    """
    message = [
        {
            "role": "user",
            "content": [
                {
                    'type': 'text',
                    'text': query
                },
                {
                    'type': 'image_url',
                    'image_url':{
                        'url': f'data:image/jpg;base64,{encoded_image}',
                    }
                }
            ]
        }
    ]
    response = vision_llm.invoke(message).content
    print(response)
    return response