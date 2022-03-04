from service.image_diff import ImageDiff
from flask import request


score=ImageDiff().get_image_score("/Users/xh/Downloads/ks/vision-ui/image/1_0.png", "/Users/xh/Downloads/ks/vision-ui/image/1_1.png",
                                            "/Users/xh/Downloads/ks/vision-ui/image/image_diff.png")

print("score:",score)