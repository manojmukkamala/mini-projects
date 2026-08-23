% Reading the data
X = DeathRateLinearRegdataset(:,2:16);
Y = DeathRateLinearRegdataset(:,17);
m = length(Y);

% Scale features and set them to zero mean
[X mu sigma] = featureNormalize(X);

% Add intercept term to input
% Remember, intercept should not be normalized.
X = [ones(m,1) X];

% Splitting the train and test sets (I used 75% to train, 25% to test)
r = randperm(m);
Xtrain = X(r(1:45),:);
Xtest = X(r(46:60),:);
Ytrain = Y(r(1:45),:);
Ytest = Y(r(46:60),:);

% Choosing the learning rate alpha and number of iterations
% I have tried various combinations of alpha and num_iters but the below
% values worked well with my data set.
alpha = 0.3;
num_iters = 1500;

% Initialize theta
theta = zeros(size(Xtrain,2),1);

% Computing the initial cost
computeCostMulti(Xtrain,Ytrain,theta);

% Run Gradient Descent
[theta, J_history] = gradientDescentMulti(Xtrain, Ytrain, theta, alpha, num_iters);

% Checking cost w.r.t number of iterations
plot(J_history);

% Prediction over the test set
pred = Xtest * theta;

% Calculating the error between prediction and actual values
error = Ytest - pred;
error = error.*error;
error = sqrt(error);

% The sum of all the errors is our cost.

% We can do the above exercise using normal equations as well
theta = normalEqn(Xtrain, Ytrain);
pred = Xtest*theta;
error = Ytest - pred;
error = error.*error;
error = sqrt(error);
sum(error)










