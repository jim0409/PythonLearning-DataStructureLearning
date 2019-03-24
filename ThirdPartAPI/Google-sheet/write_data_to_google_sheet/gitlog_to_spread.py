import datetime
import sys
from subprocess import check_output

import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC

GDriveJSON = 'PythonUpload.json'
GSpreadSheet = 'TestGithubCommit'

path = 'cd /Users/jimweng/MlyticsRepo/'
execute_folder = 'mlytics-qa'
git_log = 'git log --pretty=format:"%h% -%d% %s (%ci) <%an>" --abbrev-commit|grep tag|tail -1'
execute_cmd = path+execute_folder+" && "+git_log

print(execute_cmd)

print('write data to', GSpreadSheet)
try:
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    key = SAC.from_json_keyfile_name(GDriveJSON, scope)
    gc = gspread.authorize(key)
    worksheet = gc.open(GSpreadSheet).sheet1
except Exception as ex:
    print('invalid to connect to server', ex)
    sys.exit(1)

add_line_array = check_output(execute_cmd, shell=True)

print(add_line_array)
if add_line_array == "":
    print("invalid input")

add_line_array = str(add_line_array)
worksheet.append_row([datetime.datetime.now().__str__(), add_line_array])
print('add new lines to', GSpreadSheet)
