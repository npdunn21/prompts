from prompt_generator import generate_prompt


def test_prompt_generation():
    prompts = generate_prompt()
    print(prompts)
    assert len(prompts) == 3
