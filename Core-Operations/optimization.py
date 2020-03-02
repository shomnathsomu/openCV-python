# check if optimization is enabled
cv2.useOptimized()
Out[21]: True

%timeit res = cv2.medianBlur(img,49)
154 ms ± 158 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)

# Disable it
In [7]: cv2.setUseOptimized(False)

In [8]: cv2.useOptimized()
Out[8]: False

%timeit res = cv2.medianBlur(img,49)
155 ms ± 1.74 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

