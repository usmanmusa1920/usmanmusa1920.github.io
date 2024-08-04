# -*- coding: utf-8 -*-
import os
import kyaah
import random
from datetime import datetime
from account.models import (
	Messages,
	Search,
	Metrix,
	Visitors)
from blog.models import (
	Category,
	Comment,
	Reply)


def integrate_mail(sender_name, sender_email, text_body, what=None, _url_=None):
	"""Kyaah mail functionality here! the `what` should be either `comment` or `reply` """
	
	receiver = []
	fetch_addr = os.environ.get('GMAIL_ADDRESS_RECEIVER')
	receiver.append(fetch_addr)
	
	if what == None:
		subjct = f'An email sent through personal website - {sender_name}'
		txt_body = f'Hi! Usman,\n\n{text_body}\n\nSender details:\n\tName: {sender_name}\n\tEmail: {sender_email}'
	else:
		subjct = f'A {what} email sent through personal website - {sender_name}'
		txt_body = f'Hi! Usman,\n\n{text_body}\n\nMail details:\n\tName: {sender_name}\n\tEmail: {sender_email}\n\t{what}_url: {_url_}'

	payload = dict(
		sender = 'GMAIL_ADDRESS',
		receiver = receiver,
		subject = subjct,
		body = txt_body,
		password = 'GMAIL_APP_PWD',
		env = True
	)

	kyaah.send(credentials=payload)

	
def general_context():
	"""This `general_context` function, is mainly created so that it can be use (access) in any page, for example the year that will show in the footer, it is not only for one page it is for all pages in the site, so by using this function we can access it in any page instead of creating `the_year` variable in each view.

	Like-wise the category list in the menu bar also it is not for one page and possibly for other variables ==> [the_year, category, comment, reply, search, message].

	Also for the notification of new recent comment, reply, search, or message
	that will show on the menu bar button (in the header).
	"""

	# some import, be wise 🤔 with circular import error
	# from *.* import *

	# queries (datas)
	the_year = datetime.utcnow().year
	category = Category.objects.all().order_by('title')
	comment = Comment.objects.filter(is_read=False).order_by('-timestamp')
	reply = Reply.objects.filter(is_read=False).order_by('-timestamp')
	search = Search.objects.filter(is_seen=False).order_by('-timestamp')
	message = Messages.objects.filter(is_read=False).order_by('-timestamp')
	new_visitors = Visitors.objects.filter(is_seen=False).order_by('-timestamp')
	month_visit = Metrix.objects.all().last()

	rand_1 = False
	rand_2 = False

	try:
		rand_1 = random.choice(Category.objects.all())
		rand_2 = random.choice(Category.objects.all())

		# try another choice for a category if the two match
		if rand_1 == rand_2:
			rand_2 = random.choice(Category.objects.all())
	except:
		pass

	# general context for any pages, using a naming convention of `gen_con_*` for any of the dictionary key down below, but the values naming convention doesn`t matter.
	data = {
		'gen_con_the_year': the_year,
		'gen_con_category': category,
		'gen_con_comment': comment,
		'gen_con_reply': reply,
		'gen_con_search': search,
		'gen_con_message': message,
		'gen_con_new_visitors': new_visitors,
		'gen_con_month_visit': month_visit,
		'gen_con_rand_1': rand_1,
		'gen_con_rand_2': rand_2,
	}
	return data


def blog_url_processed(get_blog):
	"""This class view method is for parsing links of an article, and a post.

	------------------ *** METHOD 1 *** USING LOOP APPEND & TRY BLOCK ------------------
		>>> urls_to_parse = str([('Google', 'www.google.com'), ('Apple', 'www.apple.com'), ('IBM', 'www.ibm.com')])
		>>> unwanted_character = ['(', ')', '\'', '[', ']']
		>>> removed_unwanted = []
		>>> try:
		...	 for i in urls_to_parse:
		...		 if i in unwanted_character:
		...			 continue
		...		 else:
		...			 removed_unwanted.append(i)
		...	 joining_list = ''.join(removed_unwanted)
		...
		...	 url_value = []
		...	 url_name = []
		...	 for idx, i in enumerate(joining_list.split(',')):
		...		 if (idx + 1) % 2 == 0:
		...			 url_name.append(i.strip())
		...		 else:
		...			 url_value.append(i.strip())
		...
		...	 real_url = {url_value[i] : url_name[i] for i in range(len(url_value))}
		...	 print('The url dict is', real_url)
		... except:
		...	 real_url = []
		...	 print('The url dict is empty')
		... 
		The url dict is {'Google': 'www.google.com', 'Apple': 'www.apple.com', 'IBM': 'www.ibm.com'}
		...
		>>> real_url
		{'Google': 'www.google.com', 'Apple': 'www.apple.com', 'IBM': 'www.ibm.com'}
	------------------ *** METHOD 2 *** USING NAIVE SOLUTION ------------------
		>>> urls_to_parse = ['Google', 'Apple', 'IBM']
		>>> value = ['www.google.com', 'www.apple.com', 'www.ibm.com']
		>>> url_dict = {}
		>>> for k in urls_to_parse:
		...	 for j in value:
		...		 url_dict[k] = j
		...		 value.remove(j)
		...		 break
		... 
		>>> url_dict
		{'Google': 'www.google.com', 'Apple': 'www.apple.com', 'IBM': 'www.ibm.com'}
	------------------ *** METHOD 3 *** USING A DICT COMPREHENSION ------------------
		>>> urls_to_parse = ['Google', 'Apple', 'IBM']
		>>> value = ['www.google.com', 'www.apple.com', 'www.ibm.com']
		>>> url_dict = {urls_to_parse[i] : value[i] for i in range(len(urls_to_parse))}
		>>> url_dict
		{'Google': 'www.google.com', 'Apple': 'www.apple.com', 'IBM': 'www.ibm.com'}
	------------------ *** METHOD 4 *** USING THE BUILT-IN `ZIP` FUNCTION ------------------
		>>> urls_to_parse = ['Google', 'Apple', 'IBM']
		>>> value = ['www.google.com', 'www.apple.com', 'www.ibm.com']
		>>> dict(zip(urls_to_parse, value))
		{'Google': 'www.google.com', 'Apple': 'www.apple.com', 'IBM': 'www.ibm.com'}
	------------------ *** METHOD 5 *** USING BUILT-IN `MAP` FUNCTION ------------------
		>>> urls_to_parse = ['Google', 'Apple', 'IBM']
		>>> value = ['www.google.com', 'www.apple.com', 'www.ibm.com']
		>>> dict(map(lambda k, v : (k, v), urls_to_parse, value))
		{'Google': 'www.google.com', 'Apple': 'www.apple.com', 'IBM': 'www.ibm.com'}
	"""
	
	# convert `blog_urls` into string
	blog_str = str(get_blog.url_list)
	
	# characters we will remove in the url list, if found
	unwanted_character = ['(', ')', '\'', '[', ']']

	# list containing `blog_str` after removing `unwanted_character`
	removed_unwanted = []
	
	try:
		for i in blog_str:
			# escaping a data if found in `unwanted_character` list by continue
			if i in unwanted_character:
				continue
			else:
				# appending a data if not found in `unwanted_character` to `removed_unwanted`
				removed_unwanted.append(i)

		# list containing url name e.g ['Google', 'Apple', 'IBM']
		url_value = []

		# list containing url, url e.g ['https://www.google.com', 'https://www.apple.com', https://www.ibm.com']
		url_name = []
		
		# joining the `removed_unwanted` list
		joining_list = ''.join(removed_unwanted)
		
		# doing a for loop to split with `,` (make a list) of the `joining_list`
		for idx, i in enumerate(joining_list.split(',')):
			if (idx + 1) % 2 == 0:
				url_name.append(i.strip())
			else:
				url_value.append(i.strip())

		# makiing a dictionary of the `url_name` as key, and `url_value` as value using set comprehension (METHOD 2), but the following method can be use also
		real_url = {url_value[i] : url_name[i] for i in range(len(url_value))}
	except:
		real_url = []
	return real_url


class Viz:
	"""Viz class"""

	@staticmethod
	def vizFun():
		"""vizFun"""

		# checking if `Metrix` table is empty, then it will create one to avoid error
		if len(Metrix.objects.all()) == 0:
			first_metrix = Metrix()
			first_metrix.save()

		# checking to see if the current month matches the month of our last metrix, and current year if it matches the year of our last metrix, if both matches, it will not create new metrix table, else it will
		if Metrix.objects.all().last().timestamp.month == datetime.utcnow().month and Metrix.objects.all().last().timestamp.year == datetime.utcnow().year:
			pass
		else:
			# create new metrix if the above condition is false
			new_month_metrix = Metrix()
			new_month_metrix.save()

		# incrementing the last metrix `visit_num` in `Metrix` table of our database
		last_metrix = Metrix.objects.all().last()
		last_metrix.visit_num += 1
		last_metrix.save()
		
		# adding new visitor into our database
		viz = Visitors()
		viz.metrix = last_metrix
		viz.save()
