

class Player:
    #Defines the attributes of this class(Parent class)
    sport = "Basketball"
    country = "USA"
    team = "Portland Trail Blazers"


#Both classes followed by (Player) are child classes of the parent class, Player
    
class Damian(Player):#Damian inherits all attributes from player, while getting the listed ones as well
    position: "Point Guard"
    height: "6 foot 2"

class Chauncey(Player):#Chauncey inherits all attributes from player, while also getting its own unique attributes as well
    role: "Head Coach"
    years: "2"
    
    
