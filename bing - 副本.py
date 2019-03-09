import urllib.request
import requests
import os.path
import win32api,win32con,win32gui
from PIL import Image



def save_image(img_url,dirname):
    try:
        if not os.path.exists(dirname):
            print("文件",
                  dirname,"不存在，请建一个")
            os.makedirs(dirname)
        basename = os.path.basename(img_url)
        filepath = os.path.join(dirname,basename)
        urllib.request.urlretrieve(img_url,filepath)
    except IOError as e:
        print('文件操作失败',e)
    except Exception as e:
        print("错误",e)
    print("save",filepath,"successfully!")
    return filepath
def get_img_url(raw_img_url = "https://area.sinaapp.com/bingImg/"):
    r = requests.get(raw_img_url)
    img_url = r.url
    return img_url
def set_img_as_wallpaper(newpath):
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(reg_key,"WallpaperStyle",0,win32con.REG_SZ,"2")
    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,newpath,1+2)
def covrtfiletype(filepath):
    bmpimage = Image.open(filepath)
    newpath = filepath.replace('.jpg','.bmp')
    bmpimage.save(newpath,'BMP')
    #set_img_as_wallpaper(newpath)
    return newpath
def main():
    dirname = "F:\\bing"
    img_url = get_img_url()
    filepath = save_image(img_url,dirname)
    newpath =covrtfiletype(filepath)
    set_img_as_wallpaper(newpath)
    #print(filepath)
main()
