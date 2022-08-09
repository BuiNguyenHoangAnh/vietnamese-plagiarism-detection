# import thư viện
from utils import *
from plagiarism_detection_ngram import *

TRAINDATA_PATH = "pos.txt"
TESTDATA_PATH = "pos.txt"
n = 4 # set ngram number

# tiền xử lý
train_data = read_txt_files(TRAINDATA_PATH)
train_data = word_segmentation(train_data)
train_data = remove_punctuation_marks(train_data)
train_data = remove_stop_words(train_data)
train_data = remove_numbers(train_data)
train_data = remove_spaces(train_data)
print("train data:", train_data)

test_data = read_txt_files(TESTDATA_PATH)
test_data = word_segmentation(test_data)
test_data = remove_punctuation_marks(test_data)
test_data = remove_stop_words(test_data)
test_data = remove_numbers(test_data)
test_data = remove_spaces(test_data)

# kiểm tra đạo văn sử dụng thuật toán n-gram
result, grams =diff_ngram(train_data, test_data, n)
print("result: ", result, grams)

# kiểm tra đạo văn sử dụng thuật toán lcs và cs

# kiểm tra đạo văn sử dụng thuật toán fuzzy-based

# đưa ra kết quả