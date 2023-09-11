# First Assigment
# -------------------------------------------------------------------------------------------------------------------
NUM = input("Add Your Number ")

if not NUM.isdigit() :
    raise Exception("Only Numbers Allowed")  # I Want To Check If input is Lettrs Not Numbers

NUM = int(NUM)

if len(str(NUM))>1:
    raise IndexError("Only One Character Allowed")
elif NUM <= 0:
    raise ValueError("Number Must Be Larger Than 0")
elif NUM:
    print("#" * 10)
    print(f"The Number Is {NUM}")
    print("#" * 10)
# -------------------------------------------------------------------------------------------------------------------
print("#" * 70)
# Second Assigment
# -------------------------------------------------------------------------------------------------------------------

def check_cinditions(letter):
  if str(letter).isdigit():
    raise ValueError
  if len(str(letter))>1:
    raise IndexError
  elif str(letter).isalpha():
    return True
  

try:
  
  LETTER = input("Add Letter From A to Z ").upper()
  
  check_cinditions(LETTER)
  
except ValueError:
  print("The Letter Not In A - Z")
  
except IndexError:
  print("You Must Write One Character Only")
else:
  print(f"You Typed {LETTER}")
  
# -------------------------------------------------------------------------------------------------------------------
print("#" * 70)
# Third Assigment
# -------------------------------------------------------------------------------------------------------------------
def calculate(num1, num2) -> int:
  return num1 + num2

print(calculate(20, 30))