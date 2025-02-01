class user:
    l = []

    def add(self, *args):
        # Using *args to allow multiple items to be added at once
        self.l.extend(args)

    def delete(self, a):
        if a in self.l:
            self.l.remove(a)

    def update(self, old_value, new_value):
        if old_value in self.l:
            # Update the first occurrence of old_value
            index = self.l.index(old_value)
            self.l[index] = new_value

    def display(self):
        print(self.l)


a = user()
a.add("apple", "banana", "apple")
a.delete("banana")
a.update("apple", "grape")
a.display()
