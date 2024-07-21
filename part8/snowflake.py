from voxelamming import BuildBox

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# BuildBoxクラスのインスタンスを生成します
build_box = BuildBox(room_name)
build_box.set_box_size(0.2)
build_box.set_build_interval(0.01)
build_box.set_command('liteRender')

# 雪の結晶の枝の長さ
branch_length = 30
# 枝分かれ角度
angle = 60

def snowflake_branch(length, level):
    if level == 0:
        return

    build_box.push_matrix()
    build_box.draw_line(0, 0, 0, 0, length, 0, 1, 1, 1)

    length *= 0.8
    build_box.translate(0, length, 0, 0, 0, -angle)
    snowflake_branch(length, level - 1)

    build_box.translate(0, length, 0, 0, 0, 0)
    snowflake_branch(length, level - 1)

    build_box.translate(0, length, 0, 0, 0, angle)
    snowflake_branch(length, level - 1)

    build_box.pop_matrix()

# 雪の結晶を描画
for i in range(6):
    build_box.push_matrix()
    build_box.translate(0, 0, 0, 0, 0, 60 * i)
    snowflake_branch(branch_length, 4)
    build_box.pop_matrix()

build_box.translate(0, branch_length * 2, 0, 0, 0, 0)
build_box.send_data("snowflake")