import openai

def parse_with_gpt(search_data: str, api_key: str):
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or any other available model like gpt-4
        messages=[
            {"role": "system", "content": "Thank you GPT for your help :)"},
            {"role": "user", "content": search_data},
        ],
        max_tokens=200
    )

    return response['choices'][0]['message']['content']
