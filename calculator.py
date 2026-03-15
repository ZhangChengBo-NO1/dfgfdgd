"""
简易计算器程序
功能：实现加减乘除四则运算
作者：AI Assistant
适合：Python新手学习
"""


def get_number(prompt):
    """
    获取用户输入的数字
    参数 prompt: 提示信息
    返回: 用户输入的数字（浮点数）
    """
    while True:
        try:
            # 尝试将用户输入转换为浮点数
            number = float(input(prompt))
            return number
        except ValueError:
            # 如果转换失败，说明输入的不是数字
            print("❌ 输入错误！请输入一个有效的数字。")


def get_operator():
    """
    获取用户输入的运算符
    返回: 用户选择的运算符（+、-、*、/）
    """
    while True:
        operator = input("请输入运算符 (+、-、*、/)：").strip()
        if operator in ['+', '-', '*', '/']:
            return operator
        else:
            print("❌ 运算符错误！请输入 +、-、* 或 / 中的一个。")


def calculate(num1, operator, num2):
    """
    执行计算
    参数 num1: 第一个数字
    参数 operator: 运算符
    参数 num2: 第二个数字
    返回: 计算结果
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # 检查除数是否为0
        if num2 == 0:
            raise ZeroDivisionError("除数不能为0！")
        return num1 / num2


def main():
    """
    主函数：程序入口
    """
    print("=" * 40)
    print("       🧮 欢迎使用简易计算器 🧮")
    print("=" * 40)
    print()

    while True:
        # 步骤1：获取第一个数字
        num1 = get_number("请输入第一个数字：")

        # 步骤2：获取运算符
        operator = get_operator()

        # 步骤3：获取第二个数字
        num2 = get_number("请输入第二个数字：")

        # 步骤4：执行计算并显示结果
        try:
            result = calculate(num1, operator, num2)
            print()
            print(f"✅ 计算结果：{num1} {operator} {num2} = {result}")
        except ZeroDivisionError as e:
            print(f"❌ 错误：{e}")

        print()

        # 步骤5：询问是否继续
        while True:
            choice = input("是否继续计算？(y/n)：").strip().lower()
            if choice == 'y':
                print()
                break  # 继续循环，进行新的计算
            elif choice == 'n':
                print()
                print("=" * 40)
                print("       感谢使用，再见！👋")
                print("=" * 40)
                return  # 退出程序
            else:
                print("❌ 请输入 y 或 n")


# 程序入口
if __name__ == "__main__":
    main()
