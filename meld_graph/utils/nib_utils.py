import nibabel as nib
import numpy as np

def load_f32(path):
    img = nib.load(path)
    return img, img.get_fdata().astype(np.float32, copy=False)