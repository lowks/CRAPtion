#coding: utf-8

from craption import settings, upload, utils
import opster
import shutil
import os

#@opster.command(name='dropbox-login', )
#def dropbox_login():
#    "Log in to dropbox"
#    settings.dropbox_login()
#
#@opster.command(name="clear-conf")
#def clear_conf():
#    "Rewrite noise and example config"
#    utils.install()
#
@opster.command()
def main(clear_conf=('c', False, 'Rewrite example config and noise'),
         dropbox_login=('d', False, 'Login to dropbox')):
    if dropbox_login:
        settings.dropbox_login()
        return
    if clear_conf:
        utils.install()
        return

    local_image = utils.screenshot()
    assert os.path.exists(local_image)
    filename = utils.get_filename()
    url = upload.upload(local_image, filename)
    print(url)
    utils.set_clipboard(url)
    conf = settings.get_conf()
    if conf['file']['keep']:
        dest = os.path.expanduser(os.path.join(conf['file']['dir'], filename))
        shutil.move(local_image, dest)
    else:
        os.unlink(local_image)
    utils.play_noise()

def dispatch():
    main.command()
