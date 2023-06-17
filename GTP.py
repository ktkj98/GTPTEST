import time

def concentration_timer(duration):
    print("专注时钟开始！")
    time.sleep(duration * 60)
    print("时间到！专注时钟结束！")

if __name__ == "__main__":
    duration = int(input("请输入专注时钟的持续时间（分钟）："))
    concentration_timer(duration)
