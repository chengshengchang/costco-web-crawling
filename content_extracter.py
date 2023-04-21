import os
import openai

openai.api_key = os.getenv("api_key")

class GPT3Model:
    def __init__(self, model_name):
        self.model_name = model_name

    def generate_text(self, prompt):
        try:
            response = openai.Completion.create(
                model=self.model_name,
                prompt=prompt,
                temperature=0,
                max_tokens=64,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            return response['choices'][0].text
        except Exception as e:
            print("Error:", e)
            return None
