# String

+ [Valid Anagram](#valid-anagram)
+ [Reverse String](#reverse-string)
+ [Reverse Vowels of a String](#submissions)
+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)
+ [To Lower Case](#to-lower-case)

## Valid Anagram

https://leetcode.com/problems/valid-anagram/

```python
def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    for i in s:
        if t.find(i) == -1:
            return False
        t = t.replace(str(i), '', 1)
    return True
```

## Reverse String

https://leetcode.com/problems/reverse-string/

```python
def reverseString(self, s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    n = len(s)
    for i in range(n // 2):
        s[i], s[n - 1 - i] = s[n - 1 - i], s[i]
    return s
```

## Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/

```python
def reverseVowels(self, s):
    """
    :type s: str
    :rtype: str
    """
    a = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    n = 0
    l = [i for i in s]
    m = len(l)-1
    while n < m:
        if l[n] not in a and l[m] not in a:
            n += 1
            m -= 1
        elif l[n] not in a:
            n += 1
        elif l[m] not in a:
            m -= 1
        else:
            l[n], l[m] = l[m], l[n]
            n += 1
            m -= 1
    return "".join(l)
```

## Reverse Words in a String III

https://leetcode.com/problems/reverse-words-in-a-string-iii/

```python
def reverseWords(self, s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return s
    s2 = ""
    t = ""
    for i in s:
        if i != " ":
            t = i + t
        else:
            s2 = s2 + t + " "
            t = ""
    s2 = s2 + t
    return s2
```

## To Lower Case

https://leetcode.com/problems/to-lower-case/

```python
def toLowerCase(self, s):
    """
    :type s: str
    :rtype: str
    """
    if s == '':
        return str
    t = ''
    for i in s:
        if ord(i) > 64 and ord(i) < 91:
            t += chr(ord(i) + 32)
        else:
            t += i
    return t
```

