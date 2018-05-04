clear;
clc;
Pos = xlsread('Charging.xlsx');
load Charging.xlsx;

Pos(:,2) = 700 - Pos(:,2);
Pos(:,4) = 700 - Pos(:,4);

Charging_info.posx = Pos(:,1);
Charging_info.posy = Pos(:,2);
Charging_info.sumcar = 0;

Consum_info.posx = Pos(:,3);
Consum_info.posx = Pos(:,4);
Consum_info.car = Pos(:,5);

x = Charging_info.posx(index);
y = Charging_info.posy(index);

[diff,money,level] = level_dif(num);
[status] = getStatus(level,num);
%status = 1;
%wanting output

