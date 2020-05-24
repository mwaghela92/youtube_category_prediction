import pandas as pd 
import re
data_file = pd.read_csv('/data/Youtube Video Dataset.csv')
blank_list = [' ']* len(data_file)
data_file['blank_list'] = blank_list
data_file['total_text'] = data_file['Title'] + data_file['blank_list'] + data_file['Description']

for i in range(len(data_file['total_text'])):
	#if type(data_file['total_text'][i]) == 'str':
		#print(type(data_file['total_text'][i]))
	data_file.loc[i,'total_text'] = re.sub('[^a-zA-Z ]+', '', str(data_file.loc[i,'total_text'])).lower()

print(data_file['total_text'])
                             


