def movePlayer(coord, direction):
    match direction:
        case "right":
            coord['x'] += 1
        case "up":
            coord['y'] += 1
        case "left":
            coord['x'] -= 1
        case "down":
            coord['y'] -= 1
        case _:
            print("Invalid Direction")
    return coord


coordinates = {"x": 0, "y": 0}

print("Input \"exit\" to close")

while True:
    print(f"Your coordinates are now ({coordinates['x']}, {coordinates['y']})")
    inputDirection = input("Input: ")

    if inputDirection.lower() == "exit":
        break;
    
    newCoords = movePlayer(coordinates, inputDirection)
    coordinates = newCoords
