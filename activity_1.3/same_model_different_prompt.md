# Overview
Using **llama3.2** to understand how the same model's output changes depending on how the prompt is structured.


## Step 1: Minimal prompt
**Prompt**
Explain machine learning.

**Output**
Machine learning (ML) is a subset of artificial intelligence (AI) that involves training algorithms to learn from data, make predictions, and improve their performance over time. The goal of machine learning is to enable computers to automatically improve their performance on a specific task, without being explicitly programmed.

Here's a simplified overview of how machine learning works:

1. **Data Collection**: A large dataset is gathered, which contains the information that the algorithm will learn from. This dataset can come from 
various sources, such as images, text, audio, or sensor data.
2. **Data Preprocessing**: The collected data is preprocessed to prepare it for the algorithm. This may involve cleaning, transforming, and normalizing 
the data to ensure it's in a suitable format.
3. **Model Selection**: A suitable machine learning algorithm is chosen based on the type of problem and data. Some common algorithms include supervised 
learning, unsupervised learning, and deep learning.
4. **Training**: The algorithm is trained on the preprocessed data, allowing it to learn patterns, relationships, and decisions from the data. This 
process is also known as "learning from data."
5. **Evaluation**: The trained algorithm is evaluated on a separate test dataset to assess its performance and accuracy.
6. **Deployment**: The trained algorithm is deployed in a production environment, where it can be used to make predictions or take actions based on new, 
unseen data.

There are several types of machine learning:

1. **Supervised Learning**: The algorithm learns from labeled data, where the correct output is already known. Examples include image classification, 
sentiment analysis, and speech recognition.
2. **Unsupervised Learning**: The algorithm learns from unlabeled data, where the correct output is not known. Examples include clustering, 
dimensionality reduction, and anomaly detection.
3. **Deep Learning**: A subset of machine learning that uses neural networks with multiple layers to learn complex patterns in data. Examples include 
image recognition, natural language processing, and speech recognition.

Some key concepts in machine learning include:

1. **Bias-Variance Tradeoff**: The balance between the complexity of the model and the amount of error it produces.
2. **Regularization**: Techniques used to prevent overfitting, such as dropout, L1, and L2 regularization.
3. **Hyperparameter Tuning**: The process of adjusting model parameters to optimize performance.
4. **Ensemble Methods**: Combining the predictions of multiple models to improve overall performance.

Machine learning has numerous applications across various industries, including:

1. **Computer Vision**: Image recognition, object detection, facial recognition, and autonomous vehicles.
2. **Natural Language Processing**: Sentiment analysis, text classification, language translation, and chatbots.
3. **Speech Recognition**: Speech-to-text systems, voice assistants, and voice-controlled interfaces.
4. **Predictive Maintenance**: Predicting equipment failures, maintenance scheduling, and quality control.
5. **Recommendation Systems**: Personalized product recommendations, content filtering, and user behavior analysis.

In summary, machine learning is a powerful technology that enables computers to learn from data, make predictions, and improve their performance over 
time. Its applications are diverse and continue to grow, with new use cases emerging in various industries.


## Step 2: Audience and format constraints
**Prompt**
Explain machine learning to a 12-year-old using a cooking analogy in fewer than 100 words.

**Output**
Imagine you want to teach a robot to make the perfect chocolate chip cookie. You show it many pictures of cookies and tell it what makes a great cookie (soft center, crunchy edges, etc.). At first, the robot makes some weird cookies, but you keep showing it more pictures and giving it feedback. As the robot practices, it starts to learn from its mistakes and get better and better at making perfect cookies. Machine learning is like teaching the robot to make perfect cookies, but instead of using pictures, it uses data and computers to learn from it.


## Step 3: Role, audience, and structure
**Prompt**
You are a university lecturer teaching Master's students in Data Science.
Explain machine learning using a practical example.
Include supervised, unsupervised and reinforcement learning.
Use a table.

**Output**
Welcome, students, to today's lecture on machine learning. Machine learning is a crucial aspect of data science, and I'm excited to dive into a 
practical example to illustrate the different types of machine learning.

**Practical Example:**

Let's say we're a food delivery company, and we want to predict the likelihood of a customer ordering a pizza based on their past orders. We have a dataset of customer information, including their order history, preferences, and demographic details.

**Supervised Learning:**

Our goal is to build a model that can predict the likelihood of a customer ordering a pizza based on their past orders. We have a labeled dataset, where each customer is labeled as either a "pizza lover" or not. We'll use a supervised learning approach to train a model.

Our model is trained on the dataset using a supervised learning algorithm, such as logistic regression or decision trees. The goal is to minimize the error between our predicted probabilities and the actual labels.

**Unsupervised Learning:**

Now, let's say we want to analyze our customer data to identify patterns and clusters. We don't have labeled data, so we'll use an unsupervised learning approach. We'll use techniques like k-means clustering or hierarchical clustering to group customers based on their demographic details and order history.

For example, we might identify a cluster of customers who frequently order pizzas, followed by a cluster of customers who rarely order pizzas. This information can help us target our marketing efforts and personalize our service.

**Reinforcement Learning:**

In our food delivery company, we also want to optimize our delivery routes to minimize costs and maximize customer satisfaction. We'll use reinforcement learning to train an agent to navigate our delivery routes.

The agent will learn to evaluate the quality of each possible route based on factors like distance, traffic, and customer satisfaction. Over time, the agent will adjust its route planning to optimize its performance, and we'll see improvements in our delivery efficiency and customer satisfaction.

**Table: Machine Learning Types**

| Type of Machine Learning | Description | Application |
| --- | --- | --- |
| Supervised Learning | Predicting outcomes based on labeled data | Pizza ordering prediction, image classification |
| Unsupervised Learning | Discovering patterns and clusters in unlabeled data | Customer segmentation, market analysis |
| Reinforcement Learning | Training agents to optimize performance in complex environments | Delivery route optimization, game playing |

In summary, machine learning is a powerful tool that can be applied to various problems in data science. By understanding the different types of machine learning, we can choose the right approach for our specific problem and develop effective solutions.