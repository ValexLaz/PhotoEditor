import cv2
import numpy as np

class Fourier:
    def __init__(self, image):
        self.image = image

    def apply_fourier_transform(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        dft = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)
        dft_shift = np.fft.fftshift(dft)
        magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]) + 1)
        cv2.normalize(magnitude_spectrum, magnitude_spectrum, 0, 255, cv2.NORM_MINMAX)
        magnitude_spectrum = np.uint8(magnitude_spectrum)

        return magnitude_spectrum

    def get_fourier_spectrum(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        f = np.fft.fft2(gray)
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20 * np.log(np.abs(fshift))
        return magnitude_spectrum
