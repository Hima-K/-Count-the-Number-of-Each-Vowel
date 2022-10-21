{\rtf1\ansi\ansicpg1252\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Program to count the number of each vowels\
\
# string of vowels\
vowels = 'aeiou'\
\
ip_str = 'Hello, have you tried our tutorial section yet?'\
\
# make it suitable for caseless comparisions\
ip_str = ip_str.casefold()\
\
# make a dictionary with each vowel a key and value 0\
count = \{\}.fromkeys(vowels,0)\
\
# count the vowels\
for char in ip_str:\
   if char in count:\
       count[char] += 1\
\
print(count)\
}