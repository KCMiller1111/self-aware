
class Opponent:
    life = 10
    stamina = 8
    ba = 4
    qa = 3
    advantage = 0
    distance = 0

    def turn(you):
        SA = input("You 'Attack' or 'Move'? >> ")
        if  SA == "Attack":
            SAS = input("'Hard' or 'Quick'>> ")
            if SAS == 'Hard':
                if abs(enemy.distance) - abs(you.distance) <= 1:
                    enemy.life -= 4
                    you.advantage +=4
                    you.stamina -=4
                if abs(enemy.distance) - abs(you.distance) > 1 <= 6:
                    enemy.life -= 3
                    you.advantage += 1
                    you.stamina -= 5
                if abs(enemy.distance) - abs(you.distance) > 6:
                    enemy.life -= 1
                    you.advantage -= 4
                    you.stamina -= 9
            if SAS == 'Quick':
                if(you.advantage+you.stamina>enemy.advantage+enemy.stamina):
                    enemy.life-=6
                    you.stamina -=1
                    you.advantage +=8
                else:
                    enemy.life -=2
                    you.stamina -=1
                    you.advantage +=6
        if SA == "Move":
            SAM = input("'Walk', 'Run', 'Back'>> ")
            if SAM == "Walk":
                you.distance += 6
                you.stamina -= 1
                if you.advantage > enemy.advantage:
                        you.life += 2
                        you.advantage +=3
                if you.advantage <= enemy.advantage:
                        you.life +=1
                        you.advantage +=2
            if SAM == "Run":
                you.advantage += 5
                you.stamina -=3
                you.distance +=12
            if SAM == "Back":
               if you.advantage > enemy.advantage:
                        you.life += 4
                        you.distance +=1
               if you.advantage <= enemy.advantage:
                        you.life +=2
    def turn2(enemy):
        SA = input("Enemy 'Attack' or 'Move'? >> ")
        if  SA == "Attack":
            SAS = input("'Hard' or 'Quick'>> ")
            if SAS == 'Hard':
                if abs(you.distance) - abs(enemy.distance) <= 1:
                    you.life -= 4
                    enemy.advantage +=4
                    enemy.stamina -=4
                if abs(you.distance) - abs(enemy.distance) > 1 <= 6:
                    you.life -= 3
                    enemy.advantage += 1
                    enemy.stamina -= 5
                if abs(you.distance) - abs(enemy.distance) > 6:
                    you.life -= 1
                    enemy.advantage -= 4
                    enemy.stamina -= 9
            if SAS == 'Quick':
                if(enemy.advantage+enemy.stamina>you.advantage+enemy.stamina):
                    you.life-=6
                    enemy.stamina -=1
                    enemy.advantage +=8
                else:
                    you.life -=2
                    enemy.stamina -=1
                    enemy.advantage +=6
        if SA == "Move":
            SAM = input("'Walk', 'Run', 'Back'>> ")
            if SAM == "Walk":
                enemy.distance += 6
                enemy.stamina -= 1
                if enemy.advantage > you.advantage:
                        enemy.life += 2
                        enemy.advantage +=3
                if enemy.advantage <= you.advantage:
                        enemy.life +=1
                        enemy.advantage +=2
            if SAM == "Run":
                enemy.advantage += 5
                enemy.stamina -=3
                enemy.distance +=12
            if SAM == "Back":
                if enemy.advantage > enemy.advantage:
                        enemy.life += 4
                        enemy.distance +=1
                if you.advantage <= enemy.advantage:
                        enemy.life +=2
        print(" ");
        ly = "Your life is " + str(you.life) + "  ";
        print(ly)
        sy = "Your stamina is " + str(you.stamina) + " ";
        print(sy)
        dy = "Your distance is " + str(you.distance) + " ";
        print(dy)
        ay = "Your advantage is " + str(you.advantage) + " ";
        print(ay)
        print(" ");
        le = "Enemy's life is " + str(enemy.life) + "  ";
        print(le)
        se = "Enemy's stamina is " + str(enemy.stamina) + " ";
        print(se)
        de = "Enemy's distance is " + str(enemy.distance) + " ";
        print(de)
        ae = "Enemy's advantage is " + str(you.advantage) + " ";
        print(ae)
        print(" ")

you = Opponent()
enemy = Opponent()
nextup = 1

while nextup == 1:
    if(you.life <= 0):
        if(enemy.life <= 0):
            if(you.advantage+you.stamina>enemy.advantage+enemy.stamina):
                print("He dayd.  U saved.")
                nextup = 0
                quit
            if(enemy.advantage+enemy.stamina>you.advantage+you.stamina):
                print("You dayd.  He saved.")
                nextup = 0
                quit
            elif(you.advantage+you.stamina==enemy.advantage+enemy.stamina):
                print("You both dayd.  Treasure is mine")
                nextup = 0
                quit
        else:
            print("You dayd")
            nextup = 0
            quit
    elif(enemy.life <= 0):
        print("He dayd")
        nextup = 0
        quit
    else:
        nextup = 1
        you.turn()
        enemy.turn2()
