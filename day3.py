import math

input = open("day3-input.txt", "r")
taboggan_map = input.read().split("\n")

def tree_encounters(right: int, down: int, taboggan_map: list) -> int:
    latitude = right
    adj_map = taboggan_map[0::down]

    tree_count = 0
    for longitude in adj_map[1:]:
        map_extension = math.ceil((latitude + 1) / len(longitude))
        adj_longitude = longitude * map_extension

        if adj_longitude[latitude] == "#":
            tree_count = tree_count + 1
        latitude = latitude + right
    return tree_count


### Part 1 ###
tree_count = tree_encounters(3, 1, taboggan_map)
print(f"Part 1: The number of trees encountered on this map is: {tree_count}")

### Part 2 ###
right1_down1 = tree_encounters(1, 1, taboggan_map)
right3_down1 = tree_encounters(3, 1, taboggan_map)
right5_down1 = tree_encounters(5, 1, taboggan_map)
right7_down1 = tree_encounters(7, 1, taboggan_map)
right1_down2 = tree_encounters(1, 2, taboggan_map)

total_product = right1_down1 * right1_down2 * right3_down1 * right5_down1 * right7_down1
print(f"Part 2: The number of trees encountered on this map is: {total_product}")


