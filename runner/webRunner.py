from selenium.webdriver import ChromeOptions, Chrome

from runner.webdriveroption import WebdriverOption


def init_webdriver(url):
    """初始化webdriver测试驱动"""
    # 初始化测试驱动
    # chrome功能设置
    option = ChromeOptions()
    # 处理https显示通知弹窗
    prefs = {
        'profile.default_content_setting_values': {
            'notifications': 2
        }
    }
    option.add_experimental_option('prefs', prefs)
    # 设置无头模式
    option.add_argument('--no-sandbox')
    option.add_argument('--headless')  # 无头模式，浏览器不提供可视化页面
    option.add_argument('--disable-dev-shm-usage')
    option.add_argument('--window-size=1366,768')
    # 解决https私密连接问题
    option.add_argument('--ignore-certificate-errors')
    option.add_experimental_option("excludeSwitches", ["ignore-certificate-errors", "enable-logging"])
    # 实例化驱动
    op = WebdriverOption(Chrome(options=option))
    op.maximize_window()
    op.open_website(url)
    return op


async def web_case_runner(case):
    """执行测试用例"""
    steps = []
    actions = []
    for content in case.content.split(',')[:-1]:
        content_list = content.split('-')
        if int(content_list[0]) == 1:
            steps.append({'name': content_list[1], 'expect': content_list[2]})
        else:
            for step in crud.Suite(db).get_suite_by_name(content_list[1]).step.split(',')[:-1]:
                steps.append({'name': step, 'expect': content_list[2]})
    for step in steps:
        step_data = crud.Step(db).get_step_by_name(step['name'])
        actions.append(
            {'option': step_data.option, 'element': crud.Element(db).get_element_by_name(step_data.element).element,
             'value': step_data.value, 'expect': step['expect']})
    await manager.send_json_message({'timestamp': now(), 'casename': case.name}, ws)
    try:
        op = init_webdriver(url)
        # 执行测试步骤集合中的步骤
        for index, action in enumerate(actions):
            await manager.send_json_message({'timestamp': now(), 'stepname': steps[index]['name']}, ws)
            match action['option']:
                case '点击':
                    op.wait_element_visibility(action['element'])
                    sleep(1)
                    op.click(action['element'])
                    sleep(1)
                case '输入':
                    op.wait_element_visibility(action['element'])
                    sleep(1)
                    op.input_text(action['element'], action['value'])
                    sleep(1)
            image = op.driver.get_screenshot_as_base64()
            await manager.send_json_message({'images': image}, ws)
        else:
            await manager.send_json_message({'casestatus': 0}, ws)
    except Exception:
        await manager.send_json_message({'casestatus': 1}, ws)
    finally:
        # 关闭测试驱动
        op.driver.quit()
        await manager.disconnect(ws)
