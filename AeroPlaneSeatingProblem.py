def Test(InputArr,TotalPerson):
    FinalArr=[]
    for i in InputArr:
        alist=[[0 for k in range(i[0])]for j in range(i[1])]
        FinalArr.append(alist)
    if TotalPerson<1:
        return FinalArr
    FindMaxArr=[]
    for i in InputArr:
        FindMaxArr.append(i[1])
    n=max(FindMaxArr)
    row=0
    num=1
    N=len(InputArr)
    for l in range(n):
        for k in range(N):
            if InputArr[k][1]>row:
                if(k==0 or k==N-1) and InputArr[k][0]>=1:
                    if k==0:
                        FinalArr[k][row][-1]=num
                    else:
                        FinalArr[k][row][0]=num
                elif InputArr[k][0]>=2:
                    FinalArr[k][row][0]=num
                    if num<TotalPerson:
                        num+=1
                    else:
                        return FinalArr
                    FinalArr[k][row][-1]=num
                if num<TotalPerson:
                    num+=1
                else:
                    return FinalArr
                if k==N-1:
                    row+=1
    row=0   
    for l in range(n):
        for k in range(N):
            if InputArr[k][1]>row:
                if(k==0 or k==N-1) and InputArr[k][0]>1:
                    if k==0:
                        FinalArr[k][row][0]=num
                    else:
                        FinalArr[k][row][-1]=num
                
                    if num<TotalPerson:
                        num+=1
                    else:
                        return FinalArr
                    if k==N-1:
                        row+=1
    row=0
    for l in range(n):
        for k in range(N):
            if InputArr[k][1]>row:
                if InputArr[k][0]>2:
                    i=1
                    while i<(InputArr[k][0])-1:
                        FinalArr[k][row][i]=num
                        if num<TotalPerson:
                            num+=1
                        else:
                            return FinalArr
                        i+=1
                    if k==N-1:
                        row+=1
                        
    return FinalArr

if __name__ == "__main__":

    InputArr= [[3,4], [4,5], [2,3], [3,4]]
    TotalPerson=30
    print(Test(InputArr,TotalPerson))
                    