import json
import qrcode
from flask import Flask, request, render_template, send_file

app = Flask(__name__)

# Define a route for the home page
@app.route("/")
def home():
    return render_template("home.html")

# Define a route for the QR code generation page
@app.route("/generate_qr_code", methods=["POST"])
def generate_qr_code():
    # Load user information from form data
    name = request.form["name"]
    email = request.form["email"]
    linkedin = request.form["linkedin"]
    instagram = request.form["instagram"]
    phone_number = request.form["phone"]
    user_info = {"name": name, "email": email, "linkedin": linkedin, "instagram": instagram, "phone_number": phone_number}
    print("User info:", user_info)

    # Create QR code data
    qr_data = ""
    for field in user_info.keys():
        if user_info[field]:
            qr_data += f"{user_info[field]}\n"
    print("QR data:", qr_data)

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(qr_data)
    qr.make(fit=True)
    print("QR code version:", qr.version)
    print("QR code box size:", qr.box_size)
    print("QR code border:", qr.border)

    # Save QR code as PNG file
    img = qr.make_image(fill_color="black", back_color="white")
    img_file = "qr_code.png"
    img.save(img_file)
    print("QR code saved as:", img_file)

    # Serve the QR code image file
    return send_file(img_file, mimetype="image/png")


if __name__ == "__main__":
    app.config["DEBUG"] = True
    app.run(debug=True)
