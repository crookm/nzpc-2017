def main():
    outcome = "accept"
    output_sting = ""
    stations_visited = []
    current_stat = int(input())
    output_sting += str(current_stat)
    stations_visited.append(current_stat)
    new_stat = 0
    next_stat = input()
    
    while next_stat != "#":
        direction = next_stat[0]
        places_moved = int(next_stat[1])
        
        #move left or right
        
        if direction == "A":
            new_stat = current_stat - places_moved
            if new_stat < 1:
                new_stat = new_stat%8
                if new_stat == 0:
                    new_stat = 8
                
        elif direction == "C":
            
            new_stat = current_stat + places_moved
            if new_stat > 8:
                new_stat = new_stat%8
                if new_stat == 0:
                    new_stat = 8
                
        output_sting += " " + str(new_stat)
        
        if new_stat in stations_visited:
            outcome = "reject"
        
        stations_visited.append(new_stat)

            
        current_stat = new_stat
        next_stat = input()

        
    for i in stations_visited:
        print(i, end=' ')
        
    print(outcome)
            

main()
