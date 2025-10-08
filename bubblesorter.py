class BubbleSorter:
    def __init__(self, data):
        self.data = data

    def show_data(self):
        print("ข้อมูล:", self.data)

    def bubble_sort(self):
        n = len(self.data)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]

# โปรแกรมทดสอบ
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    sorter = BubbleSorter(numbers)

    print("ก่อนเรียงลำดับ:")
    sorter.show_data()

    sorter.bubble_sort()

    print("หลังเรียงลำดับ:")
    sorter.show_data()
