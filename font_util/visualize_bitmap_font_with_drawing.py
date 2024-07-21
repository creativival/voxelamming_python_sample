from PIL import Image, ImageDraw


def visualize_bitmap_font_with_drawing(csv_data_list, dot_size=10, dot_color="red"):
    """
    CSVデータのリストからビットマップフォントを描画で可視化する関数

    Args:
        csv_data_list (list): CSVデータのリスト (各要素は1行のCSVデータ)
        dot_size (int): ドットのサイズ (ピクセル)
        dot_color (str): ドットの色

    Returns:
        Image: ビットマップフォントの可視化結果 (Pillow Imageオブジェクト)
    """

    images = []  # 各文字の画像を格納するリスト
    for csv_data in csv_data_list:
        data = csv_data.split(",")
        _, character, *bitmap_data = data

        binary_data = [bin(int(x, 16))[2:].zfill(16) for x in bitmap_data]

        # キャンバスの作成
        canvas_size = (len(binary_data[0]) * dot_size, len(binary_data) * dot_size)
        canvas = Image.new("RGB", canvas_size, "white")
        draw = ImageDraw.Draw(canvas)

        # ドットの描画
        # for y, row in enumerate(binary_data):
        #     for x, bit in enumerate(row):
        #         if bit == "1":
        #             draw.rectangle(
        #                 [
        #                     (x * dot_size, y * dot_size),
        #                     ((x + 1) * dot_size, (y + 1) * dot_size),
        #                 ],
        #                 fill=dot_color,
        #             )

        for y, row in enumerate(binary_data):
            for x, bit in enumerate(row):
                # ドットの描画 (1ピクセル分縮小)
                draw.rectangle(
                    [(x * dot_size, y * dot_size), ((x + 1) * dot_size - 1, (y + 1) * dot_size - 1)],
                    fill=dot_color if bit == "1" else "white",  # bitが"1"なら赤、そうでなければ白
                )
                # 黒い線の描画 (右端と下端に線を追加)
                draw.line([(x * dot_size + dot_size - 1, y * dot_size), (x * dot_size + dot_size - 1, y * dot_size + dot_size - 1)], fill="black", width=1)
                draw.line([(x * dot_size, y * dot_size + dot_size - 1), (x * dot_size + dot_size - 1, y * dot_size + dot_size - 1)], fill="black", width=1)

        images.append(canvas)  # 文字の画像をリストに追加

    # 横方向に結合した画像を作成
    total_width = sum(image.width for image in images)
    combined_image = Image.new("RGB", (total_width, images[0].height), "white")

    x_offset = 0
    for image in images:
        combined_image.paste(image, (x_offset, 0))
        x_offset += image.width

    return combined_image


if __name__ == "__main__":
    # CSVデータ
    csv_data_list = [
        "9250,あ,0200,0200,0260,1f80,0200,0240,03f0,0448,0c44,1482,2482,2302,2504,1818,0060,0000",
        # "9252,い,0000,0000,0000,1000,1010,1008,2004,2004,2002,2002,2002,1202,1200,0c00,0000,0000",
        # "9254,う,0300,00c0,0000,0000,03e0,1c10,0008,0008,0008,0010,0010,0020,0040,0180,0600,0000",
        # "9256,え,0200,0100,00c0,0000,0ff0,0020,0040,0080,0100,0380,0440,0840,1040,2020,001c,0000",
        # "9258,お,0200,0200,0218,03c4,3e02,0201,0200,03e0,0e18,1204,2204,2204,2408,1830,00c0,0000",
    ]

    # ビットマップフォントを描画で可視化
    image = visualize_bitmap_font_with_drawing(csv_data_list)
    image.save("bitmap_font_visualization_drawing2.png")  # 画像を保存
