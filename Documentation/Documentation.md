# About her ideology

Language：English, [简体中文](./Documentation_zh-CN.md)

This is a backend for configuring her ideology. You can choose your favorite backend and configure it with unique ideology.

The project has great freedom to choose any large language model backend, known to support ChatGLM, ChatRWKV, as well as features such as ChatGPT, Yuan, Moss, Llama, and so on.

Suggest using [Wenda](https://github.com/wenda-LLM/wenda) The open-source project is more convenient to support the above model, and the sample of this project is also based on this project.

Specifically, please refer to **_"[Demo](./Demo)"_** And **_"[Documentation](./Documentation)"_** Folder.

# Installation

## Dependency

- [color_logger](./Ext)
- [chat_record](./Ext/chat_record.py)
- [api_key_authenticator](./Ext/api_key_authenticator.py)
- [python](https://www.python.org/) (The specific version depends on the backend you choose)

# Usage

### Use Wenda project + a Demo code
1. Refer to the Demo to modify the original code of the Wenda project. The code file name in the Demo corresponds to the file name of the code in the Wenda project. The specific modifications are explained in the Demo code.
2. Place the modules under the dependent module folder [Ext](./Ext) in the root directory of the Wenda project (at the same level as wenda.py).
3. Install additional dependency libraries [requirements-extra](./requirements/requirements-extra.txt).
4. After configuring the project according to the Wenda project requirements, run it.

### Use other projects + a Demo code
1. Refer to the method of using the Wenda project, combine it with the Demo code, and modify the corresponding area code.
2. Ensure that the entire communication meets the communication protocol.
3. Run your backend.

# Communication protocol

## Chat

### The data requested by client

Method：Web Post

Format：Web Form

Content：

|   Key   |  Format   | Value | Remark                                              |
|:-------:|:---------:|-------|-----------------------------------------------------|
| APIKey  |   Text    | --  | You can customize the value yourself.               |
| Words | Json text(UTF-8) | --  | Please refer to "Words data" for detailed values. |

Words data：
```json lines
{
  // prompt
  "prompt": "你好",
  // temperature
  "temperature": 0.8,
  // top_p
  "top_p": 0.2,
  // Will not modify its value
  "is_add_words_div_mark": true,
  // Will not modify its value
  "is_only_send_new_word": true,
  // Will not modify its value
  "is_show_cal_tip": false,
  // Chat record
  "history": [
    {
      // Enumeration values: user represents what the user says, 
      // and AI represents what the backend says.
      "role": "user",
      // What was said
      "content": "You are an intelligent assistant who is good at chatting."
    },
    {
      "role": "AI",
      "content": "OK."
    }
  ],
  // This is an item that only comes with RWKV
  "presence_penalty": 0.6,
  // This is an item that only comes with RWKV
  "frequency_penalty": 0.3
}
```

### The data returned by the server

Method: Please refer to for details **_"[Demo](./Demo)"_**

Format: Text for generating content, UTF-8

Attention:
- Adopting streaming generation to enhance the client experience.
- Each time the content is returned, add "///" (without quotation marks) at the end.
- After generating all the content, add "/././" (without quotation marks) at the end.
- When encounter punctuation points '. ','! ','. ','! ','? ','; ',': ', the client will automatically break the sentence and output a bubble without quotation marks.

Example:<br>
Complete content:**_I am an AI assistant and I enjoy chatting with you. Do you like it?_**<br>
The first batch may return data and must be marked with a tail:**_I am///_**<br>
The second batch may return data and must be marked with a tail:**_an AI assistant, and I enjoy///_**<br>
The third batch may return data and must be marked with a tail:**_chatting with you. Do you like it///_**<br>
The third batch may return data, with two tail labels: "single return" and "current generation completed":**_?////././_**<br>

## Request the chat records

### The data requested by client

Method：Web Post

Format：Web Form

Content：

|   Key   |  Format   | Value | Remark                                              |
|:-------:|:---------:|-------|-----------------------------------------------------|
| APIKey  |   Text    | --  | You can customize the value yourself.               |
| RecData | Json text(UTF-8) | --  | Please refer to "RecData data" for detailed values. |

RecData data：
```json lines
{
  // -1 indicates starting the search from scratch, 
  // zero and positive values indicate searching forward from that ID
  "StartRecId": -1,
  // Number of request records
  "RecQty": 20,
  // No keywords set, data is an empty list.
  "KeysList": [
    "Hello"
  ],
  // Unlimited date, set to null, without quotation marks.
  "StartDate": "2023/01/01 16:16:55",
  // Unlimited date, set to null, without quotation marks.
  "EndDate": "2023/01/02 16:16:55"
}
```

### The data returned by the server

Method: Web Post

Format：json, UTF-8

Content：
```json lines
{
  "RecordsList": [
    {
      // The ID of this record
      "Id": 12,
      // The time of the record generation
      "Time": "2023/01/02 16:16:55",
      // Speaker's nickname
      "NickName": "Role XXX",
      // Chat content
      "ChatContent": "Hello",
      // Is it said by the user.
      "IsMine": false
    }
  ]
}
```

# Technical details

## Known limitations

- Currently it has only been tested under Windows 10. It is theoretically supported on other platforms supported by Python.
- Currently only streaming replies are supported for front-end bubble display.

## Package content

The following table shows the function of each major folder or file in the package:

|Location| Description |
|---|---------------------|
|`..\Demo`| Contains examples, including code, that demonstrate the main functionality. |
|`..\Documentation`| Contains multilingual documentation for introduction and usage, such as the main document. |
|`..\requirements`| Contains dependent modules required for the installation environment. |

# Document version log

| Date | Description |
|------------|------------------------|
| 2024-01-17 | Document (v1.0) created, matching package version 1.0.1. |