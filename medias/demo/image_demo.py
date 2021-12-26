import nibabel as nib

def load_nii(img_path):
    """
    Function to load a 'nii' or 'nii.gz' file, The function returns
    everyting needed to save another 'nii' or 'nii.gz'
    in the same dimensional space, i.e. the affine matrix and the header

    Parameters
    ----------

    img_path: string
    String with the path of the 'nii' or 'nii.gz' image file name.

    Returns
    -------
    Three element, the first is a numpy array of the image values,
    the second is the affine transformation of the image, and the
    last one is the header of the image.
    """
    nimg = nib.load(img_path)
    return nimg.get_data(), nimg.affine, nimg.header

def load_img_demo():
    np_no_lbl = load_nii('medias/demo/anonyme.nii.gz')[0]
    np_lbl = load_nii('medias/demo/anonyme_gt.nii.gz')[0]
    return np_no_lbl, np_lbl
