"""
 @file : CacuFrames
 @Author : Pale.R
 @Date : 2022/9/30
"""
"""
 @file : CaculateFrames
 @Author : Pale.R
 @Date : 2022/9/30
"""


def CaculateFrams():
    result = []
    i = 0

    imgs = int(input("请输入图片数："))
    frams = imgs
    steps = imgs - 1
    caculate = 100 / steps

    print("imgs: ", imgs)
    print("frams: ", frams)
    print("steps: ", steps)

    # print(caculate)

    while (i < frams):
        result.append(i * caculate)
        i = i + 1

    for i in result:
        i = round(i, 2)
        print(str(i) + "%{background-position: }")
    # print(len(result))


CaculateFrams()