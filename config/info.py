class InFo:
    # 필수 입력 값
    devices = "" # 디바이스 id 입력
    name = ""   # 홍길동
    rrn_a = ""  # 880101
    rrn_b = "" # 주민번호 뒤에 첫자리 1,2,3,4 등
    loan_rrn = "" # 주민번호 뒤에 7자리
    autoloan_rrn = "" # 주민번호 뒤에 첫자리를 제외한 6자리
    rrnfull = "" #주민번호 13자리
    phone_number = "" #전화번호 - 제외 하고 01000000000
    news_agency = "KT" # 통신사 정보 (KT,LGU+,SKT,KT알뜰폰,등등)

    # 미입력 영역
    user_id = []
    usertoken = []
    txseqno = []
    idtoken = []
    loans_data = []
    loans_data_b = []
    loans_data_c = []
    loans_data_d = []
    credit_score = []
    autoNo = "323다4004" #자동차번호 공백없이


    #슬랙 웹훅 결과 보고 URL (슬렉 url 설정하면 해당 url로 결과 전송됨)
    slack_webhook_url = 'https://hooks.slack.com/services/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'
    # slack_webhook_url = 'https://hooks.slack.com/services/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'




