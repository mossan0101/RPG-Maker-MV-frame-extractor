from PIL import Image

import os
import shutil


imageList = []
for ex in os.listdir():
    if "png" in ex:
        imageList.append(ex)

rootdir = "outdir"
try:
    os.makedirs(rootdir)
except:
    shutil.rmtree(rootdir)
    os.makedirs(rootdir)

for n, fname in enumerate(imageList):
    dirname = "out-" + str(n).zfill(5)
    try:
        os.makedirs(f"{rootdir}/{dirname}")
    except:
        os._exit(0)

    im = Image.open(fname)
    total = int(im.size[0] / 256) * 4
    
    # フレームサイズは 192x256
    # 下まで走査したら右に行って上に戻る
    x_count = 0
    y_count = 0
    for i in range(1, total):

        lx = x_count * 256
        ly = y_count * 192
        rx = x_count * 256 + 256
        ry = y_count * 192 + 192

        if i%4 == 0:
            x_count += 1

        y_count += 1
        if y_count == 4:
            y_count = 0
    
        cropped = im.crop((lx, ly, rx, ry))

        filename = str(i).zfill(5)
        outpath = f"{rootdir}/{dirname}/{filename}.png"
        cropped.save(outpath)

    print(f"{dirname} OK")