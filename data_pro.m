clear;
clc;
final = xlsread('result_10.xlsx');
final_result = [];
n = 1;
for i=1:848
    a = 0;
    for j = 1:10
        if(final(i,j)~=100000 && final(i,j)>400)
            a = 1;
        end
    end
    if(a==0)  
        final_result(n,:)=final(i,:);
        n = n+1;
    end   
end