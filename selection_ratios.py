
import math
from collections import Counter


def entropy(data):
    # Extract the labels from the instances
    labels = [instance['label'] for instance in data]

    # Count the occurrences of each label
    label_counts = Counter(labels)

    # Calculate the total number of instances
    total_instances = len(labels)

    # Initialize entropy value
    entropy_value = 0

    # Iterate over label counts
    for count in label_counts.values():
        # Calculate the probability of each label
        probability = count / total_instances

        # Update entropy using the formula
        entropy_value -= probability * math.log2(probability)

    return entropy_value


def information_gain(data, attribute):
    # Get unique values of the attribute in the dataset
    attribute_values = set([instance[attribute] for instance in data])

    # Calculate the total number of instances
    total_instances = len(data)

    # Initialize attribute entropy
    attribute_entropy = 0

    # Iterate over attribute values
    for value in attribute_values:
        # Create a subset of instances with the current attribute value
        subset = [instance for instance in data if instance[attribute] == value]

        # Calculate the entropy of the subset
        subset_entropy = entropy(subset)

        # Calculate the number of instances in the subset
        subset_instances = len(subset)

        # Update attribute entropy using the weighted average of subset entropies
        attribute_entropy += (subset_instances / total_instances) * subset_entropy

    # Calculate and return the information gain
    return entropy(data) - attribute_entropy


def majority_vote(data):
    # Extract the labels from the instances
    labels = [instance['label'] for instance in data]

    # Count the occurrences of each label
    label_counts = Counter(labels)

    # Get the label with the highest count (majority label)
    majority_label = label_counts.most_common(1)[0][0]

    return majority_label


def get_best_attribute(data, attributes):
    # Initialize variables to track the best gain and attribute
    best_gain = 0
    best_attribute = None

    # Iterate over the attributes
    for attribute in attributes:
        # Calculate the information gain for the current attribute
        gain = information_gain(data, attribute)

        # Check if the gain is better than the previous best gain
        if gain > best_gain:
            # Update the best gain and attribute
            best_gain = gain
            best_attribute = attribute

    # Return the best attribute
    return best_attribute


def create_decision_tree(data, attributes):
    # Extract the labels from the instances
    labels = [instance['label'] for instance in data]

    # Base cases for recursion
    # If all instances have the same label, return that label
    if len(set(labels)) == 1:
        return labels[0]

    # If there are no attributes left to split on, return the majority label
    if len(attributes) == 0:
        return majority_vote(data)

    # Get the best attribute to split on
    best_attribute = get_best_attribute(data, attributes)

    # Create a new tree node with the best attribute as the key
    tree = {best_attribute: {}}

    # Get the unique values of the best attribute in the dataset
    attribute_values = set([instance[best_attribute] for instance in data])

    # Remove the best attribute from the list of attributes for the next recursion
    remaining_attributes = [attr for attr in attributes if attr != best_attribute]

    # Recursively create subtrees for each attribute value
    for value in attribute_values:
        # Create a subset of instances with the current attribute value
        subset = [instance for instance in data if instance[best_attribute] == value]

        # Create a subtree by recursively calling the create_decision_tree function
        subtree = create_decision_tree(subset, remaining_attributes)

        # Add the subtree to the current tree node
        tree[best_attribute][value] = subtree

    return tree


def classify(instance, tree):
    # Check if the current node is a leaf node (a string label)
    if isinstance(tree, str):
        return tree

    # Get the attribute and value for the current node
    attribute = list(tree.keys())[0]
    value = instance[attribute]

    # Check if the instance's attribute value is present in the tree
    if value not in tree[attribute]:
        return None

    # Recursively classify the instance using the appropriate subtree
    subtree = tree[attribute][value]
    return classify(instance, subtree)


def evaluate_accuracy(data, tree):
    # Initialize variables for correct predictions and total instances
    correct_predictions = 0
    total_instances = len(data)

    # Iterate over the instances in the data
    for instance in data:
        # Classify the instance using the tree
        prediction = classify(instance, tree)

        # Check if the predicted label matches the actual label
        if prediction == instance['label']:
            correct_predictions += 1

    # Calculate and return the accuracy
    accuracy = correct_predictions / total_instances
    return accuracy


# Example usage
data = [
    {'outlook': 'sunny', 'temperature': 'hot', 'humidity': 'high', 'windy': False, 'label': 'no'},
    {'outlook': 'sunny', 'temperature': 'hot', 'humidity': 'high', 'windy': True, 'label': 'no'},
    {'outlook': 'overcast', 'temperature': 'hot', 'humidity': 'high', 'windy': False, 'label': 'yes'},
    {'outlook': 'rain', 'temperature': 'mild', 'humidity': 'high', 'windy': False, 'label': 'yes'},
    {'outlook': 'rain', 'temperature': 'cool', 'humidity': 'normal', 'windy': False, 'label': 'yes'},
    {'outlook': 'rain', 'temperature': 'cool', 'humidity': 'normal', 'windy': True, 'label': 'no'},
    {'outlook': 'overcast', 'temperature': 'cool', 'humidity': 'normal', 'windy': True, 'label': 'yes'},
    {'outlook': 'sunny', 'temperature': 'mild', 'humidity': 'high', 'windy': False, 'label': 'no'},
    {'outlook': 'sunny', 'temperature': 'cool', 'humidity': 'normal', 'windy': False, 'label': 'yes'},
    {'outlook': 'rain', 'temperature': 'mild', 'humidity': 'normal', 'windy': False, 'label': 'yes'},
    {'outlook': 'sunny', 'temperature': 'mild', 'humidity': 'normal', 'windy': True, 'label': 'yes'},
    {'outlook': 'overcast', 'temperature': 'mild', 'humidity': 'high', 'windy': True, 'label': 'yes'},
    {'outlook': 'overcast', 'temperature': 'hot', 'humidity': 'normal', 'windy': False, 'label': 'yes'},
    {'outlook': 'rain', 'temperature': 'mild', 'humidity': 'high', 'windy': True, 'label': 'no'}
]

attributes = ['outlook', 'temperature', 'humidity', 'windy']

# Build the decision tree
tree = create_decision_tree(data, attributes)

# Print the decision tree
print(tree)

# Test the decision tree with a sample instance
test_instance = {'outlook': 'overcast', 'temperature': 'hot', 'humidity': 'normal', 'windy': False}
classification = classify(test_instance, tree)
print('Classification:', classification)

# Evaluate the accuracy of the decision tree
accuracy = evaluate_accuracy(data, tree)
print('Accuracy:', accuracy)