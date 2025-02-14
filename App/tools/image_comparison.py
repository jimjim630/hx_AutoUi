from PIL import Image, ImageDraw
import numpy as np
from scipy.ndimage import label as ndi_label
from scipy.ndimage import morphology  # 用于形态学操作，合并相邻区域

def compare_images(image1_path, image2_path):
    """
    比较两张APP截图的差异点，并将差异区域在第二张图片内体现出来，
    使用红色矩形框标记差异区域，对小区域进行合并使其不过于细碎

    :param image1_path: 第一张截图的路径
    :param image2_path: 第二张截图的路径
    :return: 返回标记了差异区域的第二张图片（使用相对简洁的红色矩形框标记各个差异区域大致范围）
    """
    # 打开两张图片并转换为RGB模式（确保色彩模式一致便于对比）
    img1 = Image.open(image1_path).convert('RGB')
    img2 = Image.open(image2_path).convert('RGB')

    # 获取图片尺寸，若尺寸不一致则调整为相同尺寸（以第一张图片尺寸为准）
    width1, height1 = img1.size
    width2, height2 = img2.size
    if width1!= width2 or height1!= height2:
        img2 = img2.resize((width1, height1))

    # 将图片转换为numpy数组，方便进行像素级的计算
    img1_array = np.array(img1)
    img2_array = np.array(img2)

    # 计算两张图片每个像素点的差值
    diff_array = np.abs(img1_array - img2_array)
    # 判断差值是否大于一定阈值（这里设为30，可根据实际情况调整），生成差异掩码
    threshold = 200
    diff_mask = np.any(diff_array > threshold, axis=2)

    # 进行形态学操作，先腐蚀再膨胀，可去除小的孤立差异点并合并相邻区域
    structuring_element = np.ones((3, 3), dtype=np.uint8)
    processed_mask = morphology.binary_opening(diff_mask, structuring_element)
    processed_mask = morphology.binary_closing(processed_mask, structuring_element)

    # 获取用于在第二张图片上绘图的对象
    draw = ImageDraw.Draw(img2)

    # 使用scipy的ndi_label函数标记连通的差异区域，每个区域有一个唯一的标签
    labeled_mask, num_features = ndi_label(processed_mask)

    for label in range(1, num_features + 1):  # 遍历每个连通区域（标签从1开始）
        # 获取当前连通区域的像素坐标
        coords = np.column_stack(np.where(labeled_mask == label))
        if len(coords) > 0:
            min_y, min_x = coords.min(axis=0)
            max_y, max_x = coords.max(axis=0)

            # 绘制红色矩形框标记当前差异区域大致范围
            draw.rectangle([min_x, min_y, max_x + 1, max_y + 1], outline="red", width=2)

    return img2

if __name__ == "__main__":

    # 定义两张APP截图的路径，替换为实际的图片路径
    image1_path = "Xnip2024-12-14_16-13-54.png"
    image2_path = "Xnip2024-12-14_16-13-59.png"
    result_image = compare_images(image1_path, image2_path)
    result_image.show()
