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
        model = "llama-3.2-90b-vision-preview",
        api_key=GROQ_API_KEY
        ) 
    

    query = """আপনি একজন ডাক্তার। আপনার রোগী তার অবস্থা চিত্র এবং লেখার মাধ্যমে প্রকাশ করে আপনার কাছে সাহায্য চাইবেন। ছবি এবং রোগীর বক্তব্য বিশ্লেষণ করুন এবং রোগীর রোগ সনাক্ত করুন। আউটপুটে আপনার বিশ্লেষণ সংক্ষেপে বর্ণনা করুন।" 
    \
    Patient statement: {patient_statement}
    \
    your Answer:
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

    message = [
        {
            "role": "user",
            "content": [
                {
                    'type': 'text',
                    'text': "Translate this text into bangla: {response}"
                }    
            ]
        }
    ]

    translation_llm = ChatGroq(
        model = "gemma2-9b-it",
        api_key=GROQ_API_KEY
        ) 

    bangla_response = translation_llm.invoke(message).content
    print(bangla_response)
    return response