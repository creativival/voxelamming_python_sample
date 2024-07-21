# voxelammingパッケージからBuildBoxクラスをインポートします
from voxelamming import BuildBox


# 変数の設定
INITIAL_LENGTH = 10
REPEAT_COUNT = 5
ANGLE_TO_OPEN = 30
LENGTH_DECAY = 0.8
BRANCH_COLOR = [0.5, 0, 0]
LEAF_COLOR = [0, 0.5, 0]


# 色を計算する関数
def calculate_color(count):
    r1, g1, b1 = BRANCH_COLOR
    r2, g2, b2 = LEAF_COLOR
    r = r2 - (r2 - r1) * count / REPEAT_COUNT
    g = g2 - (g2 - g1) * count / REPEAT_COUNT
    b = b2 - (b2 - b1) * count / REPEAT_COUNT

    return r, g, b


# 三分木を描画する関数
def draw_three_branches(count, branch_length):
    count -= 1
    if count < 0:
        return

    # draw branches
    length = branch_length * LENGTH_DECAY
    color = calculate_color(count)

    print("push_matrix")
    build_box.push_matrix()

    # first branch
    build_box.translate(0, branch_length, 0, pitch=ANGLE_TO_OPEN, yaw=0, roll=0)
    build_box.draw_line(0, 0, 0, 0, length, 0, *color)
    draw_three_branches(count, length)

    # second branch
    build_box.translate(0, branch_length, 0, pitch=ANGLE_TO_OPEN, yaw=120, roll=0)
    build_box.draw_line(0, 0, 0, 0, length, 0, *color)
    draw_three_branches(count, length)

    # third branch
    build_box.translate(0, branch_length, 0, pitch=ANGLE_TO_OPEN, yaw=240, roll=0)
    build_box.draw_line(0, 0, 0, 0, length, 0, *color)
    draw_three_branches(count, length)

    print("pop_matrix")
    build_box.pop_matrix()


# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# BuildBoxクラスのインスタンスを生成します
build_box = BuildBox(room_name)
build_box.set_box_size(0.5)
build_box.set_build_interval(0.01)

build_box.change_shape("sphere")
build_box.set_command("float")
build_box.draw_line(0, 0, 0, 0, INITIAL_LENGTH, 0, *BRANCH_COLOR)

draw_three_branches(REPEAT_COUNT, INITIAL_LENGTH)
build_box.send_data("fractal_tree")
