def count_smileys(arr):
    total = 0
    eye = ':' or ';'
    nose = '-' or '~'
    mouth = ')' or 'D'
    
    for item in arr:
        check = '{}{}{}'.format(eye, nose, mouth) or '{}{}'.format(eye,mouth)
        
        if item == check:
            total += 1
                    
    return total