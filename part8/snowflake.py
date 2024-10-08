from voxelamming import Voxelamming

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# Voxelammingクラスのインスタンスを生成します
vox = Voxelamming(room_name)
vox.set_box_size(0.2)
vox.set_build_interval(0.01)
vox.set_command('liteRender')

# 雪の結晶の枝の長さ
branch_length = 30
# 枝分かれ角度
angle = 60


def snowflake_branch(length, level):
    if level == 0:
        return

    vox.push_matrix()
    vox.draw_line(0, 0, 0, 0, length, 0, 1, 1, 1)

    length *= 0.8
    vox.transform(0, length, 0, 0, 0, -angle)
    snowflake_branch(length, level - 1)

    vox.transform(0, length, 0, 0, 0, 0)
    snowflake_branch(length, level - 1)

    vox.transform(0, length, 0, 0, 0, angle)
    snowflake_branch(length, level - 1)

    vox.pop_matrix()


# 雪の結晶を描画
for i in range(6):
    vox.push_matrix()
    vox.transform(0, 0, 0, 0, 0, 60 * i)
    snowflake_branch(branch_length, 4)
    vox.pop_matrix()

vox.transform(0, branch_length * 2, 0, 0, 0, 0)
vox.send_data("snowflake")
