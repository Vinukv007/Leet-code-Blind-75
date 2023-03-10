# -*- coding: utf-8 -*-
"""Product of an array except self leetcode 238.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EBy7aZDdiOKNY8IxCSFhxVt_UB79WQIo
"""

#Product of an array except self leetcode 238

def product_array(lists):   #238 Product of an array except self
  prefix=[1]*(len(lists)+1)
  postfix=[1]*(len(lists)+1)
  outputlist=[None for i in range(len(lists))]
  for i in range(len(lists)):
    j=i+1
    k=len(lists)-1-i
    prefix[j]=lists[i]*prefix[i]
    postfix[k]=lists[k]*postfix[k+1]
  for i in range(len(lists)):
    outputlist[i]=prefix[i]*postfix[i+1]
  return outputlist

