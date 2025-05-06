# Take a paragraph check the count of words, if count is more than 100, print valid ; else invalid

para="""Biodiversity is essential for maintaining the health and stability of ecosystems, 
which in turn support all life on Earth. A rich variety of species ensures natural
sustainability by enabling ecosystems to recover from disturbances, adapt to changes,
and provide vital services such as clean air and water, pollination of crops, climate 
regulation, and soil fertility. Each species, no matter how small, plays a unique role
in the ecological balance, and the loss of even a few can have cascading effects.
Moreover, biodiversity holds cultural, recreational, and economic value, contributing
to human well-being and global development. Protecting it is crucial for our survival 
and the planet's resilience in the face of environmental challenges."""
para=para.split()
if len(para)>100:
    print("valid")
else:
    print("invalid")



# ------------------------------------------------------------------------------------------------------------------
# take a input with both upper and lower cases characters count the no.of uppercases and
#  lower cases without using any methods
my_name=input("enter a string with upper and lower cases characters: ")
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case="abcdefghijklmnopqrstuvwxyz"
l_c=0
u_c=0
for i in range(0, len(my_name)):
    letter=my_name[i]
    if my_name[i] in upper_case:
        u_c+=1
    elif my_name[i] in lower_case: 
        l_c+=1
print('The number of uppercase characters',u_c)
print('The number of lowercase characters',l_c)



