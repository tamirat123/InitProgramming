from stegano import lsb

secret_Incoded = input("Enter data to be encoded : ")


secret = lsb.hide('image.png', secret_Incoded)
secret.save('changed.png')
