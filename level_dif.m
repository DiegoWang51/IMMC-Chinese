function [diff,money,force,level] = level_dif(numOfCars)

    if numOfCars == 100000
        level = 0;
        diff = 99750;
        money = 120000;
        
    elseif numOfCars > 250
        level = 6500000; % this is the construction money
        diff = numOfCars - 250;
        money = 1200000;
        
        
    elseif numOfCars > 110
        level = 5300000;
        diff = numOfCars - 110;
        money = 1300000;
        
    elseif numOfCars > 70
        level = 4000000;
        diff = numOfCars - 70;
        money = 500000;
        
    elseif numOfCars > 0
        level = 3500000;
        diff = 100000; % make the station willing to accept cars to prevent negative number of cars
        money = 3500000;
        
    else % strange, number of cars < 0, need cars
        level = 5;
        diff = 100000;
        money = 0;
    end
    
    force = 1 / diff * money;

end