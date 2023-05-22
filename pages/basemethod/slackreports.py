import reports as reports
import requests
import json


# 웹훅 들어갈 주소

slack_webhook_url = 'https://hooks.slack.com/services/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'


class SlackWebHook:


    # 로그인 테스트 결과
    def join_SendSlackWebHook(data):
        headers = {
            'Content-type': 'application/json'
        }

        data = {
            'text': "*2.[AOS]더보기 테스트 결과*\n\n\n" + data
        }

        res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))

        if res.status_code == 200:
            return 'ok'
        else:
            return 'error'

    # 더보기 테스트 결과
    def more_SendSlackWebHook(data):
        headers = {
            'Content-type': 'application/json'
        }

        data = {
            'text': "*2.[AOS]더보기 테스트 결과*\n\n\n" + data
        }

        res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))

        if res.status_code == 200:
            return 'ok'
        else:
            return 'error'


