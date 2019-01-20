logo1 = open('logo1.jpg', 'rb')
logo2 = open('logo2.jpg', 'rb')

print(*[(chr(x)) for x, y in zip(logo1.read(), logo2.read()) if x != y], sep='')

logo1.close()
logo2.close()
