import requests
import json

from config.info import InFo

# 웹훅 들어갈 주소
info = InFo()
# slack_webhook_url = info.slack_webhook_url


class SlackWebHook:

    # 로그인 테스트 결과
    def join_send_slack_webhook(data):
        headers = {
            'Content-type': 'application/json'
        }

        data = {
            'text': "\n\n\n*1.[AOS]회원가입 테스트 결과*\n\n\n" + data
        }

        res = requests.post(info.slack_webhook_url, headers=headers, data=json.dumps(data))

        if res.status_code == 200:
            return 'ok'
        else:
            return 'error'

    def my_home_send_slack_webhook(data):
        headers = {
            'Content-type': 'application/json'
        }

        data = {
            'text': "\n\n\n*2.[AOS]마이홈 테스트 결과*\n\n\n" + data
        }

        res = requests.post(info.slack_webhook_url, headers=headers, data=json.dumps(data))

        if res.status_code == 200:
            return 'ok'
        else:
            return 'error'

    # 더보기 테스트 결과
    def more_send_slack_webhook(data):
        headers = {
            'Content-type': 'application/json'
        }

        data = {
            'text': "\n\n\n*3.[AOS]더보기 테스트 결과*\n\n\n" + data
        }

        res = requests.post(info.slack_webhook_url, headers=headers, data=json.dumps(data))

        if res.status_code == 200:
            return 'ok'
        else:
            return 'error'

    # 비교대출+오토론 테스트 결과
    def auto_loan_send_slack_webhook(data):
        headers = {
            'Content-type': 'application/json'
        }

        data = {
            'text': "\n\n\n*4.[AOS]비교대출+오토론 테스트 결과*\n\n\n" + data
        }

        res = requests.post(info.slack_webhook_url, headers=headers, data=json.dumps(data))

        if res.status_code == 200:
            return 'ok'
        else:
            return 'error'

