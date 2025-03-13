# Fazpass OTP Sender

A Python script for sending OTPs using the Fazpass API with secure gateway key and token-based authentication.

---

## 🚀 Features
- Sends OTP to a provided phone number using the Fazpass API.
- Handles success and error responses effectively.
- Logs detailed responses for debugging.
- Easily configurable for other phone numbers or gateway keys.

---

## 📂 Project Structure
```
├── fazpass_otp.py    # Main script to send OTPs
└── README.md         # Documentation file
```

---

## ⚙️ Requirements
- Python 3.x
- `requests` library

### Install Dependencies
```bash
pip install requests
```

---

## 🔧 Setup
1. **Clone the Repository**
```bash
git clone https://github.com/NadirAliOfficial/Fazpass-otp-sender
cd fazpass-otp-sender
```

2. **Configure Your Phone Number and Credentials**
- Replace the `YOUR_PHONE_NUMBER` with the recipient's number.
- Replace the `gateway_key` and `Authorization` token if required.


---

## 📄 Usage

Run the script using:

```bash
python fazpass_otp.py
```

### Sample Output
```
Status Code: 200
Response Text: {"status":true,"message":"Request generated successfully","code":"2000200","data":{"id":"UUID","otp":"XXXXXX","otp_length":6,"channel":"WA Generic OTP","provider":"FAZPASS","purpose":"Development"}}

OTP sent successfully!
```

---

## ✅ Success Response
```json
{
  "status": true,
  "message": "Request generated successfully",
  "code": "2000200",
  "data": {
    "id": "5179e737-1525-41c1-b50f-db217e4f3189",
    "otp": "XXXXXX",
    "otp_length": 6,
    "channel": "WA Generic OTP",
    "provider": "FAZPASS",
    "purpose": "Development"
  }
}
```

---

## ⚠️ Error Handling
- The script prints detailed error messages in case of any failures.
- Common issues could be:
  - Invalid gateway key or token.
  - Incorrect phone number format.
  - Network or API errors.


---

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements.

---

## 📜 License
This project is licensed under the MIT License.

---

## 🔒 Security Notice
- Keep your API keys and tokens secure.
- Do not expose sensitive information in public repositories.

---

## 🙋‍♂️ Support
For any issues, please contact [Your Name] or open an issue in the repository.

