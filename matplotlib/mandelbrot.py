import matplotlib.pyplot as plt
import numpy as np


def mandelbrot(c, max_iter):
    """
    複素数cがマンデルブロ集合に属するか判定する関数

    Args:
        c (complex): 複素数
        max_iter (int): 最大反復回数

    Returns:
        int: cが発散するまでの反復回数
    """
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z ** 2 + c
        n += 1
    return n


# マンデルブロ集合を描画する範囲
width, height = 500, 500
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5
max_iter = 255

# 複素平面上の座標を生成
real, imag = np.meshgrid(np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height))
c = real + imag * 1j

# 各座標についてマンデルブロ集合に属するか判定
mandelbrot_set = np.array([mandelbrot(c, max_iter) for c in c.ravel()]).reshape((height, width))

# マンデルブロ集合を描画
plt.imshow(mandelbrot_set, extent=(x_min, x_max, y_min, y_max), cmap="hot")
plt.colorbar()
plt.title("Mandelbrot Set")
plt.show()
