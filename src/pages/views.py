from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import scrapy


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello world</h1>")
    my_context = {
        "name": "Hao Ping",
        "age": 23,
        "skill": ["Java", "Python", "C++"],
        "fact": True
    }

    return render(request, "home.html", my_context)


def course_view(request, *args, **kwargs):
    name = "course"
    start_urls = ["https://stackoverflow.com/questions?sort=votes"]

    return render(request, "course.html", {})


def parse(self, response):
    for href in response.css('.question-summary h3 a::attr(href)'):
        full_url = response.urljoin(href.extract())
        yield scrapy.Request(full_url, callback=self.parse_question)


def parse_qustion(self, response):
    yield {
        'title': response.css('h1 a::text').extract()[0],
        'votes': response.css(".question .vote-count-post::text").extract()[0],
        'body': response.css(".question .post-text").extract()[0],
        'tags': response.css('.question .post-tag::text').extract(),
        'link': response.url,
    }


def plan_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello world</h1>")
    return render(request, "plan.html", {})
