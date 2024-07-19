import os

from funasr import AutoModel


class FunAsr:

    def __init__(self, model_dir):
        self.model = AutoModel(model=model_dir,  vad_model="fsmn-vad", punc_model="ct-punc")

    def generate(self, input):
        # res = self.model.generate(input=f"{self.model.model_path}/example/{input}",

        res = self.model.generate(input=os.path.abspath(f"./files/{input}"),
            batch_size_s=300,
            hotword='魔搭')
        return res
