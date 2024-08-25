from voxelamming import Voxelamming

room_name = "1000"
vox = Voxelamming(room_name)

vox.set_box_size(0.5)
vox.set_build_interval(0.01)

step_num = 20
for i in range(step_num):  # 段数
    for j in range(i * 2 + 1):  # 各段のボクセル数
        vox.create_box(j - i, step_num - i, 0)  # x座標を調整して中央に配置

vox.send_data("pyramid")
