import glob
import cv2

def laplacian_of_gaussian(img):
    blur = cv2.GaussianBlur(img,(3,3),0)
    laplacian = cv2.Laplacian(blur,cv2.CV_64F)
    # _, laplacian = cv2.threshold(laplacian, 50, 255, cv2.THRESH_BINARY)
    return laplacian

if __name__ == "__main__":
    fnames = glob.glob("./inputs/*")
    for fname in fnames:
        img = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
        out_img = laplacian_of_gaussian(img)
        cv2.imwrite(fname.replace("inputs", "outputs"), out_img)
