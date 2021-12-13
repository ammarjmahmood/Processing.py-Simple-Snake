playerx = 195
playery = 145
xspeed = 0
yspeed = 0

def setup():
    global itemx_red, itemy_red, itemx_green, itemy_green, power_boost, wait_sec, current_millisec, new_position_green , new_position_red
    
    size(400,300)
    frameRate(30)
    background("#004477")
    noStroke()
    textAlign(CENTER)
    itemx_red = 300
    itemy_red = 60
    itemx_green = 100
    itemy_green = 20
    power_boost = False
    wait_sec = -1
    current_millisec = 0
    new_position_green = False
    new_position_red = False

def draw():
    global playerx, playery, xspeed, yspeed, itemx_red, itemy_red, itemx_green, itemy_green, power_boost, wait_sec, current_millisec, new_position_green , new_position_red
    playerx += xspeed
    playery += yspeed
    fill(0x66004477)
    rect(0,0, width,height)
    
    if keyPressed:
        if key == "w" or key == "87":
            xspeed = 0
            yspeed = -4
            if power_boost == True:
                xspeed = 0
                yspeed += -2
        if key == "d" or key == "D":
            xspeed = 4
            yspeed = 0
            if power_boost == True:
                xspeed += 2
                yspeed = 0
        if key == "s" or key == "S":
            xspeed = 0
            yspeed = 4
            if power_boost == True:
                xspeed = 0
                yspeed += 2
        if key == "a" or key == "A":
            xspeed = -4
            yspeed = 0
            if power_boost == True:
                xspeed += -2
                yspeed = 0
        
    fill("#FFFFFF")
    rect(playerx, playery, 10, 10)
    
    if playerx > width:
        playerx = 0
    if playerx < 0:
        playerx = width
    if playery < 0:
        playery = height
    if playery > height:
        playery = 0
        
    fill("#FF0000")
    rect(itemx_red, itemy_red, 10, 10) # red item
    
    if (playerx+10 >= itemx_red and playerx <= itemx_red+10       #checks if the right edge of the head is overlapping the left edge of the red item
        and playery+10 >= itemy_red and playery <= itemy_red+10): #checks if the left edge of the head is overlapping the right edge of the red item
        fill("#00FF00")
        text("hit!", 373,28)
        playery = random(0, 300)
        playerx = random(0, 300)
        #current_millisec = millis()
        #new_position_red = True
        itemx_red = random(0, 300)
        itemy_red = random(0, 300)
        
    fill("#00FF00")
    rect(itemx_green, itemy_green, 10, 10) # green item
    
    if (playerx+10 >= itemx_green and playerx <= itemx_green+10       #checks if the right edge of the head is overlapping the left edge of the red item
        and playery+10 >= itemy_green and playery <= itemy_green+10): #checks if the left edge of the head is overlapping the right edge of the red item
        fill("#00FF00")
        text("hit!", 373,28)
        playery = random(0, 300)
        playerx = random(0, 300)
        power_boost = True
        #current_millisec = millis()
        #new_position_green = True
        itemx_green = random(0, 300)
        itemy_green = random(0, 300)
   
    #if new_position_green == True or new_position_red == True:
    #    if wait_sec < 0:
    #        wait_sec = (current_millisec + 3000) # wait 3 seconds before proceeding
    #    if current_millisec > wait_sec:
    #        itemx_green = random(0, 300)
    #        itemy_green = random(0, 300)
    #        itemx_red = random(0, 300)
    #        itemy_red = random(0, 300)
    ##        new_position_green = False
    #       new_position_red = False
        
        
    
def keyTyped():
    print(key)

def keyPressed():
    global xspeed, yspeed, power_boost

    if key == CODED:
        if keyCode == UP :
            xspeed = 0
            yspeed = -4
            if power_boost == True:
                xspeed = 0
                yspeed += -2
        elif keyCode == RIGHT:
            xspeed = 4
            yspeed = 0
            if power_boost == True:
                xspeed += 2
                yspeed = 0
        elif keyCode == LEFT:
            xspeed = -4
            yspeed = 0
            if power_boost == True:
                xspeed += -2
                yspeed = 0
        elif keyCode == DOWN:
            xspeed = 0
            yspeed = 4
            if power_boost == True:
                xspeed = 0
                yspeed += 2
        

    
    print(keyCode)
