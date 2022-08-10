# import thư viện
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Nguồn: https://towardsdatascience.com/fuzzy-string-matching-in-python-68f240d910fe
def diff_fuzzy(source, input):
    return fuzz.token_sort_ratio(source, input)/100