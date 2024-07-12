class colors:
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    BLUE = '\033[34m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
import pyautogui as pag
import time
import pyfiglet
text = "Azota Bypass v1.1"
ascii_art = pyfiglet.figlet_format(text)
print(colors.BLUE + ascii_art + colors.END)
print(colors.RED + "Language:" + colors.END, end=' ')
lang = int(input(" 1-Vietnamese ; 2-English: "))
if lang == 1:
    print(colors.RED + "Quản lý: " + colors.END, end=' ')
    print("Nguyễn Huỳnh Đăng Nhựt")
    print(colors.RED + "Liên hệ: " + colors.END, end=' ')
    print("penciltalk0910@gmail.com")
    password1 = int(input(colors.RED + "Vui lòng nhập mật khẩu: " + colors.END))
    while True:
        if password1 == 122333445:
            print("")
            print(colors.BLUE + "Chúc bạn sử dụng phần mềm vui vẻ" + colors.END)
            print(colors.RED + 'Lưu ý: Phần mềm chỉ sử dụng dưới mục đích học tập và tìm hiểu, không dùng phần mềm dưới mục đính thực hiện trái phép các hoạt động trong kì thi' + colors.END)
            print(colors.RED + '"Bạn đồng ý chứ:' + colors.END)
            Ok1 = int(input( "1-Đồng ý ; 2-Không đồng ý: "))
            while True:
                if Ok1 == 1:
                    print(colors.BLUE + "Tôi ghi nhận ý kiến này từ bạn" + colors.END)
                    time1 = float(input(colors.YELLOW + "Nhập thời gian chờ để (Kể từ thời gian bạn chạy chương trình cho đến khi dùng AZOTA (Khuyến khích: 5): " + colors.END))
                    print("Đã ghi nhận thời gian chờ của bạn là: ", time1)
                    time.sleep(1)
                    while True:
                        print(colors.YELLOW + 'Sau khi bắt đầu, bạn bật AZOTA và đợi khoảng chờ hệ thống sẽ chạy sau khoảng thời gian bạn đã định sẵn' + colors.END)
                        do = int(input("Nhấn 1 để bắt đầu, 2 để quay lại thao tác: "))
                        if do == 1:
                            time.sleep(time1)
                            pag.hotkey('ctrl', 'shift', 'i')
                            time.sleep(1)
                            pag.locateOnScreen("Element0.png", confidence = 0.7)
                            time.sleep(0.5)
                            pag.click("Element0.png")
                            time.sleep(0.5)
                            pag.locateOnScreen("EL0.png", confidence = 0.7)
                            time.sleep(1)
                            pag.click("EL0.png")
                            time.sleep(0.2)
                            pag.locateOnScreen("Resize.png", confidence = 0.7)
                            time.sleep(0.2)
                            pag.click("Resize.png")
                            time.sleep(0.2)
                            pag.locateOnScreen("Remove.png", confidence = 0.7)
                            pointclick = (pag.locateOnScreen("Remove.png", confidence = 0.7).left + 88, pag.locateOnScreen("Remove.png", confidence = 0.7).top + 10)
                            time.sleep(0.2)
                            pag.click(pointclick)
                            time.sleep(0.1)
                            pag.click(pointclick)
                            time.sleep(0.2)
                            pag.locateOnScreen("X.png", confidence=0.7)
                            time.sleep(0.1)
                            pag.click("X.png")
                            time.sleep(0.2)
                            pag.hotkey('esc')
                            print (colors.YELLOW + 'Thực hiện Bypass thành công' + colors.END)
                        else:
                            break
                else:
                    print("")
                    print(colors.RED + "Nếu bạn không đồng ý thì không nên sử dụng phần mềm trái phép này" + colors.END)
                    break
        else:
            print(colors.RED + "Mật khẩu sai, vui lòng liên hệ Admin để nhận đúng" + colors.END)
            break
else:
        print(colors.RED + "Adminator: " + colors.END, end=' ')
        print("Nguyễn Huỳnh Đăng Nhựt")
        print(colors.RED + "Contact: " + colors.END, end=' ')
        print("penciltalk0910@gmail.com")
        password1 = int(input(colors.RED + "Please enter password: " + colors.END))
        while True:
            if password1 == 122333445:
                print("")
                print(colors.BLUE + "Good luck!" + colors.END)
                print(colors.RED + "This tool only use for education. Please don't use this tool for your tests and crack some thing special" + colors.END)
                print(colors.RED + 'Agree? ' + colors.END, end=' ')
                Ok1 = int(input("1 - Agree; 2 - Disagree: "))
                while True:
                    if Ok1 == 1:
                        print(colors.BLUE + "I recorded that" + colors.END)
                        time1 = float(input(colors.YELLOW + "Enter time for waiting you open the AZOTA Website (Recommend: 5) " + colors.END))
                        print("Your time is: ", time1)
                        time.sleep(1)
                        while True:
                            print(
                                colors.YELLOW + 'After you run this script, open the AZOTA tab before this script working' + colors.END)
                            do = int(input("Press 1 to start, 2 to stop "))
                            if do == 1:
                                time.sleep(time1)
                                pag.hotkey('ctrl', 'shift', 'i')
                                time.sleep(1)
                                pag.locateOnScreen("Element0.png", confidence=0.7)
                                time.sleep(0.5)
                                pag.click("Element0.png")
                                time.sleep(0.5)
                                pag.locateOnScreen("EL0.png", confidence=0.7)
                                time.sleep(1)
                                pag.click("EL0.png")
                                time.sleep(0.2)
                                pag.locateOnScreen("Resize.png", confidence=0.7)
                                time.sleep(0.2)
                                pag.click("Resize.png")
                                time.sleep(0.2)
                                pag.locateOnScreen("Remove.png", confidence=0.7)
                                pointclick = (pag.locateOnScreen("Remove.png", confidence=0.7).left + 88, pag.locateOnScreen("Remove.png", confidence=0.7).top + 10)
                                time.sleep(0.2)
                                pag.click(pointclick)
                                time.sleep(0.1)
                                pag.click(pointclick)
                                time.sleep(0.2)
                                pag.locateOnScreen("X.png", confidence=0.7)
                                time.sleep(0.1)
                                pag.click("X.png")
                                time.sleep(0.2)
                                pag.hotkey('esc')
                                print(colors.YELLOW + 'AZOTA Bypass Successfully work' + colors.END)
                            else:
                                break
                    else:
                        print("")
                        print(
                            colors.RED + "If you don't agree to this license, please don't work on it" + colors.END)
                        break
            else:
                print(colors.RED + "Wrong password, Contact to admin for more" + colors.END)
                break

