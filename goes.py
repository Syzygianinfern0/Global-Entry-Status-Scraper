import requests
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Check status of passport application')
    parser.add_argument('--arn', help='Application Reference Number', required=True)

    return parser.parse_args()

def main():
    args = parse_args()
    arn = args.arn

    cookies = {
        "cookiesession1": "678A3E0D147C113DC5FDA20ADB91D268",
        "JSESSIONID": "0000lVEKQ2FBLuf4mmNELtMsp_R:1cpjkoq1h",
    }

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "DNT": "1",
        "Origin": "https://portal3.passportindia.gov.in",
        "Referer": "https://portal3.passportindia.gov.in/Online/user/authStatus",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
    }

    data = {
        "applnName": "AppOnlineMissionProject",
    }

    response = requests.post(
        "https://portal3.passportindia.gov.in/Online/secure/loginAction",
        cookies=cookies,
        headers=headers,
        data=data,
    )

    ltpa = response.cookies.get_dict()["LtpaToken2"]

    cookies["LtpaToken2"] = ltpa

    params = {
        "timestamp": "1723758910754",
    }

    json_data = {
        "appRefNo": f"{arn}",
    }

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "DNT": "1",
        "Origin": "https://portal3.passportindia.gov.in",
        "Referer": "https://portal3.passportindia.gov.in/Online/secure/loginAction",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "content-type": "application/json",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
    }

    response = requests.post(
        "https://portal3.passportindia.gov.in/Online/secure/trackStatusForFilledApplication",
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    response = response.json()
    updates = [f'{each["LAST_MODIFIED_DATE"][:-9]}: {each["EMP_ACTION"].strip()}' for each in response["statusIdMap"]]
    for update in updates:
        print(update)


if __name__ == '__main__':
    main()

