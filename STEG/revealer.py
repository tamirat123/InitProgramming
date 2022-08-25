from stegano import lsb


secret_text = lsb.reveal('changed.png')
print(secret_text)