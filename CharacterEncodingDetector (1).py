#!/usr/bin/env python
# coding: utf-8

#  # FUNCTION TO DETECT THE CHARACTER ENCODING SCHEME OF A FILE

# In[29]:


def encodingDetector(filepath, increment):
    import charset_normalizer
    import pandas as pd
    increaseby = 500
    while True:
        try:
            with open(filepath, 'rb') as f:
                result = charset_normalizer.detect(f.read(increaseby))
            data = pd.read_csv(filepath, encoding = result['encoding'])
            break
        except UnicodeDecodeError:
            increaseby += increment
    return data


# # TRYING IT OUT

# In[27]:


books = encodingDetector('test data.csv', 500)


# In[28]:


print(books)

