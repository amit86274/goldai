
class NewsSummarizer:
    def summarize(self,article,max_words=50):
        words=article.split()
        return " ".join(words[:max_words])
