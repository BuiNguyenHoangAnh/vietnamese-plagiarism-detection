#import thư viện
import re
import io

from docx import *

from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

from vws import RDRSegmenter, Tokenizer # https://github.com/Sudo-VP/Vietnamese-Word-Segmentation-Python

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

# đọc từ file word
def read_doc_files(path):
    document = Document(path)
    text = []
    for docpara in document.paragraphs:
        text.append(docpara.text)
    return text[0]

# đọc từ file pdf
def read_pdf_files(path):
    with open(path, 'rb') as fp:
        rsrcmgr = PDFResourceManager()
        outfp = io.StringIO()
        laparams = LAParams()
        device = TextConverter(rsrcmgr, outfp, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(fp):
            interpreter.process_page(page)
    text = outfp.getvalue()
    return text

##############
# TIỀN XỬ LÝ #
##############

# tách từ (word segmentation)
def word_segmentation(document):
    rdrsegment = RDRSegmenter()
    tokenizer = Tokenizer()
    doc = rdrsegment.segmentRawSentences(tokenizer, document)
    print("word segmentation: ", doc)
    return doc

# loại bỏ ký tự đặc biệt
def remove_punctuation_marks(document):
    doc = re.sub(r"\W", " ", document)
    print("remove punctuation marks: ", doc)
    return doc

# loại bỏ hư từ (stop word) (từ điển stop word: https://github.com/stopwords/vietnamese-stopwords)
def load_stop_words():
    stop_word_list = []
    with open(STOPWORD_PATH, encoding="utf8") as stop_words:
        for line in stop_words:
            word = re.sub(r"\n", "", line)
            stop_word_list.append(word)
    return stop_word_list

def remove_stop_words(document):
    stop_word_list = load_stop_words()
    doc = document
    for word in document.split():
        # for stop_word in stop_word_list:
        if word in stop_word_list:
            doc = doc.replace(word, "")
    print("remove stop words: ", doc)
    return doc

#loại bỏ số
def remove_numbers(document):
    doc = re.sub(r"[0-9]", "", document)
    print("remove numbers: ", doc)
    return doc


# loại bỏ khoảng trắng thừa
def remove_spaces(document):
    doc = re.sub(r"\s+", " ", document, flags=re.I)
    print("remove spaces: ", doc)
    return doc