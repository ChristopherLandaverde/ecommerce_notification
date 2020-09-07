import scrapy

from scrapy.mail import MailSender

class fray_fitness(scrapy.Spider):
    
    name ='Check what just became in stock!'
    
    start_urls =['https://www.frayfitness.com/230lb-fray-crumb-rubber-bumper-set.html']
    
    def parse(self,response):
        
        blue = response.xpath('//span[@class="in-stock"]/text()').extract()
        
        if not blue:
           self.logger.info('This is not in stock yet')
       
            
            
        else:
            mailer = MailSender(
                smptphost='christopherlandaverde@gmail.com',
                mailfrom='scrapy.send@gmail.com',
                smtpuser='scrapy.send@gmail.com',
                smtppas='Hankmoody9243!',
                smtpport=587
            )
        