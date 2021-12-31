import numpy as np



def cross_correlate(x, kernel=[1, 1, 1], padding='same'):
    
    """Computes cross-correlation between `x` and `kernel`.
    
    :param x: An array-like of real numbers
    :type x: array-like
    
    :param kernel: An array-like of real numbers to be used as kernel, defaults to [1, 1, 1]
    :type kernel: array-like
    
    :param padding: Defines if padding should be aaplied; values: 'same', 'valid'; 
        if 'valid', no padding is applied, defaults to 'same'
    :type padding: str

    :return: Cross-correlated result
    :rtype: list
    """
    
    result = []
    
    x = np.array(x)
    
    if padding == 'same':
        x = np.pad(x, 1)
        
    n_cols = len(x)
    kernel_size = len(kernel)
        
    for i in range(len(x) - kernel_size + 1):
        result.append(np.sum(x[i : i+kernel_size] * kernel))
        
    return result
        