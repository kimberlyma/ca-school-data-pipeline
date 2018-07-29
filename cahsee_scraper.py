from io import BytesIO
from bs4 import BeautifulSoup 
import requests
import zipfile
import re
import boto3



base = "https://cahsee.cde.ca.gov/"
cahsee_base_url = "https://cahsee.cde.ca.gov/datafiles.asp"
cahsee_page = requests.get(cahsee_base_url)
c = cahsee_page.content

soup = BeautifulSoup(c, 'html.parser')

s3 = boto3.client('s3')

for link in soup.findAll(href=re.compile("\.zip$")):
	file_name = link.get('href')
	handle = base + file_name

	r = requests.get(handle)	
	z = zipfile.ZipFile(BytesIO(r.content))

	zip_data = z.open(z.namelist()[0]) #only safe if you know the files in the zip
	value_name = file_name.split("/")[1][:10] + '.txt'	
	s3.upload_fileobj(zip_data, 'personproject.b', value_name)