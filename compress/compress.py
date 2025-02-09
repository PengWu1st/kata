import os
from PIL import Image, ImageOps


def compress_images(input_folder, output_folder, scale_factor=0.50):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    compressed_count = 0  # 添加计数器
    total_size = 0  # 添加总大小计数器
    images = []  # 用于存储图片对象
    image_names = []  # 用于存储图片文件名（不带扩展名）

    # 收集所有图片文件名
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.jpeg') or filename.lower().endswith('.jpg'):
            image_names.append(filename)

    # 按名称排序
    image_names.sort(key=lambda x: int(x.split('.')[0][9:]))
    print(image_names)

    for filename in image_names:
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # 计算新的尺寸
        new_width = int(img.width * scale_factor)
        new_height = int(img.height * scale_factor)

        # 压缩图片
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # 保存压缩后的图片
        output_path = os.path.join(output_folder, filename)
        img.save(output_path, 'JPEG', quality=85)
        compressed_count += 1  # 更新计数器
        total_size += os.path.getsize(output_path)  # 更新总大小

        images.append(img.convert('RGB'))  # 添加图片对象到列表

    total_size_mb = total_size / (1024 * 1024)  # 将总大小转换为MB
    print(f"Number of images compressed: {compressed_count}")  # 打印压缩的图片数量
    print(f"Total size of compressed images: {
          total_size_mb:.2f} MB")  # 打印压缩图片的总大小（MB）

    if images:
        pdf_path = os.path.join(output_folder, 'compressed_images.pdf')
        images[0].save(pdf_path, save_all=True,
                       append_images=images[1:])  # 保存所有图片到一个PDF文件


input_folder = 'c'
output_folder = 'output'
compress_images(input_folder, output_folder)
