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
#hacemos la coneccion con google y las creddenciales
gc = gspread.service_account(KEY)
#abrimos el sheet por medio del id del link
sh = gc.open_by_key(SPREADSHEET_ID)
#seleccoianamos la tabla de trabajo
worksheet = sh.worksheet('Hoja 1')
#extraemos la informacion
list_of_lists=worksheet.get_values()
print(list_of_lists)