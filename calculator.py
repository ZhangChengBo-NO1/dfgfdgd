# 简易加减乘除计算器
# 适合Python新手学习

def get_number(prompt):
    """
    获取用户输入的数字
    参数: prompt - 提示信息
    返回: 有效的数字
    """
    while True:
        try:
            user_input = input(prompt)
            number = float(user_input)
            return number
        except ValueError:
            print("错误：请输入有效的数字！")

def get_operator():
    """
    获取用户输入的运算符
    返回: 有效的运算符
    """
    while True:
        operator = input("请输入运算符（+、-、*、/）：")
        if operator in ['+', '-', '*', '/']:
            return operator
        else:
            print("错误：请输入有效的运算符（+、-、*、/）！")

def calculate(num1, operator, num2):
    """
    执行计算
    参数: num1 - 第一个数字, operator - 运算符, num2 - 第二个数字
    返回: 计算结果或错误信息
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "错误：除数不能为0！"
        return num1 / num2

def main():
    """
    主函数：程序入口
    """
    print("=" * 30)
    print("      简易计算器")
    print("=" * 30)
    
    while True:
        print("\n" + "-" * 30)
        print("开始新的计算：")
        
        # 获取第一个数字
        num1 = get_number("请输入第一个数字：")
        
        # 获取运算符
        operator = get_operator()
        
        # 获取第二个数字
        num2 = get_number("请输入第二个数字：")
        
        # 执行计算
        result = calculate(num1, operator, num2)
        
        # 显示结果
        print("\n计算结果：")
        if isinstance(result, str):
            print(result)
        else:
            print(f"{num1} {operator} {num2} = {result}")
        
        # 询问用户是否继续
        while True:
            continue_calc = input("\n是否继续计算？(y/n)：").lower()
            if continue_calc == 'n':
                print("\n感谢使用计算器，再见！")
                return
            elif continue_calc == 'y':
                break
            else:
                print("错误：请输入 y 或 n！")

if __name__ == "__main__":
    main()
