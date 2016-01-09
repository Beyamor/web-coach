import urllib2, re, random
from flask import render_template

def define(app):
	@app.route("/mario")
	def mario():	
	    url = "https://supermariomakerbookmark.nintendo.net/profile/ColtonPhillips"	
	    data = urllib2.urlopen(url).read()
	    courses = re.findall('href="/courses/(.*?)"',data , re.DOTALL)
	    names = re.findall('<div class="course-title">(.*?)</div>',data , re.DOTALL)
	    return render_template("mario.html", levels=zip(courses, names))
