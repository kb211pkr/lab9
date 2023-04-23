def main():
    separator = '\n' + '-' * 30 + '\n'
    globals_ = globals()

    for i in range(1, 5):
        print(separator)
        globals_.get(f'task{i}')()


def task1():
    class Alphabet:
        lang = 'українська'
        letters = (
            'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї',
            'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
            'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я'
        )

        def __init__(self, lang=lang, letters=letters):
            self.lang = lang
            self.letters = letters

        def print_alphabet(self):
            print(f'{self.lang} => {self.letters}')

        def letters_num(self):
            return len(self.letters)

        def is_ua_lang(self, text):
            for letter in text.lower():
                if letter not in self.__class__.letters:
                    return False

            return True

    class EngAlphabet(Alphabet):
        lang = 'українська'
        letters = (
            'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж',
            'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о',
            'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я'
        )

        __en_letters_num = len(letters)

        def __innit__(self, lang=lang, letters=letters):
            super().__init__(lang, letters if type(letters) is list else [*letters])
            self.__en_letters_num = len(self.letters)

        def is_en_lang(self, text):
            return bool(sum(map(text.lower().count, self.letters)))

        def letters_num(self):
            return self.__en_letters_num

        @staticmethod
        def example():
            return 'This is an example of english string'

    lettersEng = 'abcdefghijklmnopqrstuvwxyz'
    testEng = EngAlphabet('english', lettersEng)
    print(f'Кількість букв англ -> {testEng.letters_num()}')
    print(f'J -> {testEng.is_en_lang("J")}')
    print(f'Щ -> {testEng.is_ua_lang("Щ")}')
    print(f'Example -> {EngAlphabet.example()}')


def task2():
    class House:
        def __init__(self, area=100, price=1000000):
            self._area = area
            self._price = price

        def final_price(self, discount=10):
            return self._price * (1 - (discount / 100))

    class SmallHouse(House):
        def __init__(self, area=40, price=400000):
            super().__init__(area, price)

    class Human:
        default_name = "Karina"
        default_age = 18

        def __init__(self, name=default_name, age=default_age, money=0, house=None):
            if house is None:
                house = [House()]

            self.name = name
            self.age = age
            self.__money = money
            self.__house = house

        def info(self):
            print(f'Name: {self.name}')

            print(f'Age: {self.age}')
            print(f'House: {[i._area for i in self.__house]} m2')
            print(f'Money: {self.__money} $')

        @staticmethod
        def default_info():
            print(f'Name: {Human.default_name}')

            print(f'Age: {Human.default_age}')

        def __make_deal(self, house, price):
            self.__money -= price

            self.__house.append(house)

        def earn_money(self, money):
            self.__money += money

            print(f'You have => {self.__money} $')

        def buy_house(self, house, discount):
            if self.__money >= house.final_price(discount):
                self.__make_deal(house, house.final_price(discount))

                print('Deal is done')

            else:
                print(f'Not enough money => {house.final_price(discount) - self.__money} $')

    Human.default_info()
    human = Human()
    print()
    human.info()
    small_house = SmallHouse()
    print()
    human.buy_house(small_house, 10)
    print()
    human.earn_money(1000000)
    print()
    human.buy_house(small_house, 10)
    print()
    human.info()


def task3():
    class Apple:
        states = {0: 'Відсутнє', 1: 'Цвітіння', 2: 'Зелене', 3: 'Червоне'}

        def __init__(self, _index, _state=0):
            self._index = _index
            self._state = _state

        def grow(self):
            if not self.is_ripe():
                self._state += 1

        def is_ripe(self):
            return True if self._state == 3 else False

        def give_away(self):
            self._state = 0

        def get_state(self):
            return Apple.states[self._state]

        def __str__(self):
            return f'Яблуко #{self._index} є {self.get_state()}'

    class AppleTree:
        def __init__(self, count=10):
            self.apples = [Apple(i) for i in range(count)]

        def grow_all(self):
            for apple in self.apples:
                apple.grow()

        def all_are_ripe(self):
            return all([apple.is_ripe() for apple in self.apples])

        def get_states(self):
            return self.apples[0].get_state()

        def give_away_all(self):
            self.apples = [Apple(i) for i in range(len(self.apples))]

    class Gardener:
        def __init__(self, name, _tree=AppleTree()):
            self.name = name
            self._tree = _tree

        def work(self):
            print(f'Садівник {self.name} працює')

            self._tree.grow_all()

        def harvest(self):
            if self._tree.all_are_ripe():
                self._tree.give_away_all()

                print(f'Садівник {self.name} зібрав усі яблука')
            else:
                print(f'Садівник {self.name} не зібрав яблука')

        def get_count_apples(self):
            return len(self._tree.apples)

        def get_states(self):
            return self._tree.get_states()

        @staticmethod
        def apple_base(gardener):
            print(f'Кількість яблук: {gardener.get_count_apples()}')
            print(f'Стан яблук: {gardener.get_states()}')

    apple1 = Apple(0)
    apple2 = Apple(1)
    print(apple1)
    print(apple2)
    apple_tree = AppleTree(20)
    gardener = Gardener('Остап', apple_tree)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()
    Gardener.apple_base(gardener)


def task4():
    import csv
    import os
    import matplotlib.pyplot as plt
    import codecs

    class KmrCsv:
        def __init__(self, num=1, ref='files\\marks2.lab11.csv'):
            self.ref = ref
            self.num = num

        def set_ref(self, ref):
            self.ref = ref

        def set_num(self, num):
            self.num = num

        def __str__(self):
            return f'Файл: {self.ref}\nНомер: {self.num}'

    class Statistic:
        def __init__(self, KmrCsv):
            self.KmrCsv = KmrCsv

        def avg_stat(self):
            correct = ()

            with open(self.KmrCsv.ref, 'r') as file:
                allStudents = len(list(csv.reader(file)))
                for i in range(20):
                    true = 0
                    file.seek(0)
                    for row in csv.reader(file):
                        try:
                            if float(row[5 + i].replace(',', '.')) == 0.5:
                                true += 1
                        except ValueError:
                            true += 0
                    file.seek(0)
                    percent = round((true * 100) / allStudents, 2)
                    correct += (percent,)
            return correct

        def marks_stat(self):
            rating = {}

            with open(self.KmrCsv.ref, 'r') as file:
                for row in csv.reader(file):
                    rating[row[4]] = 0
                file.seek(0)
                for row in csv.reader(file):
                    rating[row[4]] += 1
            return rating

        def marks_per_time(self):
            with open(self.KmrCsv.ref, 'r') as file:
                file.seek(0)
                bestRating = {}
                for row in csv.reader(file):
                    try:
                        time = int(row[3][:2]) + int(row[3][-9:-7]) / 60
                    except:
                        time = int(row[3][:2])
                    rating = float(row[4].replace(',', '.'))
                    bestRating[row[0]] = round(rating / time, 2)
                return bestRating

        def best_marks_per_time(self, bottom_margin=0, top_margin=20):
            with open(self.KmrCsv.ref, 'r') as file:
                file.seek(0)
                bestRating = ()
                for row in csv.reader(file):
                    try:
                        time = int(row[3][:2]) + int(row[3][-9:-7]) / 60
                    except:
                        time = int(row[3][:2])
                    rating = float(row[4].replace(',', '.'))
                    if bottom_margin <= rating <= top_margin:
                        bestRating += ((row[0], rating, round(rating / time, 2)),)

                bestRating = sorted(bestRating, key=lambda x: x[2], reverse=True)
                return bestRating[:5]

    class Plots:
        def __init__(self, Statistic, path="files\\graphs"):
            self.Statistic = Statistic
            self.set_cat(path)
            self.path = path

        def set_cat(self, path):
            if not os.path.exists(path):
                os.mkdir(path)
                KmrWork.cat = path

        def avg_plot(self):
            correctPercent = self.Statistic.avg_stat()
            plt.xlabel('Відсотки правильних відповідей')
            plt.title('Статистика відповідей')
            plt.ylabel('Номер питання')
            plt.hist(correctPercent)
            plt.savefig(f'{self.path}\\[{self.Statistic.KmrCsv.num}] Відсотки правильних відповідей.png')
            plt.show()

        def marks_plot(self):
            rating = self.Statistic.marks_stat()
            plt.figure(figsize=(10, 6))
            plt.title('Статистика оцінок')
            plt.xlabel('Оцінка')
            plt.ylabel('Кількість студентів')
            plt.bar(rating.keys(), rating.values())
            plt.savefig(f'{self.path}\\[{self.Statistic.KmrCsv.num}] Розподіл оцінок.png')
            plt.show()

        def best_marks_plot(self):
            bestRating = self.Statistic.best_marks_per_time()
            plt.title('Статистика п\'яти найкращих оцінок')
            plt.xlabel('Студент')
            plt.ylabel('Оцінка/час')
            plt.bar([i[0][:5] + '...' for i in bestRating], [i[-1] for i in bestRating])
            plt.savefig(f'{self.path}\\[{self.Statistic.KmrCsv.num}] Кращі оцінки.png')
            plt.show()

    class KmrWork(KmrCsv, Statistic, Plots):
        kmrs = {1: 'files\\marks2.lab11.csv'}
        cat = 'files\\graphs'

        def __init__(self, num=1, ref='files\\marks2.lab11.csv'):
            KmrCsv.__init__(self, num, ref)
            Statistic.__init__(self, self)
            Plots.__init__(self, self)
            KmrWork.kmrs[num] = ref

        @staticmethod
        def compare_csv(kmr1, kmr2):
            with open(kmr1.ref, 'r') as file1:
                with open(kmr2.ref, 'r') as file2:
                    with codecs.open(f'files\\Статистика.txt', 'w', "utf-8") as file3:
                        allStudents_1 = len(list(csv.reader(file1)))
                        allStudents_2 = len(list(csv.reader(file2)))
                        print(f'Кількість студентів у файлі 1: {allStudents_1}')
                        print(f'Кількість студентів у файлі 2: {allStudents_2}')
                        file3.write(f'Кількість студентів у файлі 1: {allStudents_1}\n')
                        file3.write(f'Кількість студентів у файлі 2: {allStudents_2}\n')
                        file1.seek(0)
                        file2.seek(0)
                        average_rating_1 = 0
                        average_rating_2 = 0
                        average_time_1 = 0
                        average_time_2 = 0
                        for row1 in csv.reader(file1):
                            average_rating_1 += float(row1[4].replace(',', '.'))
                            try:
                                average_time_1 += int(row1[3][:2]) + int(row1[3][-9:-7]) / 60
                            except:
                                average_time_1 += int(row1[3][:2])
                        average_rating_1 = round(average_rating_1 / allStudents_1, 2)
                        average_time_1 = round(average_time_1 / allStudents_1, 2)
                        for row2 in csv.reader(file2):
                            average_rating_2 += float(row2[4].replace(',', '.'))
                            try:
                                average_time_2 += int(row2[3][:2]) + int(row2[3][-9:-7]) / 60
                            except:
                                average_time_2 += int(row2[3][:2])
                        average_rating_2 = round(average_rating_2 / allStudents_2, 2)
                        average_time_2 = round(average_time_2 / allStudents_2, 2)
                        print(f'Середня оцінка у файлі 1: {average_rating_1}')
                        print(f'Середня оцінка у файлі 2: {average_rating_2}')
                        file3.write(f'Середня оцінка у файлі 1: {average_rating_1}\n')
                        file3.write(f'Середня оцінка у файлі 2: {average_rating_2}\n')
                        print(f'Середній час виконання у файлі 1: {average_time_1}')
                        print(f'Середній час виконання у файлі 2: {average_time_2}')
                        file3.write(f'Середній час виконання у файлі 1: {average_time_1}\n')
                        file3.write(f'Середній час виконання у файлі 2:{average_time_2}\n') \

        @staticmethod
        def compare_avg_plots(kmr1, kmr2):
            correctPercent = kmr1.Statistic.avg_stat()
            plt.figure('Відсотки правильних відповідей 1')
            plt.hist(correctPercent)
            plt.savefig(f'{KmrWork.cat}\\[{kmr1.Statistic.KmrCsv.num}] Відсотки правильних відповідей 1.png')
            correctPercent = kmr2.Statistic.avg_stat()
            plt.figure('Відсотки правильних відповідей 2')
            plt.hist(correctPercent)
            plt.savefig(f'{KmrWork.cat}\\[{kmr2.Statistic.KmrCsv.num}] Відсотки правильних відповідей 2.png')
            plt.show()
    kmr1 = KmrWork(1)
    kmr2 = KmrWork(2)

    kmr1.set_cat('files\\graphs')

    kmr2.avg_plot()
    kmr2.marks_plot()

    KmrWork.compare_csv(kmr1, kmr2)
    KmrWork.compare_avg_plots(kmr1, kmr2)

    kmr1.best_marks_plot()


if __name__ == "__main__":
    main()
