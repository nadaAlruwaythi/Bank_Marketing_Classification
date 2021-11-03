# Bank_Marketing_Classification(MVP)

### Goal the project:
> The primary goal of the project is to predict whether or not a customer will subscribe to a service offered by the bank.
### Findings:
> So far in the project we found out that our target column has a very large gap between the values of ‘yes’ and ‘no’. in the graph below we can see that gap. We resolved this problem by using the over sample and smote. The result of the over sampler was better, and we decided to go with the result from the over sampler. The chart indicates our target column data before solving the imbalance. 
The percent of ‘no’ vs. ‘yes’ are %88 vs. %11, that how we know for sure that we have an imbalance in the target column.

![image](https://user-images.githubusercontent.com/67028272/140027197-c71b3aef-2ab5-43b3-9b3f-65c898cd14cf.png)


> In the graph below we trained our training portion of the data with the random forest classifier and plotted the area under the curve, we can see that the score of the area under the curve is %91 which is considered good. To elaborate, the meaning of the score 91 is that the random forest classifier has successfully classified class 0 as 0 and class 1 as 1 with an accuracy of %91. Noting that we still have a margin of error of %9. 
Currently, we are working to improve the features we included in training the model and thinking of ways that can improve the score even more.

![image](https://user-images.githubusercontent.com/67028272/140031497-a9b1f1ce-3cc3-4d02-bf78-2410bce3bfe4.png)

