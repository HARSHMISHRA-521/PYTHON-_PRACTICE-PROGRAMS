# The first code snippet is an implementation of the ID3 algorithm for building a decision tree

import pandas as pd
import numpy as np

# Import the necessary libraries

data = pd.DataFrame(
    {
        "age": ["youth", "youth", "middle", "senior", "senior", "senior", "middle", "youth", "youth", "senior", "youth",
                "middle", "middle", "senior"],
        "income": ["high", "high", "high", "medium", "low", "low", "low", "medium", "low", "medium", "medium", "medium",
                   "high", "medium"],
        "student": ["no", "no", "no", "no", "yes", "yes", "yes", "no", "yes", "yes", "yes", "no", "yes", "no"],
        "credit_rating": ["fair", "excellent", "fair", "fair", "fair", "excellent", "excellent", "fair", "fair", "fair",
                          "excellent", "excellent", "fair", "excellent"],
        "class:buys_comp": ["no", "no", "yes", "yes", "yes", "no", "yes", "no", "yes", "yes", "yes", "yes", "yes", "no"]
    },
    columns=["age", "income", "student", "credit_rating", "class:buys_comp"]
)

# Create a DataFrame with the dataset

features = data[["age", "income", "student", "credit_rating"]]
target = data["class:buys_comp"]


# Separate features and target variable

def compute_impurity(feature, impurity_criterion):
    # Compute the impurity of a feature using entropy or gini

    probs = feature.value_counts(normalize=True)

    if impurity_criterion == 'entropy':
        impurity = -1 * np.sum(np.log2(probs) * probs)
    elif impurity_criterion == 'gini':
        impurity = 1 - np.sum(np.square(probs))
    else:
        raise ValueError('Unknown impurity criterion')

    return round(impurity, 3)


# Compute the impurity of a feature based on the specified criterion

def comp_feature_information_gain(data, target, descriptive_feature, split_criterion):
    # Compute the information gain of a descriptive feature

    target_entropy = compute_impurity(data[target], 'entropy')

    entropy_list = []
    weight_list = []

    for level in data[descriptive_feature].unique():
        data_feature_level = data[data[descriptive_feature] == level]
        entropy_level = compute_impurity(data_feature_level[target], split_criterion)
        entropy_list.append(round(entropy_level, 3))
        weight_level = len(data_feature_level) / len(data)
        weight_list.append(round(weight_level, 3))

    feature_remaining_impurity = np.sum(np.array(entropy_list) * np.array(weight_list))
    information_gain = target_entropy - feature_remaining_impurity
    impurity = -1 * np.sum((weight_list) * (np.log2(weight_list)))
    gain = (information_gain) / (impurity)

    return gain


# Compute the information gain of a descriptive feature using the specified split criterion

def ID3(data, originaldata, features, target_attribute_name="class:buys_comp", parent_node_class=None):
    # Implement the ID3 algorithm for building a decision tree

    if len(np.unique(data[target_attribute_name])) <= 1:
        # If all instances have the same class, return the class label
        return np.unique(data[target_attribute_name])[0]
    elif len(data) == 0:
        # If the dataset is empty, return the class label of the majority class in the original dataset
        return np.unique(originaldata[target_attribute_name])[
            np.argmax(np.unique(originaldata[target_attribute_name], return_counts=True)[1])]
    elif len(features) == 0:
        # If there are no more features to split on, return the parent node class
        return parent_node_class
    else:
        parent_node_class = np.unique(data[target_attribute_name])[
            np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])]
        split_criterion = 'entropy'
        item_values = [comp_feature_information_gain(data, target_attribute_name, feature, split_criterion) for feature
                       in features]
        best_feature_index = np.argmax(item_values)
        best_feature = features[best_feature_index]

        tree = {best_feature: {}}
        features = [i for i in features if i != best_feature]

        for value in np.unique(data[best_feature]):
            value = value
            sub_data = data.where(data[best_feature] == value).dropna()

            subtree = ID3(sub_data, data, features, target_attribute_name, parent_node_class)
            tree[best_feature][value] = subtree

        return tree


# Recursive function to build the decision tree using the ID3 algorithm

def train_test_split(data):
    # Split the data into training and testing sets

    training_data = data.iloc[:80].reset_index(drop=True)
    testing_data = data.iloc[80:].reset_index(drop=True)
    return training_data, testing_data


# Split the data into training and testing sets

training_data = train_test_split(data)[0]
testing_data = train_test_split(data)[1]

# Separate the training and testing datasets

from pprint import pprint

tree = ID3(training_data, training_data, training_data.columns[:-1])
pprint(tree)

# Build the decision tree using the training data and print it

new_instance = {
    'age': 'youth',
    'income': '$400',
    'student': 'yes',
    'credit_rating': 'fair'
}


# Define a new instance for classification

def classify_instance(instance, tree):
    # Classify a new instance using the trained decision tree

    for key in list(instance.keys()):
        if key in list(tree.keys()):
            try:
                result = tree[key][instance[key]]
            except:
                return None
            result = tree[key][instance[key]]
            if isinstance(result, dict):
                return classify_instance(instance, result)
            else:
                return result


# Recursive function to classify a new instance using the decision tree

classification = classify_instance(new_instance, tree)
print("Classification:", classification)