from voxelamming import BuildBox

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# BuildBoxクラスのインスタンスを生成します
build_box = BuildBox(room_name)
build_box.set_box_size(0.1)
build_box.set_build_interval(0.01)
build_box.set_command('liteRender')

# 三角形の辺の長さ
side_length = 200

def sierpinski_triangle(x, y, z, length, level):
    """
    シェルピンスキーの三角形を描画する関数

    Args:
        x (int): 三角形の頂点のx座標
        y (int): 三角形の頂点のy座標
        z (int): 三角形の頂点のz座標
        length (int): 三角形の辺の長さ
        level (int): 再帰レベル
    """
    if level == 0:
        # 三角形の3つの頂点の座標を計算
        p1 = [x, y, z]
        p2 = [x + length, y, z]
        p3 = [x + length / 2, y + length * 0.866, z] # 0.866は√3/2

        # 三角形の3辺を描画
        build_box.draw_line(*p1, *p2, 1, 0, 0)
        build_box.draw_line(*p2, *p3, 1, 0, 0)
        build_box.draw_line(*p3, *p1, 1, 0, 0)
        return

    # 再帰的にシェルピンスキーの三角形を描画
    half_length = length / 2
    sierpinski_triangle(x, y, z, half_length, level - 1)  # 左下の三角形
    sierpinski_triangle(x + half_length, y, z, half_length, level - 1)  # 右下の三角形
    sierpinski_triangle(x + half_length / 2, y + half_length * 0.866, z, half_length, level - 1)  # 上の三角形

# シェルピンスキーの三角形を描画
sierpinski_triangle(0, 0, 0, side_length, 6)

build_box.send_data("sierpinski_triangle")