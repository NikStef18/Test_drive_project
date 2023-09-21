def check_sentence_grammar(text):
    if text == "":
        raise Exception("Cannot check grammar of empty string.")
    return text[0].isupper() and text[-1] in ".?!"
    
