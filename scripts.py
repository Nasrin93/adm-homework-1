# =====================================
# Problem 1 - Python Challenges
# =====================================

# Exercise 1: If-Else
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")


# Exercise 2: Loops
# Your solution here


# Exercise : Validating Postal Codes

regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"



# Exercise : 


import re

pattern = re.compile(r'^[456](?:\d{15}|\d{4}-\d{4}-\d{4}-\d{4})$')

for _ in range(int(input())):
    card = input()

    if pattern.fullmatch(card):
        digits = card.replace('-', '')

        if not re.search(r'(\d)\1{3,}', digits):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")


# Exercise : Validating Credit Card Numbers

import re

for _ in range(int(input())):
    card = input()

    pattern = r'^(4|5|6)(\d{15}|(\d{3}-\d{4}-\d{4}-\d{4}))$'

    if re.match(pattern, card):
        digits = card.replace('-', '')

        if (len(digits) == 16
            and not re.search(r'(\d)\1{3,}', digits)):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")

# Exercise : Validating UID

import re

for _ in range(int(input())):
    uid = input()

    if (len(uid) == 10
        and uid.isalnum()
        and len(set(uid)) == 10
        and len(re.findall(r'[A-Z]', uid)) >= 2
        and len(re.findall(r'[0-9]', uid)) >= 3):
        print("Valid")
    else:
        print("Invalid")


# Exercise : Detect HTML Tags, Attributes and Attribute Values

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print(tag)
        for attribute, value in attrs:
            print(f"-> {attribute} > {value}")

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attribute, value in attrs:
            print(f"-> {attribute} > {value}")


n = int(input())
html = ""

for _ in range(n):
    html += input() + "\n"

parser = MyHTMLParser()
parser.feed(html)


# Exercise : HTMLParser – Part 1

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)


n = int(input())
html = ""

for _ in range(n):
    html += input() + "\n"

parser = MyHTMLParser()
parser.feed(html)


# Exercise : HTML Parser – Part 1

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr, value in attrs:
            print(f"-> {attr} > {value}")

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr, value in attrs:
            print(f"-> {attr} > {value}")

n = int(input())
html = ""

for _ in range(n):
    html += input() + "\n"

parser = MyHTMLParser()
parser.feed(html)


# Exercise : Hex Color Code

import re

n = int(input())
inside_block = False

for _ in range(n):
    line = input()

    if '{' in line:
        inside_block = True
    elif '}' in line:
        inside_block = False
    elif inside_block:
        codes = re.findall(r'#[0-9a-fA-F]{3,6}(?=[;,) \t])', line)
        for code in codes:
            if len(code) in (4, 7):
                print(code)


# Exercise : Validating Email Addresses

import re
import email.utils

pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

for _ in range(int(input())):
    line = input()
    name, email_address = email.utils.parseaddr(line)

    if re.fullmatch(pattern, email_address):
        print(email.utils.formataddr((name, email_address)))


# Exercise : Validating Roman Numerals

import re

regex_pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

print(bool(re.match(regex_pattern, input())))


# Exercise : Regex Substitution

import re

n = int(input())

for _ in range(n):
    line = input()
    line = re.sub(r'(?<= )&&(?= )', 'and', line)
    line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
    print(line)


# Exercise : re.start() & re.end()

import re

s = input()
k = input()

matches = list(re.finditer(f'(?={re.escape(k)})', s))

if matches:
    for match in matches:
        start = match.start()
        end = start + len(k) - 1
        print((start, end))
else:
    print((-1, -1))


# Exercise : Re.findall() and Re.finditer()

import re

s = input()

matches = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])[aeiou]{2,}(?=[qwrtypsdfghjklzxcvbnm])', s, re.IGNORECASE)

if matches:
    print(*matches, sep='\n')
else:
    print(-1)


# Exercise : Regex Split

import re

regex_pattern = r'[,.]'

print("\n".join(re.split(regex_pattern, input())))


# Exercise : Detect Floating Point Number


import re

for _ in range(int(input())):
    s = input()
    print(bool(re.fullmatch(r'[+-]?([0-9]*\.)[0-9]+', s)))


# Exercise : Map and Lambda Function


cube = lambda x: x ** 3

def fibonacci(n):
    a, b = 0, 1
    result = []

    for _ in range(n):
        result.append(a)
        a, b = b, a + b

    return result

if __name__ == '__main__':
    n = int(input())
    numbers = fibonacci(n)
    print(list(map(cube, numbers)))


# Exercise : ginortS


s = input()

result = sorted(s, key=lambda c: (
    c.isdigit(),
    c.isdigit() and int(c) % 2 == 0,
    c.isupper(),
    c
))

print(''.join(result))


# Exercise : Athlete Sort


if __name__ == '__main__':
    n, m = map(int, input().split())

    athletes = []
    for _ in range(n):
        athletes.append(list(map(int, input().split())))

    k = int(input())

    athletes.sort(key=lambda athlete: athlete[k])

    for athlete in athletes:
        print(*athlete)


# Exercise : Validating Regex


import re

for _ in range(int(input())):
    pattern = input()
    try:
        re.compile(pattern)
        if re.search(r'(?<!\\)[*+?]\s*[*+?]', pattern):
            print("False")
        else:
            print("True")
    except re.error:
        print("False")


# Exercise : Exceptions

for _ in range(int(input())):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)


# Exercise : Time Delta

from datetime import datetime

for _ in range(int(input())):
    t1 = datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
    print(int(abs((t1 - t2).total_seconds())))





# =====================================
# Problem 2 - Algorithm Implementation
# =====================================

# Exercise : insertion Sort2

def insertionSort2(n, arr):
    for i in range(1, n):
        value = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = value
        print(*arr)

# Exercise : insertion Sort1

def insertionSort1(n, arr):
    value = arr[n - 1]
    i = n - 2

    while i >= 0 and arr[i] > value:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1

    arr[i + 1] = value
    print(*arr)

# Exercise : Recursive Digit Sum


#!/bin/python3

import math
import os
import random
import re
import sys

def superDigit(n, k):
    total = sum(int(digit) for digit in n) * k

    while total >= 10:
        total = sum(int(digit) for digit in str(total))

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]
    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')
    fptr.close()



# Exercise : viral Advertising

def viralAdvertising(n):
    shared = 5
    total_likes = 0

    for day in range(n):
        liked = shared // 2
        total_likes += liked
        shared = liked * 3

    return total_likes


# Exercise : kangaroo

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"

    if (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) // (v1 - v2) >= 0:
        return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

# Exercise : birthdayCakeCandles

import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    return candles.count(max(candles))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
