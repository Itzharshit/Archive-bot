from pony.orm import *
from pyrogram.types import Message
from os import listdir

# ========= DB build =========
db = Database()


class User(db.Entity):
    uid = PrimaryKey(int, auto=True)
    status = Required(int)  # status-user: "INSERT"/"NOT-INSERT"


db.bind(provider='sqlite', filename='zipbot.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


# ========= helping func =========
def dir_work(uid: int) -> str:
    """ static-user folder """
    return f"static/{uid}/"


def zip_work(uid: int) -> str:
    """ zip-archive file """
    return f'static/{uid}.zip'


def list_dir(uid: int) -> list:
    """ items in static-user folder """
    return listdir(dir_work(uid))


def up_progress(current, total, msg: Message):
    """ edit status-msg with progress of the uploading """
    msg.edit(f"**Upload progress: {current * 100 / total:.1f}%**")


# ========= MSG class =========
class Msg:

    def start(msg: Message) -> str:
        """ return start-message text """
        txt = f"Hii {msg.from_user.mention}!\n" \
              "\nI am file file zipper bot created by @pyrogrammers, i can convert multiple files into zip files." \
              "\nJust send /zip to get further instructions of zipping your files."
        return txt

    zip = "Now send me all the files that you want to archive, and when done send /done after all files Downloaded.\n" \
          "\n\nNote: due to TG upload limit, the total size of the files can't upto 2GB."
    too_big = "Note: due to TG upload limit, the total size of the file can't be greater than 2GB."
    too_much = "Note: the total number of the files can be upto 500"
    send_zip = "Send /zip to compress the files"
    zipping = "start compressing {} files..."
    uploading = "uploading archive..."
    unknow_error = "An unknown error occurred"
    downloading = "downloading your files..."
    zero_files = "Files not sent."
