import re
import string
from collections import defaultdict

import nltk 
from nltk.corpus import stopwords


nltk.download('punkt')
nltk.download('stopwords')
ptbr_stopwords = stopwords.words('portuguese')

class Ngrams:
    def __init__(self, dataset_files: list) -> None:
        self.dataset_files = dataset_files

    def to_lower(self, text) -> str:
        return " ".join([w.lower() for w in text.split()])

    def remove_punctuation(self, text) -> str:
        clean_txt = "".join([c for c in text if c not in string.punctuation+'º'])
        return clean_txt

    def add_space(self, text) -> str:
        return '<s> <s> ' + text + ' </s> </s>'

    def remove_stopwords(self, text) -> str:
        phrase = " ".join([w.lower() for w in text.split() if w not in ptbr_stopwords])
        return phrase

    def text_preprocessing(self, text) -> list:
        text = re.sub('\n\n', '\n', text)
        text = re.findall('(?<=<TEXT>)[\s\S]*?(?=<\/TEXT>)', text)
        treated_corpus = [[] for i in range(len(text))]
        for i in range(len(text)):
            text_bl = re.findall('(?<=\\n)[\s\S]*?(?=\\n)', text[i])
            for j in range(len(text_bl)):
                text_bl[j] = re.sub('(^[\s])|([\s]$)','',text_bl[j])
                text_point = re.findall('[^\.]+', text_bl[j])
                for k in range(len(text_point)):
                    text_comma = re.findall('[^\;]+', text_point[k])
                    for l in range(len(text_comma)):
                        text_comma[l] = re.sub('([\d+])','',text_comma[l])
                        text_comma[l] = re.sub('(^[\s])|([\s]$)','',text_comma[l])
                        text_comma[l] = self.to_lower(text_comma[l])
                        text_comma[l] = self.remove_stopwords(text_comma[l])
                        text_comma[l] = self.remove_punctuation(text_comma[l])
                        text_comma[l] = self.add_space(text_comma[l])
                        treated_corpus[i].append(text_comma[l])
        
        return treated_corpus

    def get_corpus(self, dir_name: str) -> list:
        corpus = list()

        for dataset_file in self.dataset_files:
            with open(dir_name + dataset_file, 'r') as f:
                text = f.read()
                corpus += self.text_preprocessing(text)

        return corpus

    def make_three_gram(self, text, three_gram):
        words = text.split()

        for i in range(len(words) - 2):
            if (words[i], words[i+1]) in three_gram.keys():
                if words[i + 2] in three_gram[(words[i], words[i+1])].keys():
                    three_gram[(words[i], words[i+1])][words[i + 2]] += 1
                else:
                    three_gram[(words[i], words[i+1])][words[i + 2]] = 1
            else:
                three_gram[(words[i], words[i+1])] = {words[i + 2] : 1}

        return three_gram

    def make_bi_gram(self, text, bi_gram):
        words = text.split()

        for i in range(len(words) - 2):
            if (words[i+1]) in bi_gram.keys():
                if words[i + 2] in bi_gram[(words[i+1])].keys():
                    bi_gram[(words[i+1])][words[i + 2]] += 1
                else:
                    bi_gram[(words[i+1])][words[i + 2]] = 1
            else:
                bi_gram[(words[i+1])] = {words[i + 2] : 1}
        
        return bi_gram

    def make_uni_gram(self, text, uni_gram):
        words = text.split()
        for i in range(len(words) - 2):
            if words[i+2] in uni_gram.keys():
                uni_gram[words[i + 2]] += 1
            else:
                uni_gram[words[i + 2]] = 1
        
        return uni_gram

    def probability(self, w3, sentence, three_gram, bi_gram, uni_gram):
        w1, w2 = sentence
        
        try: 
            three_gram_prob = three_gram[(w1,w2)][w3] / bi_gram[w1][w2]
            bi_gram_prob = bi_gram[(w1)][w2] / uni_gram[w2]
            uni_gram_prob = uni_gram[w3] / len(uni_gram)
            final_prob = 0.8 * three_gram_prob * 0.15 * bi_gram_prob * 0.05 * uni_gram_prob
            return final_prob
        except KeyError:
            return 0

    def make_n_grams(self, corpus, grams=3) -> None:
        three_gram, bi_gram, uni_gram = defaultdict(), defaultdict(), defaultdict()

        for text_list in corpus:
            for text in text_list:
                self.make_three_gram(text, three_gram)

        for text_list in corpus:
            for text in text_list:
                self.make_bi_gram(text, bi_gram)

        for text_list in corpus:
            for text in text_list:
                self.make_uni_gram(text, uni_gram)

        return uni_gram, bi_gram, three_gram 

    def mask_n_gram(self, text, n_gram_lvl=0):
        return self.make_n_grams([[text]])[n_gram_lvl]
