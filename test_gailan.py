import unittest
import requests


class MyTestCase(unittest.TestCase):
    # 概览-概览基础数据
    def test_gl001(self):
        url = "https://api.yuyidata.com:20242/gateway-test/datacenter/v1/overview/basic"
        params = {
            "companyId": "418",
            "startTime": "2021-08-14 00:00:00",
            "endTime": "2021-08-14 23:59:59"
        }
        headers = {
            'YuYi-Token': "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJiMzJlNTZlNC0yNTRiLTQxYzEtOWJiOS1hNWVhMjNiNWM0ZDQiLCJpYXQiOjE2Mjg5MjMzNjAsImV4cCI6MTYyOTUyODE2MCwicmVhbE5hbWUiOiJ5dXlpcWEiLCJjb21wYW55X2lkIjo0MTgsImFjdGlvbkNvZGUiOltdLCJ1c2VyVHlwZSI6MSwidXNlcklkIjo4NTc3NTQ2MzkxMDQzNTIyNTYsInVzZXJuYW1lIjoieXV5aXFhIn0.6GpneERwpUuwJFVyH3gL9v1D-jtUIA1pbUpelt-2_2cMjpAsLiHVfTmUqAleCrhI6q-oJ8WrYhXbNGQk1cNbjg"
        }
        response = requests.request("GET", url, headers=headers, params=params)
        print(response.json())
        assert response.json()["code"] == 200

    # 概览-数据分布
    def test_gl002(self):
        url = "https://api.yuyidata.com:20242/gateway-test/datacenter/v1/overview/distribution-overview"
        params = {
            "companyId": "418",
            "startTime": "2021-08-14 00:00:00",
            "endTime": "2021-08-14 23:59:59"
        }
        headers = {
            "YuYi-Token": "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJiMzJlNTZlNC0yNTRiLTQxYzEtOWJiOS1hNWVhMjNiNWM0ZDQiLCJpYXQiOjE2Mjg5MjMzNjAsImV4cCI6MTYyOTUyODE2MCwicmVhbE5hbWUiOiJ5dXlpcWEiLCJjb21wYW55X2lkIjo0MTgsImFjdGlvbkNvZGUiOltdLCJ1c2VyVHlwZSI6MSwidXNlcklkIjo4NTc3NTQ2MzkxMDQzNTIyNTYsInVzZXJuYW1lIjoieXV5aXFhIn0.6GpneERwpUuwJFVyH3gL9v1D-jtUIA1pbUpelt-2_2cMjpAsLiHVfTmUqAleCrhI6q-oJ8WrYhXbNGQk1cNbjg"
        }
        response = requests.request("GET", url, params=params, headers=headers)
        print(response.json())
        assert response.json()["code"] == 200

    # 概览-生命周期监控
    def test_gl003(self):
        url = "https://api.yuyidata.com:20242/gateway-test/datacenter/v1/overview/lifecycle-monitor"
        params = {
            "companyId": "418",
            "startTime": "2021-08-14 00:00:00",
            "endTime": "2021-08-14 23:59:59"
        }
        headers = {
            "YuYi-Token": "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJiMzJlNTZlNC0yNTRiLTQxYzEtOWJiOS1hNWVhMjNiNWM0ZDQiLCJpYXQiOjE2Mjg5MjMzNjAsImV4cCI6MTYyOTUyODE2MCwicmVhbE5hbWUiOiJ5dXlpcWEiLCJjb21wYW55X2lkIjo0MTgsImFjdGlvbkNvZGUiOltdLCJ1c2VyVHlwZSI6MSwidXNlcklkIjo4NTc3NTQ2MzkxMDQzNTIyNTYsInVzZXJuYW1lIjoieXV5aXFhIn0.6GpneERwpUuwJFVyH3gL9v1D-jtUIA1pbUpelt-2_2cMjpAsLiHVfTmUqAleCrhI6q-oJ8WrYhXbNGQk1cNbjg"
        }
        response = requests.request("GET", url, params=params, headers=headers)
        print(response.json())
        assert response.json()["code"] == 200

    # 概览-趋势总览每日数据
    def test_gl004(self):
        url = "https://api.yuyidata.com:20242/gateway-test/datacenter/v1/overview/trend-overview"
        params = {
            "companyId": "418",
            "startTime": "2021-08-14 00:00:00",
            "endTime": "2021-08-14 23:59:59"
        }
        headers = {
            "YuYi-Token": "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJiMzJlNTZlNC0yNTRiLTQxYzEtOWJiOS1hNWVhMjNiNWM0ZDQiLCJpYXQiOjE2Mjg5MjMzNjAsImV4cCI6MTYyOTUyODE2MCwicmVhbE5hbWUiOiJ5dXlpcWEiLCJjb21wYW55X2lkIjo0MTgsImFjdGlvbkNvZGUiOltdLCJ1c2VyVHlwZSI6MSwidXNlcklkIjo4NTc3NTQ2MzkxMDQzNTIyNTYsInVzZXJuYW1lIjoieXV5aXFhIn0.6GpneERwpUuwJFVyH3gL9v1D-jtUIA1pbUpelt-2_2cMjpAsLiHVfTmUqAleCrhI6q-oJ8WrYhXbNGQk1cNbjg"
        }
        response = requests.request("GET", url, params=params, headers=headers)
        print(response.json())
        assert response.json()["code"] == 200

    # 概览-特别关注
    def test_gl005(self):
        url = "https://api.yuyidata.com:20242/gateway-test/datacenter/v1/overview/special-attention"
        params = {
            "companyId": "418",
            "startTime": "2021-08-14 00:00:00",
            "endTime": "2021-08-14 23:59:59"
        }
        headers = {
            "YuYi-Token": "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJiMzJlNTZlNC0yNTRiLTQxYzEtOWJiOS1hNWVhMjNiNWM0ZDQiLCJpYXQiOjE2Mjg5MjMzNjAsImV4cCI6MTYyOTUyODE2MCwicmVhbE5hbWUiOiJ5dXlpcWEiLCJjb21wYW55X2lkIjo0MTgsImFjdGlvbkNvZGUiOltdLCJ1c2VyVHlwZSI6MSwidXNlcklkIjo4NTc3NTQ2MzkxMDQzNTIyNTYsInVzZXJuYW1lIjoieXV5aXFhIn0.6GpneERwpUuwJFVyH3gL9v1D-jtUIA1pbUpelt-2_2cMjpAsLiHVfTmUqAleCrhI6q-oJ8WrYhXbNGQk1cNbjg"
        }
        response = requests.request("GET", url, params=params, headers=headers)
        print(response.json())
        assert response.json()["code"] == 200

    # 概览-复检排行
    def test_gl006(self):
        url = "https://api.yuyidata.com:20242/gateway-test/datacenter/v1/overview/review-rank"
        params = {
            "companyId": "418",
            "startTime": "2021-08-14 00:00:00",
            "endTime": "2021-08-14 23:59:59"
        }
        headers = {
            "YuYi-Token": "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJiMzJlNTZlNC0yNTRiLTQxYzEtOWJiOS1hNWVhMjNiNWM0ZDQiLCJpYXQiOjE2Mjg5MjMzNjAsImV4cCI6MTYyOTUyODE2MCwicmVhbE5hbWUiOiJ5dXlpcWEiLCJjb21wYW55X2lkIjo0MTgsImFjdGlvbkNvZGUiOltdLCJ1c2VyVHlwZSI6MSwidXNlcklkIjo4NTc3NTQ2MzkxMDQzNTIyNTYsInVzZXJuYW1lIjoieXV5aXFhIn0.6GpneERwpUuwJFVyH3gL9v1D-jtUIA1pbUpelt-2_2cMjpAsLiHVfTmUqAleCrhI6q-oJ8WrYhXbNGQk1cNbjg"
        }
        response = requests.request("GET", url, params=params, headers=headers)
        print(response.json())
        assert response.json()["code"] == 200

    # -概览-规则告警
    def test_gl007(self):
        url = "https://api.yuyidata.com:20242/gateway-test/datacenter/v1/overview/rule-alarm"
        params = {
            "companyId": "418",
            "startTime": "2021-08-14 00:00:00",
            "endTime": "2021-08-14 23:59:59"
        }
        headers = {
            'Connection': "keep-alive",
            'Pragma': "no-cache",
            'Cache-Control': "no-cache",
            'Accept': "application/json, text/plain, */*",
            'YuYi-Token': "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJiMzJlNTZlNC0yNTRiLTQxYzEtOWJiOS1hNWVhMjNiNWM0ZDQiLCJpYXQiOjE2Mjg5MjMzNjAsImV4cCI6MTYyOTUyODE2MCwicmVhbE5hbWUiOiJ5dXlpcWEiLCJjb21wYW55X2lkIjo0MTgsImFjdGlvbkNvZGUiOltdLCJ1c2VyVHlwZSI6MSwidXNlcklkIjo4NTc3NTQ2MzkxMDQzNTIyNTYsInVzZXJuYW1lIjoieXV5aXFhIn0.6GpneERwpUuwJFVyH3gL9v1D-jtUIA1pbUpelt-2_2cMjpAsLiHVfTmUqAleCrhI6q-oJ8WrYhXbNGQk1cNbjg",
            'sec-ch-ua-mobile': "?0",
            'companyId': "418",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            'Origin': "https://beta-usight.yuyidata.com",
            'Sec-Fetch-Site': "same-site",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Dest': "empty",
            'Referer': "https://beta-usight.yuyidata.com/",
            'Accept-Language': "zh-CN,zh;q=0.9",
        }
        response = requests.request("GET", url, params=params, headers=headers)
        print(response.json())
        assert response.json()["code"] == 200

    # 概览-关键词告警
    def test_gl008(self):
        url = "https://api.yuyidata.com:20242/gateway-test/datacenter/v1/overview/keyword-alarm"
        params = {
            "companyId": "418",
            "startTime": "2021-08-14 00:00:00",
            "endTime": "2021-08-14 23:59:59"
        }
        headers = {
            'Connection': "keep-alive",
            'Pragma': "no-cache",
            'Cache-Control': "no-cache",
            'YuYi-Token': "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJiMzJlNTZlNC0yNTRiLTQxYzEtOWJiOS1hNWVhMjNiNWM0ZDQiLCJpYXQiOjE2Mjg5MjMzNjAsImV4cCI6MTYyOTUyODE2MCwicmVhbE5hbWUiOiJ5dXlpcWEiLCJjb21wYW55X2lkIjo0MTgsImFjdGlvbkNvZGUiOltdLCJ1c2VyVHlwZSI6MSwidXNlcklkIjo4NTc3NTQ2MzkxMDQzNTIyNTYsInVzZXJuYW1lIjoieXV5aXFhIn0.6GpneERwpUuwJFVyH3gL9v1D-jtUIA1pbUpelt-2_2cMjpAsLiHVfTmUqAleCrhI6q-oJ8WrYhXbNGQk1cNbjg",
            'sec-ch-ua-mobile': "?0",
            'companyId': "418",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            'Origin': "https://beta-usight.yuyidata.com",
            'Sec-Fetch-Site': "same-site",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Dest': "empty",
            'Referer': "https://beta-usight.yuyidata.com/",
            'Accept-Language': "zh-CN,zh;q=0.9",
        }
        response = requests.request("GET", url, params=params, headers=headers)
        print(response.json())
        assert response.json()["code"] == 200

    # 概览-情绪告警
    def test_gl009(self):
        url = "https://api.yuyidata.com:20242/gateway-test/datacenter/v1/overview/emotion-alarm"
        params = {
            "companyId": "418",
            "startTime": "2021-08-14 00:00:00",
            "endTime": "2021-08-14 23:59:59"
        }
        headers = {
            'Connection': "keep-alive",
            'Pragma': "no-cache",
            'Cache-Control': "no-cache",
            'YuYi-Token': "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJiMzJlNTZlNC0yNTRiLTQxYzEtOWJiOS1hNWVhMjNiNWM0ZDQiLCJpYXQiOjE2Mjg5MjMzNjAsImV4cCI6MTYyOTUyODE2MCwicmVhbE5hbWUiOiJ5dXlpcWEiLCJjb21wYW55X2lkIjo0MTgsImFjdGlvbkNvZGUiOltdLCJ1c2VyVHlwZSI6MSwidXNlcklkIjo4NTc3NTQ2MzkxMDQzNTIyNTYsInVzZXJuYW1lIjoieXV5aXFhIn0.6GpneERwpUuwJFVyH3gL9v1D-jtUIA1pbUpelt-2_2cMjpAsLiHVfTmUqAleCrhI6q-oJ8WrYhXbNGQk1cNbjg",
            'sec-ch-ua-mobile': "?0",
            'companyId': "418",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            'Origin': "https://beta-usight.yuyidata.com",
            'Sec-Fetch-Site': "same-site",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Dest': "empty",
            'Referer': "https://beta-usight.yuyidata.com/",
            'Accept-Language': "zh-CN,zh;q=0.9",
        }
        response = requests.request("GET", url, params=params, headers=headers)
        print(response.json())
        assert response.json()["code"] == 200

    # 概览-自定义标签
    def test_gl010(self):
        url = "https://api.yuyidata.com:20242/gateway-test/datacenter/v1/overview/customized-label"
        params = {
            "companyId": "418",
            "startTime": "2021-08-14 00:00:00",
            "endTime": "2021-08-14 23:59:59"
        }
        headers = {
            "Content-Type": "application/json",
            "YuYi-Token": "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJiMzJlNTZlNC0yNTRiLTQxYzEtOWJiOS1hNWVhMjNiNWM0ZDQiLCJpYXQiOjE2Mjg5MjMzNjAsImV4cCI6MTYyOTUyODE2MCwicmVhbE5hbWUiOiJ5dXlpcWEiLCJjb21wYW55X2lkIjo0MTgsImFjdGlvbkNvZGUiOltdLCJ1c2VyVHlwZSI6MSwidXNlcklkIjo4NTc3NTQ2MzkxMDQzNTIyNTYsInVzZXJuYW1lIjoieXV5aXFhIn0.6GpneERwpUuwJFVyH3gL9v1D-jtUIA1pbUpelt-2_2cMjpAsLiHVfTmUqAleCrhI6q-oJ8WrYhXbNGQk1cNbjg"
        }
        response = requests.request("GET", url, params=params, headers=headers)
        print(response.json())
        assert response.json()["code"] == 200

    # 概览-场景意图
    def test_gl011(self):
        url = "https://api.yuyidata.com:20242/gateway-test/datacenter/v1/overview/scene-intention"
        params = {
            "companyId": "418",
            "startTime": "2021-08-14 00:00:00",
            "endTime": "2021-08-14 23:59:59"
        }
        headers = {
            "Content-Type": "application/json",
            "YuYi-Token": "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJiMzJlNTZlNC0yNTRiLTQxYzEtOWJiOS1hNWVhMjNiNWM0ZDQiLCJpYXQiOjE2Mjg5MjMzNjAsImV4cCI6MTYyOTUyODE2MCwicmVhbE5hbWUiOiJ5dXlpcWEiLCJjb21wYW55X2lkIjo0MTgsImFjdGlvbkNvZGUiOltdLCJ1c2VyVHlwZSI6MSwidXNlcklkIjo4NTc3NTQ2MzkxMDQzNTIyNTYsInVzZXJuYW1lIjoieXV5aXFhIn0.6GpneERwpUuwJFVyH3gL9v1D-jtUIA1pbUpelt-2_2cMjpAsLiHVfTmUqAleCrhI6q-oJ8WrYhXbNGQk1cNbjg"
        }
        response = requests.request("GET", url, params=params, headers=headers)
        print(response.json())
        assert response.json()["code"] == 200


if __name__ == '__main__':
    unittest.main()
