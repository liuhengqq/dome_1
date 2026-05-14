import pytest
import allure
from operation.user import create_order
from testcases.conftest import api_data
from common.logger import logger
import json


@allure.step("步骤1==>>创建订单")
def step_1():
    logger.info("步骤1==>>创建订单")

@allure.step("步骤2 ==>> 创建重复的订单")
def step_2():
    logger.info("步骤2 ==>> 创建重复的订单")

@allure.title("创建订单")
@allure.feature("订单模块")
@allure.severity(allure.severity_level.NORMAL)
class Test_create_order:
    @allure.story("订单功能")
    @allure.description("订单幂等性测试")
    @pytest.mark.parametrize("idem_key, product_name, amount, except_msg, except_code", api_data["test_create_order"])
    def test_create_order(self, idem_key, product_name, amount, except_msg, except_code):
        logger.info("*************** 开始执行用例 ***************")
        step_1()
        result = create_order(product_name,
        amount,
        idem_key)
        logger.info(result.response.json())
        assert result.msg == except_msg
        assert result.response.json()["code"] == except_code
        allure.attach(
            result.msg,
            name="返回结果",
            attachment_type=allure.attachment_type.TEXT
        )