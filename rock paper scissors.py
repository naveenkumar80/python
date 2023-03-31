import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("welcome to the rock, paper and scissors game \n")
user_input=input("choose one \n rock\n paper\n scissors \n")
print(f"you choose {user_input}")
if user_input=='rock':
  print(rock)
elif user_input=='paper':
  print(paper)
elif user_input=='scissors':
  print(scissors)
else :
  print("please give the vaild input")
options=[rock,paper,scissors]
cpu_choose=random.randint(0,2)
print("cpu chooses\n")
print(options[cpu_choose])

# rock = 0
# paper = 1
# scissors = 2
if (cpu_choose == 0 and user_input =='rock') or (cpu_choose == 1 and user_input == 'paper') or (cpu_choose == 2 and user_input == 'scissors'):
  print("its draw")
elif (cpu_choose == 0 and user_input=='scissors') or (cpu_choose == 1 and user_input=='rock') or (cpu_choose == 2 and user_input== 'paper') :
  print("you loose ")
else :
  print("you wins")
