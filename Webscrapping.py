import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
final = pd.DataFrame()

# url="https://www.amazon.in/PHILIPS-Fryer-NA130-00-Technology/dp/B0D14861L9/?_encoding=UTF8&pd_rd_w=aU6jF&content-id=amzn1.sym.6abece96-bed1-4bc5-91cd-40fd48c68e65&pf_rd_p=6abece96-bed1-4bc5-91cd-40fd48c68e65&pf_rd_r=4E74Q2AV1B82SQX1XY9G&pd_rd_wg=PvQXa&pd_rd_r=0af243e3-cac4-4dad-b462-52b94ef177ec&ref_=pd_hp_d_btf_ls_gwc_pc_en2_&th=1"
class ReviewExtractor:
    def __init__(self,url:str):
        self.url=url
        self.review_data=[]
        self.image_url=''
    
    def scrap(self):
        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
        webpage=requests.get(self.url,headers=header)
        soup=BeautifulSoup(webpage.content,features="lxml")
        reviews_section = soup.find("div", id="localTopReviews")
        blocks= reviews_section.find_all('div',{'data-hook':"reviewContainer"})
        image=soup.find('img',{'id':'landingImage'})
        image_url=image['src']
        for  block in blocks:
            # each block is now a bs4 element and now we can extract the text  from it
            review=block.find('div',{'data-hook':"reviewRichContentContainer"})
            name=block.find('span',{'class':"a-profile-name"})
            rating=block.find('span',{'class':'a-icon-alt'})
            self.review_data.append({'name':name.get_text(),'review':review.get_text(),'rating':rating.get_text()})
        return image_url, self.review_data