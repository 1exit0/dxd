import requests

api_url = 'https://console.melipayamak.com/api/send/otp/05e90a0904544586a8e81bf31f8ca965'
username = '09121067554'
password = 'Ap12345Ap@'
sender_number = 'YOUR_SENDER_NUMBER'
recipient_number = 'RECIPIENT_PHONE_NUMBER'  # شماره گیرنده
otp_code = '12345'  # کد تایید مورد نظر

headers = {
    'Content-Type': 'application/json',
    'x-sms-ir-secure-token': 'YOUR_SECURE_TOKEN'  # این بخش برای برخی سرویس‌ها ممکن است نیاز باشد
}

data = {
    'username': username,
    'password': password,
    'to': recipient_number,
    'from': sender_number,
    'text': f'Your verification code is: {otp_code}'
}

response = requests.post(api_url, json=data, headers=headers)

if response.status_code == 200:
    print("پیام با موفقیت ارسال شد.")
else:
    print("مشکلی در ارسال پیام به وجود آمد.")
    print(response.text)
