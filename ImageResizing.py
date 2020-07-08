import os
from glob import glob
from logging import getLogger, StreamHandler, DEBUG

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False
logger.debug('hello')


#aaahh
class GetPath:
    def __init__(self):
        # カレントディレクトを設定
        select_path = r"C:\Users\20191108-5\Documents\画像編集用".replace(os.path.sep, '/')
        os.chdir(select_path)
        logger.debug("現在のパスは{0}".format(os.getcwd()))
        # カレントディレクトリに存在する画像ファイルをリスト化する
        images = glob('*.gif') + glob('*.GIF') + glob('*png') + glob('*PNG') + glob('*jpg') + glob('*JPG') + glob(
            '*jpeg') + glob('*JPEG')
        logger.debug(images)


getpath = GetPath()

print("aaa")
print("aaa")