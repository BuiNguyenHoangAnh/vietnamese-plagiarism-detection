# import thư viện
from plagiarism_detection_fuzzy import diff_fuzzy
from utils import *
from plagiarism_detection_ngram import *
from plagiarism_detection_lcs_cs import *

TRAINDATA_PATH = "pos1.txt"
TESTDATA_PATH = "pos2.txt"

n = 4 # set ngram number

# plagiarism threshold
threshold_ngram = 0.5
threshold_lcs_cs = 0.5
threshold_fuzzy = 0.5

# tiền xử lý
train_data = read_txt_files(TRAINDATA_PATH)
train_data = word_segmentation(train_data)
train_data = remove_punctuation_marks(train_data)
train_data = remove_stop_words(train_data)
train_data = remove_numbers(train_data)
train_data = remove_spaces(train_data)

test_data = read_txt_files(TESTDATA_PATH)
test_data = word_segmentation(test_data)
test_data = remove_punctuation_marks(test_data)
test_data = remove_stop_words(test_data)
test_data = remove_numbers(test_data)
test_data = remove_spaces(test_data)

# kiểm tra đạo văn sử dụng thuật toán n-gram
result_ngram, grams =diff_ngram(train_data, test_data, n)
print("plagiarism detection result using n-gram: ", result_ngram, grams)
# TO DO: if result >= p thong bao ket qua va ket thuc chuong trinh

# kiểm tra đạo văn sử dụng thuật toán lcs và cs
result_lcs_cs = diff_lcs_cs(train_data, test_data)
print("plagiarism detection result using lcs & cs: ", result_lcs_cs)

# kiểm tra đạo văn sử dụng thuật toán fuzzy-based
result_fuzzy = diff_fuzzy(train_data, test_data)
print("plagiarism detection result using fuzzy: ", result_fuzzy)

# đưa ra kết quả