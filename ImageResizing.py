import os
from glob import glob
from logging import getLogger, StreamHandler, DEBUG
from PIL import Image

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False


class ImageResizing:
    def __init__(self, directry, width, height):

        # フォルダパスから全てのファイルを取得
        files = glob(directry)
        logger.debug(f"以下のファイルのサイズを変更します{files}")

        # フォルダパス内の画像ファイルを設定した変更サイズにすべて変更
        for f in files:
            title, ext = os.path.splitext(f)
            if ext in ['.jpg', '.JPG', '.png', '.PNG', '.gif', '.GIF']:
                img = Image.open(f)
                img_resize = img.resize((width, height))
                img_resize.save(title + ext)
        logger.debug("変更終了")


if __name__ == "__main__":
    ImageResizing(directry='images/*', width=3000, height=2001)