from stegano import lsb

secret_file_path = input("Enter the name of the image you want to decode: ")
secret_text = lsb.reveal(secret_file_path)
print(secret_text)
