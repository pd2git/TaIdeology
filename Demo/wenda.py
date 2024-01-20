# Explanation: Only list the modified parts, starting with # [AAModified Start] and ending with # [AAModified End].
# 说明：仅列出修改的部分，以# [AAModified-Start]打头，# [AAModified-End]结束。

# [AAModified-Start]
from Ext import chat_record
from Ext.color_logger.color_logger import color_logger
from Ext import api_key_authenticator

# Output color logs to the console and respond accordingly
# 输出彩色日志至控制台，并响应
def log_response_msg(msg, status, log_level):
    match log_level:
        case logging.DEBUG:
            color_logger.debug(msg)
        case logging.INFO:
            color_logger.info(msg)
        case logging.WARNING | logging.WARN:
            color_logger.warning(msg)
        case logging.ERROR:
            color_logger.error(msg)
        case logging.CRITICAL:
            color_logger.critical(msg)
    #
    msg_data = {
        "msg": msg,
    }
    response.status = status
    response.content_type = "application/json"
    response.body = json.dumps(msg_data)
    return response

# Read API Key List
# 读取API Key列表
api_keys = api_key_authenticator.load_line_txt_data('./APIKeys/APIKeys.txt')

# Check and verify API Key
# 检查与检验API Key
def check_api_key():
    api_key = request.forms.get('APIKey')
    if api_key is not None:
        rs = api_key_authenticator.check_api_key(api_key, api_keys,
                                                 lambda error: log_response_msg(error, 412, logging.WARN))
        if rs is not None:
            return rs
    else:
        # 412=Precondition Failed	The prerequisite for client request information is incorrect
        # 412=Precondition Failed	客户端请求信息的先决条件错误
        return log_response_msg("Can not get API key. Please pass with API key.", 412, logging.WARN)

@route('/chat_stream_for_yxxy', method=("POST", "OPTIONS"))
def api_chat_stream_for_yxxy():
    # Check and verify API Key
    # 检查与检验API Key
    is_pass, rsq = check_api_key()
    if is_pass is False:
        return rsq
    # Extract data
    # 提取数据
    words = request.forms.get('Words')
    print(f"[Key:{request.forms.get('APIKey')}]:{words}")
    # Preference
    # 设置
    allowCROS()
    response.add_header("Connection", "keep-alive")
    response.add_header("Cache-Control", "no-cache")
    response.add_header("X-Accel-Buffering", "no")
    from websocket import create_connection
    protocol = request.urlparts.scheme
    if protocol == 'https':
        import ssl
        sslopt = {
            "cert_reqs": ssl.CERT_NONE,
        }
        ws = create_connection("wss://127.0.0.1:" + str(settings.port) + "/ws", sslopt=sslopt)
        # print("ssl")
    else:
        ws = create_connection("ws://127.0.0.1:" + str(settings.port) + "/ws")
        # print("http")
    ws.send(words)
    try:
        while True:
            result = ws.recv()
            if len(result) > 0:
                yield result
    except:
        pass
    ws.close()


# Get chat records
# 获取聊天纪录
@route('/chat_records', method=('POST', "OPTIONS"))
def api_chat_records():
    # Check and verify API Key
    # 检查与检验API Key
    is_pass, rsq = check_api_key()
    if is_pass is False:
        return rsq
    # Check chat record data
    # 检查聊天纪录数据
    form = bottle.FormsDict(request.forms).decode('utf-8')
    json_data = form.get('RecData')
    print(f"Rev request:{json_data}")
    data = json.loads(json_data)
    if data is None:
        # 412=Precondition Failed	客户端请求信息的先决条件错误
        return log_response_msg("Can not get record request data.", 412, logging.WARN)
    # Start querying
    # 开始查询
    response.body = chat_record.search_records(data.get("RecQty"), data.get("StartRecId"), data.get("KeysList"),
                                               data.get("StartDate"), data.get("EndDate"))
    return response

# [AAModified-End]

# [AAModified-Start]
# Save chat history
# 保存聊天纪录
# logging = settings.is_logging
# if logging:
#     from plugins.defineSQL import session_maker, 记录
is_logging = settings.is_logging
if is_logging:
    from plugins.defineSQL import session_maker, ChatRecordData
# [AAModified-End]

@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    try:
        # Omitting the previous paragraph...
        # 原有前段省略...
        # [AAModified-Start]
        if data is not None:
            # The start timing of asking - calculate queue
            # 问计时开始-计算排队
            ask_start_time = time.time()
            server_IP = websocket.base_url.hostname
            # [AAModified-End]
            # Omitting of the original middle section...
            # 原有中间段省略...
            # [AAModified-Start]
            # End marker for each paragraph of text
            # 每段文本的结束标记
            PER_WORD_END_SIGN = "///"
            # End marker for the entire text paragraph
            # 整段文本的结束标记
            STEAM_WORD_END_SIGN = "/././"
            # Do you want to add segment identifiers
            # 是否添加分段标识符
            is_add_words_div_mark = data.get('is_add_words_div_mark')
            if is_add_words_div_mark is None:
                is_add_words_div_mark = False
            # Calculate chat response time
            # 计算聊天回应时间
            chat_answer_cost = 0
            # [AAModified-End]

            lock = Lock(level)
            async with lock:
                # [AAModified-Start]
                # print("\033[1;32m"+IP+":\033[1;31m"+prompt+"\033[1;37m")
                # [AAModified-End]
                try:
                    # [AAModified-Start]
                    # Console output
                    # 控制台输出
                    from colorama import Fore
                    from colorama import Style
                    print(f"{Fore.BLUE}[{IP}]({len(prompt)}):{Style.RESET_ALL}{prompt}")
                    # The end of asking timing - calculate queue
                    # 问计时结束-计算排队
                    ask_end_time = time.time()
                    # Calculate chat queue time
                    # 计算聊天排队时间
                    chat_ask_cost = ask_end_time - ask_start_time
                    # Timing Start - Calculate Response Time
                    # 计时开始-计算回应时间
                    answer_start_time = time.time()
                    # Last returned text
                    # 上一次返回的文本
                    lastResponse = ''
                    # Do you want to only send new text compared to the previous round
                    # 是否仅发送较上一轮而言新的文本
                    is_only_send_new_word = data.get('is_only_send_new_word')
                    if is_only_send_new_word is None:
                        is_only_send_new_word = False
                    # Show and hide the "Calculating" prompt
                    # 显示与隐藏“正在计算”提示
                    is_show_cal_tip = data.get('is_show_cal_tip')
                    if is_show_cal_tip is not None and is_show_cal_tip is False:
                        data.update({"is_show_cal_tip": False})
                    # [AAModified-End]
                    for response in LLM.chat_one(prompt, history_formatted, max_length, top_p, temperature, data):
                        if (response):
                            # start = time.time()
                            # [AAModified-Start]
                            # await websocket.send_text(response)
                            # Only send the new words
                            # 只发新字段
                            if is_only_send_new_word:
                                newResponse = response.replace(lastResponse, '')
                            # Send all words
                            # 全部字段发送
                            else:
                                newResponse = response
                            # Add separator
                            # 添加分隔符
                            if is_add_words_div_mark:
                                await websocket.send_text(newResponse + PER_WORD_END_SIGN)
                            else:
                                await websocket.send_text(newResponse)
                            # print(f"{newResponse + PER_WORD_END_SIGN}")
                            lastResponse += newResponse
                            # [AAModified-End]
                            await asyncio.sleep(0)
                            # end = time.time()
                            # cost+=end-start
                    # [AAModified-Start]
                    # response = f'{prompt}：{datetime.datetime.now()}'
                    # Timing End - Calculate Response Time
                    # 计时结束-计算回应时间
                    answer_end_time = time.time()
                    chat_answer_cost = answer_end_time - answer_start_time
                    # Output End
                    # 输出结尾
                    if is_add_words_div_mark:
                        await websocket.send_text(STEAM_WORD_END_SIGN)
                    # Console output
                    # 控制台输出
                    print(f"{Fore.GREEN}[{settings.role.name}]({chat_answer_cost:.5f}sec):{Style.RESET_ALL}{response}")
                    # [AAModified-End]
                except Exception as e:
                    error = str(e)
                    # [AAModified-Start]
                    # await websocket.send_text("错误" + error)
                    error_print(error)
                    # Notify the client that the backend is restarting.
                    # 通知客户端，后端在重启。
                    await websocket.send_text(f'[ErrorCode_552]{STEAM_WORD_END_SIGN}')
                    # [AAModified-End]
                    await websocket.close()
                    raise e
                torch.cuda.empty_cache()
            # [AAModified-Start]
            if is_logging:
                # [AAModified-End]
                with session_maker() as session:
                    # [AAModified-Start]
                    #  jl = 记录(时间=datetime.datetime.now(),
                    #         IP=IP, 问=prompt, 答=response)
                    # Record asking
                    # 记录问
                    jl = ChatRecordData(Time=datetime.datetime.fromtimestamp(ask_start_time), IP=IP, ChatCost=chat_ask_cost,
                                        Content=prompt, RoleName='我', IsMine=1)
                    session.add(jl)
                    # Record answering
                    # 记录答
                    jl = ChatRecordData(Time=datetime.datetime.fromtimestamp(answer_end_time), IP=server_IP, ChatCost=chat_answer_cost,
                                        Content=response, RoleName=settings.role.name, IsMine=0)
                    # [AAModified-End]
                    session.add(jl)
                    session.commit()
            # [AAModified-Start]
            # print(response)
            # [AAModified-End]
        await websocket.close()
    except WebSocketDisconnect:
        pass
    waiting_threads -= 1

if __name__ == "__main__":
    # [AAModified-Start]
    # Use HTTPS for self-signed files。
    # 有自签名文件就使用https。
    ssl_root_path = f'{os.getcwd()}/../Safe/SSL/'
    ssl_key_file = f'{ssl_root_path}/key.pem'
    ssl_cert_file = f'{ssl_root_path}/cert.pem'
    if os.path.exists(ssl_key_file) and os.path.exists(ssl_cert_file):
        print("\033[0;32;32mFound the ssl config files and will use https.\033[0m")
        uvicorn.run(app, host="0.0.0.0", port=settings.port,
                    ssl_keyfile=ssl_key_file,
                    ssl_certfile=ssl_cert_file,
                    ssl_cert_reqs=ssl.CERT_NONE,
                    # ssl_ca_certs=ssl_ca_cert_file,
                    log_level='error',
                    loop="asyncio")
    # Otherwise, use HTTP.
    # 否则使用http。
    else:
        print("Can not find the ssl config files and will use http.")
        # [AAModified-End]
        uvicorn.run(app, host="0.0.0.0", port=settings.port,
                    log_level='error', loop="asyncio")
