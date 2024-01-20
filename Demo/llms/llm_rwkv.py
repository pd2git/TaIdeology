# Explanation: Only list the modified parts, starting with # [AAModified Start] and ending with # [AAModified End].
# 说明：仅列出修改的部分，以# [AAModified-Start]打头，# [AAModified-End]结束。

    def chat_one(prompt, history, max_length, top_p, temperature, data):
        cfg_factor = data.get('cfg_factor')
        cfg_ctx = data.get('cfg_ctx')
        cfg_ctx_history = data.get('cfg_ctx_history')
        # [AAModified-Start]
        # If these are present in the parameters, update the configuration.
        # 如果参数中有这些则更新配置
        # Presence penalty
        # 存在惩罚
        presence_penalty = data.get('presence_penalty')
        if presence_penalty is not None:
            presencePenalty = presence_penalty
        # Frequency penalty
        # 频率惩罚
        frequency_penalty = data.get('frequency_penalty')
        if frequency_penalty is not None:
            countPenalty = frequency_penalty
        # [AAModified-End]
        # Omitting of the original middle section...
        # 原有中间段省略...
        # [AAModified-Start]
        # yield str(len(ctx))+'字正在计算\n'+str(len(tokens))+" tokens"
        is_show_cal_tip = True
        if data is not None:
            if data is not None and data.get("is_show_cal_tip") is not None and data.get("is_show_cal_tip") is False:
                is_show_cal_tip = False
        if is_show_cal_tip:
            yield str(len(ctx)) + '字正在计算\n' + str(len(tokens)) + " tokens"
        # [AAModified-End]
        # Omitting of the original middle section...
        # 原有中间段省略...
        # [AAModified-Start]
        # yield response.strip()
        if is_show_cal_tip:
            yield response.strip()
            print(f"all={response.strip()}")
        # [AAModified-End]
        # Omitting the original posterior paragraph...
        # 原有后段省略...
