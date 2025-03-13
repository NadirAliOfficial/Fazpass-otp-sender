import requests
import json

def sendOTP(YOUR_PHONE_NUMBER):
    data = {
        "phone": YOUR_PHONE_NUMBER,
        "gateway_key": "f6bb7523-3210-46fa-8b2d-13c88a6eabbf"
    }

    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjo5ODY4fQ.wMV0iaP9cxMJPuvwU0BuYzO9u9pJz-UTcC0fr1idZXc",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            'https://api.fazpass.com/v1/otp/request',
            data=json.dumps(data),
            headers=headers
        )
        
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
        
        result = response.json()

        if result.get('status') == True:
            return 'OTP sent successfully!'
        else:
            return 'Error: ' + result.get('message', 'Something went wrong while requesting OTP.')
    except requests.exceptions.RequestException as e:
        return 'Error: ' + str(e)

# Example usage with phone number
YOUR_PHONE_NUMBER = "+923042019543"
   # Without country code based on the success response
response = sendOTP(YOUR_PHONE_NUMBER)
print(response)
