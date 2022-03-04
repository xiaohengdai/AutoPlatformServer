ocr_result=[{'pos': [38, 14], 'text': 'P:0/1', 'score': 0.81}, {'pos': [109, 11], 'text': 'dX', 'score': 0.83}, {'pos': [81, 27], 'text': '8141', 'score': 0.8}]
target_text="P:1"

for j in (0, len(ocr_result)):
    print("j:", j)
    print("ocr_result[j]:", ocr_result[j])
    print("ocr_result[j]['text']:", ocr_result[j]['text'])
    print("target_text:", target_text)
    if target_text in ocr_result[j]['text']:
        # if re.search(target_text, ocr_result[key][1]):
        print(True)
print(False)