function [city] = findPattern()

    Pos = xlsread('Charging.xlsx');

    Charge_x = Pos(:,1);
    Charge_y = 700-Pos(:,2);
    Consume_x = Pos(:,3);
    Consume_y = 700-Pos(:,4);
    Consum_car = Pos(:,5);
    hehe = 0;

    for chargeNum = 3:10

        sum = 0;
        sum_result = [];
        indexs = nchoosek([1:10],chargeNum);
        [x,y] = size(indexs);
        individual_result = [];
        a = 0;
        b = 0;
        city(1,10).i = [];
        for i = 1:968
            for j = 1:10
                city(i,j).i(30,1) = 0;
            end
        end
        % x is ??
        for k = 1:x
            options = indexs(k,:);
            for i = 1:30
                min = 10000;
                for j = 1:y
                    if (getDist(Charge_x(options(j)),Charge_y(options(j)),Consume_x(i),Consume_y(i))<min)
                        min = getDist(Charge_x(options(j)),Charge_y(options(j)),Consume_x(i),Consume_y(i));
                        a = i;
                        c = j;
                        b = options(j);
                    end
                end

                city(k+hehe,b).i(a,1) = Consum_car(a);

                sum = sum + min*Consum_car(i);
                sum_result(k,1) = sum;
                individual_result(b,a) = 1;
                [sum_result_1(k).x,sum_result_1(k).y] = find(individual_result==1);

            end

        end
         hehe = hehe + k;
        individual_result = 0;
    end
    
end