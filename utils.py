#import thư viện
import re
from vws import RDRSegmenter, Tokenizer

# khia báo hằng
STOPWORD_PATH = "vietnamese-stopwords-dash.txt"

################
# ĐỌC TÀI LIỆU #
################

# đọc từ file .txt
def read_txt_files(path):
    f = open(path, "r", encoding="utf8")
    document = f.read().lower()
    f.close()
    return document

# đọc từ file word - TO DO

##############
# TIỀN XỬ LÝ #
##############

# tách từ (word segmentation)
def word_segmentation(document):
    rdrsegment = RDRSegmenter()
    tokenizer = Tokenizer()
    doc = rdrsegment.segmentRawSentences(tokenizer, document)
    print(doc)
    return doc

# loại bỏ ký tự đặc biệt
def remove_punctuation_marks(document):
    doc = re.sub(r"\W", " ", document)
    return doc

# loại bỏ hư từ (stop word) (từ điển stop word: https://github.com/stopwords/vietnamese-stopwords)
def load_stop_words():
    stop_word_list = []
    with open(STOPWORD_PATH, encoding="utf8") as stop_words:
        for line in stop_words:
            stop_word_list.append(line)
    return stop_word_list

def remove_stop_words(document):
    stop_word_list = load_stop_words()
    doc = ""
    for word in document:
        for stop_word in stop_word_list:
            if word == stop_word:
                doc = doc.replace(word, "")
                break
    return doc

#loại bỏ số
def remove_numbers(document):
    doc = re.sub(r"[^0-9]","",document)
    return doc


# loại bỏ khoảng trắng thừa
def remove_spaces(document):
    doc = re.sub(r"\s+", " ", document, flags=re.I)
    return doc