from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib, ssl

app = Flask(__name__)
CORS(app)

@app.route("/send_letter", methods=["POST"])
def send_letter():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    course = data.get("course")
    program = data.get("program")

    # Example admission letter content
    admission_text = f"""
    Dear {name},

    Congratulations! You have been admitted to Kigumo Technical and Vocational College.

    Course: {course}
    Program: {program}

    Please print this email as your provisional admission letter.

    Regards,
    Kigumo TVC
    """

    # Send email (configure with your email + app password)
    sender_email = "yourgmail@gmail.com"
    sender_password = "your_app_password"
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, admission_text)

        return jsonify({"message": f"✅ Admission letter sent to {email}."})
    except Exception as e:
        return jsonify({"message": f"❌ Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
