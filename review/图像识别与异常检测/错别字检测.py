# 规则的解决思路
# 中文纠错分为两步走，第一步是错误检测，第二步是错误纠正；
# 错误检测部分先通过结巴中文分词器切词，由于句子中含有错别字，所以切词结果往往会有切分错误的情况，这样从字粒度和词粒度两方面检测错误， 整合这两种粒度的疑似错误结果，形成疑似错误位置候选集；
# 错误纠正部分，是遍历所有的疑似错误位置，并使用音似、形似词典替换错误位置的词，然后通过语言模型计算句子困惑度，对所有候选集结果比较并排序，得到最优纠正词。

# 错误检测
# 字粒度：语言模型困惑度（ppl）检测某字的似然概率值低于句子文本平均值，则判定该字是疑似错别字的概率大。
# 词粒度：切词后不在词典中的词是疑似错词的概率大。
# 错误纠正
# 通过错误检测定位所有疑似错误后，取所有疑似错字的音似、形似候选词，
# 使用候选词替换，基于语言模型得到类似翻译模型的候选排序结果，得到最优纠正词。