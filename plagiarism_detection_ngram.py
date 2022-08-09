def ngram(document, n):
    doc = document.split()
    tmp = [] 
    sent_len = len(doc) - n +1
    for i in range(sent_len):
        tmp.append(doc[i : i+n]) 
    return tmp

def diff_ngram(sent_a, sent_b, n):
    a = ngram(sent_a, n)
    b = ngram(sent_b, n) 
    common = [] 
    cnt = 0 
    for i in a:
        for j in b:
            if i == j:
                cnt += 1
                common.append(i)
    return cnt/len(a), common


# # Nguồn: https://towardsdatascience.com/simple-plagiarism-detection-in-python-2314ac3aee88
# # import thư viện
# import re
# from nltk.util import ngrams, pad_sequence, everygrams
# from nltk.tokenize import word_tokenize
# from nltk.lm import MLE, WittenBellInterpolated
# import numpy as np
# import plotly.graph_objects as go
# from scipy.ndimage import gaussian_filter

# def detect_plagiarism_ngram(train_data, test_data, n):
#     # pad the text and tokenize
#     training_data = list(pad_sequence(word_tokenize(train_data), n, pad_left=True, left_pad_symbol="<s>"))

#     # generate ngrams
#     ngrams = list(everygrams(training_data, max_len=n))
#     print("Number of ngrams:", len(ngrams))

#     # build ngram language models
#     model = WittenBellInterpolated(n)
#     model.fit([ngrams], vocabulary_text=training_data)
#     print(model.vocab)

#     # Tokenize and pad the text
#     testing_data = list(pad_sequence(word_tokenize(test_data), n, pad_left=True, left_pad_symbol="<s>"))
#     print("Length of test data:", len(testing_data))

#     # assign scores
#     scores = []
#     for i, item in enumerate(testing_data[n-1:]):
#         s = model.score(item, testing_data[i:i+n-1])
#         scores.append(s)

#     scores_np = np.array(scores)

#     # set width and height
#     width = 8
#     height = np.ceil(len(testing_data)/width).astype("int32")
#     print("Width, Height:", width, ",", height)

#     # copy scores to rectangular blank array
#     a = np.zeros(width*height)
#     a[:len(scores_np)] = scores_np
#     diff = len(a) - len(scores_np)

#     # apply gaussian smoothing for aesthetics
#     a = gaussian_filter(a, sigma=1.0)

#     # reshape to fit rectangle
#     a = a.reshape(-1, width)

#     # format labels
#     labels = [" ".join(testing_data[i:i+width]) for i in range(n-1, len(testing_data), width)]
#     labels_individual = [x.split() for x in labels]
#     labels_individual[-1] += [""]*diff
#     labels = [f"{x:60.60}" for x in labels]

#     # create heatmap
#     fig = go.Figure(data=go.Heatmap(
#                     z=a, x0=0, dx=1,
#                     y=labels, zmin=0, zmax=1,
#                     customdata=labels_individual,
#                     hovertemplate='%{customdata} <br><b>Score:%{z:.3f}<extra></extra>',
#                     colorscale="burg"))
#     fig.update_layout({"height":height*28, "width":1000, "font":{"family":"Courier New"}})
#     fig['layout']['yaxis']['autorange'] = "reversed"
#     fig.show()