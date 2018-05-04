result = zeros(x,10);
money_sum = 0;

for i = 1:x
    money_sum = 0;
    x_cor = sum_result_1(i).x;
    y_cor = sum_result_1(i).y;
    
    for e = 1:30
        result(i,x_cor(e)) = result(i,x_cor(e)) + Consum_car(y_cor(e));    
    end
    
    for n = 1:10
        [diff,money] = level_dif(result(i,n));
        %money_sum = money_sum + money;
        money_sum = money_sum + 2*(sum_result(i)/51.6388)
    end
    
    result(i,11) = money_sum;
    
end


[i,j] = find(result==0);
if(size(i)~=0)
    for h = 1:size(i)
        result(i(h),j(h)) = 100000;
    end
end