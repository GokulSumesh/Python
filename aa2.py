class SimpleList:
    def __init__(self):
        self.items = []  # Initialize an empty list

    def add(self, item):
        """Adds an item to the list."""
        self.items.append(item)

    def delete(self, item):
        """Deletes an item from the list if it exists."""
        if item in self.items:
            self.items.remove(item)

    def update(self, old_item, new_item):
        """Updates an item in the list."""
        if old_item in self.items:
            index = self.items.index(old_item)
            self.items[index] = new_item

    def modify(self, old_item, new_item):
        """Modifies an item in the list (similar to update)."""
        self.update(old_item, new_item)

    def display(self):
        """Displays the current list."""
        print(self.items)


# Example usage:
simple_list = SimpleList()

# Add items
simple_list.add("Apple")
simple_list.add("Banana")
simple_list.add("Cherry")
simple_list.display()

# Delete an item
simple_list.delete("Banana")
simple_list.display()

# Update an item
simple_list.update("Apple", "Grapes")
simple_list.display()

# Modify an item (same as update in this case)
simple_list.modify("Cherry", "Peach")
simple_list.display()
