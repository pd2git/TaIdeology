# Explanation: Only list the modified parts, starting with # [AAModified Start] and ending with # [AAModified End].
# 说明：仅列出修改的部分，以# [AAModified-Start]打头，# [AAModified-End]结束。

def chat_one(prompt, history_formatted, max_length, top_p, temperature, data):
    # [AAModified-Start]
    # yield str(len(prompt)) + '字正在计算'
    is_show_cal_tip = True
    if data is not None:
        if data is not None and data.get("is_show_cal_tip") is not None and data.get("is_show_cal_tip") is False:
            is_show_cal_tip = False
    if is_show_cal_tip:
        yield str(len(prompt)) + '字正在计算'

    if len(history_formatted) > 0 and chatglm3_mode and history_formatted[0]['role'] == "system":
        # if len(history_formatted)>0 and history_formatted[0]['role']=="system":
        # [AAModified-End]
        # Omitting the original posterior paragraph...
        # 原有后段省略...
