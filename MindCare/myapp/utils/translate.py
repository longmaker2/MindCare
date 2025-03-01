# translate.py

def translate_text(text, target_language):
    """
    Translates text into the target language using Google Translate.
    """
    from googletrans import Translator

    translator = Translator()
    try:
        result = translator.translate(text, dest=target_language)
        return result.text
    except Exception as e:
        return f"Error: {str(e)}"
