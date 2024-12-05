[English](README.md) | [日本語](README.ja.md)

<img src="https://img.shields.io/badge/-Python-3776AB.svg?logo=python&style=plastic">

# HEIC to Image Converter
A Python script to convert HEIC files to other image formats such as JPG, PNG, or BMP.

## Required Libraries
- Pillow
- pillow-heif

You can install the required libraries by running:

```shell
pip install pillow pillow-heif
```

## Usage

```shell
python convert_heic.py [path_to_file_or_directory] [output_format]
```

### Parameters
- path_to_file_or_directory: Path to a single HEIC file or a directory containing HEIC files.
- output_format (optional): The output image format (jpg, png, bmp, etc.). Default is jpg.

## Specification

- If a file is specified, it converts the single HEIC file and saves it in the same directory with the specified format.
- If a directory is specified, all HEIC files within that directory are converted, and the converted files are saved in a new directory. The new directory's name is the original directory name suffixed with _[output_format].

### Examples

### Single File Conversion
Command:
```
python convert_heic.py C:\Images\photo.heic
```
Output:
```
C:\Images\photo.jpg
```

### Directory Conversion
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
