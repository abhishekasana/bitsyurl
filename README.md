# BitsyUrl

A url shortner microservice in Flask.

Being a Read-heavy service. Assuming 100:1 ratio between read and write, as there will be a lots of redirection requests compared to new URL shortenings.


# Finialize the requirements

# System APIs

REST APIS

1. createURL(api_dev_key, original_url, custom_alias=None, user_name=None, expire_data=None)
   api_dev_key(string): API developer key
   original_url(string): Original URL to be shortened.
   custom_alias (string): Optional custom key for the URL.
   user_name (string): Optional user name to be used in encoding.
   expire_data (string): Optional expiration date for the shortened URL.

  Return: (string)
2. deleteURL(api_dev_key, url_key)
   url_key (string): string representing the shortened URL

DETECT/PREVENT ABUSE: Each api_dev_key can be limited to a certain number of URL creations and redirections per some time or else a user may consume all URL keys in this design.

# Database Design
1. Read-heavy services
2. Each object we store is small.
3. No relationshops between records, other  than storing which user created a URL.

URL TABLE -> pk -> hash,originalUrl,createdOn,expirattionDate,userID
USER TABLE -> pk -> userid,name,email,createOn

Storing billion of rows, and with no relationship between objects, hence a NoSQL key-value store is better choice for database.

# System Design and Algorithm
base64 encoding -> [A-Z,a-z,0-9,.,-]

6 letter key -> 64^6 = ~69 billion possible strings
8 letter key -> 64^8 = ~281 trillion possible string

MD5 algo -> 128bit hash value
