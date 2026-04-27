'''
Regular expressions(RegEx)
--------------------------
-->This regular expression or RegEx is a sequence of characters that forms a searching pattern.
-->To use this we have to import re, which will unlock the package

Functions
---------
1.findall
---------
-->by using this function, it wiff find all sequence in the string
syntax:-->re.findall("metachar",variable_name)

2.search
--------
-->by using this function ,it will only find first sequence in the string 
syntax:-->re.search("metachar",variable_name

meta characters 
---------------
-->meta characters are used to form searching patterns

1.[]
----
-->In this meta character we can search for [a-z],[A-Z],[0-9]

import re
any="this method can read the entire file and return54 thE into list with "
so=re.findall("[a-z0-9A-Z]",any)
an=re.search("[a-c]",any)
print(so)
print(an)

some="by using this function we will only find first sequence"
ty=re.search("[a]",some)
print(ty)

2.dot(.)
--------
-->This meta character will form a searching pattern  as it will take any single character for (.)

import re
we="hello"
the=re.findall("h...o",we)
thing=re.search("he..o",we)
print(the)
print(thing)

make="build"
se=re.search("bu..d",make)
print(se)

3.cap(^)
--------
-->This string is used to find the string is starting with the sequence or not

syntax:-->re,findall("metachar",variable_name)

import re
how="this is used to find the string is starting with the sequence or not"
who=re.findall("^this is",how)
then=re.search("^This",how)
print(who)
print(then)

4.$
---
This is used to find the string is ending with the sequence or not

syntax:--> re.findall("$",variable_name)

5.*
----
---> this meta character will from a searching pattern as it will take any zero or more character for (*)

6.+
----
-->this meta character will form a searching pattern as it will take any on or more character for (+)

syntax --> re.search(".+",variable_name)
'''
import re
out="This is used to find the string is ending with the sequence or not"
one=re.findall("not $",out)
two=re.search("This$",out)
print(one)
print(two)

import re
teja = "this meta character will form a searching pattern as it will "
gk = re.findall("c.*i",teja)
nk = re.search("t.*",teja)
print(gk)
print(nk)

import re
teja = "this meta character will form a searching pattern as it will "
gk = re.findall("an.+y",teja)
koll = re.search("t.*",teja)
print(gk)
print(koll)
