#write a program that reads a string and print its length.
st = "hello world"
print(st)
print(len(st))
#convert the input string to uppercase and lowercase.
st = "python3"
print(st)
# uppercase.st:
print(st.upper())
#lowercase .st:
print(st.lower())
# count how many times a given character apears in a string.
st = "banana"
ch = "a"
print(st.count(ch))

#print first and last character of a  string:
st = "drawer"
print(st[0])
print(st[5])
#check if a substring exist in a string:
st = "data science"
subst = "science"
print(subst in st)

#print a substring from index start to end:
subst = "programming"
print(subst[3:8])

# reverse the string:
st = "python"
print(st[::-1])
#replace all occurance of a word with another word:
st = "I love apples. Apples are great!"
print(st.replace("apples", "oranges"))

#split a sentence on spaces and jion with-:
st = "split this sentence"
words = st.split()
new_st = '-'.join(words)
print(new_st)

#remove leading and trailing spaces:
st = "padded text"
print(st.strip())

# count vowels and constanents :
st = "Hello, World! 123"

vowels = 0
consonants = 0

for ch in st.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)
#determine if string is a palindrome  ignoring case and non- alphanumeric characters.

st = "a man, a plan, a canal: a panama!"
clean = ""

for ch in st:()  
if ch.isalnum():
        clean += ch.lower()
         
if clean == clean[::-1]:
     print(True)
else:
     print(False)
 #convert a case to  tittle without using .tittle():
st = "hELLO wORLD from PYTHON"

words = st.split()

result = []

for word in words:
    new_word = word[0].upper() + word[1:].lower()
    result.append(new_word)

print(" ".join(result))
#4.	Find All Indices of a Substring (Allow Overlaps)
#Return a list of starting indices where a substring occurs
st = "aaaa"
subst = "aa"
indices = []

for i in range(len(st) - len(subst) + 1):
     if st[i:i+len(subst)] == subst:
          indices.append(i)

print(indices)
#5.	Character Frequency Dictionary
#Build a frequency dictionary for characters (case-insensitive, skip spaces).
st = "Baa Baa Black Sheep"
freq = {}
for ch in st.lower():
     if ch != " ":
          freq[ch] = freq.get(ch,0) + 1
          print(freq)
          #6.	Anagram Checker
#Check if two strings are anagrams (ignore spaces, punctuation, and case).
s1 = "Listen"
s2 = "Silent"

str1 = ""
str2 = ""

for ch in s1:
    if ch.isalpha():
        str1 += ch.lower()

for ch in s2:
    if ch.isalpha():
        str2 += ch.lower()

print(sorted(str1) == sorted(str2))
#7.	Compress Repeated Characters (RLE-lite)
#Compress runs of the same character as <char><count>.
s = "aaabbcaaaa"

result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result += s[i - 1] + str(count)
        count = 1

result += s[-1] + str(count)

print(result)
#8.	Longest Word in a Sentence
#Find the longest word; if multiple, return the first. Consider words as alphabetic sequences

s = "Find the longest_word here!"

words = s.split()
longest = ""

for word in words:
    clean = ""

    for ch in word:
        if ch.isalpha():
            clean += ch

    if len(clean) > len(longest):
        longest = clean

print(longest)
#9.	Remove Duplicate Characters but Keep Order
#Remove duplicates while preserving the first occurrence order
s = "banana"

result = ""
seen = set()

for ch in s:
    if ch not in seen:
        result += ch
        seen.add(ch)

print(result)
#mask email username:

email = "john.doe@example.com"

username, domain = email.split("@")

if len(username) >= 2:
    masked = username[0] + "*" * (len(username) - 2) + username[-1]
else:
    masked = username

print(masked + "@" + domain)
          