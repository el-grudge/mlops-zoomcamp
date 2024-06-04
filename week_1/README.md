In week 1️⃣ of the MLOps Zoomcamp we learned about

⚙️ MLOps: A set of best practices for automating an ML project through its various stages - design, training, and operating, and for collaborating with others.

☁️ We setup our environments. I'm using github codespaces for this course, a new experience to me and my initial impression is positive. It's very easy to setup - just click the "Code" button in your github repo's home page and then "Create codespace on main". It's also easy to connect it to your local vscode, which is more convenient than using the web-based version. It's free for the 60 hours per month, after which you pay-as-you-go (details here). Had some issues with crashing cells in jupyter notebook.

🚕 We used the Yellow taxi data set to build a model that predicts a trip's duration. We started by running some analytics on the current trips, we looked at the average and standard deviation of trips taken in January of 2023, we removed outliers and kept only the trips that had a duration between 1 and 60 minutes

0️⃣1️⃣ Next, we one-hot encoded 2 categorical features, pickup and dropoff using scikit-learn's DictVectorizer. Note: DictVectorizer deals with strings, so make sure that your data has the right type.

📈 We then used these features to train a simple linear regression model and calculated its RMSE on the training and validation datasets. The model's performance was pretty bad, predicting that all trips will take aprox 16 minutes. It's not a great result, but it's a start. We then trained a Lasso regression model, but the results were worse. Feature engineering helped, when combining the pickup and drop-off locations as one feature the RMSE dropped from 11 to 7 when using Lasso regression.

🚀 Finally, we saved the model binary as a pickle file to be deployed later.

👉 Checkout my code here

#mlops_zoomcamp #git_codespaces #linear_regression #machine_learning #learning_in_public

