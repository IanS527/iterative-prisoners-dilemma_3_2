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
            if len(history)==0: #It's the first round: collude
                return 'c'
                
            elif history[-1]=='b' and opponent_history[-1]=='c':
                return 'b' # betray is they were severely punished last time
            
            elif len(history)==1:
                if random.random()<0.2:
                    return 'c'
                else:
                    return 'b'
                    
            elif len(history)==4:
                return 'b'
                
            elif len(history)==8:
                return 'c'
                
            elif len(history)>= 2:
               if history[-1]=='c' and opponent_history[-1]=='b':
                    return 'b' # betray
               else:
                    return 'c' #otherwise collude
            
            else:
                if random.random()<0.00001: #% of the other rounds
                    return 'c'         #collude
                else:
                    return 'b'         #otherwise betray

Team Chase
    if getting_team_name:
            return 'TEAM_CHASE_'
        else:
            if len(opponent_history)==0: #It's the first round: betray
                return 'b'
            if history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' 
            if opponent_history[-1]=='c' and history[-1]=='b':
                return 'b'
            if score >= opponent_score:
                return 'c'
            if score <= opponent_score:
                return 'b'
            else:
                return 'c'
