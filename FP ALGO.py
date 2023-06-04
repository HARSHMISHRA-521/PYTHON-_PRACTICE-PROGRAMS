# # Explanation
# This code implements the FP-growth algorithm for frequent
#     itemset mining. Here are the main components:
#
# The TreeNode class represents a node in the FP-tree. It has attributes
# for the node's value, count, parent, and children.
#
# The create_tree function builds the FP-tree from a given dataset
# and minimum support. It uses the TreeNode class to represent nodes
# and constructs the tree by traversing the dataset multiple times.
#
# The update_tree function updates the FP-tree with a list of items
# and their count. It recursively adds new nodes and increments the
# count of existing nodes as necessary.
#
# The load_simple_data function provides a simple dataset for testing.
#
# The create_initset function converts a dataset into the initial
# itemset format required by the FP-tree construction.
#
# The ascend_tree function recursively ascends from a leaf node
# to the root, building a prefix path.
#
# The find_prefix_path function finds all prefix paths for a given
#     base path and tree node. It uses the ascend_tree function to
#     construct the paths.
#
# The mine_tree function mines frequent itemsets from the FP-tree using
# recursion. It generates new frequent itemsets by adding a base path
# to the prefix, creates conditional pattern bases, and recursively mines
# them to find more frequent itemsets.
#
# The code concludes by calling mine_tree on the FP-tree and displaying the resulting frequent itemsets.
#
#



class TreeNode:
    def __init__(self, value, count, parent):
        self.value = value
        self.count = count
        self.node = None
        self.parent = parent
        self.children = {}

    def inc(self, count):
        self.count += count

    def disp(self, ind=1):
        """
        Displays the contents of the tree in a hierarchical format.
        """
        print("  " * ind, self.value, " ", self.count)
        for child in self.children.values():
            child.disp(ind + 1)

# Define the root node of the FP-tree
root_node = TreeNode("pyramid", 9, None)
root_node.children["eye"] = TreeNode("eye", 13, None)
root_node.children["phoenix"] = TreeNode("phoenix", 3, None)

def create_tree(dataset, min_support=1):
    """
    Creates the FP-tree from the given dataset using the specified minimum support.
    Returns the root node of the tree and the header table.
    """
    # Build the header table to store the support count of each item
    header_table = {}
    for trans in dataset:
        for item in trans:
            header_table[item] = header_table.get(item, 0) + dataset[trans]

    # Remove items with support below the minimum threshold
    header_table_copy = header_table.copy()
    for k in header_table_copy.keys():
        if header_table[k] < min_support:
            del header_table[k]

    freq_itemset = set(header_table.keys())
    if len(freq_itemset) == 0:
        return None, None

    # Update the header table to include the support count and link to the first occurrence
    for k in header_table:
        header_table[k] = [header_table[k], None]

    # Create the root node of the tree
    ret_tree = TreeNode("Null Set", 1, None)
    # Traverse the dataset to construct the FP-tree
    for trans_set, count in dataset.items():
        local = {}
        for item in trans_set:
            if item in freq_itemset:
                local[item] = header_table[item][0]
        if len(local) > 0:
            # Sort the items in descending order based on support count
            ordered_items = [
                v[0]
                for v in sorted(
                    local.items(),
                    key=lambda p: (
                        p[1],
                        p[0],
                    ),
                    reverse=True,
                )
            ]
            # Update the tree with the ordered items
            update_tree(ordered_items, ret_tree, header_table, count)

    return ret_tree, header_table

def update_tree(items, in_tree, header_table, count):
    """
    Updates the FP-tree with the given items and their count.
    """
    if items[0] in in_tree.children:
        # Item already exists as a child, increment its count
        in_tree.children[items[0]].inc(count)
    else:
        # Create a new child node for the item
        in_tree.children[items[0]] = TreeNode(items[0], count, in_tree)
        # Update the header table link if necessary
        if header_table[items[0]][1] is None:
            header_table[items[0]][1] = in_tree.children[items[0]]
        else:
            update_header(header_table[items[0]][1], in_tree.children[items[0]])
    # Recursively update the remaining items
    if len(items) > 1:
        update_tree(items[1::], in_tree.children[items[0]], header_table, count)

def update_header(node_to_test, target_node):
    """
    Updates the header table node links.
    """
    while node_to_test.node is not None:
        node_to_test = node_to_test.node
    node_to_test.node = target_node

def load_simple_data():
    """
    Loads a simple dataset for testing.
    """
    return [
        ['T100', 'I1', 'I2', 'I5'],
        ['T200', 'I2', 'I4'],
        ['T300', 'I2', 'I3'],
        ['T400', 'I1', 'I2', 'I4'],
        ['T500', 'I1', 'I3'],
        ['T600', 'I2', 'I3'],
        ['T700', 'I1', 'I3'],
        ['T800', 'I1', 'I2', 'I3', 'I5'],
        ['T900', 'I1', 'I2', 'I3']
    ]

def create_initset(dataset):
    """
    Creates the initial itemset from the given dataset.
    """
    out = {}
    for trans in dataset:
        out[frozenset(trans)] = 1
    return out

# Create the initial dataset and build the FP-tree
initset = create_initset(load_simple_data())
fp_tree, header = create_tree(initset, 3)
# Display the FP-tree
fp_tree.disp()

def ascend_tree(leaf_node, prefix_path):
    """
    Ascends from a leaf node to the root, adding the nodes to the prefix path.
    """
    if leaf_node.parent is not None:
        prefix_path.append(leaf_node.value)
        ascend_tree(leaf_node.parent, prefix_path)

def find_prefix_path(base_path, tree_node):
    """
    Finds the prefix paths for a given base path and tree node.
    """
    cond_paths = {}
    while tree_node is not None:
        prefix_path = []
        ascend_tree(tree_node, prefix_path)
        if len(prefix_path) > 1:
            cond_paths[frozenset(prefix_path[1:])] = tree_node.count
        tree_node = tree_node.node
    return cond_paths

def mine_tree(in_tree, header_table, min_support, prefix, freq_item_list):
    """
    Mines the frequent itemsets from the FP-tree using recursion.
    """
    # Sort the items in ascending order based on support count
    big_list = [v[0]
                for v in sorted(header_table.items(), key=lambda p: p[1][0])]

    for base_path in big_list:
        new_freq_set = prefix.copy()
        new_freq_set.add(base_path)
        freq_item_list.append(new_freq_set)
        cond_pattern_bases = find_prefix_path(
            base_path, header_table[base_path][1])
        my_cond_tree, my_head = create_tree(cond_pattern_bases, min_support)

        if my_head is not None:
            print("Conditional tree for: ", new_freq_set)
            my_cond_tree.disp(1)
            mine_tree(my_cond_tree, my_head, min_support,
                      new_freq_set, freq_item_list)

# Perform frequent itemset mining on the FP-tree
freq_items = []
mine_tree(fp_tree, header, 2, set([]), freq_items)
print(freq_items)
