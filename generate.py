import qrcode
import argparse

def generate(args):
    data = args.data

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
    # Parse the input
    parser = argparse.ArgumentParser(description="Generate a QR code")
    parser.add_argument("data", type=str, help="Data to encode in the QR code")
    parser.add_argument("-o", metavar="output_file", help="Output file name")
    args = parser.parse_args()
    
    # Generate the QR code
    generate(args)