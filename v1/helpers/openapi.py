import os

import openai
from dotenv import load_dotenv
import v1.helpers.command_template as CT

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")


class OpenAPI:
    def __init__(self):
        pass

    def get_product_names(self, param):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=CT.PRODUCT_NAME.format(
                param.get("product_description"),
                param.get("vibe_words")),
            max_tokens=4000
        )
        return response["choices"][0]["text"].replace("\n", "").replace("\"", "").split(",")

    def get_one_add(self, product, description, template):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=template.format(
                product,
                description),
            max_tokens=4000
        )
        return response["choices"][0]["text"].replace("\n", "")
