
class MultilingualProcessor:
    def normalize(self,text,language="en"):
        return {"language":language,"text":text.strip()}
