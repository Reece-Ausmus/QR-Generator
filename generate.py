import qrcode

def generate(data):
    # Create the QR code object
    qr = qrcode.QRCode(
        version=1,  # QR version: controls the size, choose 1-40 (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # Error correction level (L, M, Q, H)
        box_size=10,  # Size of each box in pixels
        border=4,  # Border size (4 is the default and recommended)
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Generate the QR code as an image
    img = qr.make_image(fill="black", back_color="white")

    # Save the image
    img.save("basic_qr_code.png")


if __name__ == "__main__":
    # Data to encode
    data = input("Enter the data to encode in the QR code: ")

    # Generate the QR code
    generate(data)