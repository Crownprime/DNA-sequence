## 批量提交 code 解析 DNA 序列

仅兼容 python3

### 安装第三方模块

```
pip install -r requirements.txt
```

### 环境变量

拷贝项目根目录下的 .env.example 重命名为 .env，并填写值

```
// 序列
SEQUENCE=AAAAABBBBB
// code 值，多个请用半角逗号隔开(,)
CODES=AAA,BBBB,CCC
```

### 运行

```
python app.py
```
循环查询较慢，请耐心等待（或者我之后优化）

提示全部成功之后，查看根目录底下 `result.txt`

需注意，每次运行代码都会覆盖上次生成的 result.txt 文件，若为有效数据请在生成后马上拷贝转移。

### 额外内容

查询额外参数可手动配置，详情请查看 `vars.py` 文件