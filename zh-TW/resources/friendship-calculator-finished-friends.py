#!/bin/python3

score = 0
names = input('輸入兩個人的名字: ')

for character in names:
  if character in 'aeiou':
    score += 5
  if character in 'friend':
    score += 10

print('你的友情分數是 :', score)

if score > 100:
  print('最好的朋友!')