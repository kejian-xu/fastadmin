import base64
import random
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageFilter


class EasyCaptcha:
    __key_code = ''
    def __init__(self, width, height, code_num=4, code_type=1, font_size=24, is_blur=False, font='Arial.ttf',
                 x_offset=None, y_offset=None):
        """
        :param width: 验证码图片宽度
        :param height: 验证码图片高度
        :param code_num: 验证码字符个数 默认是4个
        :param key_code: 验证码
        :param code_type: 验证码类型  1字母或数字 2全字母 alpha 3全数字 digit
        :param font_size: 验证码字体尺寸
        :param is_blur: 验证码图片是否模糊处理
        :param font: 字体全路径  例如 '/Library/Fonts/Arial.ttf'
        :param x_offset: 验证码字符水平偏移量 默认自动计算
        :param y_offset: 验证码字符垂直偏移量 默认自动计算
        """
        self.width = width
        self.height = height
        self.code_num = code_num
        self.code_type = code_type
        self.font_size = font_size
        self.is_blur = is_blur
        self.x_offset = x_offset
        self.y_offset = y_offset

    def save_image(self, image_path, image_type='png'):
        image = self._get_captcha_image()
        image.save(image_path, image_type)

    def get_base64_image(self, image_type='png'):
        io_obj = BytesIO()
        image = self._get_captcha_image()
        image.save(io_obj, image_type)
        byte_data = io_obj.getvalue()
        base64_str = 'data:image/' + image_type + ';base64,' + base64.b64encode(byte_data).decode('utf-8')
        return base64_str
    
    def get_key_code(self):
        return self.__key_code

    def _get_captcha_image(self):
        image = Image.new('RGB', (self.width, self.height), (255, 255, 255))
        # 创建Font对象:
        font = ImageFont.truetype('Arial.ttf', self.font_size)
        # 创建Draw对象:
        draw = ImageDraw.Draw(image)
        # 填充每个像素:
        for x in range(self.width):
            for y in range(self.height):
                draw.point((x, y), fill=self._get_img_color())
        xw = self.width // self.code_num
        x_offset = self.x_offset if self.x_offset else ((self.width - self.code_num * self.font_size - (
                    self.code_num - 1) * (xw - self.font_size)) // 2) + (xw - self.font_size) // 3
        y_offset = self.y_offset if self.y_offset else (self.height - self.font_size) // 2
        # 输出文字:
        for t in range(self.code_num):
            str = self._get_random_code()
            self.__key_code += str
            draw.text((xw * t + x_offset, y_offset), str, fill=self._get_font_color(), font=font)
        # 模糊:
        if self.is_blur:
            image = image.filter(ImageFilter.BLUR)
        return image

    def _get_random_code(self):
        if self.code_type == 1:
            return self._get_alpha_digit()
        elif self.code_type == 2:
            return self._get_alpha()
        elif self.code_type == 3:
            return self._get_digit()
        return self._get_alpha_digit()

    def _get_alpha_digit(self):
        return random.choice([self._get_alpha(), self._get_digit()])

    def _get_alpha(self):
        return random.choice([chr(random.randint(65, 90)), chr(random.randint(97, 122))])

    def _get_digit(self):
        return str(random.randint(0, 9))

    def _get_img_color(self):
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

    def _get_font_color(self):
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))