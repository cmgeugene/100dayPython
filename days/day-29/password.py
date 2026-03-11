#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():

  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)
  nr_letters = 12 - nr_symbols - nr_numbers


  rand_letters = [random.choice(letters) for n in range(nr_letters)]
  rand_numbers = [random.choice(numbers) for n in range(nr_numbers)]
  rand_symbols = [random.choice(symbols) for n in range(nr_symbols)]

  password_list = rand_letters + rand_symbols + rand_numbers

  random.shuffle(password_list)

  password = "".join(password_list)
  return password

generate_password()