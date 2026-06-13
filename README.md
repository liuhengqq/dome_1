
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
