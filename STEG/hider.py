from stegano import lsb



secret = lsb.hide('image.png', '1928371732817')
secret.save('changed.png')