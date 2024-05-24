class Br:
    def __init__(self, name, price) :
        self.name = name
        self.price = int(price)
        self.total_sold = 0

    def bark(self) :
        print(self.name + "은 " + str(self.price) + "원에 팔았습니다.")

    def sell(self) :
        self.total_sold += self.price
        print(f"{self.name}을 {self.price}원에 팔았습니다.")

    def total(self) :
        return self.total_sold * self.price

bean = Br("bean", "2000")
cream = Br("cream", "1500")

bean.sell()
bean.sell()
bean.sell()
bean.sell()
bean.sell()

print(f"총 판매액: {bean.total_sold}원")