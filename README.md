# QR Code Generator

This Python script allows you to generate QR codes using the `qrcode` library. It provides a simple and convenient way to encode various types of information, such as links, text, or contact details, into QR codes. Additionally, the script utilizes the `Pillow` library to customize the appearance of the QR code by adding text.

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Clone or download the repository to your local machine.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Install the required libraries by running the following command:
   ```
   pip install qrcode Pillow
   ```
4. Run the script using the following command:
   ```
   python generator.py
   ```
5. Follow the instructions in the terminal to enter the content you want to encode in the QR code.
6. Once the QR code is generated, the script will save it as an image file named `qr_code.png` in the same directory.

## Customization

If you want to customize the appearance of the QR code or add text, you can modify the following parameters in the `generate_qr_code` function:

- `fill_color`: Sets the color of the QR code pattern (foreground). You can specify any valid color code or name.
- `back_color`: Sets the background color of the QR code. Again, you can specify any valid color code or name.
- `text_to_add`: The text you want to add to the QR code image. You can change it to suit your needs.
- `font`: The font to be used for the added text. You can replace it with the path to your desired font file or use a different font installed on your system.
- `font_size`: The size of the font for the added text. Adjust it as necessary.

Feel free to modify these parameters to achieve the desired QR code appearance and text customization.

## Dependencies

The script relies on the following Python libraries:

- `qrcode`: Used to generate the QR code.
- `Pillow`: A dependency of `qrcode` that allows customization of the QR code image.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions to this project are welcome. Feel free to open issues or submit pull requests to suggest improvements, report bugs, or add new features.

## Acknowledgments

The QR code generation functionality is provided by the `qrcode` library, and the text customization is achieved using the `Pillow` library. Many thanks to the developers of these libraries for their valuable contributions.

## References

- `qrcode` library: [https://github.com/lincolnloop/python-qrcode](https://github.com/lincolnloop/python-qrcode)
- `Pillow` library: [https://pillow.readthedocs.io](https://pillow.readthedocs.io)