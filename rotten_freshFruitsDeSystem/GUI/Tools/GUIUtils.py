# 自动生成对应的宽和高 0:根据高度生成 1:根据宽度生成
def autoMeas(w0, h0, w, h, mode=0):
    rate = w / h  # 传入图片的宽高比
    if mode == 0:
        newW = rate * h0
        if newW > w0:
            newH = h0
            while (w0 <= newW):
                newH = newH - 10
                newW = rate * newH
            w = newW
            h = newH
        else:
            w = newW
            h = h0
        return int(w), int(h)
