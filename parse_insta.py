from bs4 import BeautifulSoup as bs
from time import sleep, time
import os, fake_useragent, datetime, requests

def request(url, head=None):
    r = requests.get(url, headers=head)
    return r

def delete_file(filename):
    os.remove(filename)

def write_file(file_name):
    file_format = file_name.split('/')[-1].split('?')[0].split('.')[-1]
    created_name = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    full_name = f"{created_name}.{file_format}"
    with open(full_name, 'wb') as file:
        file.write(request(file_name).content)
    return full_name  

def get_meta_tag(response):
    soup = bs(response.text, 'html.parser')
    if soup.find_all('meta', {'property':'og:video'}):
       return soup.find_all('meta', {'property':'og:video'})
    else:
       return soup.find_all('meta', {'property':'og:image'})

def main(link):
    fake_headers = fake_useragent.UserAgent().random
    head = {'user-agent': fake_headers}
    response = request(link, head)
    metaTag = get_meta_tag(response)
    file_name = write_file(metaTag[0]["content"])
    return file_name

if __name__ == '__main__':
    main()
