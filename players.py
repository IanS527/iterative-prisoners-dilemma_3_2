Team Jake:
    if getting_team_name:
        return 'TEAM_JAKE'
    else:
        if len(opponent_history)==0:
            return 'b'
        size = len(history)
        if opponent_history[-1]=='c' and history[-1]=='b':
            return 'b' 
        if opponent_history[-1]=='c':
             if random.random()<0.75: 
                return 'b'        
             else: 
                return 'c'  
Team John:
    if getting_team_name:
        return 'Team_John'
    else:
        if len(history)==0: #It's the first round: betray
            return 'b'
        elif len(history)>=1:
            if len(history)>=4:
                if opponent_history[0]=='c' and opponent_history[1]=='b' and opponent_history[2]=='b' and opponent_history[3]=='c':
                    return 'b'
            if opponent_history[-1]=='c' and history[-1]=='b':
                return 'b'
            if score <= opponent_score:
                return 'b'
            elif score >= opponent_score:
                return 'c'

Team Chase
    if getting_team_name:
            return 'TEAM_CHASE'
        else:
            if len(opponent_history)==0: 
                return 'b'
            if history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' 
            if opponent_history[-1]=='c' and history[-1]=='b':
                return 'b'
            if score >= opponent_score/2:
                return 'c'
            if score <= opponent_score*score:
                return 'b'
            if history[-1]=='b':
                return 'b'
            else:
                return 'c'

Team Nate:
    if getting_team_name:
        return 'Team_Nate'
    else:
        if len(opponent_history)==0:
            return 'c'
        if history[-1]=='c':
            if opponent_history[-1]=='c':
                return 'c'
            else:
                return 'b'
        if history[-1]=='b':
<<<<<<< HEAD
            return 'b'
                
=======

>>>>>>> refs/remotes/origin/master
=======
            if opponent_history[-1]=='c':
                return 'b'
            else:
                return 'b'
Team Heather:
        if getting_team_name:
            return 'Team Heather'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='c':
                return 'c' #If player and opponent both collude, collude again
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' #If player is betrayed by opponent, betray
            elif history[-1]=='b' and opponent_history[-1]=='c':
                return 'b' #If player betrays a colluding opponent, betray
            elif history[-1]=='b' and opponent_history[-1]=='b':
                return 'b' #If player and opponent betray eachother, betray
            else:
                return 'c' #otherwise collude

Team Ryan:
        if getting_team_name:
            return 'Team_Ryan'
        else:
            if len(opponent_history)==0: 
                return 'b'
            elif history[-1]=='b' and opponent_history[-1]=='b':
                return 'b' 
            else:
                return 'b' 
>>>>>>> refs/remotes/origin/master
