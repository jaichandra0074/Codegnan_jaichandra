'''
7.?
-----
---> This meta character will form a searching pattern as it will take any zero or one character for (?)
syntax --> re.findall(".?",Variable_name)

8.{}
----------
---> This meta character will form asearching pattern as we can mention the size in the {}
syntax --> re.search(".{size},variable")

9.
----
--> this meta character will form a searching pattern as it consider right or left any string is present or not for (  )

speical sequence:
--------------------
a special sequence is a \ followed by one of the characters in the list below, and has a

special meaning:
\A
----
return a match if the specified characters are at the beginning of thr string
eg: "\Athe"

\b - returns a match where the specified characters are at the beginning or at the end of a word
eg: r"\bain"


\s - return a match where the string contains a white space
character
eg: "\s"
'''
import re
any = "This meta character"
an = re.findall("Th..?",any)
print(an)

import re
can = "This meta character will form asearching pattern as we can mention the size in the {}"
a = re.findall(".{25}",can)
print(a)

import re
txt = "The rain in 56 spain"
x = re.findall("\d", txt)
print(x)
if x:
    print("yes, there i sat least one match!")
else:
    print("No match")

'''
time and date
---------------
%d ---> day
%m ---> month
%y ---> year
%H ---> hour
%M ---> min
%s ---> sec
%p ---> AM/PM
%A ---> day name
%B ---> month name

'''

import datetime
now = datetime.datetime.now()
print(now)
