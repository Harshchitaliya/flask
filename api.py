import paralleldots
paralleldots.set_api_key("5JylQcGoQlbtTzEQP7v4nw3xBhMqOq1rS20EeUuQV2Y")
def ner(text):

    lang_code = "en"
    ner = paralleldots.ner(text)
    return ner