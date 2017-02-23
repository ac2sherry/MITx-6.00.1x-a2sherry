def f(a, b):
    return a + b


def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    d1_key = list(d1.keys())
    d2_key = list(d2.keys())
    same_key = list(set(d1_key) & set(d2_key))
    diff_key1 = list(set(d1_key) - set(d2_key))
    diff_key2 = list(set(d2_key) - set(d1_key))
   
    same_dic = {}
    for idx in same_key:
        same_dic[idx] = f(d1[idx],d2[idx])
        
    diff_dic = {}
    for idx in diff_key1:
        diff_dic[idx] = d1[idx]
    for idx in diff_key2:
        diff_dic[idx] = d2[idx]

    return (same_dic,diff_dic)

    
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
print(dict_interdiff(d1,d2))