%% Initialization
clear ; close all; clc

% Loading the dataset after importing from Excel
X = Cancerdata(:, 2:31);
Y = Cancerdata(:, 1);
[m, n] = size(X);

% Feature Scaling
[X, mu, sigma] = featureNormalize(X);

% Adding the intercept term
X = [ones(m, 1) X];

% Initialize fitting parameters
initial_theta = zeros(n + 1, 1);

% Compute and display initial cost and gradient
[cost, grad] = costFunction(initial_theta, X, Y);

fprintf('Cost at initial theta (zeros): %f\n', cost);
fprintf('Gradient at initial theta (zeros): \n');
fprintf(' %f \n', grad);

%  Using a built-in function (fminunc) to find the optimal parameters theta.
%  Set options for fminunc
options = optimset('GradObj', 'on', 'MaxIter', 400);

%  Run fminunc to obtain the optimal theta
%  This function will return theta and the cost 
[theta, cost] = fminunc(@(t)(costFunction(t, X, Y)), initial_theta, options);

% Print theta to screen
fprintf('Cost at theta found by fminunc: %f\n', cost);
fprintf('theta: \n');
fprintf(' %f \n', theta);

% Compute accuracy on our training set
p = predict(theta, X);

fprintf('Train Accuracy: %f\n', mean(double(p == Y)) * 100);
fprintf('Expected accuracy (approx): 98.7\n');
fprintf('\n');

