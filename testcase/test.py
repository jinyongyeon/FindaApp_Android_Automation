import subprocess
import re

# SMS 데이터를 가져오는 ADB 명령 실행
command = "adb shell content query --uri content://sms/inbox"
sms_data = subprocess.check_output(command, shell=True).decode("utf-8")

# SMS 데이터 파싱 및 필터링
sms_messages = sms_data.strip().split("\n\n")  # 각 SMS 메시지는 빈 줄로 구분

# address=027081007로 필터링된 메시지 찾기
filtered_messages = [msg for msg in sms_messages if "address=027081007" in msg]

# 필터링된 메시지 중에서 첫 번째 메시지에서 인증번호 추출 (정규 표현식 사용)
if filtered_messages:
    first_message = filtered_messages[0]
    match = re.search(r'인증번호\[(\d+)\]', first_message)
    if match:
        authentication_code = match.group(1)
    else:
        print("첫 번째 메시지에서 인증번호를 찾을 수 없습니다.")
else:
    print("address=027081007로 필터링된 메시지가 없습니다.")