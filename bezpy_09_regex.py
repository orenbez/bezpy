# TRY THIS https://towardsdatascience.com/regular-expressions-in-python-7c991daab100
# TRY THIS https://towardsdatascience.com/python-regex-basics-in-5-minutes-b28c0df8d51d?source=bookmarks---------0----------------------------

import os
import re

# Test your regex here … https://www.regextester.com/
# or BETTER here https://regex101.com/

# Documentation: https://docs.python.org/3/library/re.html
# https://www.tutorialspoint.com/python/python_reg_expressions.htm
# https://www.youtube.com/watch?v=7DG3kCDx53c&list=PLRqwX-V7Uu6YEypLuls7iidwHMdCM6o2w
# for powershell file search use gci .\path\ -r | ? -FilterScript {$_.name  -match <regex> }
# for powershell text search use gci .\path\ -r *.py | sls -Pattern <regex>

# ======================================================================================================================
# the 14 REGEX Meta Characters
# ======================================================================================================================
# + ? . * ^ $ ( ) [ ] { } | \
# ======================================================================================================================
# []	A set of characters	e.g. "[a-m]"
# \	    Signals a special sequence (can also be used to escape special characters)	"\d"
# .	    Any single character (except newline character)	e.g. "he..o"
# ^	    Starts with	e.g. "^hello"
# $	    Ends with e.g "world$"
# *	    Zero or more occurrences e.g. "aix*"
# +	    One or more occurrences	e.g. "aix+"
# {}	Exactly the specified number of occurrences	e.g. "al{2}"
# |	    Either or e.g. "falls|stays"
# ()	Capture and group
#

# ======================================================================================================================
# Character Set (or Character Class)
# ======================================================================================================================
# . =  any single character except newline
# [abc] = ANY of a, b, or c  - single char
# [^abc] = NOT (a, b, or c)  - single char which can not be any of the char set
# [a-g] = ANY single char BETWEEN a -> g - lower case
# [a-zA-Z0-9] ANY char between a -> 9
# \w = single char =  a-z OR A-Z OR 0-9 OR _ underscore  = [a-zA-Z0-9_]
# \d = single digit = [0-9]
# \s = whitespace char = [\t\n\r\f]
# \W = not char = [^a-zA-Z0-9_]
# \D = not digit = [^0-9]
# \S =  not whitespace char = [^\t\n\r\f]


# Note: Within a character set []  .... 
# +, *, ., |, (), $, {} have no special meaning, they are taken literally
# '-' is literal only if it is the first char e.g. [-.] matches hypen or dot
# '^' is literal only if it is not the first character in the character class.  e.g.  [a^] means search for 'a' or for '^'
# Otherwise '^' and '-' are the only two special characters that are used inside a character set [].  So [^a-z] reads NOT a thru z
# '-' if the hyphen is not between chars, then it is also literal e.g. [a-q-] means a thru to q or a hyphen '-'
# '\' is interpreted as an escape character in a character set 
# '\\' within a character set would match a literal '\'


# ======================================================================================================================
# Anchors
# ======================================================================================================================
# ^abc$ = start ^, end $ of the Line
# \A = beginning of line match, same as '^'
# \Z = end of line match, same as '$'
# \b = word boundary e.g. \bWORD\b matches 'xx WORD xx'   (can have full stop or next line)
# \B = non boundary character
#
# ======================================================================================================================
# Escaped characters
# ======================================================================================================================
# \ = escapes the 14 special chars + ? . * ^ $ ( ) [ ] { } | \
# \. \* \\ = escaped special characters
# \t \n \r = tab, linefeed, carriage return
# \u00A9 = unicode escaped ©
# \/ some systems may require forward slash to be escaped
#
# ======================================================================================================================
# Groups
# ======================================================================================================================
# (abc)   = capture group
# (?:abc) = passive group or non-capturing group, captures a group but doesn't numerate
# \1      = back-reference to whatever was matched in group #1;  e.g. ([Pp])ython&\1ails
#           here \1 is equivalent to whatever was matched in the 1st group which was either a 'P' or 'p'
#           so this would match 'Python&Pails'  or 'python&pails' not 'Python&pails'
# \3      = matches the exact string of the 3rd group in the previous part of the regular expression
# NOTE:  ([ab])c\1  will match aca or bcb but no other permutation e.g. acb
#        e.g. re.match(r'(\w{3})-(\1)', 'abc-abc') This will match since the first and 2nd group are the same
#        match = 'abc-abc'
# (?P<group_name>regex)  = Named Captured Group   e.g.  (?P<first_name>\w+)\s   captures 'first_name' 
#
# ======================================================================================================================
# Quantifiers '*', '+', '?', {n} and Alternation '|'
# ======================================================================================================================
# x* = 0 or more of the previous character 'x'
# x+ = 1 or more of the previous character 'x', i.e. a positive number of the previous char
# x? = 0 or 1 of the previous character 'x'  (effectively '?' means optional character)
# (XYZ)?  0 or 1 of the entire group 'XYZ'
# (XYZ?)  0 or 1 of just for the character 'Z'; the entire string match is grouped
# x{5}  = exactly five
# x{2,} = two or more
# x{1,3} = between one & three
# ab|cd = # match ab or cd (known as alternation)
# (ab|cd) = alternation that forms a group
# Note that a(b|c) will match the same as a[bc] but second letter forms a group
# Note that quantifiers * + {} are greedy quantifiers
# Note that quantifiers *? +? {}? are ungreedy quantifiers
# x+     = 1 or more 'x' greedy  e.g  ax+   matches 'axxx' from 'axxxb'
# x+?    = 1 or more 'x' ungreedy (match as few as possible ) e.g  ax+?   matches 'ax' from 'axxxxxxb'
#        WARNING: 'x+?b'  and 'x+b' both seem to match greedily e.g. both  match  'xxxxxb' from 'axxxxxb'
# x{3,}? = 3 or more ungreedy  e.g  ax{3,}?   matches 'axxx' from 'axxxxxxb'
# x*?    = 0 or more ungreedy  (this will just choose zero length, doesn't seem useful)
# .* = match any character, Zero or More i.e. of any length with greedy repetition:
#      e.g <.*> matches "<python>perl>" in "xxx<python>perl>xxx"
# .*? = nongreedy repetition, e.g. <.*?> matches "<python>" in "<python>perl>"

# ======================================================================================================================
# Lookaround Assertions  (?=  ) , (?!  ), (?<=  ),  (?<!  )  Will excluded this grouping from the matched string
# ======================================================================================================================
# Note: none of the below are matched as a group, the lookaround assertions are used if you don't want the previous or
#       following section to be part of the full match
# (?=abc)  = positive lookahead = next chars must match 'abc',  e.g. 'python(?=abc) matches 'python' from 'pythonabc'
# (?!abc)  = negative lookahead,= next char musn't match 'abc',  e.g. 'python(?!x)' matches 'python' from 'pythons'
# (?<=abc) = positive lookbehind = prev chars must match 'abc', e.g. 	(?<=\d)cat matches  'cat' in '1cat'
# (?<!abc) = negative lookbehind = prev chars musn't match 'abc', e.g.	\w{3}(?<!mon)ster matches 'munster' but not 'monster'
#
# ======================================================================================================================


# ======================================================================================================================
# the MATCH function - match checks for a match only at the beginning of the string
# ======================================================================================================================
# re.match(pattern, string, flags=0)
# flags:
#   re.M = MULTILINE Makes the '$' match the end of a line (not just the end of the string) and makes ^ match the start of any line (not just the start of the string).
#   re.A = ASCII-only matching flag
#   re.I = IGNORECASE
#   re.L = Interprets words according to the current locale. This interpretation affects the alphabetic group (\w and \W), as well as word boundary behavior(\b and \B).
#   re.S = Makes a period (dot) match any character, including a newline.
#   re.U = Interprets letters according to the Unicode character set. This flag affects the behavior of \w, \W, \b, \B.
#   re.X = Permits "cuter" regular expression syntax. It ignores whitespace (except inside a set [] or when escaped by a backslash) and treats unescaped # as a comment marker.
# ======================================================================================================================

line = "123-456-7899  \n   333.444.6666\n   (234)455-8888"
telephone_regex = r'\(?(\d{3})[-\s.\)](\d{3})[\s.-](\d{4})'
flags = re.M|re.I  # Example of a flag combination
m = re.match(telephone_regex, line, flags)  # returns FIRST match object starting from the beginning of the string

if m: # if we have at match then we have a match object <class 're.Match'>
    print (m.group())  # returns full FIRST match 123-456-7899
    print (m.group(1)) # returns match on bracketed group 1 = (\d{3}) = 123
    print (m.group(2)) # returns match on bracketed group 2 = (\d{3}) = 456
    print (m.group(3))  # returns match on bracketed group 3 = (\d{4}) = 7899
else:
    print ("No match!!")

# re.fullmatch(pattern, string) = Match pattern if whole string matches regular expression

# ======================================================================================================================
# the SEARCH function - search checks for a match ANYWHERE in the string, returns 1st match as an object
# ======================================================================================================================
# re.search(pattern, string, flags=0)
# ======================================================================================================================
line = "XXXXXX 123-456-7899 XXXXXXXX"
s = re.search(telephone_regex, line)  # returns match object

if s: # if we have at match then we have a match object <class 're.Match'>
    s.groups()  # returns all groups as tuple ('123', '456', '7899')
    s.group()   # returns match of the full FIRST string "123-456-7899" referred to as $0 when using replacement in text editor
    s.group(0)  # same as above
    s.group(1)  # returns match on bracketed group 1 = "123"
    s.group(2)  # returns match on bracketed group 2 = "456" referred to as $2 when using replacement in text editor
    s.group(3)  # returns match on bracketed group 2 = "7899"
    s.span()    # returns (7, 19) which is the span for the whole matched string from the original string, i.e. line[7:19] is the match
    s.span(0)   # returns same as above, span of full returned string
    s.span(1)   # returns (7, 10) span for group 1   i.e. s.group(1) = line[7:10]
    s.span(2)   # returns (11, 14) span for group 2
    s.span(3)   # returns (15, 19) span for group 3
    s.start(1)  # returns 7, start of group 1
    s.start()   # same as above
    s.end(1)    # returns 10, end of group 1
    s.end()     # same as above
    s.start(2)  # returns 11, start of group 2
    print ("No match!!")

# ========================================== Named Groups Example ======================================================
names = ['Fred Blogs', 'Oren Nissan Bez', 'James Bond']
for name in names:
    s = re.search('^(?P<first_name>\w+)\s(?P<last_name>\w+)$', name)    # using 'named captured group' format
    if s:
        print(s.group('first_name'), s.group('last_name'))

# Fred Blogs
# James Bond

s.groupdict()  # returns {'first_name': 'James', 'last_name': 'Bond'}  -- only applies to named groups

# ======================================================================================================================

# ======================================================================================================================
# the FINDALL function - returns list of tuples of all non-overlapping matches, each tuple is a set of groups matched,
#                        if groups are not used then a list of matched strings are returned
# ======================================================================================================================
# re.findall(pattern, string)  = Return all non-overlapping match STRINGS of pattern as a list
# re.finditer(pattern, string) =  Return an iterator yielding match OBJECTS over non-overlapping matches of pattern in string
# ======================================================================================================================
line = "XXXXXXXXX123-456-7899   \nYYYYYYYYYYYYY333.444.6666\nZZZZZZZZZZZZZ(234)455-8888"


fa = re.findall(telephone_regex, line)
# fa = [('123', '456', '7899'), ('333', '444', '6666'), ('234', '455', '8888')]

# stores a MATCH object for each value of iterator
fi = re.finditer(telephone_regex, line)

list(fi)
# [<re.Match object; span=(9, 21), match='123-456-7899'>,
#  <re.Match object; span=(38, 50), match='333.444.6666'>,
#  <re.Match object; span=(64, 77), match='(234)455-8888'>]

next(fi).group() # returns next match OBJECT


# ======================================================================================================================
# the SPLIT function - searches and splits  string by occurrences of pattern
# ======================================================================================================================
# re.split(pattern, string, flags=0)
s = "aaaxxxbbbxxxcccxxxddd"
sp = re.split('x{3}', s)
# sp = ['aaa', 'bbb', 'ccc', 'ddd']

# ======================================================================================================================
# the sub() and subn() functions - replaces occurrences of the RE pattern in
# string with repl, subs all occurrences unless max provided. Returns modified str
# ======================================================================================================================
# re.sub(pattern, repl_with, orig_string, max=0)
# re.subn(pattern, str2, string) Replace left most occurrences of pattern in string with str2, but return a tuple of (newstring, # subs made)
# ======================================================================================================================
phone = "204-959-5539 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print (num) # 204-959-5539

# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print (num) # 2049595539

# ======================================================================================================================
# re.scanner()  # not used yet
# # ======================================================================================================================



# ======================================================================================================================
# the COMPILE function - compile a regular expression object of pattern, with flags
# this can be reused in later searches
# ======================================================================================================================
# regex = re.compile(pattern, flags)
# ======================================================================================================================
# regex to match emails
regex = re.compile(r'([\w.]+)@\w+\.(net|com|edu)', re.M|re.I)
regex.pattern # returns '([\\w.]+)@\\w+\\.(net|com|edu)' 
regex.groups  # returns 2

re.search(regex,"EmailAddress: email@website.edu")    # returns <re.Match object; span=(14, 31), match='email@website.edu'>
regex.search('EmailAddress: email@website.edu')       # returns <re.Match object; span=(14, 31), match='email@website.edu'>  (same as above)
regex.split('fred@gmail.com')                         # returns ['', 'fred', 'com', '']
# regex.match()  - as usage above
# regex.sub()  - as usage above
# regex.findall() -as usage above
# regex.finditer()  -as usage above
# ======================================================================================================================
re.purge() # this clears the regular expression cache
           # with webscraping may need to purge cache for meaningful results






# ======================================================================================================================
#    def Swap(regex, string):  replaces group one match with substitute
# ======================================================================================================================
def swap(string):
    regex = r'(\bSTREET\b)'
    swap = 'St'
    # replace group(1) match
    m = re.search(regex, string, re.I)
    if m:
        x,y = m.span(1) # coordinates for group(1) match
        string = string[:x] + swap + string[y:]
    return string

swap('74 Parsons Street, London')  # -> '74 Parsons St, London'
swap('74 Greenstreet, London')     # -> '74 Greenstreet, London'





# ======================================================================================================================
#   clean_street(street):  replaces group one match with substitute
# ======================================================================================================================
def clean_street(street):
    tmp = street
    swaps = ( (r'(-)', ''),
              (r'(#)', ''),
              (r'(\.)', ''),
              (r'(\bSTREET\b)', 'ST'),
              (r'(\bAVENUE\b)', 'AV'),
              (r'(\bAVE\b)', 'AV'),
              (r'(\bDRIVE\b)',  'DR'),
              (r'(\bDRI\b)',  'DR'),
              (r'(\bLANE\b)',   'LN'),
              (r'(\bPOND\b)',   'PD'),
              (r'(\bPLACE\b)',   'PL'),
              (r'(\bCOURT\b)',  'CT'),
              (r'(\bWALK\b)',   'WK'),
              (r'(\bROAD\b)',   'RD'),
              (r'(\bEXPRESS\b)',   'EX'),
              (r'(\bCRESCENT\b)',   'CS'),
              (r'(\bBOULEVARD\b)',   'BD'),
              (r'(\bBLVD\b)',   'BD'),
              (r'(\bPARKWAY\b)',   'PY'),
              (r'(\bPKWY\b)',   'PY'),
              (r'(\bEXPRESS\b)',   'EX'),
              (r'(\bEXPRESSWAY\b)',   'EX'),
              (r'(\bEXPWY\b)',   'EX'),
              (r'(\bNECK\b)',   'NK'),
              (r'(\bHOLLOW\b)',   'HW'),
              (r'(\bTERRACE\b)',   'TR'),
              (r'(\bTERR\b)',   'TR'),
              (r'^\d+\s(\bNORTH\b)', 'N'),
              (r'^\d+\s(\bSOUTH\b)', 'S'),
              (r'^\d+\s(\bEAST\b)', 'E'),
              (r'^\d+\s(\bWEST\b)', 'W'),
    )

    # replace each group(1) match
    for s in swaps:
        m = re.search(s[0],tmp)
        if m:
            r = m.span(1) # coordinates of group(1) match
            tmp = tmp[:r[0]] + s[1] + tmp[r[1]:]

    # Reduce the 2nd main word in the string by removing vowels
    if len(tmp) > 20:
        m = re.search(r'^(\d+)(\s\b\w\b)?(\s\b\w{2,}\b)\s(\b[a-zA-Z]{3,}\b)',tmp)
        if m:
            r = m.span(4)
            tmp = tmp[:r[0]] + re.sub(r'A|E|I|O|U', '', m.group(4)) + tmp[r[1]:]
            #print (tmp, len(tmp))
    return tmp
# ======================================================================================================================

def regex_name(x):
    m = re.match(r'(.*?)@(.*?)@(.*?)@(.*?)@', x)
    if m:
        a = m.group(1).upper().replace(' ','-').replace("'","").replace('.','')
        b = m.group(2).upper().replace(' ','-').replace("'","").replace('.','')
        c = m.group(3).upper().replace(' ','-').replace("'","").replace('.','')
        d = m.group(4).upper().replace(' ','-').replace("'","").replace('.','')
        return (a,b,c,d)


with open(r".\myfiles\NameAsOne.txt", "r") as f:
    for _ in range(20):
        x = f.readline().rstrip()
        t = regex_name(x)
        print(x,'--->', t)

# ======================================================================================================================
#    FILE RENAME EXAMPLE
# ======================================================================================================================
# IdCard_AP-10109133_1.txt -> IdCard_TMP1.txt
# IdCard_AP-10109133_2.txt -> IdCard_TMP2.txt
# ======================================================================================================================
src = '.\myfiles'
with open(src + '\IdCard_AP-10109133_1.txt', 'w') as f:
    pass
with open(src + '\IdCard_AP-10109133_2.txt', 'w') as f:
    pass


for old in os.listdir(src):    # loops through all files/directories in directory
    if os.path.isfile(old):
        new = re.sub(r'AP-\d*_', 'TMP', old)
        print(old,'->',new)
        os.rename(old,new)

# ======================================================================================================================
# Word Count Example
# ======================================================================================================================
# Note that text.split() will contain punctuation which is not desired

text = """Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.
Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.
But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth"""

x = re.findall(r'\b\w+\b', text)

total = len(x)

e_count = 0
for word in x:
    if word.find('e') > 0:
        e_count += 1

print('Total Number of Words:', total)
print('Words with "e":', e_count)


#>> Total Number of Words: 272
#>> Words with "e": 122

# ======================================================================================================================