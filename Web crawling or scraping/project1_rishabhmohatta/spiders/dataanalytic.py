import scrapy
from project1_rishabhmohatta.items import memberitem
from scrapy.loader import ItemLoader


class memberdetails(scrapy.Spider):
    name = 'dataanalytic'
    start_urls = ['http://www.naukri.com/jobs-in-delhi-ncr/']


    def parse(self,response):
        member_list = response.css('div.row')


        for member in member_list:
            member_loader = ItemLoader(memberitem(),selector = member)


            member_loader.add_css('job_title','span.content>ul>li::text')
            member_loader.add_css('experience','span.exp::text')
            member_loader.add_css('location','span.loc>span::text')
            member_loader.add_css('company_name','span.org::text')
            member_loader.add_css('job_description_link','div.row::attr(data-url)')
            member_loader.add_css('keyskills','span.skill::text')
            member_loader.add_css('jdescp','span.desc::text')
            member_loader.add_css('salary','span.salary::text')

            yield member_loader.load_item()


           
                
    
