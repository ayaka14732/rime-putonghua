# rime-putonghua

rime 有声调普通话拼音方案

## 特性

- [x] 基本输入：按照标准普通话拼音输入
- [x] 声调输入：输入拼音后可加 <kbd>[</kbd>, <kbd>]</kbd>, <kbd>;</kbd>, <kbd>/</kbd> 表示四声，降低重码率
- [x] Emoji 输入：在选单中选择「有 Emoji」模式开启
- [x] 流行语输入：预置中国大陆网络流行语，如「蓝瘦香菇」、「吃枣药丸」
- [x] 符号输入：预置特殊符号，如 ⅓（三分之一）、¥（人民币）
- [x] 简繁转换：利用 OpenCC 进行基本的简繁转换，在选单中选择「繁體」模式开启
- [x] 百度云输入：按 <kbd>Ctrl</kbd> + <kbd>t</kbd> 触发，不按键时不触发
- [x] 两分反查：按 <kbd>&#x60;</kbd> 键进入两分输入，如 `caofu` 输入「苻」
- [x] 笔画反查：按 <kbd>v</kbd> 键进入笔画输入，以横竖撇捺折 (hspnz) 五键输入汉字

本方案码表采用有声调拼音，可以用于纠正普通话发音，也可用于其他自然语言处理任务。

本方案基础词库词条数约 16 万，在收词数量与性能之间取得平衡。

## 安装

### 手动安装

librime 需装配以下插件：

- [librime-lua](https://github.com/hchunhui/librime-lua)：lua 支持

安装以下依赖项：

- [szc126/rime-liangfen](https://github.com/szc126/rime-liangfen)：两分反查
- [rime/rime-stroke](https://github.com/rime/rime-stroke)：笔画反查
- [rime/rime-emoji](https://github.com/rime/rime-emoji)：Emoji 输入
- [sgalal/rime-symbolic-simp](https://github.com/sgalal/rime-symbolic-simp)：符号输入
- [rime/rime-essay-simp](https://github.com/rime/rime-essay-simp)：词频数据
- [hchunhui/librime-cloud](https://github.com/hchunhui/librime-cloud)：百度云输入

### Arch Linux

从 AUR 安装 [`rime-putonghua`](https://aur.archlinux.org/packages/rime-putonghua/)。

### 使用 plum 安装

确保 librime 装配了 [librime-lua](https://github.com/hchunhui/librime-lua) 插件，然后手动安装 [hchunhui/librime-cloud](https://github.com/hchunhui/librime-cloud)。 

打开命令行，输入以下命令：

```sh
curl -fsSL https://git.io/rime-install | bash -s -- szc126/rime-liangfen stroke emoji sgalal/rime-symbolic-simp essay-simp ayaka14732/rime-putonghua custom:set:config=default,key=installed_from,value=ayaka14732/rime-putonghua custom:add:schema=putonghua
```

## 数据来源

见本仓库 [`build`](https://github.com/ayaka14732/rime-putonghua/tree/build) 分支。

## 授权条款

本项目 `putonghua` 词库与 `putonghua.liuxingyu` 词库循[知识共享署名 4.0 国际许可协议](https://creativecommons.org/licenses/by/4.0/)进行许可。

本项目 `putonghua.extra` 词库循[知识共享署名-相同方式共享 4.0 国际许可协议](https://creativecommons.org/licenses/by-sa/4.0/)进行许可。
