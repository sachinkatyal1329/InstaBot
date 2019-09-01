import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import random
import string

class Database:

	def __init__(self, gdoc_name):

		#initialize gdoc api with specific key from 'Data.json' JSON file
		scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
		creds = ServiceAccountCredentials.from_json_keyfile_name('Data.json', scope)
		client = gspread.authorize(creds)

		self.sheet = client.open(gdoc_name).sheet1



	def print_records(self):

		pp = pprint.PrettyPrinter()
		hackers = self.sheet.get_all_records()
		pp.pprint(hackers)


class FileHandler:

	def __init__(self, file_names, file_usernames):
		names = open(file_names, "r") 
		self.names_array = names.read().split(',')

		usernames = open(file_usernames, "r")
		self.usernames_array = usernames.read().split(',')

	def get_rand_name(self):
		ran_name = random.randint(0, len(self.names_array))
		return self.names_array[ran_name]

	def get_rand_username(self):
		ran_username = random.randint(0,len(self.usernames_array))
		return self.usernames_array[ran_username] + str(random.randint(0,10)) + str(random.randint(0,10)) + str(random.randint(0,10))

	def get_rand_password(self):
		chars = "".join( [random.choice(string.ascii_letters) for i in range(15)] )
		return chars


#file_ = FileHandler("names.txt")
#gdocdata@focus-ensign-205222.iam.gserviceaccount.com
'''
hackers = sheet.row_values(6)
hackers = sheet.col_values(6)
hackers = sheet.cell(6,11).value
sheet.update_cell(6,11, 'AL')
pp.pprint(hackers)

row = ["I'm", "updating", "a", "spreadsheet", "from", "Python"]
index = 3
sheet.insert_row(row, index)
sheet.delete_row(index)
'''