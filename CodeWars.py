def opposite(number):
  if number < 0:
      number = abs(number)
      return number
  else:
      number = int(("-" + str(number)))
      return number

print(opposite(-25.6))
