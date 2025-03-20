'''
Write a function that implements a "median" image filter. The function takes an input and an output image buffer, a width and a height, and a parameter called "kernel width", or k for short.
You may assume k is odd and greater than zero.
The function must write every output pixel. Each output pixel is the median of a square of k-by-k input image values, centered at the corresponding location in the input image.
The definition for median is, given an odd number of values, it is the middle value when sorted, or if there are an even number of values, it is the average of the middle two values.
You can assume you have a sort function, you do not have to write one.
'''
