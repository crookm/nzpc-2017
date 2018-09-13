def main():
  teams = [
    { "name": input(), "score": 0 },
    { "name": input(), "score": 0 }
  ]
  
  strokes_num = int(input())
  strokes = input()

  team = 0
  won = False
  for char in strokes:
    if teams[0]["score"] == 7 or teams[1]["score"] == 7:
      won = True
      break
    
    if char == "S":
      pass
    elif char == "H":
      teams[team]["score"] += 1
    elif char == "D":
      if teams[team]["score"] == 6:
        teams[team]["score"] += 1
        team_win(teams[team])
      else:
        teams[team]["score"] += 2
    elif char == "O":
      teams[0 if team == 1 else 1]["score"] += 1
    
    team = 0 if team == 1 else 1

  print("{} {} {} {}.".format(
    teams[0]["name"], teams[0]["score"],
    teams[1]["name"], teams[1]["score"]), end='')

  if teams[0]["score"] == teams[1]["score"]:
    print("All square.")
  else:
    leader = teams[0] if teams[0]["score"] > teams[1]["score"] else teams[1]
    print("{} {}".format(
      leader["name"],
      "has won" if won else "is winning"))

main()

