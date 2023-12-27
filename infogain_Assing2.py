import math

insval=-1
def calc_entropy(data):
    """Calculate the entropy of a given dataset."""
    num_instances = len(data)
    label_counts = {}
    for instance in data:
        label = instance[insval]          #here
        if label not in label_counts:
            label_counts[label] = 0
        label_counts[label] += 1
    entropy = 0.0
    for label in label_counts:
        probability = float(label_counts[label]) / num_instances
        entropy -= probability * math.log2(probability)
    return entropy

def calc_info_gain(data, attr_index):
    """Calculate the information gain of a given attribute in the dataset."""
    total_entropy = calc_entropy(data)
    attr_values = {}
    for instance in data:
        attr_value = instance[attr_index]
        if attr_value not in attr_values:
            attr_values[attr_value] = []
        attr_values[attr_value].append(instance)
    attr_entropy = 0.0
    for attr_value in attr_values:
        attr_instances = attr_values[attr_value]
        attr_probability = len(attr_instances) / len(data)
        attr_entropy += attr_probability * calc_entropy(attr_instances)
    info_gain = total_entropy - attr_entropy
    return info_gain

def majority_label(data):
    """Get the majority label in the dataset."""
    label_counts = {}
    for instance in data:
        label = instance[insval]                  #-1 for rid
        if label not in label_counts:
            label_counts[label] = 0
        label_counts[label] += 1
    majority_label = max(label_counts, key=label_counts.get)
    return majority_label

def create_decision_tree(data, attributes):
    """Create a decision tree recursively using the ID3 algorithm."""
    labels = [instance[insval] for instance in data]             #here for rid
    
    # Base case 1: All instances have the same label
    if labels.count(labels[0]) == len(labels):
        return labels[0]
    
    # Base case 2: No more attributes to split on
    if len(attributes) == 0:
        return majority_label(data)
    
    best_attr_index = 0
    best_info_gain = 0.0
    
    # Calculate information gain for each attribute
    for i in range(len(attributes)):
        info_gain = calc_info_gain(data, i)
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_attr_index = i
    
    best_attr = attributes[1]#best_attr_index] #here
    tree = {best_attr: {}}
    remaining_attributes = attributes[:best_attr_index] + attributes[best_attr_index+1:]
    attr_values = set([instance[best_attr_index] for instance in data])
    
    # Recursive construction of subtrees
    for attr_value in attr_values:
        attr_instances = [instance for instance in data if instance[best_attr_index] == attr_value]
        tree[best_attr][attr_value] = create_decision_tree(attr_instances, remaining_attributes)
    
    return tree

def predict_buy_computer(input_values, decision_tree):
    attribute = list(decision_tree.keys())[0]
    attribute_index = attributes.index(attribute)
    attribute_value = input_values[attribute_index]
    subtree = decision_tree[attribute].get(attribute_value)
    if subtree is None:
        return majority_label(data)
    if isinstance(subtree, dict):
        return predict_buy_computer(input_values, subtree)
    else:
        return subtree

data=[
    ['1',   'youth',	    'high',     'no',	'fair',	        'no' ],
    ['2',	'youth',	    'high',     'no',	'excellent',	'no' ],
    ['3',	'middle aged',	'high',	    'no',	'fair',	        'yes'],
    ['4',	'senior',	    'medium',   'no',	'fair',	        'yes'],
    ['5',	'senior',	    'low',	    'yes',	'fair',	        'yes'],
    ['6',	'senior',	    'low',	    'yes',	'excellent',	'no' ],
    ['7',	'middle aged',	'low',	    'yes',	'excellent',	'yes'],
    ['8',	'youth',	    'medium',	'no',	'fair',     	'no' ],
    ['9',	'youth',	    'low',	    'yes',	'fair',     	'yes'],
    ['10',	'senior',	    'medium',	'yes',	'fair',	        'yes'],
    ['11',	'youth',	    'medium',	'yes',	'excellent',	'yes'],
    ['12',	'middle aged',	'medium',	'no',	'excellent',	'yes'],
    ['13',	'middle aged',	'high',	    'yes',	'fair',	        'yes'],
    ['14',	'senior',	    'medium',	'no',	'excellent',	'no' ]
]

attributes=['rid','age','income','student','credit_rating','buys_computer']

decision_tree = create_decision_tree(data, attributes)
print(decision_tree)

input_values = ['youth', 'medium', 'yes', 'fair']
predicted_value = predict_buy_computer(input_values, decision_tree)

print("Input Values:", input_values)
print("Predicted Value:", predicted_value)