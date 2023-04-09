clear
clc
close all

counter = 0;
iterations = 2500;
triangle_points = [-1 1 0;0 0 1];
scatter(triangle_points(1,:),triangle_points(2,:),'filled','k')
hold on

x_min = -1;
x_max = 1;

x_rand = (x_max-x_min)*rand(1,1) + x_min;

y_min = 0;

if x_rand < 0
    y_max = x_rand + 1;
elseif x_rand > 0
    y_max = -x_rand + 1;
else
    print('error')
end

y_rand = (y_max-y_min)*rand(1,1) + y_min;

scatter(x_rand, y_rand, 'r', 'filled')

X = [];
Y = [];

while counter < iterations
    random_corner = randi([1 3]);
    corner  = [triangle_points(:,random_corner)];
    counter = counter + 1;
    x_new = (x_rand + corner(1)) / 2;
    y_new = (y_rand + corner(2)) / 2;
    X = [X x_new];
    Y = [Y y_new];
    x_rand = x_new;
    y_rand = y_new;
end

scatter(X,Y,'filled','b')
axis off
hold off
    
