import segno

encode = input("Enter the link or text you would like to encode: ")
file = input("Enter the file name (must end in .png): ")
color = input("Enter the color of the QR code: ")
size = input("Enter the size (1-5): ")

qr_code = segno.make_qr(encode)
qr_code.save(
    file,
    light = color,
    scale = size,
    )