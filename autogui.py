
    
    #安装pyautogui时需要用pip install pyautogui和pip install pillow,一起按装

import pyautogui#关于img.shape[0]、[1]、[2]img.shape[0]：图像的垂直尺寸（高度）img.shape[1]：图像的水平尺寸（宽度）img.shape[2]：图像的通道数在矩阵中，[0]就表示行数，[1]则表示列数。




    im1 = pyautogui.screenshot(region=(0,0, 1920, 1080))#区域截图,然后保存
    im2 = pyautogui.screenshot('my_screenshot.png')
    location_pic = pyautogui.locateOnScreen('my_screenshot.png')#返回图片的宽高和坐标
    #print(location_pic.left)
    pyautogui.PAUSE = 1#每执行一个操作停顿1.5s
    pyautogui.FAILSAFE = False#鼠标移动到左上角会自动触发一个自动操作的中断,是保护错失.设置false可以禁用保护
    #pyautogui.moveTo(location_pic.left, location_pic.top, 1)#鼠标移动到图片的左上角处.有时会报错
    location_xy = pyautogui.center(location_pic)#中心位置坐标
    print(location_xy)
    pyautogui.moveTo(location_xy.x,location_xy.y,1)

    for pos in pyautogui.locateAllOnScreen('英文文字.png'):
        print("定位所有图片",pos)
    im2.getpixel((100, 200))#获取截图中的某点颜色
    pyautogui.pixelMatchesColor(100, 200, (130, 135, 144))#参数为x,y,目标rgb
