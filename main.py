class Pattern:
    def __init__(self, itemset: list, support=0):
        self.itemset = itemset
        self.support = support

    def __lt__(self, other):
        return self.itemset < other.itemset

    def __le__(self, other):
        return self.itemset <= other.itemset

    def __gt__(self, other):
        return self.itemset > other.itemset

    def __ge__(self, other):
        return self.itemset >= other.itemset

    def __str__(self):
        return str(self.itemset)


class Apriori:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.dataset = []
        self.n = 0
        self.all_items = []
        self.candidates = []
        self.l = []
        self.c_series = {}
        self.l_series = {}
        self.min_support_threshold_percentage = 90
        self.min_support_threshold_count = (self.min_support_threshold_percentage / 100) * self.n

    def preprocess_data(self):
        with open(self.dataset_path, 'r') as fptr:
            self.n = 0

            while True:
                line = fptr.readline()

                if not line:
                    break

                self.n += 1
                token = line.split()
                token.sort()
                self.dataset.append(token)

        self.min_support_threshold_count = (self.min_support_threshold_percentage / 100) * self.n

    def calculate_support(self, item: Pattern):
        for data in self.dataset:
            if set(item.itemset).issubset(data):
                item.support += 1

    def get_all_items(self):
        for i in self.dataset:
            for j in i:
                if j not in self.all_items:
                    self.all_items.append(j)
                    




if __name__ == '__main__':
    # obj1 = Pattern(itemset=[1, 2, 3], support=1)
    # obj2 = Pattern(itemset=[1, 3, 4], support=1)
    # obj3 = Pattern(itemset=[1, 3, 4], support=1)
    # obj4 = Pattern(itemset=[1, 4, 5], support=1)
    #
    # custom_objects = [obj1, obj2, obj3, obj4]
    # sorted_objects = sorted(custom_objects)
    # print([obj.itemset for obj in sorted_objects])

    # print(str([1, 2, 3]))
    print(['a', 'b', 'c'] > ['a', 'b', 'd'])
