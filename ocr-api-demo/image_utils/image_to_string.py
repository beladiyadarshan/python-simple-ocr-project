import pytesseract
from image_utils.segment import get_lines

# not working
config_str = (
            r'-c tessedit_char_whitelist=" 0123456789'
            r'abcdefghijklmnopqrstuvwxyz'
            r'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            r':.,/|()-" '
            r'-c preserve_interword_spaces=1 '
            )


def from_image_to_string(img_list):
    """
    extracts text from the list of images
    applies tesseract on entire image without any preprocessing
    """
    text_list = []
    for img in img_list:
        text = str(pytesseract.image_to_string(img, lang='eng'))
        text = text.replace('-\n', '')
        text_list.append(text)
    text = "\n".join(text_list)
    return text


def from_lines_to_string(img_list):
    """
    converts the list of images into lines and extracts text from lines
    """
    text_list = []
    for img in img_list:
        lines = get_lines(img)
        for line in lines:
            text = str(pytesseract.image_to_string(line, lang='eng'))
            text = text.replace('-\n', '')
            text_list.append(text)
    text = "\n".join(text_list)
    return text