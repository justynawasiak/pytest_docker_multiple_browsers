import requests
import time
import pytest


def check_status():
    for _ in range(60):
        try:
            result = requests.get('http://selenium:4444/wd/hub/status')
            if result.status_code < 300:
                if result.json()['value']['ready']:
                    return True
        except:
            pass
        time.sleep(1)
    return False


if __name__ == '__main__':
    browsers = ['firefox', 'chrome']
    for browser in browsers:
        if check_status():
            print('Hub running')
            exit(pytest.main(['-v', '--junitxml=results/report.xml']))
        else:
            print("Waiting for hub timed out")


