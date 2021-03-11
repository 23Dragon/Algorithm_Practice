from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    df_tot = defaultdict(int)
    # set total count
    for idx, value in enumerate(genres):
        df_tot[value] += plays[idx]
    
    srt_df_tot = sorted(df_tot.items(), key=lambda x: x[1], reverse=True)
    
    # 1. order by genre
    for idx, value in enumerate(srt_df_tot):
        
        # 2. max 2 pick
        
        print(idx, value)
    
    
    
    return answer