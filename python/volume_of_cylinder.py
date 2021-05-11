#https://practice.geeksforgeeks.org/problems/compute-the-volume-of-a-cylinder/0/?track=pw-2&batchId=321
radius , length = map(float, input().split(','))

area_of_base = radius * radius * 3.14 
volume = area_of_base * length

print(round(volume,2))
