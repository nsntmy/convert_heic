import os
import sys
from pathlib import Path
from PIL import Image
import pillow_heif


def convert_heic(input_path, output_format="jpg"):
    input_path = Path(input_path)
    output_format = output_format.lower()

    # ディレクトリの場合
    if input_path.is_dir():
        output_dir = input_path.parent / f"{input_path.stem}_{output_format}"
        output_dir.mkdir(exist_ok=True)
        for heic_file in input_path.glob("*.heic"):
            convert_file(heic_file, output_dir / f"{heic_file.stem}.{output_format}", output_format)
        print(f"Converted HEIC files saved in: {output_dir}")
    elif input_path.is_file() and input_path.suffix.lower() == ".heic":
        # ファイルの場合
        output_file = input_path.with_suffix(f".{output_format}")
        convert_file(input_path, output_file, output_format)
        print(f"Converted file saved as: {output_file}")
    else:
        print(f"Error: {input_path} is neither a HEIC file nor a directory containing HEIC files.")


def convert_file(heic_file, output_file, output_format):
    try:
        heif_image = pillow_heif.read_heif(str(heic_file))
        image = Image.frombytes(
            heif_image.mode, heif_image.size, heif_image.data, "raw", heif_image.mode
        )
        # フォーマット変換時にJPEGに対応
        image.save(output_file, format="JPEG" if output_format == "jpg" else output_format.upper())
        print(f"Converted: {heic_file} -> {output_file}")
    except Exception as e:
        print(f"Failed to convert {heic_file}: {e}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_heic.py <input_path> [output_format]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_format = sys.argv[2] if len(sys.argv) > 2 else "jpg"
    if output_format.lower() not in {"jpg", "jpeg", "png", "bmp"}:
        print(f"Unsupported output format: {output_format}. Supported formats are: jpg, png, bmp.")
        sys.exit(1)

    convert_heic(input_path, output_format)


if __name__ == "__main__":
    main()

