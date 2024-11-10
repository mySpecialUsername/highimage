import cv2
from himage.utils import deduce_limits
from himage.types import Image
import os

def imread(path:str):
    """reads an image from a path
    Parameters
    ----------
    path : string, the path to the image
    Returns
    -------
    ndarray, the image
    """
    im = cv2.imread(path)
    if im is None:
        raise ValueError("The provided path is invalid")
    elif im.ndim == 3:
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    else:
        pass
    return im.astype(float)/255


def imwrite(im:Image, path:str, create_path:bool = False):
    """writes an image to a path
    Parameters
    ----------
    im : ndarray, the image
    path : string, the path to the image
    Returns
    -------
    None
    """
    _, vmax = deduce_limits(im)
    if vmax == 1:
        im = im*255
    
    if im.ndim == 3:
        im = im[:,:,::-1]

    if not os.path.exists(os.path.dirname(path)):
        if create_path:
            os.makedirs(os.path.dirname(path))
        else:
            raise OSError("The provided path is invalid. You can use the create_path argument.")
    cv2.imwrite(path, im)

