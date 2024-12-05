[English](README.md) | [日本語](README.ja.md)

<img src="https://img.shields.io/badge/-Python-3776AB.svg?logo=python&style=plastic">

# HEIC to Image Converter
HEICファイルをJPG、PNG、BMPなどの形式に変換するPythonスクリプトです。

## 必要なライブラリ
- Pillow
- pillow-heif

以下のコマンドでライブラリをインストールしてください：

```shell
pip install pillow pillow-heif
```

## 使用方法

```shell
python convert_heic.py [ファイルまたはディレクトリのパス] [出力形式]
```

### パラメータ
- `ファイルまたはディレクトリのパス`: 単一のHEICファイル、またはHEICファイルを含むディレクトリのパスを指定します。
- `出力形式` (省略可能): 変換後の画像形式（`jpg`、`png`、`bmp` など）。デフォルトは`jpg`。

## 仕様

- ファイルを指定した場合、そのHEICファイルを変換し、同じディレクトリに指定形式で保存します。
- ディレクトリを指定した場合、そのディレクトリ内の全てのHEICファイルを変換します（サブディレクトリは含まれません）。変換後のファイルは、新しいディレクトリ（元のディレクトリ名に `_[出力形式] `を付加）に保存されます。

### 使用例

### 単一ファイルの変換
Command:
```
python convert_heic.py C:\Images\photo.heic
```
Output:
```
C:\Images\photo.jpg
```

### ディレクトリ内のファイル変換
Command:
```
python convert_heic.py C:\Images png
```
Output:
```
C:\Images_png
├─photo1.png
├─photo2.png
└─photo3.png
```
