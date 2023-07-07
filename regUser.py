from selenium import webdriver
from time import *
from selenium.webdriver.common.by import By
from PIL import Image
import pytesseract
from faker  import Faker
import random

class UserInfo:
    def __init__(self):
        self.phoneNum = "18611122444"
        self.enterpriseName = "中建"
        self.locate = "北京市"
        self.name = "李先生"
        self.duties = "无"

def registerUser(driver,user_info:UserInfo):
    # 点击新增用户按钮
    btn_add =  driver.find_element(By.XPATH,'//main//div//button[@class="smallbtn addBtn"]')
    btn_add.click() 
    sleep(2)
    # 账号手机
    phone_num = driver.find_element(By.XPATH,'//main//div//input[@class="el-input__inner" and @placeholder="请输入手机号"]')
    phone_num.send_keys(user_info.phoneNum) 
    # 单位名称
    enterprise_name = driver.find_element(By.XPATH,'//main//div//input[@class="el-input__inner" and @placeholder="请输入单位名称"]')
    enterprise_name.send_keys(user_info.enterpriseName) 
    # 地址
    locate_btn = driver.find_element(By.XPATH,'//main//div//u[@class="editFont"]')
    locate_btn.click()
    sleep(2)
    locate_input = driver.find_element(By.XPATH,'//main//div//input[@id="searchInput"]')
    locate_input.send_keys(user_info.locate) 
    locate_search = driver.find_element(By.XPATH,'//div//button[@id ="searchIcon"]')
    locate_search.click()
    sleep(2)
    locate_comfirm = driver.find_element(By.XPATH,'//main//div//button[@class="ensureBtn"]')
    locate_comfirm.click()
    sleep(2)
    # 联系方式
    telephone_num = driver.find_element(By.XPATH,'//main//div//input[@placeholder="请输入电话号码，例如：座机号或手机号"]')
    telephone_num.send_keys(user_info.phoneNum) 
    email_addr = driver.find_element(By.XPATH,'//main//div//input[@placeholder="请输入公司邮箱"]')
    email_addr.send_keys(user_info.phoneNum+"@163.com") 
    # 姓名
    name = driver.find_element(By.XPATH,'//main//div//input[@placeholder="请输入您的姓名"]')
    name.send_keys(user_info.name) 
    # 职务
    duties = driver.find_element(By.XPATH,'//main//div//input[@placeholder="请输入您的职务名称"]')
    duties.send_keys(user_info.duties) 
    # 保存
    sleep(2)
    all_comfirm = driver.find_element(By.XPATH,'//main//div//button[@class="el-button el-button--primary"]')
    all_comfirm.click()
    sleep(5)

def login(driver)->bool:
    # 登录
    sleep(2)
    user_name = driver.find_element(By.XPATH,'//main//div//input[@class="el-input__inner" and @placeholder="用户名"]')
    user_name.send_keys("jiaojingwei@admin.com") 
    user_name = driver.find_element(By.XPATH,'//main//div//input[@class="el-input__inner" and @placeholder="密码"]')
    user_name.send_keys("123456") 

    #验证码
    imag = driver.find_element(By.XPATH,'//main//div//img')
    imag.screenshot("code.png")
    imag = Image.open("code.png")
    #去色处理
    imag = imag.convert('L')
    imag.save("test.png")
    #图片二值化
    threshold = 130
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    photo = imag.point(table, '1')
    photo.save("test1.png")

    code = pytesseract.image_to_string(Image.open("test1.png"))[0:4]
    id_code = driver.find_element(By.XPATH,'//main//div//input[@class="el-input__inner" and @placeholder="验证码"]')
    id_code.send_keys(code)
    sleep(2)
    #登录按钮
    login_btn =  driver.find_element(By.XPATH,'//main//div//button[@class="el-button el-button--primary"]')
    login_btn.click()
    # 左侧选单
    sleep(5)
    user_manager =  driver.find_element(By.XPATH,'//aside//div[@class="el-submenu__title"]')
    user_manager.click()
    sleep(2)
    enterprise_manager =  driver.find_element(By.XPATH,'//ul//li[text()="企业管理"]')
    enterprise_manager.click()
    sleep(2)

def trylogin(driver):
    while True:
        try:
            driver.get('https://libunity.pkpm.cn:6004/')  # 打开指定路径的页面
            login(driver)
            break
        except:
            pass

def random_name():
    # 删减部分，比较大众化姓氏
    firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻水云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅卞齐康伍余元卜顾孟平" \
                "黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计成戴宋茅庞熊纪舒屈项祝董粱杜阮席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田胡凌霍万柯卢莫房缪干解应宗丁宣邓郁单杭洪包诸左石崔吉" \
                "龚程邢滑裴陆荣翁荀羊甄家封芮储靳邴松井富乌焦巴弓牧隗山谷车侯伊宁仇祖武符刘景詹束龙叶幸司韶黎乔苍双闻莘劳逄姬冉宰桂牛寿通边燕冀尚农温庄晏瞿茹习鱼容向古戈终居衡步都耿满弘国文东殴沃曾关红游盖益桓公晋楚闫"
    # 百家姓全部姓氏
    # firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平" \
    #             "黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董粱杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫经房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮" \
    #             "龚程嵇邢滑裴陆荣翁荀羊於惠甄麴家封芮羿储靳汲邴糜松井段富巫乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭厉戎祖武符刘景詹束龙叶幸司韶郜黎蓟薄印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阴欎胥能苍" \
    #             "双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍舄璩桑桂濮牛寿通边扈燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘匡国文寇广禄阙东殴殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空" \
    #             "曾毋沙乜养鞠须丰巢关蒯相查後荆红游竺权逯盖益桓公晋楚闫法汝鄢涂钦归海帅缑亢况后有琴梁丘左丘商牟佘佴伯赏南宫墨哈谯笪年爱阳佟言福百家姓终"
    # 女孩名字
    girl = '秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽'
    # 男孩名字
    boy = '伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘'
    # 名
    name = '中笑贝凯歌易仁器义礼智信友上都卡被好无九加电金马钰玉忠孝'

    firstName_name =firstName[random.choice(range(len(firstName)))]

    sex = random.choice(range(2))
    name_1 = ""
    # 生成并返回一个名字
    if sex > 0:
        girl_name = girl[random.choice(range(len(girl)))]
        if random.choice(range(2)) > 0:
            name_1 = name[random.choice(range(len(name)))]
        return firstName_name + name_1 + girl_name 
    else:
        boy_name = boy[random.choice(range(len(boy)))]
        if random.choice(range(2)) > 0:
            name_1 = name[random.choice(range(len(name)))]
        return firstName_name + name_1 + boy_name
province_name = [
'黑龙江省',
'青海省',
'陕西省',
'重庆',
'辽宁省',
'贵州省',
'西藏自治区',
'福建省',
'甘肃省',
'湖南省',
'湖北省',
'海南省',
'浙江省',
'河南省',
'河北省',
'江西省',
'江苏省',
'新疆维吾尔自治区',
'广西壮族自治区',
'广东省',
'山西省',
'山东省',
'安徽省',
'宁夏回族自治区',
'天津市',
'四川省',
'吉林省',
'北京市',
'内蒙古自治区',
'云南省',
'上海市']

if __name__ == '__main__':

    my_fake = Faker("zh-CN")
    # 启动Chrome浏览器，要求chromedriver驱动程序已经配置到环境变量
    # 将驱动程序和当前脚本放在同一个文件夹也可以
    driver = webdriver.Chrome()
    #第一次登录
    trylogin(driver)
    # 拟新增注册人数
    new_user_add_number = random.randint(1,100)
    print("注册人数：" + new_user_add_number)
    new_user_add_number_current = 0
    while True:
        try:
            if new_user_add_number == new_user_add_number_current:
                break
            name = random_name()
            user_info = UserInfo()
            user_info.phoneNum = my_fake.phone_number()
            user_info.enterpriseName = name
            user_info.locate = my_fake.city()
            user_info.name = name
            user_info.duties = "无"
            registerUser(driver,user_info)
            new_user_add_number_current += 1
        except:
            driver.close()
            driver = webdriver.Chrome()
            trylogin(driver)