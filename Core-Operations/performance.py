x = 5

%timeit y=x**2
171 ns ± 0.611 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

%timeit y=x*x
32.1 ns ± 0.0559 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

z = np.uint8([5])

%timeit y=z*z
410 ns ± 3.21 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%timeit y=np.square(z)
397 ns ± 4.67 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%timeit z = np.count_nonzero(img)
8.57 ms ± 63.7 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
