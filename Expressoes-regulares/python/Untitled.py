# Databricks notebook source
#!/usr/bin/env python
# coding: utf-8


# COMMAND ----------

# MAGIC %md # EXPRESSOES REGULARES EM PYTHON

# COMMAND ----------




import re



# COMMAND ----------

# MAGIC %md ### 01

# COMMAND ----------




string = 'Este é um teste de expressao teste regulares'




re.search(r'teste', string)




re.findall(r'teste', string)




re.sub(r'teste', '',string) #replace


# In[ ]:




