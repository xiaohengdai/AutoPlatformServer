import pycorrector

# error_sentence_1 = '我的喉咙发炎了要买点阿莫细林吃'
# correct_sent = pycorrector.correct(error_sentence_1)
# print("correct_sent:",correct_sent)


# error_sentence_2 = '7.23男子赛艇双人循坏赛'
# correct_sent = pycorrector.correct(error_sentence_2)
# print("correct_sent:",correct_sent)

error_sentence_2 = '外卖起手'
pycorrector.set_custom_confusion_dict(path='/Users/xh/Downloads/ks/vision-ui/words/my_custom_confusion.txt')
correct_sent = pycorrector.correct(error_sentence_2)
print("correct_sent:",correct_sent)
# idx_errors = pycorrector.detect(error_sentence_2)
# print("idx_errors:",idx_errors)