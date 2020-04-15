import os
import glob
import numpy as np
from PIL import Image

for src_path in sorted(glob.glob('**/*.png', recursive=True)):
    src_img = Image.open(src_path).convert('RGBA')
    src_mat = np.array(src_img)

    alpha_mat = src_mat[:, :, 3]
    diff = np.sum(alpha_mat - 255)
    if diff > 0:
        print('{} has transparent pixel.'.format(src_path))

        dst_mat = np.ones(alpha_mat.shape + (3,), dtype='uint8') * 255
        dst_mat[alpha_mat != 255] = (255, 0, 0)

        dst_img = Image.fromarray(dst_mat)

        src_basename = os.path.splitext(os.path.basename(src_path))[0]
        src_extension = os.path.splitext(src_path)[1]
        dst_path = src_basename + '-alpha' + src_extension

        dst_img.save(dst_path)

        print('  Output alpha map to {}'.format(dst_path))
