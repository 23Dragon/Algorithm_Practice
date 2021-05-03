from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    df_tot = defaultdict(int)
    df_plays = defaultdict(list)
    
    # set
    for idx, value in enumerate(genres):        
        df_plays[value].append([idx, plays[idx]])
        df_tot[value] += plays[idx]
    
    # sorting
    srt_df_tot = sorted(df_tot.items(), key=lambda x: x[1], reverse=True)
    for genre in df_plays:
        df_plays[genre].sort(key=lambda x: x[1], reverse=True)
    
    
    # pick
    for genre in srt_df_tot:
                
        # limit max 2
        for idx, play in enumerate(df_plays[genre[0]]):            
            if idx < 2:
                answer.append(play[0])
            
        
    
    
    return answer
