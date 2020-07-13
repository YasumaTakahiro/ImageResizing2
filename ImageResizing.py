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
    def __init__(self, directry, saveDirectry, width, height):
        # フォルダパスから全てのファイルを取得
        files = glob(f"{directry}/*")
        logger.debug(f"以下のファイルのサイズを変更します{files}")

        # フォルダパス内の画像ファイルをすべて指定のサイズにリサイズし、
        # 保存先フォルダに保存する
        for f in files:
            basename = os.path.basename(f)
            title, ext = os.path.splitext(basename)
            if ext in [".jpg", ".JPG", ".png", ".PNG", ".gif", ".GIF"]:
                img = Image.open(f)
                img_resize = img.resize((width, height))
                img_resize.save(f"{saveDirectry}/{basename}")

        logger.debug("変更終了")


if __name__ == "__main__":
    ImageResizing(directry=r"C:\Users\20191108-5\Documents\python_project\ImageResizing2\撮影",
                  saveDirectry=r"C:\Users\20191108-5\Documents\python_project\ImageResizing2\保存",
                  width=32, height=32)
