
# coding: utf-8

# In[3]:


s = "house train wait car time"
[len(x) for x in s.split()]


# In[5]:


def is_vowel(char):
    all_vowels = 'aeiouAEIOU'
    return char in all_vowels

c = input("Enter a letter to see if its Vowel: ")

    
print(is_vowel(c))

