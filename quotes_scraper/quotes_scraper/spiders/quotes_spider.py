import scrapy
import time


class WasteAISpider(scrapy.Spider):
    name = "waste_ai"
    start_urls = ["https://worldmetrics.org/ai-in-the-waste-industry-statistics/"]

    def parse(self, response):

        stats = response.css("ul li p::text").getall()


        stats = [s.strip() for s in stats if s.strip()]


        yield {
            "ai_waste_statistics": "\n".join(stats),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
