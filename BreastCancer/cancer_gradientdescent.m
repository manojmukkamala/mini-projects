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
[cost] = costFunction(initial_theta, X, Y);
fprintf('Cost at initial theta (zeros): %f\n', cost);

% Choose some alpha value & number of itertaions
alpha = 0.06;
num_iters = 650;

% Running Gradient Descent
[theta, J_history] = gradientDescentMulti(X, Y, initial_theta, alpha, num_iters);

% Print theta to screen
fprintf('Cost at theta found by Gradient descent: %f\n', J_history(num_iters));
fprintf('theta: \n');
fprintf(' %f \n', theta);

% Compute accuracy on our training set
p = predict(theta, X);

fprintf('Train Accuracy: %f\n', mean(double(p == Y)) * 100);
fprintf('Expected accuracy (approx): 98.5\n');
fprintf('\n');




