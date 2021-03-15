from collections import defaultdict

def solution(genres, plays):
    answer = []

    df_tot = defaultdict(int)

    # counting total numbers
    for idx, value in enumerate(genres):        
        df_tot[value] += plays[idx]
    
    # sort
    df_tot_st = sorted(df_tot.items(), key=lambda x : x[1], reverse=True)
    
    print()
    print("df_tot_st: ", df_tot_st)

    df_dict = defaultdict(list)

    for idx, value in enumerate(genres):
        df_dict[value].append([idx, plays[idx]])
        

    print()
    print("df_dict: ", df_dict)


    return answer


solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])