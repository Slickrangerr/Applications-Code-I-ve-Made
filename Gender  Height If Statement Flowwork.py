is_male = False
is_tall = False

if is_male or is_tall:
    print(" You are a Male or Tall or Both")
elif is_male and not(is_tall):
    print("You are a short Male")
elif not(is_tall and is_male):
    print("You are not a male or tall ")
else:
    print(" You are neither a Male nor Tall")
