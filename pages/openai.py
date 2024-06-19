import base64
import requests
from aiobotocore import response
from openai import OpenAI

api_key = ""

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def process_image(image_path, prompt):
    # Getting the base64 string
    base64_image = encode_image(image_path)
    
    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {api_key}"
    }
    
    payload = {
      "model": "gpt-4o",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": prompt + ", what’s in this image?"
            },
            {
              "type": "image_url",
              "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
              }
            }
          ]
        }
      ],
      "max_tokens": 300
    }
    
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response

def choose_course(course1, course2):
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a course selection assistant, skilled in helping Cornell students decide between two courses."},
            {"role": "user", "content": "I am a Cornell student, and want to choose between courses " + str(course1) + " and " + str(course2) + ". Use open_url() to read course introduction and course reviews from https://www.cureviews.org, which should I take for next fall?"},
            {"role": "user", "content": "Exclude the introduction about not being able to access information, get straight to the comparison."}
        ]
    )
    response = completion.choices[0].message.content
    return response