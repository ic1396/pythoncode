#!/usr/bin/python3
# 《Python语言程序设计》程序清单６－编程题
# Programed List 6-Test Programme
# 第六章　编程题　６．１～６．４８

# from PrimeNumberFunction import *

'''
# 6.1
# 一个返回五角数（n * （3 * n - 1） / 2， 其中 n = 1、2、3...）的函数。
def getPentagonalNumber(n):
    return int(n * (3 * n - 1) / 2)
def main():
    for i in range(1, 101, 1):
        print(format(getPentagonalNumber(i), "5d"), end=" ")
        if i % 10 == 0:
            print()
main()
# 6.2
# 计算一个整数各数字和的函数。
def sumDigits(n):
    sum = 0
    while n > 0:
        sum = sum + n % 10
        n = n // 10
    return sum

def main():
    n = eval(input("请输入一个正整数："))
    print("各数字之和为（若输入负数返回 0 ）：", sumDigits(n))
main()
# 6.3
# 判断一个数是否为回文数。
# 生成一个数的反向数
def reverse(number):
    if number <= 0:
        return  0
    re_number = 0
    while number > 0:
        re_number = re_number * 10
        re_number = re_number + number % 10
        number = number // 10
    return re_number
# 判断一个数是否为回文数
def isPalindrome(number):
    if number <= 0:
        return False
    return True if number == reverse(number) else False
def main():
    n = eval(input("请输入一个正整数："))
    if isPalindrome(n):
        print(n, "是一个回文数。")
    else:
        print(n, "不是一个回文数。")
main()
# 6.4
# 反向显示一个整数
# 生成一个数的反向数
def reverse(number):
    if number <= 0:
        return  0
    re_number = 0
    while number > 0:
        re_number = re_number * 10
        re_number = re_number + number % 10
        number = number // 10
    return re_number
def main():
    n = eval(input("请输入一个正整数："))
    print(n, "的反向数是", reverse(n))
main()
# 6.5
# 对三个数按升序进行排序。
def displaySortedNumbers(num1, num2, num3):
    minnum1 = num1
    if num2 < num1:
        minnum1 = num2
        num2 = num1
        num1 = minnum1
    if num3 < num1:
        minnum1 = num3
        num3 = num2
        num2 = num1
        num1 = minnum1
    elif num3 < num2:
        minnum1 = num3
        num3 = num2
        num2 = minnum1
    print("按升序排序为：", num1, num2, num3)
def main():
    num1, num2, num3 = eval(input("请输入三个数："))
    displaySortedNumbers(num1, num2, num3)
main():
# 6.6
def displayPattern(n):
    for i in range(1, n + 1, 1):
        j = 0
        while j < n - i:
            print("    ", end='')
            j += 1
        for k in range(i, 0, -1):
            print(format(k, "4d"), end='')
        print()
def main():
    n = eval(input("请输入一个正整数："))
    displayPattern(n)
main()
# 6.7
# 用指定的投资额度、年数和给定的利率计算未来投资价值
def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    return investmentAmount * pow(1 + monthlyInterestRate, years * 12)
def main():
    investmentAmount = eval(input("请输入投资总额度："))
    yearInterestRate = eval(input("请输入年利率："))
    years = eval(input("请输入投资总年数："))
    print("投资总额度：", investmentAmount)
    print("年利率：", yearInterestRate)
    print("投资总年数：", years)
    print("  年  ", "  收益  ")
    for i in range(1, years + 1, 1):
        print(format(i, "3d"), "    ", format(futureInvestmentValue(investmentAmount, yearInterestRate / 12 / 100, i), "6.2f"))
main()
# 6.8
# 摄氏度和华氏度间的互相转换
# 摄氏度转华氏度
def celsiusToFahrenheit(celsius):
    return (9 / 5) * celsius + 32
# 华氏度转摄氏度
def fahrenheitToCelsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)
def main():
    print("______________________________________________________")
    print("  Celsius  |  Fahrenheit  ||  Fahrenheit  |  Celsius  ")
    print("------------------------------------------------------")
    cel = 40.0
    fah = 120.0
    for i in range(0, 10, 1):
        print("  ", format(cel - i, "5.1f"), "  |  ", format(celsiusToFahrenheit(cel - i), "8.1f"),"  ||  ",
              format(fah - i * 10, "8.1f"), "  |  ", format(fahrenheitToCelsius(fah - i * 10), "4.2f"))
main()
# 6.9
# 英尺和米间的互相转换
# 英尺转米
def footToMeter(foot):
    return 0.305 * foot
# 米转英尺
def meterToFoot(meter):
    return meter / 0.305
def main():
    print("______________________________________________________")
    print("  Feet  |  Meters  ||  Meters  |  Feet  ")
    print("------------------------------------------------------")
    feet = 1.0
    meters = 20.0
    for i in range(0, 10, 1):
        print("  ", format(feet + i, "2.1f"), "  |  ", format(footToMeter(feet + i), "1.3f"),"  ||  ",
              format(meters + i * 5, "2.1f"), "  |  ", format(meterToFoot(meters + i * 5), "3.3f"))
main()
# 6.10
# 计算小于 10000 的素数的个数
# 列出个数并打印所有小于 10000 的素数
def main():
    count = 0
    Number_Per_line = 10
    for i in range(2, 10001):
        if isPrime(i):
            count += 1
            print(format(i,"6d"), end='')
            if count % Number_Per_line == 0:
                print()
    print()
    print("共有", count, "个小于 10000 的素数。")
main()
# 6.11
# 计算佣金
def computeCommission(salesAmount):
    if 0.01 <= salesAmount <= 5000:
        return salesAmount * 0.08
    elif 5000.01 <= salesAmount <= 10000:
        return 5000 * 0.08 + (salesAmount - 5000) * 0.1
    elif 10000.01 <= salesAmount:
        return 5000 * 0.08 + 5000 * 0.1 + (salesAmount - 10000) * 0.12
def main():
    print("_______________________________")
    print("  Sales Amount  |  Commission  ")
    print("-------------------------------")
    amount = 10000
    for i in range(0, 19, 1):
        print("  ", format(amount + i * 5000, "7d"), "     |  ", format(computeCommission(amount + i * 5000), "6.1f"))
main()
# 6.12
# 按规则打印字符串
def printChars(ch1, ch2, numberPerLine):
    if ord(ch1) <= ord(ch2):
        j = 1
    else:
        j = -1
    count = 0
    for i in range(ord(ch1), ord(ch2) + j, j):
        print(chr(i), end='')
        count += 1
        if count % numberPerLine == 0:
            print()
def main():
    printChars("1", "Z", 10)
main()
# 6.13
# 计算指定数列的和
def computeSum(feed):
    if feed <= 0:
        return 0
    sum = 0
    for i in range(1, feed + 1, 1):
        sum += i / (i + 1)
    return sum
def main():
    print("___________________________")
    print("     i    |      m(i)      ")
    print("---------------------------")
    count = 20
    for i in range(1, count + 1, 1):
        print("  ", format(i, "3d"), "   |    ", format(computeSum(i), "2.4f"))
main()
# 6.14
# 估算 Pi 值
def computePi(feed):
    if feed <= 0:
        return 0
    sum = 0
    for i in range(1, feed + 1, 1):
        sum += 4 * (pow(-1, i + 1) / (2 * i - 1))
    return sum
def main():
    print("___________________________")
    print("      i    |      Pi(i)    ")
    print("---------------------------")
    count = 20
    print("  ", format(1, "4d"), "   |    ", format(computePi(1), "2.4f"))
    for i in range(101, 1000, 100):
        print("  ", format(i, "4d"), "   |    ", format(computePi(i), "2.4f"))
main()
# 6.15
# 依据 Programed List 4-7 计算税款
def computeTax(status, taxableIncome):
    # Compute tax
    tax = 0
    if status == 0:  # Compute tax for single filers
        if taxableIncome <= 8350:
            tax = taxableIncome * 0.10
        elif taxableIncome <= 33950:
            tax = 8350 * 0.10 + (taxableIncome - 8350) * 0.15
        elif taxableIncome <= 82250:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                (taxableIncome - 33950) * 0.25
        elif taxableIncome <= 171550:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                (82250 - 33950) * 0.25 + (taxableIncome - 82250) * 0.28
        elif taxableIncome <= 372950:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
                (taxableIncome - 171550) * 0.33
        else:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
                (372950 - 171550) * 0.33 + (taxableIncome - 372950) * 0.35
    elif status == 1:  # Compute tax for married file jointly
        if taxableIncome <= 16700:
            tax = taxableIncome * 0.10
        elif taxableIncome <= 67900:
            tax = 16700 * 0.10 + (taxableIncome - 16700) * 0.15
        elif taxableIncome <= 137050:
            tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + (taxableIncome - 67900) * 0.25
        elif taxableIncome <= 208850:
            tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + (137050 - 67900) * 0.25 + (taxableIncome - 137050) * 0.28
        elif taxableIncome <= 372950:
            tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 + \
                  (taxableIncome - 208850) * 0.33
        else:
            tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 + \
                  (372950 - 208850) * 0.33 + (taxableIncome - 372950) * 0.35
    elif status == 2:  # Compute tax for married separately
        if taxableIncome <= 8350:
            tax = taxableIncome * 0.10
        elif taxableIncome <= 33950:
            tax = 8350 * 0.10 + (taxableIncome - 8350) * 0.15
        elif taxableIncome <= 68525:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (taxableIncome - 33950) * 0.25
        elif taxableIncome <= 104425:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (68525 - 33950) * 0.25 + (taxableIncome - 68525) * 0.28
        elif taxableIncome <= 186475:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 + \
                  (taxableIncome - 104425) * 0.33
        else:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 + \
                  (186475 - 104425) * 0.33 + (taxableIncome - 186475) * 0.35
    elif status == 3:  # Compute tax for head of household
        if taxableIncome <= 11950:
            tax = taxableIncome * 0.10
        elif taxableIncome <= 45500:
            tax = 11950 * 0.10 + (taxableIncome - 11950) * 0.15
        elif taxableIncome <= 117450:
            tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + (taxableIncome - 45500) * 0.25
        elif taxableIncome <= 190200:
            tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + (117450 - 45500) * 0.25 + (taxableIncome - 117450) * 0.28
        elif taxableIncome <= 372950:
            tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + (117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 + \
                  (taxableIncome - 190200) * 0.33
        else:
            tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + (117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 + \
                  (372950 - 190200) * 0.33 + (taxableIncome - 372950) * 0.35
    return tax
def main():
    print("________________________________________________________________________________________")
    print("  Taxable Income  |  Single  |  Married Joint  |  Married Separate  |  Head of a House  ")
    print("----------------------------------------------------------------------------------------")
    for i in range(50000, 60050, 50):
        print("    ", format(i, "8d"), "    | ", format(computeTax(0, i), "5.0f"), "  |   ",
              format(computeTax(1, i), "7.0f"), "     |    ", format(computeTax(2, i), "8.0f"), "      |   ",
              format(computeTax(3, i), "8.0f"))
main()
# 6.16
# 判断是否为闰年，闰年返回 366，否则返回 365
def numberOfDaysInAYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 366
    else:
        return 365
def main():
    for i in range(2010, 2021, 1):
        print(i, "  |  ", numberOfDaysInAYear(i))
main()
# 6.17
#  依据三角形三边长计算三角形的面积
def isValid(side1, side2, side3):
    return (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1)
def area(side1, side2, side3):
    if isValid(side1, side2, side3):
        s = (side1 + side2 + side3) / 2
        areaTriangle = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
        print("三角形的面积为", areaTriangle)
    else:
        print("输入错误，边长不构成三角形。")
def main():
    side1, side2, side3 = eval(input("请输入三角形的三个边长: "))
    area(side1, side2, side3)
main()
'''
# 6.18

# 6.19

# 6.20

# 6.21

# 6.22

# 6.23

# 6.24

# 6.25

# 6.26

# 6.27

# 6.28

# 6.29

# 6.30

# 6.31

# 6.32

# 6.33

# 6.34

# 6.35

# 6.36

# 6.37

# 6.38

# 6.39

# 6.40

# 6.41

# 6.42

# 6.43

# 6.44

# 6.45

# 6.46

# 6.47

# 6.48
