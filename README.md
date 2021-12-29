<h1 align="center">
    <b>Dicom to PNG converter </b> 
<br>
</h1>

## What is this for?
This repository convert your DICOM (.dcm) image into PNG (.png) image. this code give you a 5 diffrent palette color png image. 

## DICOM
DICOM is the international standard for medical images and related information. It defines the formats and communication protocols for media exchange in radiology, cardiology, radiotherapy and other medical domains.


## pydicom
[pydicom](https://pydicom.github.io/) is a pure Python package for working with DICOM files. It lets you read, modify and write DICOM data in an easy "pythonic" way.

As a pure Python package, pydicom can run anywhere Python runs without any other requirements, although if you're working with Pixel Data then we recommend you also install [NumPy](https://numpy.org/).

If you're looking for a Python library for DICOM networking then you might be interested in another of our projects: pynetdicom.


## Installation
#### Application tested on:

- pydicom 2.2.2
- numpy 1.21.4
- pypng 0.0.21
- Pillow 2.2.1
- gdcm 3.0.10
- OS: Linux (Ubuntu 20.04)


## Using `virtualenv`

1. Make a virtual environment using virutalenv and activate it.

```virtualenv -p python3 cartoonize```
```source cartoonize/bin/activate```

2. Install python dependencies.

```pip install -r requirements.txt```

3.To run 
```python3 mritopng.py```


## Instruction
First, set up this repository on your local machine.
Installing all dependency in your local machine.

To make changes
At line 128 on ```./dcm_img```. this is your Dicom path.
At line 129 on ```png_folder``` this is your png path.


## Sample Video

<img src="./Docs/ezgif.com-gif-maker.gif" width="40" height="40" />

