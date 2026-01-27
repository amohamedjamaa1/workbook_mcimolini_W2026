days_until_assignment_due = 14
print(f"Assignment due in {days_until_assignment_due} days!")

# Subtraction Example
days_playing_squash = 2
print(f"Days spent playing squash: {days_playing_squash}.")
# Reassign days_until_assignment_due to the result of the subtraction
days_until_assignment_due = days_until_assignment_due - days_playing_squash
print(f"Assignment due in: {days_until_assignment_due}")

# Addition Example
time_machine_days_added = 3
print(f"Days added by time machine: {time_machine_days_added}.")
days_until_assignment_due = days_until_assignment_due + time_machine_days_added
print(f"Assignment due in: {days_until_assignment_due}")

# Multiplication Example
time_warp_multiplier = 2
print(f"Time warp multiplier: {time_warp_multiplier}.")
days_until_assignment_due = days_until_assignment_due * time_warp_multiplier
print(f"Assignment due in: {days_until_assignment_due} perceived days?!")

# Division Example
slowing_spell_divisor = 7
print(f"Intructor slowing spell: {slowing_spell_divisor} times slow down!!")
#print("Result of division (/):")
#print(days_until_assignment_due / slowing_spell_divisor)
#print("Result of integer (floor) division (//)")
#print(days_until_assignment_due // slowing_spell_divisor)
#print("Result of modulus (%)")
#print(days_until_assignment_due % slowing_spell_divisor)
special_remainder_power = days_until_assignment_due % slowing_spell_divisor
days_until_assignment_due = days_until_assignment_due // slowing_spell_divisor

print(f"Result of floor division: {days_until_assignment_due}")
print(f"Remainder: {special_remainder_power}")

# Exponent Example
print("Special Remainder Power!")
days_until_assignment_due = days_until_assignment_due ** special_remainder_power
print(f"Assignment due in: {days_until_assignment_due}")

# Math Order of Operations
# BEDMAS = Brackets Exponents Division Multiplication Adition Subtraction
user_input_day = input("How many days until the next assignment is due?")

days_until_next_assignment = int(user_input_day) #Don't actually need the variable, could be 1 line

special_remainder_power = 2

days_until_next_assignment = ((days_until_next_assignment - days_playing_squash + time_machine_days_added) * time_warp_multiplier // slowing_spell_divisor) ** special_remainder_power

print("We did it all in 1 line!")
print(f"Next assignment due in: {days_until_next_assignment}")