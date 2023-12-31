from googletrans import Translator
from typing import List
from app.models import NLLBTranslator
from app.model_downloader import ModelOrchestrator


class TranslationService:
    def __init__(self):
        tokenizer, model = ModelOrchestrator.load_nllb_model()
        self.tokenizer = tokenizer
        self.model = model
        self.translator = None
        self.set_nllb_translator()
        # If we want to switch model we need to change the method by set_ and in perform_translation as well

    def set_nllb_translator(self, target_lang: str = 'eng_Latn'):
        self.translator = NLLBTranslator(self.tokenizer, self.model, target_lang=target_lang)

    def set_g_tranlsator(self):
        self.translator = Translator()

    def nllb_translate(self, sentence):
        return self.translator.translate(sentence)

    def g_translate(self, sentence, source_lang='ru', target_lang='en'):
        return self.translator.translate(sentence, src=source_lang, dest=target_lang)

    def switch_target_language(self):
        # Possible issue could be if we want to increase the scope of the project
        # Currently the output language is english with no options
        # To increase inference speed the translation model is created only once when the instance is created
        # Should possibly consider recreating the model if changing the language feature is implemented
        pass

    def perform_translation(self, sentences: List[str]) -> List[str]:
        """
        Use a model to translate sentences
        Over here we could implement switching between models
        """
        translated_sentences = []
        for sentence in sentences:
            result = self.nllb_translate(sentence)
            translated_sentences.append(result)
        return translated_sentences

    def translate_sentences(self, sentences: list):
        # Your sentence translation code goes here
        # Example: Translate the sentences using a translation service
        results = self.perform_translation(sentences)
        return 'translation: ' + ' '.join(results)
