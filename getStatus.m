function [status] = getStatus(number)
    if(number >= 100000 || number == 0)
        status = 0;
    elseif(number <= 20)
        status = 1;
        %wanting output
    elseif(number>30 && number<50)
        status = -1;
    else
        status = 0;
    end
end