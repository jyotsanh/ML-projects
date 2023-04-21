# SMS Spam Classifier Model

This project involves building a machine learning model that classifies SMS messages as either spam or not spam (ham) using the TF-IDF vectorizer.

## Data

The data used for training and testing the model is the [SMS Spam Collection Dataset](https://www.kaggle.com/uciml/sms-spam-collection-dataset), which contains a collection of over 5,500 SMS messages labeled as either spam or ham. The dataset is available on Kaggle and can be downloaded from the link provided.

## Dependencies

The following Python libraries are required to run the code in this repository:
- numpy
- pandas
- sklearn
- nltk

## Usage

1. Clone the repository using the following command:

git clone https://github.com/Jyotsan-Hamal/ML-projects/SMS-Spam-Classifier.git


2. Download the dataset from the link provided above and place it in the same directory as the cloned repository.

3. Open the `sms-spam-detection.ipynb` notebook using Jupyter Notebook or any other compatible environment.

4. Run the code cells in the notebook to train and test the model. The trained model will be saved in a file named `model.pkl`.

## Improving Model Accuracy

Here are some ways to potentially improve the accuracy of the SMS spam classifier model:

- **Feature engineering**: In addition to using the TF-IDF vectorizer, try creating additional features such as message length, number of exclamation marks, and other relevant features to see if they improve the model's accuracy.

- **Hyperparameter tuning**: Experiment with different values for hyperparameters such as the regularization parameter in the logistic regression model or the number of estimators in the random forest model.

- **Ensemble methods**: Try combining the predictions of multiple models such as logistic regression, random forest, and support vector machines to see if the ensemble model performs better than individual models.

- **Deep learning**: Consider using deep learning models such as recurrent neural networks or convolutional neural networks to classify SMS messages as spam or ham.

## Conclusion

In this project, we built a machine learning model that classifies SMS messages as spam or ham using the TF-IDF vectorizer. The model achieved an accuracy of 97% and precision score of 99%, but there are still opportunities to improve its accuracy using the techniques mentioned above.
