# -*- coding: utf-8 -*-
from lxml import html
import scrapy
from exceptions import ValueError
from time import sleep

class Tutorial1Spider(scrapy.Spider):
    name = 'tutorial1'
    allowed_domains = ['www.kickstarter.com']
    start_urls = ['http://www.kickstarter.com/']

    def kickstrter_projects_parser(url):
    for i in range(5):
        try:
            headers = {
                        'User-Agent': 'Mozilla Firefox / 66.0.2 /'
            }
            print "Fetching :",url     
            response = requests.get(url, headers = headers,verify=False)
            formatted_response = response.content.replace('<!--', '').replace('-->', '')
            doc = html.fromstring(formatted_response)
            datafrom_xpath = doc.xpath('//code[@id="global-header-promo-top-bar-embed-id-content"]//text()')
            content_about = doc.xpath('//code[@id="global-header-about-section-embed-id-content"]')
            if not content_about:
                content_about = doc.xpath('//code[@id="global-header-footer-embed-id-content"]')
            if content_about:
                pass
                # json_text = content_about[0].html_content().replace('<code id="stream-footer-embed-id-content"><!--','').replace('<code id="stream-about-section-embed-id-content"><!--','').replace('--></code>','')
            
            if datafrom_xpath:
                try:
                    json_formatted_data = json.loads(datafrom_xpath[0])
                    project_title = json_formatted_data['projectTitle'] if 'projectTitle' in json_formatted_data.keys() else None
                    url = json_formatted_data['url'] if 'url' in json_formatted_data.keys() else None
                    short_description = json_formatted_data['shortDescription'] if 'shortDescription' in json_formatted_data.keys() else None
                    primary_image = json_formatted_data['primaryImage'] if 'primaryImage' in json_formatted_data.keys() else None
                    location = json_formatted_data['location'] if 'location' in json_formatted_data.keys() else None
                    tag = json_formatted_data['tag'] if 'tag' in json_formatted_data.keys() else None
                    raised_amount = json_formatted_data['raisedAmount'] if 'raisedAmount' in json_formatted_data.keys() else None
                    backers_count = json_formatted_data['backersCount'] if 'backersCount' in json_formatted_data.keys() else None
                    remaining_days = json_formatted_data['remainingDays'] if 'remainingDays' in json_formatted_data.keys() else None
                    percentage_of_completion = json_formatted_data['percentageOfCompletion'] if 'percentageOfCompletion' in      json_formatted_data.keys() else None
                    creator = json_formatted_data['creator'] if 'creator' in json_formatted_data.keys() else None




                    data = {
                                'project_title': project_title,
                                'url':  url ,
                                'short_description': short_description,
                                'primary_image': primary_image,
                                'location': location,
                                'tag': tag,
                                'raised_amount': raised_amount,
                                'backers_count': backers_count,
                                'remaining_days': remaining_days,
                                'percentage_of_completion': percentage_of_completion,
                                'creator': creator,
                            }
                    return data
                except:
                    print "cant parse page", url

            # Retry in case of captcha or login page redirection
            if len(response.content) < 2000 or "trk=login_reg_redirect" in url:
                if response.status_code == 404:
                    print "kickstarter page not found"
                else:
                    raise ValueError('redirecting to login page or captcha found')
        except :
            print "retrying :",url
 
def readurls():
    projecturls = ['https://www.kickstarter.com/discover/advanced?category_id=1']
    extracted_data = []
    for url in projecturls:
        ext.racted_data.append(cickstarter_projects_parser(url))
        f = open('data.json', 'w')
        js.on.dump(extracted_data, f, indent=4)
 
if __name__ == "__main__":
readurls()
