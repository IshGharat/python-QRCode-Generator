
import qrcode

def generate_qr_code(text,file_name):
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill_color="#0BDFFF",back_color="#3A3839")
    img.save(file_name)

#Input text to generate QR code for
text=input("\nEnter link or text: ")
#File name to save the QR code image
file_name="qr_code.png"
#Generate the QR code
generate_qr_code(text,file_name)
print(f"QR code saved as {file_name}")
