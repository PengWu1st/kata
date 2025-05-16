from itertools import accumulate
import operator

def demo_accumulate():
    # 基础累加示例
    numbers = [1, 2, 3, 4, 5]
    acc_sum = list(accumulate(numbers))
    print(f"默认累加: {acc_sum}")  # [1, 3, 6, 10, 15]
    
    # 使用自定义操作符(乘法)
    acc_mult = list(accumulate(numbers, operator.mul))
    print(f"累乘: {acc_mult}")  # [1, 2, 6, 24, 120]
    
    # 带初始值的累加
    acc_with_initial = list(accumulate(numbers, initial=10))
    print(f"带初始值的累加: {acc_with_initial}")  # [10, 11, 13, 16, 20, 25]

if __name__ == "__main__":
    demo_accumulate()
