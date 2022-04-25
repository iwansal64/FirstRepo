import random
while True:
  makanan = random.choice(["Ayam?", "Nasgor?", "Lele?"])
  print(makanan)
  data_user = input('y/n')
  if(data_user == 'y'):
    print('okehh.. nih ', makanan)
    print('mau makan lagi gak?')
    data = input('y/n')
    if data == 'y':
      continue
    else:
      break
    
  elif(data_user == 'n'):
    print('oh yaudah oke')
    break

