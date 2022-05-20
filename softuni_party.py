def is_vip(person):
    return person[0].isdigit()


n = int(input())

vip_guest = set()
regular_guest = set()

for _ in range(n):
    guest = input()
    if is_vip(guest):
        vip_guest.add(guest)
    else:
        regular_guest.add(guest)

while True:
    command = input()
    if command == "END":
        break

    if is_vip(command):
        vip_guest.remove(command)
    else:
        regular_guest.remove(command)

print(len(vip_guest) + len(regular_guest))
[print(vip) for vip in sorted(vip_guest)]
[print(regular) for regular in sorted(regular_guest)]
