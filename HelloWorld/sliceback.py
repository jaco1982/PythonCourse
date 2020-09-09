#          012345678901234567890123456
letters = "abcdefghijklmnopqurstuvwxyz"
backwards = letters[::-1]

print(backwards)

#qpo
print(letters[16:13:-1])

#edcba
print(letters[4::-1])

#last 8 in reverse
print(letters[:18:-1])

#last n chars from sequence
print(letters[-8:][::-1])
print(letters[-1:])
print(letters[:1])