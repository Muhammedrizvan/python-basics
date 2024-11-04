#Write a Python program to check if a person qualifies
# for a discount based on their age, membership status,
# and whether they have a referral code.

#Use and to check if the person is at least 18 years old
# and has a valid membership.
#Use not to ensure the person does not have an expired membership.
#Use or to add an alternative condition that will
# pass if the person has a valid referral code,
# even if they don’t meet the age requirement.
#If any of these conditions are met,
# print "Discount Applied!", otherwise print "No Discount".

age = 19
valid_membership = True
refrrel_cod = False
membership_expired = True
if (age>=18 and valid_membership)and not membership_expired or refrrel_cod:
    print("discound applied")
else:
    print("no discount")
