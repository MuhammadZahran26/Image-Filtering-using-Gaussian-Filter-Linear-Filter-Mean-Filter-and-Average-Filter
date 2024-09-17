# Image Filters Implementation

This repository contains implementations of various image filters, including Gaussian filter, Linear filter, Mean filter, and Average filter. Each filter is designed to manipulate images for various purposes such as noise reduction and blurring.

## Table of Contents
- [Filters Overview](#filters-overview)
  - [Gaussian Filter](#gaussian-filter)
  - [Mean Filter](#mean-filter)
  - [Linear Filter](#linear-filter)
  - [Average Filter](#average-filter)
- [Conclusion](#conclusion)

## Filters Overview

### Gaussian Filter
- **Description**: A Gaussian filter is a linear filter that smooths an image and reduces noise. It uses a Gaussian function to calculate the weights of neighboring pixels, giving more importance to pixels closer to the center.
- **Formula**: The 2D Gaussian function is given by:
  $$
  G(x, y) = \frac{1}{2\pi\sigma^2} e^{-\frac{x^2 + y^2}{2\sigma^2}}
  $$
- **Purpose**: Commonly used to blur images and remove detail and noise while preserving edges better than mean filters.
- **References**: 
  - "Image Processing and Analysis" by Tony Chan
  - [Gaussian Smoothing](https://homepages.inf.ed.ac.uk/rbf/HIPR2/gsmooth.htm) 

### Mean Filter
- **Description**: The mean filter replaces each pixel value with the average of itself and its neighbors within a defined area. It is one of the simplest linear filters.
- **Formula**: For a 3x3 mean filter:
  $$
  h[i,j] = \frac{1}{9} \sum_{k=-1}^{1} \sum_{l=-1}^{1} f[i+k,j+l]
  $$
- **Purpose**: Used primarily to reduce noise, including Gaussian noise, in images.
- **References**:
  - [Mean Filter Overview](https://bioimagebook.github.io/chapters/2-processing/4-filters/filters.html) 

### Linear Filter
- **Description**: A linear filter replaces each pixel with a linear combination of its neighbors. This is done using a kernel that defines the weights for each pixel.
- **Formula**: General form for linear filtering:
  $$
  h[i,j] = \sum_{k} \sum_{l} f[i+k,j+l] \cdot w[k,l]
  $$
- **Purpose**: Effective for various image processing tasks, including smoothing and noise reduction.
- **References**:
  - "Machine Vision" by R. C. Gonzalez 

### Average Filter
- **Description**: Similar to the mean filter, the average filter computes the average of pixel values in a neighborhood.
- **Formula**: For an $$N \times N$$ average filter:
  $$
  h[i,j] = \frac{1}{N^2} \sum_{k=0}^{N-1} \sum_{l=0}^{N-1} f[i+k,j+l]
  $$
- **Purpose**: Primarily used for smoothing images and reducing noise.
- **References**:
  - "Digital Image Processing" by Rafael C. Gonzalez and Richard E. Woods

## Conclusion

These filters are fundamental tools in image processing, widely used for enhancing image quality by reducing noise and improving visual clarity. Each implementation can be adapted for specific applications based on the requirements of the task at hand.

Feel free to explore the code and adapt it for your own projects!
