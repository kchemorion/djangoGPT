import openai

class ChatGPTAdapter:
    def can_process(self, statement):
        return True

    def process(self, statement, additional_response_selection_parameters=None):
        openai.api_key = "your_openai_api_key"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=statement.text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        selected_text = response["choices"][0]["text"].strip()
        return selected_text
