class Calculator:
    """四則演算を行うクラス."""

    @staticmethod
    def add(a, b):
        """足し算を行う."""
        return a + b

    @staticmethod
    def sub(a, b):
        """引き算を行う."""
        return a - b

    @staticmethod
    def mul(a, b):
        """掛け算を行う."""
        return a * b

    @staticmethod
    def dev(a, b):
        """割り算を行う."""
        return a / b

    @staticmethod
    def cal_formula(formula:str) -> float:
        a, operator , b = formula.split()
        a = int(a)
        b = int(b)

        if operator == '+':
           return Calculator.add(a,b)
        elif operator == '-':
           return Calculator.sub(a,b)
        elif operator == '*':
           return Calculator.mul(a,b)
        elif operator == '/':
           return Calculator.dev(a,b)
        


# テストコード
if __name__ == '__main__':
    numa = 23
    numb = 22

    print(Calculator.add(numa, numb))
    print(Calculator.sub(numa, numb))
    print(Calculator.mul(numa, numb))
    print(Calculator.dev(numa, numb))
    print(Calculator.cal_formula('2 * 3')