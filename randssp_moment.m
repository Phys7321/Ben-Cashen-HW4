clear all;

k = 1;
I = 1/(1+k);    % I = 0.5 for choice of k (compare to S)

for i = 1:4
    N(i) = 10^i;
    r = randssp(N(i),1);
    x = r.^k;
    S(i) = sum(x)/N(i);
    dev(i) = abs(I - S(i));
end

n = linspace(10,10000,1000);
y = 1./sqrt(n);
disp(S);    % Value of S gives passing result (compare to I = 0.5)

plot(N,dev,'-',n,y,'-')     % Deviation from true value scales as 1/sqrt(N), giving passing result
title('Deviation vs. N')
xlabel('Number of points (N)')
ylabel('Deviation from integral')
legend('Deviation','1/sqrt(N)','Location','best')