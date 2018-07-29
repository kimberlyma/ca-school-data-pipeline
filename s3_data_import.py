import boto3
import pandas as pd
from io import StringIO

s3 = boto3.client('s3')
bucket = 'personproject.b'


def s3_func(files):
	csv_obj = s3.get_object(Bucket=bucket, Key='cahsee2015.txt')
	body = csv_obj['Body']
	csv_string = body.read().decode('utf-8')
	df = pd.read_csv(StringIO(csv_string), sep = "\t")

	process_data(df)

#Percentage Passed ELA and Math
def filter_columns():
	return

#county + district + school
def create_id():
	return

def process_data(df):
	return

def main():
	s3_func('temp')


if __name__ == "__main__":
    main()
