In week 6️⃣ of the MLOps Zoomcamp we learned about

🧪 Unit tests

Unit tests are tests that validate the functionality of specific functions. A unit tests is a simple assert statement, the test passes if the statement is true and fails if its false. When creating such tests, you might need to refactor your code (i.e. restructure it in a modular way), and avoid using global state variables. We used pytest for building our unit tests, and setup our VSCode environment to run them.

🔄 Integration tests

Integration tests test the code in its entirety. Here, we test our model by using some sample data and comparing the actual prediction with the expected prediction. The tests are run in a docker test file, but this could be replaced with any other standalone file. We also want to test any cloud services such as AWS s3 or kinesis, and for that we use [localstack](https://github.com/localstack/localstack) (note: localstack works mainly with AWS, look for relevant emulaters for other cloud providers). Localstack simulates the cloud services locally, which allows us to test the service without incurring additional costs.

📏 Code quality

We leared how to improve the quality of our code using linting and formatting. Linting is the process of analyzing the code to flag errors (either programming or stylistic), bugs, and other questionable practices, and we used pylint to lint our code (alternative linters exist). Formatting on the other hand, is use of a consistent code style. Services like black and isort can be used to achieve that.

🚀 Testing a production model
we took the ride duration prediction model that we deployed in batch mode in homework 4 and improved its reliability with unit and integration tests. You can view the code [here](https://github.com/el-grudge/mlops-zoomcamp/tree/main/week_6).

#mlops_zoomcamp #testing #unit_tests #pytest #integration_tests #localstack #learning_in_public
