from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
import gspread

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'
# Escribe aquí el ID de tu documento:
SPREADSHEET_ID = '1NiiceNHdvZxlXNjgpC3k_droC_S4Mh5xbS-lMqGktCw'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

'''service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Llamada a la api
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='A1').execute()
# Extraemos values del resultado
values = result.get('values',[])
print(values)'''

gc = gspread.service_account(KEY)

sh=gc.open_by_key(SPREADSHEET_ID)