# 简易计算器程序 - 适合Python新手学习
# 功能：实现加减乘除运算，包含异常处理和循环计算功能

def get_number(prompt):
    # 函数功能：获取用户输入的数字，处理非数字输入的异常
    # 参数：prompt - 提示用户输入的文本
    # 返回值：用户输入的数字（转换为float类型）
    while True:  # 无限循环，直到用户输入有效的数字
        try:
            # float()将字符串转换为浮点数，input()获取用户输入
            num = float(input(prompt))
            return num  # 输入成功，返回数字并退出函数
        except ValueError:
            # 如果用户输入的不是数字，float()会抛出ValueError异常
            print("错误：请输入有效的数字！")

def get_operator():
    # 函数功能：获取用户输入的运算符，确保是+、-、*、/中的一个
    # 返回值：用户输入的有效运算符
    while True:  # 无限循环，直到用户输入有效的运算符
        op = input("请输入运算符（+、-、*、/）：")
        # 检查运算符是否在允许的列表中
        if op in ['+', '-', '*', '/']:
            return op  # 返回有效运算符
        else:
            print("错误：请输入有效的运算符（+、-、*、/）！")

def calculate(num1, op, num2):
    # 函数功能：根据运算符执行相应的计算
    # 参数：num1 - 第一个数字，op - 运算符，num2 - 第二个数字
    # 返回值：计算结果
    if op == '+':
        return num1 + num2  # 加法运算
    elif op == '-':
        return num1 - num2  # 减法运算
    elif op == '*':
        return num1 * num2  # 乘法运算
    elif op == '/':
        # 除法运算前先检查除数是否为0
        if num2 == 0:
            # 抛出ZeroDivisionError异常，附带错误信息
            raise ZeroDivisionError("错误：除数不能为0！")
        return num1 / num2  # 除法运算

def main():
    # 主函数：程序入口，控制整个计算器的流程
    print("=" * 30)  # 打印分隔线，"="乘以30次
    print("欢迎使用简易计算器")
    print("=" * 30)
    
    while True:  # 主循环，控制是否继续计算
        # 第一步：获取第一个数字
        num1 = get_number("请输入第一个数字：")
        # 第二步：获取运算符
        op = get_operator()
        # 第三步：获取第二个数字
        num2 = get_number("请输入第二个数字：")
        
        try:
            # 执行计算，可能会抛出ZeroDivisionError异常
            result = calculate(num1, op, num2)
            # f-string格式化输出结果
            print(f"\n计算结果：{num1} {op} {num2} = {result}\n")
        except ZeroDivisionError as e:
            # 捕获除数为0的异常，打印错误信息
            print(f"\n{e}\n")
        
        # 询问用户是否继续
        while True:  # 循环直到用户输入y或n
            choice = input("是否继续计算？(y/n)：").lower()  # .lower()转换为小写
            if choice == 'y':
                print()  # 打印空行，美化输出
                break  # 退出当前循环，回到主循环继续计算
            elif choice == 'n':
                print("感谢使用，再见！")
                return  # 返回，结束整个程序
            else:
                print("请输入 'y' 或 'n'！")

# Python程序入口点：当直接运行此文件时，执行main()函数
# 如果是被其他文件导入，则不会执行
if __name__ == "__main__":
    main()
