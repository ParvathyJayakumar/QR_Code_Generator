import qrcode

def generate_qr_code(data, filename="qrcode.png"):
    # Create QR Code object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Border thickness
    )
    # Add data to the QR Code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Generate the image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}")

if __name__ == "__main__":
    # Ask the user for input
    text = input("Enter the text or URL to generate QR code: ")
    file_name = input("Enter the file name (default: qrcode.png): ") or "qrcode.png"
    generate_qr_code(text, file_name)
