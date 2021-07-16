# term_img_printer

![screenshots](https://raw.githubusercontent.com/fa0311/term-img-printer/master/docs/img/screenshots.png)<br>
[term-printer](https://github.com/nanato12/term-printer "term-printer") を利用したターミナルに画像を出力するプログラムです<br>

## Why?

:sweat_smile: <br>

## Installation

```console
$ pip install term-printer
$ pip install opencv-python
```

## Usage

```python
# 1/20 scale
term_img_printer.imgprint("assets/test.jpg",20,20,"  ")
```

output: [51\*51](https://raw.githubusercontent.com/fa0311/term-img-printer/master/docs/img/screenshots.png "51*51")<br><br>

```python
# 1/1 scale
term_img_printer.imgprint("assets/test.jpg",1,1,"  ")
```

output: [1025\*1026](https://raw.githubusercontent.com/fa0311/term-img-printer/master/docs/img/screenshots2.png "1025*1026")<br>

# License

term_img_printer is under MIT License
