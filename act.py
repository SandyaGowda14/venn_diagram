import matplotlib.pyplot as plt
from matplotlib_venn import venn3

total = int(input("Enter total number of students: "))

M = int(input("Enter number of students who like Mathematics: "))
P = int(input("Enter number of students who like Physics: "))
C = int(input("Enter number of students who like Chemistry: "))

MP = int(input("Enter number who like Mathematics & Physics: "))
PC = int(input("Enter number who like Physics & Chemistry: "))
MC = int(input("Enter number who like Mathematics & Chemistry: "))

MPC = int(input("Enter number who like all three subjects: "))

only_M = M - MP - MC + MPC
only_P = P - MP - PC + MPC
only_C = C - MC - PC + MPC

MP_only = MP - MPC
PC_only = PC - MPC
MC_only = MC - MPC

exactly_one = only_M + only_P + only_C
exactly_two = MP_only + PC_only + MC_only
exactly_three = MPC

at_least_one = exactly_one + exactly_two + exactly_three
at_least_two = exactly_two + exactly_three
at_least_three = exactly_three

at_most_one = exactly_one
at_most_two = exactly_one + exactly_two
at_most_three = at_least_one

none = total - at_least_one

print("\n--- RESULTS ---")
print("Only Mathematics:", only_M)
print("Only Physics:", only_P)
print("Only Chemistry:", only_C)

print("\nExactly One:", exactly_one)
print("Exactly Two:", exactly_two)
print("Exactly Three:", exactly_three)

print("\nAt Least One:", at_least_one)
print("At Least Two:", at_least_two)
print("At Least Three:", at_least_three)

print("\nAt Most One:", at_most_one)
print("At Most Two:", at_most_two)
print("At Most Three:", at_most_three)

print("\nNone:", none)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
v1 = venn3(subsets=(1, 1, 1, 1, 1, 1, 1),
           set_labels=('Mathematics', 'Physics', 'Chemistry'))

v1.get_label_by_id('100').set_text(str(M))
v1.get_label_by_id('010').set_text(str(P))
v1.get_label_by_id('001').set_text(str(C))
v1.get_label_by_id('110').set_text(str(MP))
v1.get_label_by_id('011').set_text(str(PC))
v1.get_label_by_id('101').set_text(str(MC))
v1.get_label_by_id('111').set_text(str(MPC))

plt.title("Given Data")

plt.subplot(1, 2, 2)
venn3(subsets=(
    only_M,
    only_P,
    MP_only,
    only_C,
    MC_only,
    PC_only,
    MPC
),
set_labels=('Mathematics', 'Physics', 'Chemistry'))

plt.title("Final Computed Regions")

plt.figtext(0.20, -0.05, f"At Least 1 = {at_least_one}", fontsize=10)
plt.figtext(0.60, -0.05, f"At Least 2 = {at_least_two}", fontsize=10)

plt.figtext(0.20, -0.10, f"At Most 1 = {at_most_one}", fontsize=10)
plt.figtext(0.60, -0.10, f"At Most 2 = {at_most_two}", fontsize=10)

plt.figtext(0.40, -0.15, f"None = {none}", fontsize=10)

plt.tight_layout()
plt.show()