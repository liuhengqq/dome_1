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
