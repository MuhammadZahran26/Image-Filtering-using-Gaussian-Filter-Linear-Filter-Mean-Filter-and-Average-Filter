import skimage.io
import skimage.color
import matplotlib.pyplot as plt
import numpy as np

class Filters:
    def __init__(self, image_path):
        self.image = skimage.io.imread(image_path)
        if len(self.image.shape) == 3:
            self.image = skimage.color.rgb2gray(self.image)
        else:
            print("Image is already in grayscale format")
        
    def corr(self, img, mask):
        row, col = img.shape
        m, n = mask.shape
        new = np.zeros((row + m - 1, col + n - 1))
        m = m // 2
        n = n // 2
        filtered_img = np.zeros(img.shape)
        new[m:new.shape[0] - m, n:new.shape[1] - n] = img
        for i in range(m, new.shape[0] - m):
            for j in range(n, new.shape[1] - n):
                temp = new[i - m:i + m + 1, j - n:j + n + 1]
                result = temp * mask
                filtered_img[i - m, j - n] = result.sum()
        return filtered_img

    def gaussian_filter(self, m, n, sigma):
        gaussian = np.zeros((m, n))
        m = m // 2
        n = n // 2
        for x in range(-m, m + 1):
            for y in range(-n, n + 1):
                x1 = sigma * (2 * np.pi)**2
                x2 = np.exp(-(x**2 + y**2) / (2 * sigma**2))
                gaussian[x + m, y + n] = (1 / x1) * x2
        return self.corr(self.image, gaussian)

    def mean_filter(self, size):
        mean = np.ones((size, size))
        return self.corr(self.image, mean / mean.sum())
    
    def average_filter(self, size):
        average = np.ones((size, size)) / (size * size)
        return self.corr(self.image, average)
    
    def linear_filter(self, kernel):
        return self.corr(self.image, kernel)
    
    def show_images(self, *images, titles=None):
        plt.figure(figsize=(15, 5))
        for i, img in enumerate(images):
            plt.subplot(1, len(images), i + 1)
            plt.imshow(img, cmap='gray')
            if titles:
                plt.title(titles[i])
            else:
                plt.title(f'Image {i+1}')
        plt.show()