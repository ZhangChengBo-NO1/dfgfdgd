def get_number(prompt):
    """
    获取用户输入的数字
    参数: prompt - 提示信息
    返回: 用户输入的数字(float类型)
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("输入错误！请输入一个有效的数字。")


def get_operator():
    """
    获取用户输入的运算符
    返回: 有效的运算符(+、-、*、/)
    """
    valid_operators = ['+', '-', '*', '/']
    while True:
        operator = input("请输入运算符 (+、-、*、/): ").strip()
        if operator in valid_operators:
            return operator
        print("输入错误！请输入有效的运算符 (+、-、*、/)。")


def calculate(num1, operator, num2):
    """
    执行计算
    参数: num1 - 第一个数字
          operator - 运算符
          num2 - 第二个数字
    返回: 计算结果 或 None(除数为0时)
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("错误：除数不能为0！")
            return None
        return num1 / num2


def ask_continue():
    """
    询问用户是否继续计算
    返回: True(继续) 或 False(退出)
    """
    while True:
        choice = input("\n是否继续计算？(y/n): ").strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        print("请输入 y 或 n。")


def main():
    """
    主函数：程序入口
    """
    print("=" * 40)
    print("       欢迎使用简易计算器")
    print("=" * 40)
    
    while True:
        print("\n" + "-" * 30)
        
        num1 = get_number("请输入第一个数字: ")
        operator = get_operator()
        num2 = get_number("请输入第二个数字: ")
        
        result = calculate(num1, operator, num2)
        
        if result is not None:
            print(f"\n计算结果: {num1} {operator} {num2} = {result}")
        
        if not ask_continue():
            print("\n感谢使用，再见！")
            break


if __name__ == "__main__":
    main()
