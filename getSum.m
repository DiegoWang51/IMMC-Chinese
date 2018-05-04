function [allSum] = getSum(Force)

    Pos = xlsread('Charging.xlsx');

    Charge_x = Pos(:,1);
    Charge_y = 700-Pos(:,2);
    Consume_x = Pos(:,3);
    Consume_y = 700-Pos(:,4);
    Consum_car = Pos(:,5);

    allSum = [];
    for i = 1:size(Force, 1)
        sum = 0;
        for j = 1:10
            for k = 1:30
                sum = sum + 2*365*getDist(Force(i,j).pos_x,Force(i,j).pos_y,Consume_x(k),Consume_y(k))*Force(i,j).carDistribution(k)/51.6;
            end
            sum = sum + Force(i,j).level/5;
        end   
        allSum = [allSum, sum];
    end

end