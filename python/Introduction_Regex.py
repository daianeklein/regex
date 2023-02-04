# Databricks notebook source
#!/usr/bin/env python
# coding: utf-8


# COMMAND ----------

# MAGIC %md # INTRODUCTION TO REGULAR EXPRESSIONS

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ## Libs

# COMMAND ----------




import re
import datetime




#tab
#shift tab
#shift + double tab



# COMMAND ----------

# MAGIC %md ## Raw String and Regular String

# COMMAND ----------




s = 'a\tb' # a-tab-b
print(s)




raw_s = r'a\tb' #use raw string when defining regex patterns in your code
print(raw_s)



# COMMAND ----------

# MAGIC %md ## re.match - Find the first match

# COMMAND ----------




pattern = r'\d+'
text = '42 is my lucky number'




match = re.match(pattern, text)




if match:
    print('Match success')
else:
    print('no match')




text




pattern




re.match(pattern, text)




pattern = r'\d+'
text = 'is my lucky number'
match = re.match(pattern, text)

if match:
    print('Match success')
else:
    print('no match')


# In[ ]:





# ***



pattern = r'\d+'
text = 'is my lucky number'




match = re.match(pattern, text)




if match:
    print('Match success')
else:
    print('no match')


# ***



pattern = r'\d+'
text = '42 is my lucky number'




match = re.match(pattern, text)




if match:
    print(match.group(0), 'at index:', match.start())
else:
    print('no match')




if match:
    print(match.group(0))
else:
    print('no match')


# Match - try to apply the pattern at the start of the string


# COMMAND ----------

# MAGIC %md ## Input Validation

# COMMAND ----------




def is_integer(text):
    pattern = r"\d+"
    
    match = re.match(pattern, text)
    
    if match:
        return True
    else:
        return False




is_integer("123")




is_integer("abc")




def test_is_integer():
    pass_list = ["123","456","900","0991"]
    fail_list = ["a123","124a","1 2 3","1\t2"," 12","45 "]
    
    for text in pass_list:
        if not is_integer(text):
            print('\tFailed to detect an integer',text)
    
    for text in fail_list:
        if is_integer(text):
            print('\tIncorrectly classified as an integer',text)
    
    print('Test complete')




test_is_integer()




def is_integer(text):
    pattern = r"\d+$" #look for numbers followed by end of string
    
    match = re.match(pattern, text)
    
    if match:
        return True
    else:
        return False

def test_is_integer():
    pass_list = ["123","456","900","0991"]
    fail_list = ["a123","124a","1 2 3","1\t2"," 12","45 "]
    
    for text in pass_list:
        if not is_integer(text):
            print('\tFailed to detect an integer',text)
    
    for text in fail_list:
        if is_integer(text):
            print('\tIncorrectly classified as an integer',text)
    
    print('Test complete')




test_is_integer()



# COMMAND ----------

# MAGIC %md ## re.search - Find the first match anywhere

# COMMAND ----------




pattern = r"\d+"
text = 'my lucky numbers are 42 and 24'

match = re.search(pattern,text)

if match:
    print(match.group(0), 'at index:', match.start())
else:
    print('no match')




def is_integer(text):
    pattern = r"\d+$" #look for numbers followed by end of string
    
    match = re.search(pattern, text)
    
    if match:
        return True
    else:
        return False




is_integer(text)



# COMMAND ----------

# MAGIC %md ## re.findall - Find all the matches

# COMMAND ----------




# Find all numbers in the text
pattern = r"\d+"
text = "NY Postal Codes are 10001, 10002, 10003, 10004"




match = re.findall(pattern, text)
print(match)



# COMMAND ----------

# MAGIC %md ## re.finditer - Iterator

# COMMAND ----------




pattern = r"\d+"
text = "NY Postal Codes are 10001, 10002, 10003, 10004"

match_iter = re.finditer(pattern, text)

for match in match_iter:
    print("\t", match.group(0), 'at index:', match.start())




pattern = r"\d+"
text = "NY Postal Codes are 10001, 10002, 10003, 10004"

match_iter = re.finditer(pattern, text)

for match in match_iter:
    print("\t", match.group(0), 'at index:', match.start())

i = 0    
for match in match_iter:
    print('/t', match.group(0), 'at index:', match.start())
    i += 1
    
    if i > 1:
        break



# COMMAND ----------

# MAGIC %md ### groups - find sub matches

# COMMAND ----------




pattern = r"(\d{4})(\d{2})(\d{2})"
text = "Start Date: 20200920"




match = re.search(pattern, text)
match




match.groups()




match.groups(1)[0]




match.groups(2)[1]




for idx, value in enumerate(match.groups()):
    print(idx, value, idx+1, match.start(idx+1))




pattern = r"(\d{4})(\d{2})(\d{2})"
text = "Start Date: 20200920"

print("Pattern",pattern)
match = re.search(pattern, text)

if match:
    print('Found a match', match.group(0), 'at index:', match.start())
    
    print('Groups', match.groups())
        
    for idx, value in enumerate(match.groups()):
        print ('\tGroup', idx+1, value, '\tat index', match.start(idx+1))
        
else:
    print("No Match")



# COMMAND ----------

# MAGIC %md ### named groups

# COMMAND ----------

# 

# In[ ]:


# Separate year, month and day
pattern = r"(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})"
text = "Start Date: 20200920"

print("Pattern",pattern)
match = re.search(pattern, text)

if match:
    print('Found a match', match.group(0), 'at index:', match.start())    
    print('\t',match.groupdict())
else:
    print("No Match")  




pattern = r"(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})"
text = "start date: 19910822"

match = re.search(pattern, text)

match.group(0), match.start()

match.groupdict()




match.groupdict()



# COMMAND ----------

# MAGIC %md ## re.sub - find and replace

# COMMAND ----------

# 
# two patterns: one to find the text and another pattern with replacement text



pattern = r"(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})"
text = "Start Date: 20200920, End Date: 20210920"

replacement_pattern = r"\g<month>-\g<day>-\g<year>"

print(text)

new_text = re.sub(pattern, replacement_pattern, text)

print(new_text)




def format_date(match):   
    in_date = match.groupdict()
    
    year = int(in_date['year'])
    month = int(in_date['month'])
    day = int(in_date['day'])
    
    #https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
    return datetime.date(year,month,day).strftime('%b-%d-%Y')

# Format date
pattern = r"(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})"
text = "Start Date: 20200920, End Date: 20210920"

print ('original text\t', text)
print()

# find and replace
new_text= re.sub(pattern, format_date, text)

print('new text\t', new_text)re.split - split text based on specified pattern



# COMMAND ----------

# MAGIC %md ## re.split - split text based on specified pattern

# COMMAND ----------

# 



pattern = r','
text = 'today, is, my lucky, day'

re.split(pattern, text)


# In[ ]:




