import openai

class GPT3Completion:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key = api_key)        

    def generate_completions(self, prompt, model, temperature=0, max_tokens=2000):
        response = self.client.chat.completions.create(
            model=model,
            messages=[ {
                        "role" : "user",
                        "content": prompt,
                        },
                      # could also have a system prompt if desired
                     ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return completions.choices[0].message.content.strip()
