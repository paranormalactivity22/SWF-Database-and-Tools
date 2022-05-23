#coding: utf-8
# System Made By LucasYogr#0001
import os


class Api:

    def __init__(t=""):
        p = Api.check_sys()
        if p:
            v = Api.check_version()
            if v == 1:
                Api.check_mysql()
                Api.check_pillow()
                Api.check_lupa()

    def check_sys(t=""):
        try:
            import sys
            return True
        except ImportError as e:
            print("[API] Sys Library not found. Installing Sys...")
            os.system("pip install os-sys")

    def check_version(t=""):
        import sys
        version = str(sys.version[:3])
        version_c = str(sys.version[:5])
        version_req = str('3.7')
        version_req_c = str('3.7.7')
        if version != version_req:
            print("[INFO] You Need python 3.7 to run!")
            return 0
        else:
            if version_c == version_req_c:
                print("Python %s found" %(str(version_c)))
                return 1
            else:
                print("[INFO] You are using %s version recommanded to use is %s" %(version_c, version_req_c))
                return 1

    def check_lupa(t=""):
        try:
            import lupa
        except ImportError as e:
            print("[API] Lupa Library not found. Installing Lupa...")
            os.system("pip install lupa")

    def check_mysql(t=""):
        try:
            import pymysql
        except ImportError as e:
            print("[API] Pymysql Library not found. Installing MySQL...")
            os.system("pip install pymysql")

    def check_pillow(t=""):
        try:
            import PIL
        except ImportError as e:
            print("[API] Pillow Library not found. Installing Pillow...")
            os.system("pip install Pillow")