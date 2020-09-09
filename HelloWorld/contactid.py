#          0123456789012345
message = "1234181131010158"

print("Account number: " + message[0:4])
print("Event qualifier: " + message[6:7])
print("Event code: " + message[7:10])
print("Partition: " + message[10:12])
print("Zone: " + message[12:15])
print("Check digit: " + message[15:])