
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread, imsave
from skimage.morphology import watershed, disk
from skimage.feature import canny
from skimage.exposure import histogram
from skimage.filters import rank, sobel
from skimage.util import img_as_ubyte
from scipy import ndimage as ndi

def watershed_moth(img):
    image = img_as_ubyte(imread(r"J:\2_CHRP\Bistcho_2019\ID744_croppole.png", as_gray=True))
    denoised = rank.median(image, disk(2))
    imsave(r"J:\2_CHRP\Bistcho_2019\ID744_croppoledn.png", denoised)
    markers = rank.gradient(denoised, disk(5)) < 10
    imsave(r"J:\2_CHRP\Bistcho_2019\ID744_croppolemk.png", markers)
    # markers=ndi.label(markers)[0]
    # gradient=rank.gradient(denoised,disk(2))
    #sdfsgdg
    # labels=watershed(gradient,markers)

    # fig, axes=plt.subplot(nrows=2, ncols=2, figsize=(8,8), sharex=True, sharey=True)
    # ax=axes.ravel()
    #
    # ax[0].imshow()

    # imsave(r"J:\3_RND_BD\5_Imagery\P_FCIR_seg.png", labels)

    return 0

def cannydetector(img):

    histogram(img)
    edges=canny(img/255.)
    #imsave(r"J:\2_CHRP\Bistcho_2019\ID744_croppoleEdge.png", edges)
    fill_inside=ndi.binary_fill_holes(edges)
    label_objects, nb_labels=ndi.label(fill_inside)
    size=np.bincount(label_objects.ravel())
    mask_sizes=size>20
    mask_sizes[0]=0
    cleaned=mask_sizes[label_objects]
    #imsave(r"J:\2_CHRP\Bistcho_2019\ID744_croppolecln.png", cleaned)

    markers=np.zeros_like(img)
    markers[img<30]=1
    markers[img>150]=2
    elevmap=sobel(img)
    #imsave(r"J:\2_CHRP\Bistcho_2019\ID744_croppoleElv.png", elevmap)

    segment=watershed(elevmap, markers)
    segment=ndi.binary_fill_holes(segment-1)
    imsave(r"J:\2_CHRP\Bistcho_2019\ID744_croppolesegfillhole.png", segment)
    labelmap, _=ndi.label(segment)
    imsave(r"J:\2_CHRP\Bistcho_2019\ID744_croppoleFSgm.png", labelmap)








def main():
    img=imread(r"J:\2_CHRP\Bistcho_2019\ID744_croppole.png", as_gray=True)
    cannydetector(img)


if __name__ == "__main__":
    main()

