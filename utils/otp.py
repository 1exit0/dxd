import pyotp
from datetime import datetime, timedelta


def sendOTP(request):
    totp = pyotp.TOTP(pyotp.random_base32(), interval=60)
    otp = totp.new()
    request.session['otp_secret_key'] = totp.secret
    valid_date = datetime.now() + timedelta(minutes=1)
    request.session['otp_valid_date'] = str(valid_date)

    print(f'کد تایید:{otp} /n ورود به سایت فروشگاه چی هر چی')
