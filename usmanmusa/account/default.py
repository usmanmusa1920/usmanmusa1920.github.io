import random
from datetime import datetime
from account.models import Messages, Search, Metrix, Visitors
from blog.models import Category, Post, Comment, Reply


class Default:
  
  @staticmethod
  def default():
    """
      it is mainly created so that it can be use (access) in any page,
      for example the year that will show in the footer
      it is not only for one page it is for all pages in the site
      
      so by using this class method we can access it in any page
      instead of creating `the_year` variable in each view
      
      like so the category list in the menu bar also it is not for one page
      and possibly for other variables ==> [the_year, category, comment, reply, search, message]
      
      Also for the notification of new recent comment, reply, search, or message
      that will show on the menu bar button (in the header)
    """
    the_year = datetime.utcnow().year
    category = Category.objects.all().order_by('title')
    comment = Comment.objects.filter(is_read=False).order_by('-timestamp')
    reply = Reply.objects.filter(is_read=False).order_by('-timestamp')
    search = Search.objects.filter(is_seen=False).order_by('-timestamp')
    message = Messages.objects.filter(is_read=False).order_by('-timestamp')
    new_visitors = Visitors.objects.filter(is_seen=False).order_by('-timestamp')
    month_visit = Metrix.objects.all().last()
    
    try:
      # for category
      for _ in  range(Category.objects.all().count()):
        rand_1 = random.choice(Category.objects.all())
        rand_2 = random.choice(Category.objects.all())
        break
      
      # for posts
      for _ in  range(Category.objects.all().count()):
        rand_post_1 = random.choice(Post.objects.all())
        rand_post_2 = random.choice(Post.objects.all())
        break
      
      data = {
        'the_year': the_year,
        'category': category,
        'comment': comment,
        'reply': reply,
        'search': search,
        'message': message,
        'new_visitors': new_visitors,
        'month_visit': month_visit,
        'rand_1': rand_1,
        'rand_2': rand_2,
        'rand_post_1': rand_post_1,
        'rand_post_2': rand_post_2
      }
    except:
      data = {
        'the_year': the_year,
        # 'category': None,
        'comment': comment,
        'reply': reply,
        'search': search,
        'message': message,
        'new_visitors': new_visitors,
        'month_visit': month_visit,
      }
    
    return data
  
  
  @staticmethod
  def blog_url_processed(get_blog):
    """
      this class view method is for parsing links of an article,
      and a post
    """
    blog_str = str(get_blog.url_list) # convert `blog_urls` into string
    
    # characters we will remove in the url list, if found
    unwanted_character = ['(', ')', '\'', '[', ']']
    removed_unwanted = [] # list containing `blog_str` after removing `unwanted_character`
    
    try:
      for i in blog_str:
        
        """escaping a data if found in `unwanted_character` list by continue"""
        if i in unwanted_character:
          continue
        else:
          """appending a data if not found in `unwanted_character` to `removed_unwanted`"""
          removed_unwanted.append(i)
          
      url_value = [] # list containing url name e.g ['Google', 'Apple', 'IBM']
      url_name = [] # list containing url, url e.g ['https://www.google.com', 'https://www.apple.com', https://www.ibm.com']
      
      joining_list = ''.join(removed_unwanted) # joining the `removed_unwanted` list
      
      # doing a for loop to split with `,` (make a list) of the `joining_list`
      for idx, i in enumerate(joining_list.split(',')):
        if (idx + 1) % 2 == 0:
          url_name.append(i.strip())
        else:
          url_value.append(i.strip())
          
      """
        makiing a dictionary of the `url_name` as key, and `url_value` as value
        using set comprehension (METHOD 2), but the following method can be use also
      """
      real_url = {url_value[i] : url_name[i] for i in range(len(url_value))}
      print('MY DICT:', real_url)
    except:
      real_url = []
      
      
    """
        >>> article_str = str([('Google', 'www.google.com'), ('Apple', 'www.apple.com'), ('IBM', 'www.ibm.com')])
        >>> unwanted_character = ['(', ')', '\'', '[', ']']
        >>> removed_unwanted = []
        >>> try:
        ...   for i in article_str:
        ...     if i in unwanted_character:
        ...       continue
        ...     else:
        ...       removed_unwanted.append(i)
        ...   joining_list = ''.join(removed_unwanted)
        ...
        ...   url_value = []
        ...   url_name = []
        ...   for idx, i in enumerate(joining_list.split(',')):
        ...     if (idx + 1) % 2 == 0:
        ...       url_name.append(i.strip())
        ...     else:
        ...       url_value.append(i.strip())
        ...
        ...   real_url = {url_value[i] : url_name[i] for i in range(len(url_value))}
        ...   print('The url dict is', real_url)
        ... except:
        ...   real_url = []
        ...   print('The url dict is empty')
        ... 
        The url dict is {'Google': 'www.google.com', 'Apple': 'www.apple.com', 'IBM': 'www.ibm.com'}
        ...
        >>> real_url
        {'Google': 'www.google.com', 'Apple': 'www.apple.com', 'IBM': 'www.ibm.com'}
        --------------------------------------------------------------------------------------
        
        
        
        #    #  ######   #####  #    #   ####   #####
        ##  ##  #          #    #    #  #    #  #    #
        # ## #  #####      #    ######  #    #  #    #
        #    #  #          #    #    #  #    #  #    #
        #    #  #          #    #    #  #    #  #    #
        #    #  ######     #    #    #   ####   #####
        
          #
         ##
        # #
          #
          #
          #
        #####
        --------------------- USING NAIVE SOLUTION ---------------------
        >>> name = ['Google', 'Apple', 'IBM']
        >>> value = [' www.google.com', ' www.apple.com', ' www.ibm.com']
        >>> url_dict = {}
        >>> for k in name:
        ...   for j in value:
        ...     url_dict[k] = j
        ...     value.remove(j)
        ...     break
        ... 
        >>> url_dict
        {'Google': ' www.google.com', 'Apple': ' www.apple.com', 'IBM': ' www.ibm.com'}
        
        
        
        #    #  ######   #####  #    #   ####   #####
        ##  ##  #          #    #    #  #    #  #    #
        # ## #  #####      #    ######  #    #  #    #
        #    #  #          #    #    #  #    #  #    #
        #    #  #          #    #    #  #    #  #    #
        #    #  ######     #    #    #   ####   #####
        
        #####
        #     #
              #
        #####
        #
        #
        #######
        --------------------- OR USING A DICT COMPREHENSION ---------------------
        >>> name = ['Google', 'Apple', 'IBM']
        >>> value = [' www.google.com', ' www.apple.com', ' www.ibm.com']
        >>> url_dict = {name[i] : value[i] for i in range(len(name))}
        >>> url_dict
        {'Google': ' www.google.com', 'Apple': ' www.apple.com', 'IBM': ' www.ibm.com'}
        
        
        
        #    #  ######   #####  #    #   ####   #####
        ##  ##  #          #    #    #  #    #  #    #
        # ## #  #####      #    ######  #    #  #    #
        #    #  #          #    #    #  #    #  #    #
        #    #  #          #    #    #  #    #  #    #
        #    #  ######     #    #    #   ####   #####
        
        #####
        #     #
              #
        #####
              #
        #     #
        #####
        --------------------- OR USING THE BUILT-IN `ZIP` FUNCTION ---------------------
        >>> name = ['Google', 'Apple', 'IBM']
        >>> value = [' www.google.com', ' www.apple.com', ' www.ibm.com']
        >>> dict(zip(name, value))
        {'Google': ' www.google.com', 'Apple': ' www.apple.com', 'IBM': ' www.ibm.com'}
        
        
        
        #    #  ######   #####  #    #   ####   #####
        ##  ##  #          #    #    #  #    #  #    #
        # ## #  #####      #    ######  #    #  #    #
        #    #  #          #    #    #  #    #  #    #
        #    #  #          #    #    #  #    #  #    #
        #    #  ######     #    #    #   ####   #####
        
        #
        #    #
        #    #
        #######
            #
            #
            #
        --------------------- OR USING BUILT-IN `MAP` FUNCTION ---------------------
        >>> name = ['Google', 'Apple', 'IBM']
        >>> value = [' www.google.com', ' www.apple.com', ' www.ibm.com']
        >>> dict(map(lambda k, v : (k, v), name, value))
        {'Google': ' www.google.com', 'Apple': ' www.apple.com', 'IBM': ' www.ibm.com'}

    """
      
    return real_url
      
  
  
def default():
  """
    this is the function (shortcut of `Default.default') that we will call in some of our site view
    instead of calling the `Default.default' which will make our code so large
  """
  return Default.default



class Viz:
  @staticmethod
  def vizFun():
    # checking if `Metrix` table is empty, then it will create one to avoid error
    if len(Metrix.objects.all()) == 0:
      first_metrix = Metrix()
      first_metrix.save()
      
    """
      checking to see if the:
        current month matches the month of our last metrix, and
        current year if it matches the year of our last metrix
        
        if both matches, it will not create new metrix table, else it will
    """
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