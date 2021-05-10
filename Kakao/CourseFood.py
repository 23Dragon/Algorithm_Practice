from itertools import combinations

def solution(orders, course):
    answer = []
    
    course_dict = dict()

    for cnt in course:
        #cnt is pick count
        for order in orders:
            order_list = list(map(str, ''.join(order)))
            combi = list(combinations(order_list, cnt))            
            print('order : ', order)
            print(combi)

        
        


    return answer

if __name__ == "__main__":
    orders, course = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],		[2,3,4]
    solution(orders, course)


'''
["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]		[2,3,4]	["AC", "ACDE", "BCFG", "CDE"]
["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	[2,3,5]	["ACD", "AD", "ADE", "CD", "XYZ"]
["XYZ", "XWY", "WXA"]								[2,3,4]	["WX", "XY"]
'''