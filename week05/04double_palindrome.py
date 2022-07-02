def toLower(s):
  res = ''
  for i in s:
    if i >= 'A' and i <= 'Z':
      res = res + chr(ord('a') + (ord(i) - ord('A')))
    else:
      res = res + i
  return res

def isPalindrome(s):
  if len(s) == 0 or len(s) == 1:
    return True
  res = True if s[0] == s[len(s)-1] else False
  ss = s[1:len(s)-1]
  return res and isPalindrome(ss)

def isPalindrome2(s):
  if len(s)==0:   
    return True
  if len(s)==1: 
    return True
  return s[0]==s[len(s)-1] and isPalindrome2(s[1:len(s)-1])

def lentxt(a):
  if len(a)%2==1:
    return len(a)//2+1
  else:
    return len(a)//2
Text=input("Text: ")
Text=toLower(Text)
len_txt=len(Text)
#if len_txt%2==1:
 # len_txt+=1
if isPalindrome2(Text):
  if isPalindrome2(Text[lentxt(Text):]) and isPalindrome2(Text[:len_txt//2]):
    print("Double Palindrome")
  elif isPalindrome2(Text):
    print("Palindrome")
else:
  print('No')