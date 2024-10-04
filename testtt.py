#!/usr/bin/python3
# coding=utf-8

__Author__    = 'Alexander Urluv'
__Whatsapp__  = 'Not One'
__Facebook__  = 'https://www.facebook.com/alexanderurluv'
__Instagram__ = 'https://www.instagram.com/alexanderurluv'
__Script__    = 'Facebook Boost'
__Version__   = '0.3'

import os,sys,time,random,re,json,datetime,shutil,urllib
try:import requests
except ImportError:os.system('pip install requests')
try:import bs4
except ImportError:os.system('pip install bs4')
try:import rich
except ImportError:os.system('pip install rich')
try:import colorama
except ImportError:os.system('pip install colorama')
try:import names
except ImportError:os.system('pip install names')
from bs4 import BeautifulSoup as bs
from rich import print
from time import sleep,strftime
from random import choice as rc
from random import randint as rr
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June' ,'7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'};tgl = datetime.datetime.now().day;bln = dic[(str(datetime.datetime.now().month))];thn = datetime.datetime.now().year
dic2 = {'Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu','Sunday':'Minggu'}
hari = dic2[(str(strftime("%A")))]
DefaultUAWindows = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
HeadersGet  = lambda i=DefaultUAWindows : {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-True-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Prefers-Color-Scheme':'light','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','Viewport-Width':'924'}
HeadersPost = lambda i=DefaultUAWindows : {'Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Origin':'https://www.facebook.com','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin'}
def clear():os.system('cls' if os.name == 'nt' else 'clear')
def CreateFolder():
    list_folder = ["Data","Database","Account","Cookie"]
    for name in list_folder:
        try:os.mkdir(name)
        except:pass
try:
    key = json.loads(open("Data/key.json","r").read())
except Exception:
    key = None
def baner():clear();print("""[bold white]
——————————————————————————————
┏┓┏┓┏┓┏┓┳┓┏┓┏┓┓┏┓  ┳┓┏┓┏┓┏┓┏┳┓
┣ ┣┫┃ ┣ ┣┫┃┃┃┃┃┫   ┣┫┃┃┃┃┗┓ ┃ 
┻ ┛┗┗┛┗┛┻┛┗┛┗┛┛┗┛  ┻┛┗┛┗┛┗┛ ┻ 
——————————————————————————————
OWNER    : ALEXANDER URLUV
TOOLTYPE : FACEBOOK BOOST
GITHUB   : ALEXANDERAXLURLUV15
VERSION  : 0.3
——————————————————————————————""")


def get_info_name(key):
    try:
        with requests.Session() as r:
            Data = {
                "key":key
            }
            response = r.post("https://alexander-random-tools.glitch.me/api/index.php?tools=check_login_key",allow_redirects=True,data=Data)
            if '"Key valid"' in response.text:
                return response.json()["username"]
            else:
                return None
    except Exception as e:
        return "Exception"


def menu():
    baner()
    name = get_info_name(key["key"])
    if "Exception" == name:
        print("An Error Occurred, Please Try Again !")
        exit()
    elif None == name:
        Buy_Key("Please Purchase Script Key")
    else:
        print("\n [bold white] [-] Hello [green]{} [white][-]".format(name))
        print(
            "\n  [01].Add New Account"
            "\n  [02].Create Automatic Pages"
            "\n  [03].Generate Cookies From Account"
            "\n  [04].Remove Account From List"
            "\n  [05].Save Page Data"
            "\n  [06].Bot Menu"
            "\n  [07].Exit"
        )
        option = input("   ╰─)choice> ")
        if option in ("1","01"):
            add_new_account()
        elif option in ("2","02"):
            auto_create_fp()
        elif option in ("3","03"):
            generate_cookie()
        elif option in ("4","04"):
            delete_account_from_list()
        elif option in ("5","05"):
            save_page_data()
        elif option in ("6","06"):
            bot_menu()
        elif option in ("7","07"):
            exit()
        else:
            print("   ╰─)error> Your Choices Are Unknown");sleep(2);menu()

def add_new_account():
    print("\n  [-] Enter Account ID [-]")
    account_id = input("   ╰─)id> ")
    print("\n  [-] Enter the Account Password [-]")
    account_pass = input("   ╰─)pass> ")
    save_account(account_id, account_pass)




def save_account(userid, password):
    list_file = os.listdir("Account")
    file_name = "%s.json"%("Account")
    if file_name in list_file:
        with open("Account/%s"%(file_name), "r") as file_json:
            file = json.load(file_json)
        for data in file["data"]:
            if data["userid"] == userid and data["password"] == password:
                print("\n  [-] Account Already Exists [-]")
                print("   ╰─)info> The account that wasn't added previously already exists");sleep(2)
                return
        file["data"].insert(0, {"userid": userid, "password": password})
        with open("Account/%s"%(file_name), "w") as json_file:
            json.dump(file, json_file, indent=4)
    else:
        data = {"data":[{"userid":userid, "password":password}]}
        with open("Account/%s"%(file_name), "w") as json_file:
            json.dump(data, json_file, indent=4)
    print("\n  [-] Succeed [-]")
    print("   ╰─)info> Successfully Added Account");sleep(2)
    menu()


def save_page(user, page_id, page_nm):
    list_file = os.listdir("Database")
    file_name = "%s.json"%(user)
    if file_name in list_file:
        with open("Database/%s"%(file_name), "r") as file_json:
            file = json.load(file_json)
        for data in file["data"]:
            if data["page_id"] == page_id and data["page_name"] == page_nm:
                return
        file["data"].insert(0, {"page_id": page_id, "page_name": page_nm})
        with open("Database/%s"%(file_name), "w") as json_file:
            json.dump(file, json_file, indent=4)
    else:
        data = {"data":[{"page_id":page_id, "page_name":page_nm}]}
        with open("Database/%s"%(file_name), "w") as json_file:
            json.dump(data, json_file, indent=4)


def auto_create_fp():
    success = []
    try:
        file = json.loads(open("Cookie/Cookie.json","r").read())
        total = len(file["data"])
    except FileNotFoundError:
        total = 0
    if total == 0:
        print("\n  [-] Blank Cookies [-]")
        print("   ╰─)info> Please do \"Generate Cookies\" First");sleep(2)
    else:
        while True:
            for data in file["data"]:
                status = cek_status(data["cookie"])
                if data["userid"] in success:
                    fp_status, name, pageid = create_page(data["cookie"])
                    if fp_status:
                        save_page(data["userid"], pageid, name)
                        print("\n  [-] Successfully Created Page [-]")
                        print("   ╰─)account> {}".format(data["username"]))
                        print("     ╰─)page_name> {}".format(name))
                        print("     ╰─)page_id> {}".format(pageid))
                    else:
                        print("    ╰─)info> Failed to create accounts                  ", end="\r");sleep(3)
                else:
                    if status:
                        success.append(data["userid"])
                        print("    ╰─)info> Successfully Login to Account {}                     ".format(data["username"]), end="\r");sleep(2)
                    else:
                        print("    ╰─)info> Failed to Login to Account {}                  ".format(data["username"]), end="\r");sleep(2)
            wait(60)


def wait(delay):
    dtk = delay
    for i in range(delay):
        print("   ╰─)wait> %s s                                "%(dtk), end="\r")
        sleep(1)
        dtk -= 1

def generate_name():
    with requests.Session() as r:
        response = r.get('https://story-shack-cdn-v2.glitch.me/generators/philippines-name-generator/female?count=2')
        Name1 = response.json()['data']
        Name = ' '.join([Name['name'] for Name in Name1])
        return(Name)

def create_page(cookie):
    try:
        with requests.Session() as r:pass
        name = generate_name()
        Data = {
            "key": key["key"],
            "cookie": cookie,
            "name": name
        }
        response = r.post('https://alexander-random-tools.glitch.me/api/index.php?tools=createfacebookpage',allow_redirects=True,data=Data)
        if '"additional_profile_plus_create"' in response.text:
            if '"You ve recently created too many Pages. Try again later."' in response.text or '"Cant create Pages: You have created too many Pages in a short time. Try again later."' in response.text or '"It appears that you already manage a Page named %s. Choose another name."'%(name) in response.text:
                return False, None, None
            else:
                pageid = response.json()['data']['additional_profile_plus_create']['additional_profile']['id']
                return True, name, pageid
        else:
            return False, None, None
    except Exception:
        return False, None, None


def check_status(cookie):
    try:
        Data = {
            "key": key["key"],
            "cookie": cookie
        }
        response = requests.post("https://alexander-random-tools.glitch.me/api/index.php?tools=getuserinfo", data=Data)
        if "id" in str(response.text) or "name" in str(response.text):
            return True
        else:
            return False
    except Exception:
        return False

def save_cookie(userid, username, cookie):
    if not os.path.exists("Cookie"):
        os.makedirs("Cookie")
    file_name = "Cookie.json"
    file_path = os.path.join("Cookie", file_name)
    if os.path.exists(file_path):
        with open(file_path, "r") as file_json:
            file_data = json.load(file_json)
        user_found = False
        for data in file_data["data"]:
            if data["userid"] == userid:
                data["cookie"] = cookie
                user_found = True
                break
        if not user_found:
            file_data["data"].append({"userid": userid, "username": username, "cookie": cookie})
        with open(file_path, "w") as json_file:
            json.dump(file_data, json_file, indent=4)
    else:
        data = {"data": [{"userid": userid, "username": username, "cookie": cookie}]}
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

def generate_cookie():
    with open("Account/Account.json", "r") as account_file:
        account_data = json.load(account_file)
    if len(account_data["data"]) == 0:
        print("\n  [-] Empty Account [-]")
        print("   ╰─)info> Please \"Add New Account\" First");sleep(2)
    else:
        try:
            with open("Cookie/Cookie.json", "r") as cookie_file:
                cookie_data = json.load(cookie_file)
            for account in account_data["data"]:
                userid = account["userid"]
                password = account["password"]
                cookie_entry = next((item for item in cookie_data["data"] if item["userid"] == userid), None)
                if cookie_entry:
                    status_ = check_status(cookie_entry["cookie"])
                    if status_:
                        break
                else:
                    status, name, cookie = login_status(userid, password)
                    if status:
                        save_cookie(userid, name, cookie)
                        print("   ╰─)info> Successfully Retrieving Cookies {}                  ".format(name))
                    else:
                        print("   ╰─)info> Failed to Retrieve Cookies {}                  ".format(name))
                    time.sleep(2)
        except FileNotFoundError:
            open("Cookie/Cookie.json", "w").write(json.dumps({"data":[]}))
            generate_cookie()
            return
    print("\n  [-] Finish Generating Cookies [-]")

def login_status(userid, password):
    with requests.Session() as r:pass
    try:
        response = bs(r.get(f"https://mbasic.facebook.com/login/device-based/password/?uid={userid}&flow=login_no_pin&refsrc=deprecated&_rdr").content, "html.parser")
        form = response.find("form",{"method":"post"})
        jazoest  = re.search('name="lsd" type="hidden" value="(.*?)"', str(form)).group(1)
        lsd      = re.search('name="lsd" type="hidden" value="(.*?)"', str(form)).group(1)
        data_post = {
            "lsd": lsd,
            "jazoest": jazoest,
            "uid": userid,
            "next": "https://mbasic.facebook.com/login/save-device/",
            "flow": "login_no_pin",
            "pass": password,
        }
        Headers = {
            'Host': "mbasic.facebook.com",
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'upgrade-insecure-requests': '1',
            'origin': f'https://mbasic.facebook.com',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'x-requested-with': 'XMLHttpRequest',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://mbasic.facebook.com/login/device-based/password/?uid={userid}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        response2 = bs(r.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data=data_post, headers=Headers).content, "html.parser")
        cookie = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
        if "c_user" in str(cookie):
            return True, re.search(">You now interact as (.*?)<", str(response2)).group(1), cookie
        else:
            return False, None, None
    except Exception:
        return False, None, None

def save_page_data():
    file = json.loads(open("Cookie/Cookie.json","r").read())
    total = len(file["data"])
    if total == 0:
        print("\n  [-] Blank Cookies [-]")
        print("   ╰─)info> Please do \"Generate Cookies\" First");sleep(2)
    else:
        for data in file["data"]:
            print("\n  [-] Saving Page Data {} [-]".format(data["username"]))
            list_ = get_page_data(data["cookie"])
            for data_fp in list_:
                save_page(data["userid"], data_fp["page_id"], data_fp["page_name"])
                print("   ╰─)page_id> {}".format(data_fp["page_id"]))
                print("   ╰─)page_name> {}\n".format(data_fp["page_name"]))

def get_page_data(cookie):
    list_ = []
    with requests.Session() as r:pass
    Data = {
        "key": key["key"],
        "cookie": cookie
    }
    response = r.post("https://alexander-random-tools.glitch.me/api/index.php?tools=getpageid", data=Data)
    if '"data"' in response.text:
        for data in response.json()['data']:
            IDPage = data['id']
            NamePage = data['name']
            list_.append({"page_id":IDPage,"page_name":NamePage})
    else:pass
    return list_

def delete_account_from_list():
    print("\n  [-] Enter the account ID you want to delete [-]")
    userid = input("   ╰─)userid> ")
    with open("Account/Account.json", 'r') as file:
        data = json.load(file)
    data['data'] = [user for user in data['data'] if user['userid'] != userid]
    with open("Account/Account.json", 'w') as file:
        json.dump(data, file, indent=4)
    print("   ╰─)info> Successfully Delete Account From Data");sleep(2);menu()

def update_all_page():
    pass

def bot_menu():
    print(
        "\n  [01].Follow Bot"
        "\n  [02].Reaction Bot"
        "\n  [03].Comment Bot"
        "\n  [04].Bot Join Group"
        "\n  [05].Back"
    )
    option = input("   ╰─)choice> ")
    if option in ("1","01"):
        BotMenu().follow()
    elif option in ("2","02"):
        BotMenu().reaction()
    elif option in ("3","03"):
        BotMenu().comment()
    elif option in ("4","04"):
        BotMenu().join_grup()
    elif option in ("5","05"):
        menu()
    else:
        print("   ╰─)error> Your Choices Are Unknown");sleep(2);menu()


class BotMenu:

    def __init__(self):
        self.list_cookie = json.loads(open("Cookie/Cookie.json", "r").read())
        self.ac_success, self.ac_faelid, self.ac_total, self.fp_success, self.fp_faelid, self.fp_total = 0, 0, 0, 0, 0, 0
        if len(self.list_cookie["data"]) == 0:
            print("   ╰─)info> Please \"Generate Cookies From Account\" First")
            return
        with requests.Session() as self.r:pass

    def follow(self):
        print("\n  [-] Enter the ID of the account you want to follow [-]")
        userid = input("   ╰─)userid> ")
        data_input = {}
        filter_id = []
        count = 0
        for zz in self.list_cookie["data"]:
            count += 1
            data_input.update({str(count):zz["userid"]})
            print(
                "\n  [0%s].%s (%s)"%(count, zz["userid"], zz["username"]) if count < 10
                else 
                "\n  [%s].%s (%s)"%(count, zz["userid"], zz["username"])
            )
        print("\n  [-] ID Filter So Bots Are Not Used [-]")
        filter_input = input("   ╰─)filter> ").split(",")
        for o in filter_input:
            try:filter_id.append(data_input[o])
            except KeyError:pass
        self.ac_total += len(self.list_cookie["data"])
        for data in self.list_cookie["data"]:
            cookie = data["cookie"]
            main_id = data["userid"]
            if main_id in filter_id:
                print("\n  [-] %s (%s) In Filters [-]"%(main_id, data["username"]))
                pass
            else:
                try:
                    self.ac_success += 1
                    self.list_page = json.loads(open("Database/%s.json"%(main_id),"r").read())
                except:
                    self.ac_faelid += 1
                    self.list_page = None
                    print("   ╰─)info> Page Data From %s (%s) Not Saved         "%(main_id,data["username"]), end="\r");sleep(2)
                if self.list_page == None:
                    pass
                else:
                    self.fp_total += len(self.list_page["data"])
                    for data_page in self.list_page["data"]:
                        status = self.follow_user(userid, data_page["page_id"], data_page["page_name"], cookie)
                        if status:
                            self.fp_success += 1
                            self.print_info("[green]follow ok");sleep(1)
                        else:
                            self.fp_faelid += 1
                            self.print_info("[red]follow error")
        print("\n  [-] Finished [-]                     ")
    
    def follow_user(self, userid, page_id, page_name, old_cookie):
        try:
            cookie = old_cookie + ";i_user=%s"%(page_id)
            with requests.Session() as r:
                Data = {
                    "key": key["key"],
                    "cookie": cookie,
                    "profile_id": userid
                }
                response = r.post("https://alexander-random-tools.glitch.me/api/index.php?tools=followfacebookaccount",allow_redirects=True,data=Data)
                if '"actor_subscribe"' in response.text:
                    if '"Follow"' in response.text:
                        return True
                    elif '"Follow"' in response.text:
                        return False
                else:
                    return False
        except Exception:
            return False

    def reaction(self):
        ReactType = []
        data_input = {}
        filter_id = []
        count = 0
        print("\n  [-] Enter the Post ID [-]")
        post_id = input("   ╰─)post_id> ")
        print(
            "\n  [-] React Type [-]"
            "\n  [01].Like"
            "\n  [02].Love"
            "\n  [03].Haha"
            "\n  [04].Wow"
            "\n  [05].Care"
            "\n  [06].Sad"
            "\n  [07].Angry"
        )
        InputType = input("   ╰─)type> ").split(",")
        for ChoiceType in InputType:
            if ChoiceType in ['1','01']:Type = '1635855486666999'
            if ChoiceType in ['2','02']:Type = '1678524932434102'
            if ChoiceType in ['3','03']:Type = '115940658764963'
            if ChoiceType in ['4','04']:Type = '478547315650144'
            if ChoiceType in ['5','05']:Type = '613557422527858'
            if ChoiceType in ['6','06']:Type = '908563459236466'
            if ChoiceType in ['7','07']:Type = '444813342392137'
            ReactType.append(Type)
        for zz in self.list_cookie["data"]:
            count += 1
            data_input.update({str(count):zz["userid"]})
            print(
                "\n  [0%s].%s (%s)"%(count, zz["userid"], zz["username"]) if count < 10
                else 
                "\n  [%s].%s (%s)"%(count, zz["userid"], zz["username"])
            )
        print("\n  [-] ID Filter So Bots Are Not Used [-]")
        filter_input = input("   ╰─)filter> ").split(",")
        for o in filter_input:
            try:filter_id.append(data_input[o])
            except KeyError:pass
        self.ac_total += len(self.list_cookie["data"])
        for data in self.list_cookie["data"]:
            cookie = data["cookie"]
            main_id = data["userid"]
            if main_id in filter_id:
                print("\n  [-] %s (%s) In Filters [-]"%(main_id, data["username"]))
                pass
            else:
                try:
                    self.ac_success += 1
                    self.list_page = json.loads(open("Database/%s.json"%(main_id),"r").read())
                except:
                    self.ac_faelid += 1
                    self.list_page = None
                    print("   ╰─)info> Page Data From %s (%s) Not Saved         "%(main_id,data["username"]), end="\r");sleep(2)
                if self.list_page == None:
                    pass
                else:
                    self.fp_total += len(self.list_page["data"])
                    for data_page in self.list_page["data"]:
                        react = random.choice(ReactType)
                        status = self.react_post(post_id, data_page["page_id"], react, cookie)
                        if status:
                            self.fp_success += 1
                            self.print_info("[bold green]%s"%(react));sleep(1)
                        else:
                            self.fp_faelid += 1
                            self.print_info("[bold red]react error")
        print("\n  [-] Finished [-]                     ")

    def react_post(self, post_id, page_id, type, old_cookie):
        try:
            cookie = old_cookie + ";i_user=%s"%(page_id)
            with requests.Session() as r:
                Data = {
                    "key": key["key"],
                    "cookie": cookie,
                    "post_id": post_id,
                    "type": type
                }
                response = r.post("https://alexander-random-tools.glitch.me/api/index.php?tools=reactfacebookpost",allow_redirects=True,data=Data)
                if "'can_viewer_react': True" in str(response.json()) and page_id in str(response.json()):
                    return True
                else:
                    return False
        except Exception:
            return False

    def comment(self):
        print("\n  [-] Enter the Post ID [-]")
        post_id = input("   ╰─)post_id> ")
        print("\n  [-] Enter Comment Text [-]")
        text = input("   ╰─)text> ").split("|")
        data_input = {}
        filter_id = []
        count = 0
        for zz in self.list_cookie["data"]:
            count += 1
            data_input.update({str(count):zz["userid"]})
            print(
                "\n  [0%s].%s (%s)"%(count, zz["userid"], zz["username"]) if count < 10
                else 
                "\n  [%s].%s (%s)"%(count, zz["userid"], zz["username"])
            )
        print("\n  [-] ID Filter So Bots Are Not Used [-]")
        filter_input = input("   ╰─)filter> ").split(",")
        for o in filter_input:
            try:filter_id.append(data_input[o])
            except KeyError:pass
        self.ac_total += len(self.list_cookie["data"])
        for data in self.list_cookie["data"]:
            cookie = data["cookie"]
            main_id = data["userid"]
            if main_id in filter_id:
                print("\n  [-] %s (%s) In Filters [-]"%(main_id, data["username"]))
                pass
            else:
                try:
                    self.ac_success += 1
                    self.list_page = json.loads(open("Database/%s.json"%(main_id),"r").read())
                except:
                    self.ac_faelid += 1
                    self.list_page = None
                    print("   ╰─)info> Page Data From %s (%s) Not Saved         "%(main_id,data["username"]), end="\r");sleep(2)
                if self.list_page == None:
                    pass
                else:
                    self.fp_total += len(self.list_page["data"])
                    for data_page in self.list_page["data"]:
                        status = self.comment_post(post_id, data_page["page_id"], random.choice(text), cookie)
                        if status:
                            self.fp_success += 1
                            self.print_info("[bold green]comment ok");sleep(1)
                        else:
                            self.fp_faelid += 1
                            self.print_info("[bold red]comment error")
        print("\n  [-] Finished [-]                     ")

    def comment_post(self, post_id, page_id, text, old_cookie):
        try:
            cookie = old_cookie + ";i_user=%s"%(page_id)
            with requests.Session() as r:
                Data = {
                    "key": key["key"],
                    "cookie": cookie,
                    "post_id": post_id,
                    "text": text
                }
                response = r.post("https://alexander-random-tools.glitch.me/api/index.php?tools=commentfacebookpost",allow_redirects=True,data=Data)
                if '"comment_create"' in response.text:
                    if '"Edit or delete this"' in response.text:
                        return True
                    else:
                        return False
                else:
                    return False
        except Exception:
            return False

    def join_grup(self):
        print("\n  [-] Enter Group ID [-]")
        grup_id = input("   ╰─)grup_id> ")
        data_input = {}
        filter_id = []
        count = 0
        for zz in self.list_cookie["data"]:
            count += 1
            data_input.update({str(count):zz["userid"]})
            print(
                "\n  [0%s].%s (%s)"%(count, zz["userid"], zz["username"]) if count < 10
                else 
                "\n  [%s].%s (%s)"%(count, zz["userid"], zz["username"])
            )
        print("\n  [-] ID Filter So Bots Are Not Used [-]")
        filter_input = input("   ╰─)filter> ").split(",")
        for o in filter_input:
            try:filter_id.append(data_input[o])
            except KeyError:pass
        self.ac_total += len(self.list_cookie["data"])
        for data in self.list_cookie["data"]:
            cookie = data["cookie"]
            main_id = data["userid"]
            if main_id in filter_id:
                print("\n  [-] %s (%s) In Filters [-]"%(main_id, data["username"]))
                pass
            else:
                try:
                    self.ac_success += 1
                    self.list_page = json.loads(open("Database/%s.json"%(main_id),"r").read())
                except:
                    self.ac_faelid += 1
                    self.list_page = None
                    print("   ╰─)info> Page Data From %s (%s) Not Saved         "%(main_id,data["username"]), end="\r");sleep(2)
                if self.list_page == None:
                    pass
                else:
                    self.fp_total += len(self.list_page["data"])
                    for data_page in self.list_page["data"]:
                        status = self.joined(grup_id, data_page["page_id"], data_page["page_name"], cookie)
                        if status:
                            self.fp_success += 1
                            self.print_info("[green]join ok");sleep(1)
                        else:
                            self.fp_faelid += 1
                            self.print_info("[red]join error")
        print("\n  [-] Finished [-]                     ")

    def joined(self, grup_id, page_id, page_name, old_cookie):
        try:
            cookie = old_cookie + ";i_user=%s"%(page_id)
            with requests.Session() as r:
                Data = {
                    "key": key["key"],
                    "cookie": cookie,
                    "grup_id": grup_id
                }
                response = r.post("https://alexander-random-tools.glitch.me/api/index.php?tools=joinfacebookgroup",allow_redirects=True,data=Data)
                if '"Join"' in response.text:
                    return True
                else:
                    return False
        except Exception:
            return False

    def print_info(self, text):
        print("[bold white]   ╰─)%s> [white]Account : [green]%s[white]|[red]%s[white]|[blue]%s  [white](Page : [green]%s[white]|[red]%s[white]|([blue]%s ?[white]))                   "%(text, self.ac_success, self.ac_faelid, self.ac_total, self.fp_success, self.fp_faelid, self.fp_total), end="\r")


def cek_login_key(key):
    try:
        with requests.Session() as r:
            Data = {
                "key":key
            }
            response = r.post("https://alexander-random-tools.glitch.me/api/index.php?tools=cek_login_key",allow_redirects=True,data=Data)
            if '"Your Key Expired"' in response.text:
                return "Key {} Expired".format(key)
            elif '"Invalid Your Key, Go To Facebook"' in response.text:
                return "Key {} Not registered".format(key)
            elif '"Server Error"' in response.text:
                return 'Server Error, Try Again Sometime'
            else:
                return "Key Valid"
    except Exception as e:
        return e

def detect_time_of_day():
    now = datetime.datetime.now().time()
    if now > datetime.datetime.strptime('19:00', '%H:%M').time() and now < datetime.datetime.strptime('23:59', '%H:%M').time():
        return "Evening"
    elif now > datetime.datetime.strptime('23:59', '%H:%M').time() and now < datetime.datetime.strptime('10:00', '%H:%M').time():
        return "Night"
    elif now > datetime.datetime.strptime('10:00', '%H:%M').time() and now < datetime.datetime.strptime('13:00', '%H:%M').time():
        return "Afternoon"
    else:
        return "Afternoon"

def Buy_Key(info):
    baner()
    print(
        "\n  [-] {} [-]".format(info),
        "\n  [01].1 Sunday 15k"
        "\n  [02].1 Month 50k"
        "\n  [03].Enter Key"
        "\n  [04].Exit"
    )
    option = input("   ╰─)choice> ")
    if os.name == "nt":
        print("\n  [-] Please send a message to Facebook Alexander Urluv [-]                     ")
    else:
        if option in ("1","01"):
            text = "Happy {} Brother Alexander\n I want to buy a Tools Facebook Boost key with a period of 1 week".replace(" ","%20").replace("\n","%0A").format(detect_time_of_day())
            os.system("xdg-open https://m.facebook.com/alexanderurluv?text=%s"%(text))
        elif option in ("2","02"):
            text = "Happy {} Brother Alexander\n I want to buy a Tools Facebook Boost key with a period of 1 week".replace(" ","%20").replace("\n","%0A").format(detect_time_of_day())
            os.system("xdg-open https://m.facebook.com/alexanderurluv?text=%s"%(text))
        elif option in ("3","03"):
            print("\n  [-] Enter your Key [-]                     ")
            key_ = input("   ╰─)key> ")
            key_info = check_login_key(key_)
            if key_info == "Key Valid":
                open("Data/Key.json","w").write(json.dumps({"key":key_}))
                print("   ╰─)success> Login Successfully");sleep(2)
                exit()
            else:
                print("   ╰─)error> Cannot Enter Using Key");sleep(2)
                Buy_Key(key_info)
        elif option in ("4","04"):
            exit()
        else:
            print("   ╰─)error> Unknown Options");sleep(2);Buy_Key("Buy Key For Script Access")



def check_ownership():
    if __Author__ != "Alexander Urluv":
        print("Author : False");exit()
    if __Whatsapp__ != "Not One":
        print("Whatsapp : False");exit()
    if __Facebook__ != "https://www.facebook.com/alexanderurluv":
        print("Facebook : False");exit()
    if __Instagram__ != "https://www.instagram.com/alexanderurluv":
        print("Instagram : False");exit()
    if __Script__ != "Facebook Boost":
        print("Script : False");exit()





if __name__ == "__main__":
    check_ownership()
    CreateFolder()
    if key == None:
        Buy_Key("Buy Key For Script Access")
    else:
        key_info = check_login_key(key["key"])
        if key_info == "Key Valid":
            menu()
        else:
            Buy_Key(key_info)
