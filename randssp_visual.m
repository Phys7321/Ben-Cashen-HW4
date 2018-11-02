clear all;

N = 10000;
r = randssp(N,1);
for i = 1:N/3
    x(i) = r(2*i);
    y(i) = r(2*i - 1);
    z(i) = r(2*i + 1);
end

plot3(x,y,z,'o')    % Upon rotation of 3D plot, regularity is apparent (rng does not pass visual test) 
rotate3d on
