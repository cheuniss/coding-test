def check_times(N,L,D):

    times = D
    while(times < (N * (L + 5))): 
        if (((times) % (L+5)) >=L): 
            return  times
        times += D 
    return times
            
            
if __name__ == "__main__":
    print(check_times(4,5,20))