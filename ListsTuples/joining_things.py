flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Liy",
]

# for flower in flowers:
#     print(flower)

separator = " | "
output = separator.join(flowers)
print(output)

more_flowers = output.split(separator)
print(more_flowers)
