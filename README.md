
# pytestDemo

本项目实现接口自动化的技术选型：**Python+Requests+Pytest+YAML+Allure** ，主要是针对本人的一个接口项目来开展的，通过 Python+Requests 来发送和处理HTTP协议的请求接口，使用 Pytest 作为测试执行器，使用 YAML 来管理测试数据，使用 Allure 来生成测试报告。

>相关接口项目：[使用 Python+Flask+MySQL+Redis 开发简单接口实例](https://github.com/wintests/flaskDemo)

## 项目说明

本项目在实现过程中，把整个项目拆分成请求方法封装、HTTP接口封装、关键字封装、测试用例等模块。

首先利用Python把HTTP接口封装成Python接口，接着把这些Python接口组装成一个个的关键字，再把关键字组装成测试用例，而测试数据则通过YAML文件进行统一管理，然后再通过Pytest测试执行器来运行这些脚本，并结合Allure输出测试报告。

当然，如果感兴趣的话，还可以再对接口自动化进行Jenkins持续集成。

## 项目部署

首先，下载项目源码后，在根目录下找到 ```requirements.txt``` 文件，然后通过 pip 工具安装 requirements.txt 依赖，执行命令：

```
pip3 install -r requirements.txt
```

接着，修改 ```config/setting.ini``` 配置文件，在Windows环境下，安装相应依赖之后，在命令行窗口执行命令：

```
pytest
```

**注意**：因为我这里是针对自己的接口项目进行测试，如果想直接执行我的测试用例来查看效果，需要提前部署上面提到的 [flaskDemo](https://github.com/wintests/flaskDemo) 接口项目。

## 项目结构

- api ====>> 接口封装层，如封装HTTP接口为Python接口
- common ====>> 各种工具类
- core ====>> requests请求方法封装、关键字返回结果类
- config ====>> 配置文件
- data ====>> 测试数据文件管理
- operation ====>> 关键字封装层，如把多个Python接口封装为关键字
- pytest.ini ====>> pytest配置文件
- requirements.txt ====>> 相关依赖包文件
- testcases ====>> 测试用例

## 关键字封装说明

关键字应该是具有一定业务意义的，在封装关键字的时候，可以通过调用多个接口来完成。在某些情况下，比如测试一个充值接口的时候，在充值后可能需要调用查询接口得到最新账户余额，来判断查询结果与预期结果是否一致，那么可以这样来进行测试：

- 1, 首先，可以把 **```充值-查询```** 的操作封装为一个关键字，在这个关键字中依次调用充值和查询的接口，并可以自定义关键字的返回结果。
- 2, 接着，在编写测试用例的时候，直接调用关键字来进行测试，这时就可以拿到关键字返回的结果，那么断言的时候，就可以直接对关键字返回结果进行断言。

## 测试报告效果展示

在命令行执行命令：```pytest``` 运行用例后，会得到一个测试报告的原始文件，但这个时候还不能打开成HTML的报告，还需要在项目根目录下，执行命令启动 ```allure``` 服务：

```
# 需要提前配置allure环境，才可以直接使用命令行
allure serve ./report
```

最终，可以看到测试报告的效果图如下：

![image.png](https://upload-images.jianshu.io/upload_images/16853007-248f805c82dbf99c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

https://javabetter.cn/sidebar/sanfene/mysql.html#_19-%E8%AF%B4%E8%AF%B4-sql-%E7%9A%84%E8%AF%AD%E6%B3%95%E6%A0%91%E8%A7%A3%E6%9E%90-%E8%A1%A5%E5%85%85

https://python3-cookbook.readthedocs.io/zh-cn/latest/c01/p04_find_largest_or_smallest_n_items.html


# 查最大最小的元素
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
def least_nums(nums, n):
    if n>=len(nums):
        return sorted(nums)
    return sorted(nums)[:n]

import heapq
max_5 = heapq.nlargest(5, nums)
min_6 = heapq.nsmallest(6, nums)

print(least_nums(nums, 3), max_5, min_6)

# 保留最后N个元素
from collections import deque
nums_2 = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
def search(nums, history):
    q = deque(maxlen=history)
    for i in nums:
        q.append(i)
    return q

f = search(nums_2, 5)
print(f)
#  怎样实现一个按优先级排序的队列？ 并且在这个队列上面每次 pop 操作总是返回优先级最高的那个元素
import heapq
class PriorityQueue:
    def __init__(self):
        self._queu = []
        self._index = 0
    def push(self, item, priority):
        """
        添加元素，元素越小等级越高
        """
        heapq.heappush(
            self._queu,
            (priority, self._index, item)
        )
        self._index +=1
    
    def pop(self):
        """
        返回优先级最高的元素
        """
        return heapq.heappop(self._queu)[-1]

pq = PriorityQueue()

tasks = [
    ("打印任务", 3),
    ("紧急报警", 1),
    ("后台同步", 5),
    ("用户请求", 2)
]

for task, p in tasks:
    pq.push(task, p)

while pq._queu:
    print(pq.pop())

# 怎样实现一个键对应多个值的字典（也叫 multidict）？

from collections import defaultdict

def multidict(pairs):
    d = defaultdict(list)
    for key, value in pairs:
        d[key].append(value)
    return d
pairs = [
    ('a', 1),
    ('a', 2),
    ('a', 3),
    ('b', 4),
    ('b', 5)
]
c = multidict(pairs)
print(c)

# 你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。
from collections import OrderedDict
import json
def OrderedDict_1(pairs):
    d = OrderedDict()
    for key, value in pairs:
        d[key] = value
    return json.dumps(d)
pairs_2 = [
    ('a', 1),
    ('a', 2),
    ('b', 4),
    ('b', 5),
    ('a', 3)
]
print(OrderedDict_1(pairs_2))

# 怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）？
def prices_max(pairs):
    return max(zip(pairs.values(), pairs.keys()))
def prices_min(pairs):
    return min(zip(pairs.values(), pairs.keys()))
def prices_sorted(pairs):
    return sorted(zip(pairs.values(), pairs.keys()))

prices_3 = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

print(f"最大：{prices_max(prices_3)}，最小{prices_min(prices_3),}，排序{ prices_sorted(prices_3)}")

# 怎样在两个字典中寻寻找相同点（比如相同的键、相同的值等等）？
def same_dic(dict1, dict2):
    same_keys = dict1.keys() & dict2.keys()

    same_values = set(dict1.values()) & set(dict2.values())

    same_items = dict1.items() & dict2.items()

    return {
        "same_keys": same_keys,
        "same_values": same_values,
        "same_items": same_items
    }
a = {
    "x": 1,
    "y": 2,
    "z": 3
}

b = {
    "w": 10,
    "x": 1,
    "y": 20
}

print(same_dic(a, b))

# 怎样在一个序列上面保持元素顺序的同时消除重复的值？
def dedupe(items):
    senn = set()
    for item in items:
        if item not in senn:
            yield item
            senn.add(item)

nums = [1,5,2,1,9,1,5]

print(list(dedupe(nums)))








import yaml
from appium import webdriver
from appium.options.android import UiAutomator2Options

class Devices:
    def __init__(self):
          self.devices = self.read_devices_config()
          #元素
          with open("D:/App_dome/data/locator.yaml", "r", encoding="utf-8") as f:
               self.locator_data = yaml.safe_load(f)
          #用例
          with open("D:/App_dome/data/test_devices_case.yaml", "r", encoding="utf-8") as f:
               self.case_data = yaml.safe_load(f)    

    @staticmethod
    def read_devices_config():
         with open("D:/App_dome/data/devices_config.yaml", "r", encoding="utf-8") as f:
              return yaml.safe_load(f)["devices"]
    
    def get_locator(self, page, element):
        """
        从 locator.yaml 获取定位信息
        """
        locator = self.locator_data[page][element]
        return locator["by"], locator["value"]

    def get_case(self, case_name):
        """
        获取测试用例
        """
        return self.case_data[case_name]

    def get_case_steps(self, case_name):
        """
        获取步骤并自动关联 locator
        """
        case = self.case_data[case_name]
        page = case["page"]
        result = []
        for step in case["steps"]:
            locator = self.get_locator(
                page,
                step["element"]
            )
            result.append({
                "action": step["action"],
                "locator": locator
            })
        return result
    
    def get_devices(self, devices_name):
        device = self.devices[devices_name]
        options = UiAutomator2Options()
        options.platform_name = device["platformName"]
        options.device_name = device["deviceName"]
        options.udid = device["udid"]
        options.system_port = int(device["systemPort"])  # 转换为整数
        options.app_package = device["appPackage"]
        options.app_activity = device["appActivity"]
        options.no_reset = True
        driver = webdriver.Remote(
            "http://127.0.0.1:4723",
            options=options
        )
        return driver

txt = Devices()

steps = txt.get_case_steps(
    "test_get_Device_status"
)

for step in steps:
    print(step)





import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime


class Logger:

    _logger = None

    @classmethod
    def get_logger(cls):

        if cls._logger:
            return cls._logger

        # 创建 logger
        logger = logging.getLogger("AutomationTest")

        # 日志等级
        logger.setLevel(logging.INFO)

        # 防止重复打印
        logger.propagate = False

        # 防止重复添加 handler
        if not logger.handlers:

            # 创建 logs 目录
            log_dir = "logs"

            if not os.path.exists(log_dir):
                os.makedirs(log_dir)

            # 日志文件名
            log_file = os.path.join(
                log_dir,
                f"{datetime.now().strftime('%Y-%m-%d')}.log"
            )

            # 日志格式
            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s"
            )

            # 控制台输出
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(formatter)

            # 文件输出
            file_handler = RotatingFileHandler(
                log_file,
                maxBytes=5 * 1024 * 1024,   # 5MB
                backupCount=5,
                encoding="utf-8"
            )

            file_handler.setLevel(logging.INFO)
            file_handler.setFormatter(formatter)

            # 添加 handler
            logger.addHandler(console_handler)
            logger.addHandler(file_handler)

        cls._logger = logger

        return logger



import paho.mqtt.client as mqtt
import yaml


def read_mqttconfig():
    with open("D:/App_dome/data/mqtt_config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["Mqtt"]


config = read_mqttconfig()

BROKER = config["BROKER"]
PORT = int(config["PORT"])   # ⭐关键：转 int
USERNAME = config["USERNAME"]
PASSWORD = config["PASSWORD"]
TOPIC = config["TOPIC"]

TOPIC_DOWN = f"{TOPIC}/down"
TOPIC_UP = f"{TOPIC}/up"

print(TOPIC_DOWN, TOPIC_UP)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("连接成功")

        client.subscribe(TOPIC_UP)
        client.subscribe(TOPIC_DOWN)

        print("订阅:", TOPIC_UP)
        print("订阅:", TOPIC_DOWN)

def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    if msg.topic == TOPIC_DOWN:
        print("down消息：")
        print(payload)
    elif msg.topic == TOPIC_UP:
        print("up消息：")
        print(payload)

client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

client.loop_forever()



from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from appium.webdriver.webelement import WebElement
from common.logger import Logger

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 获取元素
    def find_element(self, locator, timeout=10):
        """
        等待元素出现
        :param locator: (By.ID, "xxx")
        :param timeout:
        :return:
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutError:
            raise Exception(f"元素等待超时：{locator}")
    
    # 元素点击
    def element_click(self, locator):
        self.find_element(locator).click()



from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
class Devices(BasePage):

    device_btn = (By.XPATH, '//*[@content-desc="设备"]')
    def click(self):
        self.element_click(self.device_btn)




import pytest
from common.read_data import Devices

@pytest.fixture(params=["devices1"])
def driver(request):
    decices_name = request.param
    devices = Devices()  # 创建实例
    driver = devices.get_devices(decices_name)
    yield driver
    driver.quit()



import time
from pages.devices_page import Devices


class Testdevices:

    def test_login_success(self, driver):
        drivers = Devices(driver)
        drivers.click()


[pytest]
pythonpath = .



https://github.com/hantmac/Python-Interview-Customs-Collection

1.掌握接口理论知识及运行原理
	理解接口（API）的基本概念、作用以及客户端与服务端的数据交互流程；
	掌握常见接口通信协议：
	HTTP / HTTPS 协议
	RESTful API 规范
	WebSocket 长连接通信
	MQTT 发布/订阅通信模型
	熟悉接口请求执行流程：
	客户端(Client)
		  |
		  | 发送 Request
		  |
		  v
	服务端(Server)
		  |
		  | 业务处理、数据库操作
		  |
		  v
	返回 Response
	熟悉 HTTP 请求组成：
	请求地址 URL
	请求方法 Method（GET、POST、PUT、DELETE）
	请求头 Headers
	请求参数 Params
	请求体 Body
	掌握接口响应内容分析：
	HTTP 状态码
	200 请求成功
	400 参数错误
	401 未认证
	403 权限不足
	404 接口不存在
	500 服务端异常
	响应数据格式：
	JSON
	XML
	理解接口认证机制：
	Cookie / Session
	Token
	JWT
	OAuth
	掌握接口测试核心验证点：
	接口功能正确性
	参数校验
	返回数据校验
	异常场景测试
	权限测试
	安全测试
	性能测试
	熟悉接口测试工具：
	Postman
	JMeter
	pytest + requests
	Swagger
	能够根据接口文档分析业务逻辑，设计接口测试用例，并完成接口自动化测试。

2.掌握HTTP网络协议及Restful规范
	HTTP 是客户端和服务端通信的基础协议，接口请求由请求行、请求头、请求参数组成，服务端返回响应状态码和数据。RESTful 是一种接口设计规范，
	通过 URL 表示资源，通过 GET、POST、PUT、DELETE 等 HTTP 方法表示增删改查操作。我在接口测试中会根据接口文档校验请求参数、响应数据、状态码、权限以及异常场景

3.Requests库基本应用及Request库源码讲解
	Requests 是 Python 中用于发送 HTTP 请求的第三方库。在接口自动化测试中，我通常使用 requests 模拟客户端调用接口，通过 GET、POST 等方法发送请求，
	使用 Response 对象获取状态码、响应数据和响应时间，并结合 pytest 进行断言。
	源码层面 requests.get 最终会进入 Session 对象处理请求，通过 HTTPAdapter 调用 urllib3 完成底层网络通信。
	

4.掌握Json库应用

5.掌握JsonPath提取Json格式数据操作行为

6.掌握接口自动化测试框架的底层设计封装与优化，实现单接口与接口业务链路的自动化测试

7.基于pytest实现接口测试框架用例管理

8.基于Pytest实现接口测试用例管理及Fixture配置
	在接口自动化中，我使用 Pytest 管理测试用例，通过测试类和模块划分业务场景，
	使用 pytest.ini 统一管理运行规则。Fixture 用于实现测试前置和后置处理，例如环境初始化、数据库连接、登录获取 Token 等。
	根据资源生命周期选择 function、class、module、session 等作用域，并结合参数化实现多数据场景测试。
	Pytest Fixture 通过 yield 实现前置和后置处理，yield 前执行初始化操作，比如环境准备、登录获取 Token、数据库连接；yield 后执行清理操作，
	比如关闭连接、删除测试数据。通过 scope 控制生命周期，例如 function 每个用例执行，session 整个测试任务执行一次。

9.结合数据驱动Yaml/Excel/Mysql实现接口测试数据管理

9.基于配置项实现对项目环境一键切换

10.掌握Flask下的Mock Server技术应用

11.掌握Faker实现测试数据自动生成

12.掌握单向/双向数据加密原理与代码逻辑设计实现





一、测试基础与测试理论
Q1. 什么是软件测试？测试的目的是什么？
参考答案： 软件测试是通过设计和执行测试活动，发现缺陷、评估软件质量与风险，并为发布决策提供依据。它不是证明“没有 Bug”，而是在有限成本下尽可能降低产品质量风险。
解析： 面试回答建议从“发现问题、验证需求、控制风险、支持发布决策”四点展开。
易错点： 不要把测试目的简单说成“找 Bug”；发现缺陷只是手段。
追问： 测试能证明软件没有缺陷吗？
Q2. 测试和调试有什么区别？
参考答案： 测试主要负责发现与暴露问题，调试主要负责定位问题原因并修复。测试关注“哪里不符合预期”，调试更关注“为什么发生”。
解析： 职责可以交叉，但思维方式不同。测试通过构造输入和场景发现问题，调试则利用日志、堆栈、断点、源码等定位根因。
易错点： “测试就是调试”属于概念混淆。
追问： 开发修复后测试还要做什么？
Q3. 黑盒、白盒、灰盒测试有什么区别？
参考答案： 黑盒不依赖内部实现，基于需求和外部行为测试；白盒了解内部代码逻辑并关注语句、分支、路径等；灰盒掌握部分内部实现，用于更有针对性的测试。
解析： 测试开发往往是灰盒能力较强：知道 API、数据库、消息协议和代码结构，同时从用户行为验证业务。
易错点： 不要把黑盒等于“完全不懂技术”。
追问： 你目前更接近哪一种？
Q4. 回归测试、冒烟测试、探索性测试分别是什么？
参考答案： 冒烟验证版本是否具备进一步测试条件；回归验证已有功能及相关链路是否被新改动破坏；探索性测试强调边测试边学习、根据观察结果动态调整测试策略。
解析： 三者不是互斥分类：一次版本测试可以先冒烟、再回归，同时穿插探索性测试。
易错点： 不要把冒烟理解成“简单跑一下全部用例”。
追问： 什么情况下必须做专项回归？
Q5. Bug 的严重程度和优先级有什么区别？
参考答案： 严重程度描述缺陷对系统/用户造成的影响；优先级描述处理的紧急程度。高严重度不一定最高优先级，高优先级也不一定严重度最高。
解析： 例如低概率导致数据彻底损坏可能严重度很高；活动当天某宣传页文案错误可能业务优先级反而很高。
易错点： 不要用 P0/P1 直接代替严重度。
追问： 你和开发对优先级意见不一致怎么办？
Q6. 为什么测试不能证明程序没有 Bug？
参考答案： 测试只能覆盖有限输入、路径和环境，存在组合爆炸、未建模场景和未知风险。测试可以增加对质量的信心，但不能数学意义上证明“无缺陷”。
解析： 优秀测试工程师会谈“风险和覆盖”，而不是追求一个虚假的“100% 无 Bug”。
易错点： 不要回答成“因为测试用例写不完”就结束。
追问： 那如何判断“可以上线”？
Q7. 什么是测试左移和测试右移？
参考答案： 测试左移强调在需求、设计、开发早期介入，尽早发现可测试性和质量风险；测试右移强调上线后通过监控、灰度、日志、真实用户反馈等持续验证系统。
解析： 对 IoT/App 场景，还可以延伸到设备现场、弱网、升级、异常恢复等线上问题。
易错点： 不要把左移理解成“让测试提前写用例”这么简单。
追问： 如何提高需求阶段的可测试性？
Q8. 缺陷生命周期通常有哪些阶段？
参考答案： 常见流程是 New/Submitted → Assigned → Open/In Progress → Fixed → Retest → Closed；如果验证失败可能回到 Reopen。不同团队的状态命名会不同。
解析： 关键是形成闭环，并保留复现步骤、环境、日志、版本、严重度、优先级等证据。
易错点： 不要死背状态名字，重点是生命周期和闭环。
追问： 什么情况下 Bug 可以关闭？
Q9. 如何判断一个测试用例是否设计得好？
参考答案： 好的用例应覆盖明确风险，前置条件清楚，步骤可执行，数据可复现，预期可判定，具备必要的异常/边界覆盖，并且维护成本合理。
解析： 优秀用例不是越多越好，而是用较少的用例覆盖较高风险。
易错点： “一条用例写十页”并不等于高质量。
追问： 如何减少冗余测试用例？
二、测试用例设计与场景题
Q10. 等价类和边界值如何使用？
参考答案： 先把输入划分为有效等价类和无效等价类，再重点覆盖边界及边界附近值。
解析： 例如温度范围 0~300：重点考虑 -1、0、1、299、300、301，同时补充空值、字符串、浮点、超长、特殊字符等类型异常。
易错点： 只测 0 和 300 往往不够；类型维度也要考虑。
追问： 接口参数是字符串时怎么设计？
Q11. 如何测试一个登录功能？
参考答案： 功能上覆盖正确/错误账号密码、空值、锁定；边界覆盖长度和特殊字符；安全覆盖越权、暴力尝试、Token/Session；兼容覆盖多端；性能覆盖并发登录；异常覆盖超时、断网、重试。
解析： 建议用“功能、边界、异常、安全、性能、兼容、数据一致性”七维度组织回答。
易错点： 不要只列十几个输入框用例。
追问： 登录按钮连续点击 10 次会发生什么？
Q12. 如何测试一个电梯？
参考答案： 从功能、边界、异常、并发、安全和性能出发。包括楼层选择、开关门、超载、最高/最低楼层、断电、按钮同时按下、门未关闭禁止运行等。
解析： 这是经典开放题，面试官考的是测试思维框架，而不是电梯知识。
易错点： 不要无限罗列场景而没有分类。
追问： 两个人同时按不同楼层怎么测试？
Q13. 如何测试一个红包系统？
参考答案： 关注金额边界、人数边界、重复请求、扣款与发放一致性、并发抢红包、超时、取消、服务重启、消息重复、幂等、账务正确性。
解析： 高阶回答应主动提到“事务、幂等、一致性、并发竞态”。
易错点： 只说“金额最大最小”属于初级回答。
追问： 扣款成功但红包创建失败怎么办？
Q14. 如何基于风险制定测试优先级？
参考答案： 先识别影响最大、概率较高、变更范围大、依赖复杂或不可逆的风险，再优先覆盖核心链路和高损失场景。
解析： 可以采用影响度 × 发生概率 × 可检测性等思路，但不要机械计算。
易错点： 不要用“所有 P0 都先测”替代风险分析。
追问： 时间只剩半小时，100 个用例怎么选？
三、Python 基础与进阶
Q15. list、tuple、set、dict 的区别？
参考答案： list 有序可变；tuple 有序不可变；set 用于无序集合与去重；dict 保存键值映射。Python 运行时还要注意对象可变性与哈希能力。
解析： 测试开发里 list 常用于测试数据集合，dict 常用于 JSON，set 常用于去重或集合比较。
易错点： 不要说“tuple 一定比 list 快很多”这种绝对结论。
追问： 为什么 set 的元素通常要求可哈希？
Q16. == 和 is 的区别？
参考答案： == 比较值是否相等；is 比较两个引用是否指向同一个对象。
解析： 与 None 比较时通常使用 `is None`。
易错点： 不要把 is 当成“地址比较”简单背诵成所有 Python 实现细节。
追问： `a=256; b=256; a is b` 一定怎样？
Q17. 浅拷贝和深拷贝？
参考答案： 浅拷贝只复制对象外层结构，嵌套引用仍可能共享；深拷贝会递归复制可复制的嵌套对象。
解析： 测试数据是嵌套 dict/list 时，经常因为共享引用导致前一个用例修改数据后污染后一个用例。
易错点： 不要把 copy.copy 理解成“完全独立”。
追问： 如何证明浅拷贝的嵌套对象共享？
Q18. split、join、strip 怎么用？
参考答案： split 把字符串按分隔符拆成序列；join 用指定分隔符拼接字符串序列；strip 去掉字符串两端的空白或指定字符。
解析： 典型：`"a,b".split(",")`；`",".join(["a","b"])`；`"  a  ".strip()`。
易错点： strip 不会删除字符串中间的空格；strip("abc") 也不是删除完整子串 abc。
追问： 如何把 `"P300-1, P300-2"` 变成干净列表？
Q19. append 和 extend 的区别？
参考答案： append 把一个对象作为一个元素追加；extend 会把可迭代对象中的元素逐个加入。
解析： 例如 `[1].append([2,3])` 得到 `[1,[2,3]]`；`[1].extend([2,3])` 得到 `[1,2,3]`。
易错点： 不要只记“一个加一个、一个加多个”，要知道参数本身的可迭代性。
追问： `extend("abc")` 会发生什么？
Q20. 列表推导式有什么优缺点？
参考答案： 优点是表达简洁；缺点是逻辑复杂时可读性下降。测试代码应优先保证可维护性。
解析： 简单的数据转换适合推导式，包含多层条件或副作用时建议普通循环。
易错点： 不要为了“写一行代码”牺牲可读性。
追问： 如何把字符串列表转成整数列表？
Q21. 什么是可变对象和不可变对象？
参考答案： list、dict、set 等常见对象可变；int、float、str、tuple 等通常不可变。不可变是对象内容不能原地修改，而不是变量不能重新绑定。
解析： 这直接关联函数参数传递、默认参数和浅拷贝问题。
易错点： 不要说“变量传的是引用/值”就结束，Python 更适合表述为对象引用绑定。
追问： 函数参数修改为什么会影响外部 list？
Q22. Python 的可变默认参数问题是什么？
参考答案： 例如 `def f(x=[])`，默认 list 在函数定义时创建，多次调用会复用同一个对象。常用写法是 `def f(x=None): x=[] if x is None else x`。
解析： 这是 Python 面试经典题，也能暴露你是否真正理解对象生命周期。
易错点： 不要只记结论，不知道原因。
追问： 为什么默认参数不是每次调用重新创建？
Q23. 什么是装饰器？
参考答案： 装饰器本质上是接收函数并返回新函数/可调用对象的机制，用于在不直接修改原函数主体的情况下增加行为。
解析： Pytest 的 fixture、部分 mark 等使用了装饰器机制。
易错点： 不要把装饰器说成“继承”。
追问： 如何写一个统计函数执行时间的装饰器？
Q24. yield 和 return 的区别？
参考答案： return 结束函数并返回结果；yield 使函数变成生成器，每次迭代提供一个值并暂停，后续继续执行。
解析： Pytest fixture 常用 yield 把资源暴露给测试，并在 yield 后执行 teardown。
易错点： 不要说“yield 一定只能返回一次”，生成器可以多次 yield。
追问： Fixture 中 yield 前后分别做什么？
Q25. 什么是迭代器和可迭代对象？
参考答案： 可迭代对象能提供迭代器；迭代器实现了 `__iter__` 和 `__next__`，通过 next 逐步取得数据。
解析： 生成器是创建迭代器的一种便捷方式。
易错点： 不要把“list 就是迭代器”当成正确结论：list 是可迭代对象，但本身不是迭代器。
追问： iter(list) 返回什么？
Q26. 什么是闭包？
参考答案： 内部函数引用了外部函数作用域中的变量，并在外部函数返回后仍可使用这些变量，这类结构可称为闭包。
解析： 面试常用循环变量迟绑定例子：多个 lambda 如果直接捕获循环变量，调用时可能都读到最终值。
易错点： 不要只背“函数套函数”。
追问： 如何解决循环 lambda 的迟绑定？
解决方法之一是使用默认参数立即绑定当前值，例如：
lambda i=i: i
Q27. 浅拷贝示例：`a=[[1],[2]]; b=a.copy(); b[0].append(3)` 为什么 a 也变？
参考答案： 因为 copy 只复制外层 list，内部两个子 list 仍然是同一个对象。
解析： 深拷贝需要递归复制嵌套结构。
易错点： 不要把“copy 就是深拷贝”混为一谈。
追问： 什么时候浅拷贝反而更合适？
数据只有一层时通常使用浅拷贝
四、Python 并发、异常与工程实践
Q28. Python 多线程、多进程、协程怎么选？
参考答案： IO 密集型可以使用线程或异步 IO；CPU 密集型在 CPython 下通常更适合多进程或把计算交给原生扩展。协程适合大量可等待的 IO 与高并发连接。
解析： 测试开发中大量 HTTP、WebSocket、MQTT IO 场景可以考虑线程池或 asyncio，取决于客户端库是否原生支持异步。
易错点： 不要机械回答“Python 多线程没用”。
追问： GIL 到底限制了什么？
限制了python字节码的并行能力
Q29. 什么是 GIL？
参考答案： CPython 的全局解释器锁限制同一解释器进程内多个线程同时执行 Python 字节码，因此纯 Python CPU 密集型任务不能简单靠多线程获得线性并行收益。IO 阻塞时线程仍能交替执行。
解析： 这也是为什么测试框架中 IO 型并发通常仍有价值。
易错点： 不要说“Python 不能多线程”。
追问： 为什么 pytest-xdist 更适合多进程隔离？
因为pytest-xdist多进程可以让每个workey拥有独立的python的运行环境，从而实现测试并行+状隔离
Q30. try/except/finally 如何设计？
参考答案： try 放可能失败的代码，except 针对可处理异常，finally 做必须执行的资源清理。
解析： 测试框架中不要为了“让用例通过”而无差别吞掉 Exception；要保留 traceback 和上下文。
易错点： 滥用 `except Exception: pass` 是危险代码味道。
追问： finally 是否绝对执行？
不是绝对执行，在程序强制终止，解释器崩溃，机器断电的情况下finally都无法执行
Q31. 为什么不推荐到处 `except Exception`？
参考答案： 它容易掩盖真实错误，让测试假通过，也会损失原始异常语义。应该捕获能明确处理的异常，并记录足够上下文。
解析： 自动化框架可以做统一异常包装，但不能把所有异常都吞掉。
易错点： 不要把“防止程序崩溃”当成测试代码唯一目标。
追问： 怎么记录异常又让 pytest 正确失败？
使用raise把异常向上抛出，让pytest最终标记未失败的
Q32. logging 为什么比 print 更适合自动化框架？
参考答案： logging 支持级别、格式、handler、文件输出、模块化配置和集中管理，便于并发、CI 和问题追踪。
解析： 建议输出时间、线程/进程、测试用例、设备 ID、Topic、请求 ID 等关键字段。
易错点： print 可以临时调试，但不适合作为长期日志体系。
追问： 并发执行时日志如何区分 worker？
pytest-xdist 可以通过 PYTEST_XDIST_WORKER 获取 gw0、gw1 等 worker 信息。
五、计算机网络与 TCP/IP
Q33. TCP 和 UDP 有什么区别？
参考答案： TCP 面向连接、可靠、有序、带重传与流量/拥塞控制；UDP 无连接、机制轻量，不保证可靠和有序。
解析： 选择协议应围绕业务要求，而不是简单理解成“TCP 快/UDP 慢”。
易错点： 不要说 TCP 一定慢、UDP 一定快。
追问： 实时视频为什么常用 UDP 类方案？
因为UDP是无连接数据报协议，不保证可靠性，协议开销小，实时性更好
Q34. TCP 三次握手为什么需要三次？
参考答案： 核心目的是让双方确认通信方向可用，并建立连接状态和初始序列号等。三次可以让主动方、被动方互相确认自己的发送与接收能力。
解析： 回答时可说明 SYN、SYN+ACK、ACK。
易错点： 不要只背“第一次客户端，第二次服务端，第三次客户端”而不解释目的。
追问： 为什么不能两次？
两次握手只能确认“客户端能发、服务器能收”，不能可靠确认“服务器能发、客户端能收”。第三次握手是为了让双方都确认彼此的收发能力，并防止历史失效连接请求造成错误连接。
Q35. TCP 四次挥手？
参考答案： 典型流程是主动关闭方发送 FIN，被动方 ACK；被动方完成剩余数据发送后再 FIN，主动方最后 ACK。
解析： 因为 TCP 是全双工，两个方向的关闭需要分别处理。
易错点： 不要把 FIN 和 ACK 简化成“服务端必须先发”。
追问： TIME_WAIT 为什么存在？
确保最后一个ACK对方能收到，防止旧连接的报文影响新连接
Q36. TIME_WAIT 和 CLOSE_WAIT 区别？
参考答案： TIME_WAIT 常见于主动关闭方，用于确保旧报文不会干扰后续连接并配合重传最后 ACK；CLOSE_WAIT 表示本端已经收到对方 FIN，但本端应用还没有完成 close。
解析： CLOSE_WAIT 大量堆积通常要检查应用是否正确关闭连接；TIME_WAIT 大量出现需要结合短连接、端口范围和连接模式分析。
易错点： 不要简单认为 TIME_WAIT 就是服务器故障。
追问： 如何用 Linux 命令定位？
Q37. TCP 粘包/拆包是什么？
参考答案： TCP 是面向字节流的协议，不保留应用层消息边界。应用发送两次数据，接收端可能一次读到；一次发送大数据，也可能多次读到。
解析： 解决需要应用层定义消息边界，如固定长度、长度字段、分隔符或自描述协议。
易错点： 这不是 TCP “出错”。
追问： HTTP 为什么不会让开发者直接面对粘包？
因为HTTP底层框架已经处理了拆包和组包的过程了
Q38. 从浏览器输入一个 URL，到页面展示发生什么？
参考答案： 常见链路：URL 解析 → DNS → TCP（HTTPS 还包括 TLS）→ HTTP 请求 → 服务端处理 → 返回响应 → 浏览器解析 HTML/CSS/JS → 继续请求资源 → DOM/CSSOM/Layout/Paint/Composite。
解析： 面试时不要只说 DNS + TCP + HTTP；浏览器渲染也是重要部分。
易错点： 具体实现依浏览器、HTTP 版本和缓存策略而不同。
追问： DNS 缓存在哪里？
DNS分层缓存，浏览器>>os>>路由器>>本地DNS>>递归DNS，越靠近客户端，越早命中
Q39. DNS 做什么？
参考答案： 把域名等名称解析为 IP 等资源记录。解析过程会受到浏览器、系统、网络设备和 DNS 服务等多层缓存影响。
解析： 测试网络问题时可先区分“域名解析失败”和“解析成功但连接失败”。
易错点： 不要把 DNS 简化成“域名转换 IP”后就完全结束。
追问： dig/nslookup 怎么用？
dig和nslookup是排查DNS解释问题的工具 
nslookup 怎么用
	nslookup 域名
	nslookup 域名 DNS服务器
	nslookup -type=A 域名
	nslookup -type=AAAA 域名
dig 怎么用
	dig 域名
	dig 域名 A
	dig @8.8.8.8 域名
	dig +short 域名
	dig +trace 域
六、HTTP / HTTPS / WebSocket
Q40. HTTP 和 HTTPS 区别？
参考答案： HTTPS 是 HTTP 在 TLS 等安全机制之上的传输方式，提供机密性、完整性和服务端身份认证等能力。
解析： 测试时要关注证书有效性、域名匹配、TLS 版本/套件、代理和中间证书链等。
易错点： 不要说“HTTPS 就是 HTTP 加一个密码”。
追问： 为什么不能全程只使用非对称加密？
Q41. 常见 HTTP 状态码怎么理解？
参考答案： 200 成功；201 创建成功；204 无内容；301/302 重定向；304 未修改；400 请求错误；401 未认证；403 无权限；404 资源不存在；405 方法不允许；409 冲突；429 请求过多；500 服务端内部错误；502 网关/上游异常；503 服务不可用；504 网关超时。
解析： 回答状态码时最好结合业务场景，而不是机械背数字。
易错点： 401 与 403 经常被混淆：前者通常是认证缺失/无效，后者通常表示已识别身份但无权限。
追问： 接口返回 200 业务失败怎么办？
接口返回200不代表业务成功，只是代表HTTP请求是正常处理的，在这种情况测试时把接口和业务返回字段的校验和区分处理，要验证接口的状态码以及根据实际业务状态进行判断是否成功
Q42. Cookie、Session、Token、JWT 有什么区别？
参考答案： Cookie 是浏览器侧存储/携带机制；Session 是服务端保存会话状态的一种方案；Token 是认证凭证的统称；JWT 是一种结构化 Token 格式。
解析： 它们并不是完全同层的概念，可以组合使用，例如 Cookie 携带 Session ID 或 JWT。
易错点： 不要把 Cookie 和 Session 当成同一个东西。
追问： JWT 为什么不能简单理解为“加密字符串”？
JWT默认是不加密的，但是有Signature(签名)作用验证数据完整性和防止篡改
Q43. GET、POST、PUT、PATCH、DELETE 怎么理解？
参考答案： GET 常用于获取资源；POST 常用于创建/触发操作；PUT 常表达对资源整体替换且通常设计为幂等；PATCH 表达部分更新；DELETE 用于删除。具体 API 仍以业务契约为准。
解析： 面试时要强调 HTTP 方法语义和实际系统设计之间的关系。
易错点： 不要说“POST 永远不幂等”。
追问： POST 可以设计成幂等吗？
POST默认不是幂等性的，但完全可以通过接口设计让 POST 具备幂等性。增加幂等键 Idempotency-Key
Q44. 什么是接口幂等性？
参考答案： 同一请求重复执行一次或多次，对业务最终状态产生相同效果。常用 request_id、幂等键、唯一约束、状态机或去重表等实现。
解析： 支付、订单、设备控制等场景尤其重要。
易错点： 幂等不等于“任何重复请求都返回一样的 HTTP 响应”，重点是业务副作用。
追问： 消息重复和接口幂等有什么关系？
消息重复是指：同一条消息被系统消费了多次，接口幂等性是指：同一业务请求执行一次或多次，最终执行的结果还是一致
Q45. WebSocket 是什么？
参考答案： WebSocket 提供客户端与服务端的双向实时通信能力。典型建立连接时先进行 HTTP Upgrade 握手，成功后进入 WebSocket 帧通信。RFC 6455 定义了握手、帧、Ping/Pong 和 Close 等机制。
解析： 它适合实时状态、消息推送、监控等场景。
易错点： 不要说“WebSocket 完全不经过 HTTP”。
追问： 101 Switching Protocols 表示什么？
服务器同意客户端协议升级，接下来通信将切换到另一种协议。 101，协议切换成功
Q46. ws 和 wss 区别？
参考答案： ws 是普通 WebSocket；wss 是 WebSocket over TLS。类比 http/https，但不能简单把 TLS 当成“HTTP 的加密”。
解析： 生产环境更常见 wss，并涉及证书和 TLS 握手。
易错点： 不要忽略证书、SNI、代理等实际问题。
追问： wss 连接失败但 ws 正常怎么办？
WS → TCP → WebSocket；WSS → TCP → TLS → WebSocket。WS正常、WSS失败，优先查 TLS/证书/443/反向代理。
Q47. WebSocket 如何测试？
参考答案： 连接成功性、鉴权、订阅/发送、消息结构、消息匹配、服务端主动推送、超时、重复、乱序、断线重连、心跳、长连接稳定性、时延和资源占用。
解析： 自动化时不要只用一次 recv；应按业务字段匹配目标消息并设置超时。
易错点： 无限 while recv 是典型死循环风险。
追问： 服务端连续推 100 条消息，你如何找到目标消息？
持续接收消息 → 根据唯一标识/业务字段匹配目标消息 → 找到后立即返回 → 超时则失败。
Q48. WebSocket 心跳和 Ping/Pong 怎么测试？
参考答案： 可以验证服务端/客户端是否按协议或业务约定维持活跃，网络异常后能否检测断开，超时后是否重连。
解析： 同时检查心跳频率、超时阈值、重复连接、后台切换等。
易错点： 心跳不等于业务消息；要区分协议层保活和业务层 heartbeat。
追问： 心跳正常但业务消息不来，问题可能在哪？
业务消息还要查“订阅 → 路由 → 业务处理 → 发布 → 接收 → 匹配”整条链路。
七、MQTT 与 IoT 测试
Q49. MQTT 是什么？
参考答案： MQTT 是基于发布/订阅模型的轻量消息协议，核心角色包括 Publisher、Subscriber 和 Broker，适合设备和实时消息场景。
解析： 测试重点从 HTTP 的 request/response 转向 topic、QoS、消息时序、会话、保活与重连。
易错点： 不要把 MQTT 说成“只能一对一”。
追问： 为什么 IoT 设备常用 MQTT？
轻量级，发布订阅，长连接， 	QoS,弱网友好，broker解耦
Q50. MQTT QoS 0/1/2 分别是什么？
参考答案： QoS 0：最多一次；QoS 1：至少一次，可能重复；QoS 2：恰好一次。该语义来自 MQTT 规范。
解析： 测试 QoS 1 时必须主动考虑重复投递及业务幂等；QoS 2 的协议交互和开销更高。
易错点： 不要把 QoS 1 说成“不会丢、不会重”。
追问： QoS 1 重复了怎么办？
保证“不容易丢”，不保证“不重复”；重复问题靠业务幂等解决
Q51. MQTT retain 是什么？
参考答案： 保留消息使 Broker 为某个 Topic 保存最后的 retained message，新订阅者订阅后可以获得这条保留消息。具体清除行为需结合协议与消息设置。
解析： 常用于状态类信息的“最后已知状态”快速同步。
易错点： 不要把 retain 说成“持久保存所有历史消息”。
追问： 订阅设备状态时突然收到旧状态，可能是什么？
检查保留消息Retain = Broker 帮你保存“最后一条”
新订阅者 = 可能一订阅就收到这条旧消息
Q52. MQTT Client ID 为什么重要？
参考答案： Client ID 用于标识 MQTT 客户端会话。在很多 Broker 中，同一个 Client ID 的新连接可能导致旧连接被断开，因此并发测试必须设计唯一性。
解析： 测试开发框架可以加入 worker/device 等维度生成唯一 Client ID。
易错点： 不同 Broker 对会话处理细节依版本与配置而异。
追问： pytest-xdist 同时连 4 个客户端时怎么避免冲突？
mqttclientid不能唯一，创建四个
Q53. MQTT Keep Alive 是什么？
参考答案： Keep Alive 用于约束客户端与 Broker 之间维持连接活跃的时间窗口，协议通过控制报文等机制检测连接状态。
解析： 测试要验证网络静默、心跳、超时、重连，以及 Broker 对异常断线的判断。
易错点： Keep Alive 不是“每隔 N 秒必须发送业务消息”。
追问： 设备断网后多久 App 应该变成离线？
Keep Alive ≠ App 离线时间。
Keep Alive 是“Broker 多久确认设备还活着”，App 离线时间是“整个系统最终多久把状态展示成离线”。
Q54. MQTT 消息收不到怎么排查？
参考答案： 按链路排查：网络/TLS → Broker → 认证 → Client ID → Subscribe 是否成功 → Topic 是否精确 → QoS → Publisher 是否发送 → Broker 日志 → Subscriber 回调。
解析： 最好每层都能拿到证据，避免只在 App 层猜。
易错点： 只说“检查 Topic”属于不完整回答。
追问： 订阅返回拒绝码怎么办？
128 = 0x80 = SUBSCRIBE 被拒绝。第一优先级查 ACL / Topic 订阅权限。
Q55. MQTT publish 返回成功，是否代表设备一定收到？
参考答案： 不一定。客户端侧调用成功与 Broker 接收、Broker 分发、目标设备处理是多个阶段。还要结合 QoS、连接状态和 ACK/业务确认判断。
解析： 测试可以建立端到端证据链：发送时间、Broker 接收、设备收到、设备处理、Up 回包。
易错点： 不要把本地 API 调用成功等同于业务成功。
追问： 如何定义“消息送达率”？
在规定时间内，接收端正确匹配到的唯一消息数 ÷ 有效发送消息总数 × 100%。
Q56. 如何处理 MQTT 重复消息？
参考答案： 协议层允许的重复要按 QoS 语义理解；业务层需要用 message_id/request_id/业务主键等做去重或幂等处理。
解析： 自动化断言不能简单“同一消息出现两次就失败”，先判断协议和业务契约。
易错点： 这是 IoT 测试里很容易被追问的点。
追问： 设备控制命令重复执行会造成什么风险？
设备移动精度问题，设备状态异常
Q57. MQTT 自动化为什么需要“消息匹配”而不是只 recv 一次？
参考答案： 因为 Broker 和设备可能同时产生多种异步消息，一次 recv 只代表收到“某一条消息”，不代表它就是当前请求对应的目标响应。
解析： 可以基于 request_id、device_id、method、type、状态字段等匹配，并设置 timeout。
易错点： 用固定 sleep 解决异步问题通常不可靠。
追问： 怎样避免消息串台？
Topic 隔离 + Client ID 唯一 + Request ID 唯一 + 精确匹配 + 并发独立队列。
八、MySQL 与数据库测试
Q58. INNER JOIN 和 LEFT JOIN 区别？
参考答案： INNER JOIN 只保留两表都能匹配的记录；LEFT JOIN 保留左表全部记录，右表匹配不到则为 NULL。
解析： 数据库校验时要注意 JOIN 条件是否把结果无意中过滤掉。
易错点： 不要用“左边优先”这种模糊描述。
追问： LEFT JOIN 后又在 WHERE 里过滤右表字段会发生什么？
LEFT JOIN + WHERE 过滤右表字段，通常会让 LEFT JOIN 失去“保留左表未匹配数据”的效果，逻辑上接近 INNER JOIN。
Q59. WHERE 和 HAVING 区别？
参考答案： WHERE 通常在分组前过滤行；HAVING 用于分组/聚合后的条件过滤。
解析： 例如统计每个设备打印次数并筛选 > 10 时使用 GROUP BY + HAVING。
易错点： 不要说 HAVING 只是“第二个 WHERE”。
追问： 没有 GROUP BY 能不能使用 HAVING？
没有 GROUP BY 也可以使用 HAVING，此时整个结果集会被当成一个组，HAVING 用来过滤这个组。
Q60. 什么是索引？为什么不是越多越好？
参考答案： 索引用额外数据结构帮助快速定位记录，能降低查询成本；但索引会占空间，并增加 INSERT/UPDATE/DELETE 维护成本，过多索引还会增加优化器选择成本。
解析： MySQL 官方文档说明常见索引采用 B-tree，并支持多列索引的左前缀利用。
易错点： 不要说“加索引查询就一定更快”。
追问： 为什么小表可能不用索引？
全表扫描成本底
Q61. 联合索引 `(a,b,c)` 的最左前缀是什么？
参考答案： 可利用的左前缀通常包括 `(a)`、`(a,b)`、`(a,b,c)`；只过滤 b 或 c 不能按传统左前缀方式高效利用该联合索引。具体执行计划仍应通过 EXPLAIN 验证。
解析： 同时考虑范围条件、排序、覆盖索引等因素。
易错点： 不要把“不能高效利用左前缀”说成“绝对完全不用索引”。
追问： `where a=1 and c=3` 怎么分析？
能用 a，但 b 断了，所以 c 不能按最左前缀继续使用。
Q62. EXPLAIN 看什么？
参考答案： 重点看访问类型、可能使用的索引、实际选择的索引、估算行数、过滤比例、Extra 等执行计划信息。告诉你这条 SQL 准备怎么执行，以及数据库为什么这么执行
解析： 最终目的是理解优化器准备怎么执行，而不是只看某一个字段。
易错点： 不要机械地把 `ALL` 等同于绝对错误；要结合数据量与查询成本。
查慢 SQL：先看 type，再看 key，再看 key_len 和 rows，最后重点看 Extra
Q63. 事务 ACID 是什么？
参考答案： Atomicity 原子性、Consistency 一致性、Isolation 隔离性、Durability 持久性。
解析： 测试支付、订单、设备任务等跨表状态时，需要验证异常中断、回滚和并发。
易错点： 不要把 Consistency 解释成“所有用户任何时候看到完全相同数据”。
追问： 扣款成功、订单创建失败如何测试？
ACID：原子、一致、隔离、持久；扣款成功但订单失败，本质是分布式事务/最终一致性问题，测试重点是“不能钱扣了订单没了”，同时验证重试、补偿、退款和幂等。
Q64. MySQL 常见隔离级别？
参考答案： READ UNCOMMITTED、READ COMMITTED、REPEATABLE READ、SERIALIZABLE。InnoDB 默认隔离级别为 REPEATABLE READ。
解析： 隔离级别解决的是并发事务之间可见性与并发控制的权衡。
易错点： 不同隔离级别的具体幻读/锁行为需要结合 InnoDB 机制回答。
追问： 脏读、不可重复读、幻读怎么区分？
脏读：读到了别人“没提交”的数据。
不可重复读：同一条数据，前后两次读取结果不一样。
幻读：同一个范围，前后两次查询，行数发生了变化。
Q65. 慢 SQL 如何排查？
参考答案： 先确认慢在哪里，再看 SQL、执行计划、索引、数据量、锁等待、磁盘/CPU、网络和应用连接池。使用 EXPLAIN/EXPLAIN ANALYZE（视版本与环境）等工具验证，而不是凭感觉改索引。
解析： 性能优化必须有前后数据对比。
易错点： 不要一看到慢 SQL 就“加索引”。
追问： 加索引后查询仍慢怎么办？
索引慢不一定是索引的问题，先 EXPLAIN，看“有没有用、用了多少、扫了多少、回表多少、额外做了什么”。
九、接口测试与接口自动化
Q66. 接口测试主要验证什么？
参考答案： 请求方法、URL、Headers、鉴权、参数、状态码、响应结构、字段值、业务规则、错误码、幂等、超时、重试和性能等。
解析： 可以分“协议层 + 业务层 + 异常层 + 安全层”组织。
易错点： HTTP 200 不代表业务一定成功。
追问： 哪些字段属于强断言，哪些适合弱断言？
强断言验证“业务必须正确”的字段；弱断言验证“存在、格式、范围、结构正确”的字段
Q67. 为什么接口返回 200 也可能是失败？
参考答案： HTTP 状态码描述传输层/协议层结果，业务是否成功还要根据响应 body、错误码、状态字段和业务副作用判断。
解析： 测试时可以同时断言 HTTP status + business code + 核心字段 + 数据库/消息副作用。
易错点： 不要把“200=成功”当作万能结论。
追问： 接口业务失败应该返回 4xx 还是 200？
Q68. 接口关联怎么做？
参考答案： 从前置接口响应中提取 token、id、request_id 等动态数据，放到测试上下文或变量容器中，再传给后续接口。
解析： 同时要考虑作用域、清理、并发隔离和失效时间。
易错点： 不要把动态值写死到测试数据里。
追问： 并发跑 20 个用户时 token 如何隔离？
Q69. 什么是 Mock？为什么需要 Mock？
参考答案： Mock 是用可控替身模拟依赖服务，便于验证本服务在不同外部响应、超时和异常条件下的行为。
解析： 尤其适合第三方支付、设备云、消息服务、极端错误码等不稳定或不可控依赖。
易错点： Mock 的目标不是“永远不连真实环境”，而是控制测试边界。
追问： Mock 太多会带来什么风险？
Q70. 如何测试文件上传接口？
参考答案： 验证文件类型、大小、空文件、超限、文件名特殊字符、重复上传、并发上传、断点/超时、恶意内容校验以及上传后存储与业务记录一致性。
解析： 接口层和存储层要同时验证。
易错点： 不要只验证 HTTP 200。
追问： 文件上传成功但数据库记录没落怎么办？
Q71. 如何测试分页接口？
参考答案： 验证 page/page_size 边界、最大 page_size、空数据、最后一页、数据刚好整除和不整除、排序稳定性、重复/漏数据以及数据并发变化下的一致性。
解析： 分页测试容易暴露排序字段不稳定问题。
易错点： 不要只测第一页。
追问： 1000 条数据分页后第 2 页重复了 1 条怎么办？
十、性能测试与 JMeter
Q72. 性能测试主要关注哪些指标？
参考答案： 响应时间、吞吐量、TPS/QPS、并发、错误率、资源利用率（CPU、内存、磁盘、网络）、连接池、GC 等。
解析： 指标必须结合业务 SLA 和负载模型解释。
易错点： 不要只报一个平均响应时间。
追问： P95 和平均值为什么要一起看？
Q73. TPS、QPS、并发有什么区别？
参考答案： 并发表示同时处于活动状态的请求/用户量；QPS 表示每秒请求/查询量；TPS 表示每秒事务数。三者没有简单一一等价关系。
解析： 一个业务事务可能包含多个接口请求。
易错点： 不要说“1000 并发就是 1000 TPS”。
追问： 1000 并发时 TPS 为什么可能只有 50？
Q74. P50/P95/P99 是什么？
参考答案： 分别表示 50%、95%、99% 的请求响应时间低于该值，可用于观察延迟分布与尾延迟。
解析： P99 很高而平均值低，说明少量慢请求可能严重影响体验。
易错点： 不要把 P99 当成“最慢请求”。
追问： P99=5s 如何定位？
Q75. 什么是压力测试？
参考答案： 在逐步增加负载或目标负载下，评估系统性能、容量、稳定性和瓶颈。
解析： 压力测试必须有负载模型、验收指标、监控和结果分析。
易错点： 不是简单把线程数调大。
追问： 什么时候做负载测试、压力测试、稳定性测试？
Q76. JMeter 基本结构？
参考答案： 常见是 Test Plan → Thread Group → Sampler → Assertions → Listeners/Reports，并结合 HTTP Request、Timer、Extractor、CSV Data Set Config 等。
解析： 真实项目还需要分散式压测、后端监控和结果汇总。
易错点： 不要只背界面组件名称。
追问： 线程数、Ramp-Up、循环次数怎么设计？
Q77. 10000 用户同时登录怎么做性能测试？
参考答案： 先定义目标并发与流量模型，再设计 Ramp-Up，准备用户数据，避免缓存/账户复用导致结果失真，同时监控网关、应用、数据库、缓存、CPU、内存、连接池和网络。
解析： 登录通常是高峰入口，必须考虑验证码、限流、Token、数据库读写和热点数据。
易错点： 直接开 10000 线程不是完整性能方案。
追问： 怎么判断瓶颈在数据库还是应用？
Q78. 为什么固定 sleep 不适合性能和自动化测试？
参考答案： sleep 只按时间等待，不关心真实状态，容易等待不足或浪费时间。自动化应优先基于状态/事件/条件等待；性能测试则应按真实吞吐模型控制节奏。
解析： 设备测试中可以等待“状态变为 printing”，而不是固定等待 10 秒。
易错点： 不要完全否定 sleep，它在明确需要节流时仍有用途。
追问： 什么场景 sleep 是合理的？
十一、Pytest 与自动化测试框架
Q79. 为什么选择 Pytest？
参考答案： 语法简洁、Fixture 灵活、参数化方便、断言友好、插件生态丰富，适合构建接口、消息、设备和 UI 的自动化测试体系。
解析： 真正重要的是你如何利用它做资源管理、数据驱动、并发、报告和扩展。
易错点： 不要只说“Pytest 比 unittest 简单”。
追问： 你项目里 Pytest 负责什么？
Q80. Fixture 的作用是什么？
参考答案： 用于提供和管理测试所需资源与前后置逻辑，例如数据库连接、MQTT/WebSocket 客户端、登录状态和临时目录。
解析： Fixture 的核心价值是生命周期管理与复用。
易错点： 不要把 fixture 当成“公共函数”。
追问： 为什么数据库/MQTT 资源适合 fixture？
Q81. Fixture scope 有哪些？
参考答案： 常见有 function、class、module、package、session。scope 越大，复用越多，但资源共享和状态污染风险通常也越高。
解析： MQTT 客户端是否 session 级必须根据并发和隔离要求决定。
易错点： scope 不是越大越好。
追问： 为什么 session scope 可能导致消息串扰？
Q82. conftest.py 是干什么的？
参考答案： 用于在测试目录层级共享 fixture、hook 等 pytest 配置而无需在每个测试文件重复导入。
解析： pytest 会按测试目录结构寻找可用 fixture。
易错点： 不要说“项目里任意位置放一个 conftest 都全局生效”。
追问： 如何组织多个 conftest？
Q83. 参数化和数据驱动有什么区别？
参考答案： 参数化是测试框架层面让同一测试函数运行多组参数；数据驱动是更广义的思想，即把测试数据与测试逻辑分离，可以来自 JSON、YAML、CSV、数据库等。
解析： 两者可以结合：从 JSON 读取数据，再通过 pytest.mark.parametrize 执行。
易错点： 不要把两者当成完全同义。
追问： 什么时候动态生成参数？
Q84. pytest-xdist 并行为什么可能导致测试失败？
参考答案： 并行会暴露共享资源竞争，例如设备、MQTT Client ID、Topic、数据库数据、端口、文件、全局变量等。
解析： 解决方案是资源隔离、唯一标识、锁、数据隔离和合理的 fixture scope。
易错点： 并行失败不一定是 pytest 有问题。
追问： 4 worker 同时控制一台 P300 怎么办？
Q85. 自动化测试偶发失败怎么处理？
参考答案： 先区分真实随机缺陷与测试本身 Flaky。通过日志、重现频率、时间线、环境和消息顺序定位，再用条件等待、同步机制、资源隔离、重试策略修复根因。
解析： 重试只能降低偶发失败对流水线的影响，不能掩盖根因。
易错点： 不要第一反应就是把 reruns 从 2 调到 10。
追问： 什么样的重试是危险的？
Q86. 如何设计一个测试开发框架？
参考答案： 可按 TestCase → Business → Service/Communication → Driver/Library 分层，并配套 config、data、utils、logging、assert、report。
解析： 核心是职责分离、资源生命周期、数据与代码解耦、统一日志和可观测性。
易错点： 避免把所有功能塞进 BaseTest 或一个 Utils 类。
追问： 你的 MQTT 框架哪一层负责消息匹配？
Q87. Allure 的价值是什么？
参考答案： 用于把测试结果、步骤、附件、日志、截图等结构化展示，提升失败分析和质量追踪效率。
解析： 自动化框架应该在失败时附加关键请求、响应、设备日志或截图。
易错点： 报告漂亮不代表测试质量高。
追问： 你会把什么附加到失败用例？
十二、Selenium / Appium 与 UI 自动化
Q88. Selenium 和 Appium 区别？
参考答案： Selenium 主要用于 Web UI 自动化；Appium 用于移动端等自动化场景，并采用 WebDriver 体系与移动平台驱动进行交互。
解析： 测试设计思想相似，都要处理元素定位、等待、页面对象和稳定性。
易错点： 不要只回答“一个 Web 一个 App”。
追问： 你为什么不把所有定位都写 XPath？
Q89. 隐式等待、显式等待、Fluent Wait 有什么区别？
参考答案： 隐式等待是全局查找元素时的等待策略；显式等待针对具体条件等待；Fluent Wait 是更细粒度的等待配置，可指定轮询频率和忽略的异常。
解析： 稳定 UI 自动化通常更推荐明确的条件等待，而不是大量 sleep。
易错点： 不同工具版本和实现可能有细节差异。
追问： 为什么混用隐式/显式等待可能让时序更难理解？
Q90. Page Object Model 是什么？
参考答案： 将页面元素定位和页面行为封装到 Page Object 中，测试用例通过业务动作调用页面对象，从而降低 UI 结构变化对测试用例的影响。
解析： 进一步可以把组件对象、业务流和断言分离。
易错点： POM 不是把所有逻辑都塞到 Page 类里。
追问： 复杂 App 页面怎么分层？
Q91. 元素偶现找不到怎么排查？
参考答案： 检查页面状态、元素生命周期、定位稳定性、动画/异步加载、上下文、iframe/window、权限弹窗、网络和设备性能；再用截图、page source、日志验证。
解析： 最后才能决定是否需要重试。
易错点： “加 sleep”通常只是缓解，不是定位。
追问： StaleElementReference 怎么处理？
十三、Linux / Git / 日志排查
Q92. Linux 常用排障命令有哪些？
参考答案： 进程/资源：ps、top、free、df、du；网络：ss、lsof、ping、curl；日志：tail、grep、less；文件：find、ls；进程终止：kill。
解析： 面试时最好给出实际场景，而不是只背命令清单。
易错点： 命令参数应根据系统版本确认。
追问： 8080 端口被谁占用？
Q93. CPU 100% 怎么排查？
参考答案： 先确定是哪个进程，再细化到线程/调用栈，结合日志、监控和业务操作判断；同时看是否伴随内存、GC、磁盘或网络异常。
解析： top/ps/pidstat 等工具可以辅助定位，生产系统还应结合 APM。
易错点： 不要一看到 CPU 高就直接 kill 进程。
追问： 单个线程 CPU 100% 怎么办？
Q94. 怎么查端口是否被占用？
参考答案： 可以使用 `ss -lntp` 或 `lsof -i :端口` 查看监听和进程信息。
解析： 如果容器环境，还要继续查容器/宿主机映射。
易错点： 不要把 ping 当成端口检测工具。
追问： 端口监听正常但 curl 失败怎么办？
Q95. git merge 和 rebase 区别？
参考答案： merge 保留分支合并历史，生成合并节点；rebase 重新整理提交基线，使历史更线性，但会改写提交哈希。
解析： 公共分支上的历史改写需要谨慎，团队要有约定。
易错点： 不要把 rebase 说成“更安全”。
追问： 已经 push 的 commit 能不能 rebase？
Q96. git reset 和 git revert？
参考答案： reset 改变当前分支/HEAD 与索引/工作区状态，适合本地或允许改写历史的场景；revert 通过创建反向提交来撤销已有提交，更适合共享历史。
解析： 回答时要区分 `--soft/--mixed/--hard` 的影响。
易错点： 不要随意建议对公共分支 reset --hard + force push。
追问： 误删提交怎么恢复？
Q97. 日志排查一个线上 Bug 应该看什么？
参考答案： 时间窗口、用户/设备 ID、Trace ID/Request ID、接口、Topic、线程/进程、错误码、堆栈以及上下游日志。
解析： 最重要的是建立事件时间线，而不是盯着一个报错。
易错点： 没有上下文的“Exception”通常信息价值很低。
追问： 如何串联 MQTT → 服务端 → App 的一条链路？
十四、并发、稳定性、弱网与分布式思维
Q98. 弱网测试要测什么？
参考答案： 高延迟、丢包、抖动、限速、断网、网络切换、恢复、后台/前台切换、重连和状态一致性。
解析： IoT/App 场景尤其关注控制命令重复、状态滞后和 UI 与设备真实状态不一致。
易错点： 不要只测“断网后弹 Toast”。
追问： 网络恢复后为什么可能出现旧消息覆盖新消息？
Q99. 如何测试断线重连？
参考答案： 主动断开网络/连接，观察检测时间、重连策略、重连次数、退避、重新鉴权、重新订阅、状态恢复以及消息丢失/重复。
解析： 重连成功不等于业务恢复；还要验证订阅与状态同步。
易错点： 不要只检查“socket.connected=True”。
追问： 重连后为什么会收不到订阅消息？
Q100. 如何测试并发修改同一资源？
参考答案： 设计两个或多个客户端同时修改同一设备/订单/任务，验证最终状态、冲突处理、锁/版本控制、幂等和数据一致性。
解析： 需要定义“谁赢”和“冲突如何返回”，否则无法判断结果。
易错点： 不要只看接口返回 200。
追问： 两个请求同时把设备从 idle 改成 printing 怎么处理？
Q101. 分布式系统中为什么需要幂等、锁和一致性控制？
参考答案： 因为网络重试、消息重复、并发请求和多节点处理都可能让同一业务操作执行多次或产生竞态，需要通过幂等键、数据库约束、分布式锁、版本号/乐观锁、状态机等手段控制结果。
解析： 测试要验证异常重试与并发时是否仍保持业务正确性。
易错点： 不要把分布式锁当作所有并发问题的万能解。
追问： 设备控制为什么适合做状态机？
Q102. 状态机测试应该测什么？
参考答案： 合法状态迁移、非法迁移、重复迁移、并发迁移、异常中断、恢复、超时和最终一致性。
解析： 例如打印机 idle → heating → printing → paused → printing → finished。
易错点： 只验证最终状态而不验证过程，容易漏掉大量时序 Bug。
追问： 暂停后马上点继续会发生什么？
十五、测试实战与项目深挖
Q103. 你的 MQTT 自动化平台整体架构怎么讲？
参考答案： 可以讲成 TestCase → Business → MQTT Service → Paho MQTT，并配 config/data/logger/assert/report；测试数据使用 JSON/配置分离，消息接收通过目标字段匹配并带超时。
解析： 面试官真正关心的是你做了哪些工程化工作，而不是“调用了 paho-mqtt”。
易错点： 不要只讲工具名称，要讲解决了什么问题。
追问： 为什么消息匹配应该在 Service 层？
Q104. expected 和 actual 怎么做递归匹配？
参考答案： 字典就递归遍历 expected 的 key；若 key 不存在则失败；如果 value 是 dict 则继续递归；否则比较值。actual 可以有额外字段。
解析： 这适合验证设备上报 JSON 的部分关键字段，同时避免因服务端新增字段导致旧用例全部失败。
易错点： 要处理 list、None、类型不一致、路径定位等边界。
追问： 数组怎么比较才能既严格又灵活？
Q105. 设备显示在线但实际离线，怎么排查？
参考答案： 按链路：设备网络 → MQTT Broker → 云端服务 → 状态缓存/数据库 → WebSocket/MQTT 推送 → App 状态管理 → UI。每层采集时间戳和证据，建立事件时间线。
解析： 优秀回答会区分“真实设备状态”和“页面显示状态”。
易错点： 不要一上来就说“App 缓存没刷新”。
追问： 数据库已经 offline，但 App 仍显示 online 怎么办？
Q106. MQTT 已收到，App 页面没更新，怎么定位？
参考答案： 记录 T1 设备状态变化、T2 服务端收到、T3 推送到 App、T4 App 收到、T5 状态管理更新、T6 UI 完成渲染；按时间差定位是设备、服务端、通信、客户端处理还是渲染问题。
解析： 这是端到端实时性测试的核心方法。
易错点： 只测“消息有没有收到”无法定位 UI 延迟。
追问： 如何自动化统计 P95 页面更新时间？
Q107. 自动化测试偶发失败，你会不会直接加 rerun？
参考答案： 可以使用 rerun 降低偶发环境问题对流水线的干扰，但必须先分析 Flaky 根因。真正解决应靠条件等待、时序同步、资源隔离、重试边界和环境稳定性。
解析： rerun 是“缓冲”，不是“修复”。
易错点： 无限重试会掩盖真实缺陷。
追问： 哪些情况绝对不应该自动重试？
Q108. 4 个 pytest worker 同时控制设备，怎么设计？
参考答案： 优先做设备资源隔离；每个 worker 使用唯一 client ID、唯一测试数据和必要的 Topic/任务标识；对不可共享设备使用资源锁或调度机制；避免全局单例连接造成串台。
解析： 并发自动化的核心是“资源所有权”。
易错点： 如果业务本身就是验证并发控制，也不能简单加锁把并发屏蔽掉。
追问： 测试“两个用户同时控制一台机器”时怎么办？
Q109. 如果重新设计你的 MQTT 自动化框架，你会怎么优化？
参考答案： 将连接管理、发布、订阅、消息缓存/匹配、超时、重连、日志从业务用例中抽离；用统一消息模型；将设备/Topic/环境配置化；增加并发隔离、统计、失败上下文和可观测性。
解析： 高级回答可以进一步提出事件总线、异步接收线程/任务、消息队列缓存、按 request_id 建索引等方案。
易错点： 不要为了“架构复杂”而过度设计。
追问： 消息监听线程如何安全退出？
Q110. 你做过 MQTT 自动化，如何证明这不是“把手工步骤写成 Python”？
参考答案： 强调工程化能力：数据驱动、分层封装、消息匹配、异步等待、超时、异常处理、Fixture 生命周期、并发隔离、报告和可观测性。
解析： 最好补充一个真实难题和解决方案，形成“问题 → 原因 → 方案 → 结果”的闭环。
易错点： 不要只说“代码执行得比人快”。
追问： 自动化本身最大的缺点是什么？
Q111. 自动化测试通过率 99%，能否证明质量很好？
参考答案： 不能。还要看覆盖范围、风险、漏测场景、测试有效性、线上缺陷、Flaky 比例以及关键链路是否真正覆盖。
解析： 高通过率如果来自“只测正常主流程”，反而没有价值。
易错点： 不要用通过率代替质量。
追问： 你更看重通过率还是缺陷漏出率？
Q112. 接口正确和业务正确有什么区别？
参考答案： 接口返回正确字段只是接口层正确；完整业务还可能要求数据库状态、消息、设备动作、缓存和 UI 最终一致。
解析： 例如 WebSocket 收到正确消息但 UI 不更新，通信层可以通过，业务链路仍失败。
易错点： 这体现了分层断言思想。
追问： 在哪一层判定 Bug 最合适？
十六、代码题与代码 Review
Q113. 写一个列表去重，同时保持原顺序。
参考答案： 可使用一个 set 记录已经出现的元素，再遍历原列表输出第一次出现的元素。示例：`seen=set(); result=[]; for x in data: if x not in seen: seen.add(x); result.append(x)`。
解析： 如果元素不可哈希，就不能直接用 set，应考虑线性查找或转换策略。
易错点： 不要只写 `list(set(data))`，它不能保证题目要求的原顺序。
追问： 时间复杂度是多少？
Q114. 统计字符串中每个字符出现次数。
参考答案： 可以用 dict：遍历字符，`counter[ch]=counter.get(ch,0)+1`；也可以使用 collections.Counter。
解析： 面试官通常更想看你是否能先写出清晰正确的基础版本。
易错点： 要考虑空字符串和 Unicode 字符等。
追问： 如何按次数排序？
Q115. 找列表第二大的数。
参考答案： 先明确是否允许重复。若要求“第二大的不同值”，可维护最大值和次大值，或先去重再排序；工程上要处理少于两个不同值的异常情况。
解析： 这是典型的“先问清需求，再写代码”。
易错点： 直接 `sorted(set(data))[-2]` 虽短，但要处理长度和空列表。
追问： 能否做到 O(n)？
Q116. 代码 Review：`time.sleep(10); response=mqtt.recv(); assert response["data"]["status"]=="success"` 有什么问题？
参考答案： 固定 sleep 不可靠；recv 不保证拿到目标消息；没有显式超时和异常分类；response 可能为空/非目标；断言上下文不足；资源关闭不明确。
解析： 改进方向是条件等待 + 消息匹配 + 超时 + 日志 + finally/fixture teardown。
易错点： 这是典型测试开发思维题。
追问： 如果消息先到再进入等待怎么办？
Q117. 如何实现等待某条 MQTT/WebSocket 消息？
参考答案： 建立带 deadline 的循环，持续接收，解析后按 request_id/device_id/method/type 等关键字段匹配；匹配到目标即返回，超过 deadline 抛出带上下文的 TimeoutError。
解析： 进一步可以建立消息缓存，防止目标消息比等待线程更早到达。
易错点： 不要只依赖 sleep 或无限 while。
追问： 并发等待多个 request_id 怎么设计？
Q118. 如何写一个可靠的重试？
参考答案： 重试应限定次数、可重试异常和退避策略，并记录每次尝试原因。只对暂态故障重试，如连接瞬断、特定超时；业务逻辑错误、参数错误通常不应该重试。
解析： 分布式系统中可使用指数退避 + jitter，避免大量客户端同时重试形成惊群。
易错点： 无限重试会掩盖失败。
追问： 为什么需要 jitter？
十七、面试官终极追问与回答策略
Q119. “你做过 MQTT 自动化吗？”怎么回答才不像背八股？
参考答案： 先讲业务背景，再讲链路，再讲你负责的工程问题，最后给一个难题案例。推荐结构：背景 → 架构 → 核心实现 → 难点 → 解决方案 → 结果。
解析： 例如：FDM 设备控制 → Python/Pytest → MQTT 连接与 JSON 数据驱动 → 异步消息与状态流转 → 消息匹配/超时/隔离 → 提升回归效率与定位效率。
易错点： 不要一上来背工具清单。
追问： 最难的 Bug 是什么？
Q120. 面试官说“你这个项目是不是很简单？”怎么办？
参考答案： 不要防御式争辩。直接用一个具体技术难题证明深度，例如异步消息乱序、重复、超时、并发设备冲突、断线重连、端到端时延定位。
解析： 用真实细节展示复杂度比描述“项目很大”更有效。
易错点： 不要夸大没有做过的能力。
追问： 你亲自实现了什么？
Q121. “为什么不用 Postman 全部解决？”怎么回答？
参考答案： Postman 适合快速接口验证；当场景涉及大量数据驱动、复杂状态流、异步 MQTT/WebSocket、设备联动、并发和 CI 时，Python + Pytest 更适合做工程化自动化。
解析： 不是说 Postman 不好，而是工具要服从测试场景。
易错点： 不要贬低 Postman。
追问： 哪些测试你仍会用 Postman？
Q122. “你最擅长什么？”怎么回答更合理？
参考答案： 建议定位为“Python + Pytest 的自动化测试开发，尤其擅长 IoT/MQTT/设备控制类场景”，再补充接口、App 和性能经验。
解析： 要形成一个清晰的技术标签，而不是说“什么都会”。
易错点： 避免过度包装成后端开发或架构师。
追问： 除了 MQTT，你还能做什么？
Q123. “你不会的技术怎么办？”
参考答案： 先说明没有直接生产经验，再说明相邻能力、学习路径和验证方法，例如先看协议/官方文档、做最小 Demo、接入现有测试框架、补充场景测试。
解析： 诚实比硬背更容易获得信任。
易错点： 不要说“我都会学”但没有方法。
追问： 给你 Kafka，三天能做到什么？
Q124. “测试发现 P0，但项目明天上线怎么办？”
参考答案： 先基于影响、概率、范围给出风险判断，提供复现证据和影响面；如果确实无法修复，则推动产品/研发/负责人做有记录的风险接受或延期决策，并提出临时缓解方案。
解析： 测试不是“一票否决者”，但应确保风险透明。
易错点： 不要说“领导让上就上”或“测试说不上就不上”。
追问： 什么情况你一定坚持阻断上线？
Q125. “如果没有需求文档，给你一个陌生系统怎么测？”
参考答案： 先理解业务目标、用户角色和关键链路，再通过 UI/API/日志/数据库/代码/历史缺陷建立系统模型，识别高风险区域，先做探索性测试和冒烟，再沉淀用例。
解析： 这体现测试分析能力，而不是等待产品把所有需求写完。
易错点： 不要回答“先让产品补文档”。
追问： 如何防止探索性测试变成漫无目的乱点？


面试速记：一题四层回答法
第一层：结论：先用 1~2 句话回答是什么/为什么。
第二层：原理：解释为什么，说明底层机制或关键约束。
第三层：实战：结合你做过的 MQTT、设备、App、Pytest 场景举例。
第四层：边界：主动说异常、并发、重试、超时、资源隔离和可观测性。
高频“不要这么答”
“MQTT QoS 1 就不会丢消息。” → 不准确；QoS 1 是至少一次，可能重复，最终业务语义还要看应用。
“WebSocket 完全不经过 HTTP。” → 不准确；典型建立阶段通过 HTTP Upgrade 握手。
“HTTP 200 就代表接口成功。” → 不准确；还要验证业务响应和副作用。
“自动化偶尔失败就加 sleep。” → 往往只能掩盖时序问题，应优先使用条件等待、事件同步和超时。
“Pytest 开 4 个 worker 就一定更快。” → 不一定；设备、数据库、Broker 等共享资源可能成为瓶颈。
“索引越多越好。” → 不准确；索引有空间和写放大成本，还可能增加维护与优化器负担。
“测试通过率高就是质量高。” → 不足；还需看覆盖、漏测、风险、线上缺陷和测试有效性。
官方资料与进一步复习
Pytest 官方文档：https://docs.pytest.org/en/stable/
MQTT Version 5.0 / OASIS：https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html
RFC 6455 WebSocket Protocol：https://www.rfc-editor.org/rfc/rfc6455.html
MySQL 8.4 Reference Manual：https://dev.mysql.com/doc/refman/8.4/en/
Python 官方文档：https://docs.python.org/3/
