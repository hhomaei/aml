import re

'''
Regular Expressions (Regex)

The regex module in Pythos = re
?     --->   matches zero or one of the preceding group
*     --->   matches zero or more of the preceding group
+     --->   matches one or more of the preceding group
{n}   --->   matches exactly n of the preceding group
{n,}  --->   matches n or more of the preceding group
{,m}  --->   matches 0 to m of the preceding group
{n,m} --->   matches at least n and at most m of the preceding group
    - (Ha){3} will match the string 'HaHaHa', but it will not match 'HaHa',
    - (Ha){3,5} can match three, four, or five instances
\d    --->   anay numeric digit from 0 to 9
\D    --->   any character that is not a numeric digit from 0 to 9.
^     --->   the match must occur at the beginning of the searched text
    - ^spam means the string must begin with spam
$     --->   the string must end with this regex pattern.
    - spam$ means the string must end with spam.
.     --->   any character except for a newline
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn’t between the brackets
'''

def validate_email(email):
    if len(email) >= 6:
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))
    return False

