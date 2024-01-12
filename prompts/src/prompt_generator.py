import os

from openai import OpenAI

TOPICS = []

PROMPT = f""

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_prompt() -> list[str]:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Suggest 3 daily journal prompts. They should be about any of the following topics: reflection, gratitude, things that have been happening, or fun topics."}
        ],
        temperature=0.7,
        # https://community.openai.com/t/cheat-sheet-mastering-temperature-and-top-p-in-chatgpt-api/172683
        top_p=0.8
    )
    prompt_string: str = response.choices[0].message.content
    return [prompt for prompt in prompt_string.splitlines() if prompt != ""]
