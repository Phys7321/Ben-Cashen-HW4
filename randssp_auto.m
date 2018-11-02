clear all;

N = 10000;
r = randssp(N,1);
for i = 2:N
S(i) = (r(i-1)*r(i));
C = (sum(S))/N;
end

disp(C);

% Integral for comparison is equal to 0.25 (integral of xydxdy from 0 to 1
% w/ P normalized to equal 1 between boundaries) therefore
% autocorrelation test gives passing result