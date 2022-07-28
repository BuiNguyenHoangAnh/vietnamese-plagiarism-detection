doc = ""
################
# ĐỌC TÀI LIỆU #
################

# đọc từ file .txt
f = open("<path>/demofile.txt", "r")
document = f.read()
f.close()

# đọc từ file word - TO DO


##############
# TIỀN XỬ LÝ #
##############

# tách từ (word segmentation)
from vws import RDRSegmenter, Tokenizer
rdrsegment = RDRSegmenter.RDRSegmenter()
tokenizer = Tokenizer.Tokenizer()
doc = rdrsegment.segmentRawSentences(tokenizer, document)
print(output)

# loại bở ký tự đặc biệt
import re
doc = re.sub(r"\W", ' ', doc)

# loại bỏ hư từ (stop word) (từ điển stop word: https://github.com/stopwords/vietnamese-stopwords)
stop_word_list = []
with open("vietnamese-stopwords-dash.txt") as stop_words:
    for line in stop_words:
        stop_word_list.append(line)

def delete_stopwords(word):
    for word in doc:
        for stop_word in stop_word_list:
            if word == stop_word:
                doc = doc.replace(word, "")
                break

#loại bỏ số
doc = re.sub(r"[^0-9]","",doc)

# loại bỏ khoảng trắng thừa
doc = re.sub(r'\s+', ' ', doc, flags=re.I)