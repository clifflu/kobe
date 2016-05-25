# Kobe - 靠北工程師

透過命令列發訊至 [靠北工程師](https://engineer.kobe.ga) ，使用其提供的 cURL 介面。

注意：這是第三方工具，與靠北工程師官方無關。

## Requirements

Python (2 or 3), pip

## Install

pip install kobe

## Usage

```
% kobe
Usage:
    kobe [-i] <message>
    kobe --help
    kobe --version
```
顯示基本操作

```
% kobe -h
kobe - send message to engineer.kobe.ga
Max 1024 (text) or 300 (image) chars.

Usage:
    kobe [-i] <message>
    kobe --help
    kobe --version

Options:
    -i --image      Image mode
    -h --help       Show this page
    -v --version    Show version info
```
完整 help 畫面

```
% kobe 今天天氣也太好了吧
https://engineer.kobe.ga/2DWCINy2q
```
發信成功後，程式會印出訊息 URL

```
% kobe --image "今天天氣 也太好了吧"
https://engineer.kobe.ga/2DWCINy2q
```
訊息若包含空白，要使用單或雙引號括住

```
% kobe --image "今天天氣
dquote> 也太好了吧"
https://engineer.kobe.ga/2DWCINy2q
```
訊息若包含換行字元，要使用單或雙引號括住

## License

MIT
