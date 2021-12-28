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
```pip install pydicom```

```pip install numpy```

```pip install pypng```

```pip install Pillow==2.2.1```

```pip install gdcm```

```pip install pylibjpeg```

```pip install pylibjpeg-libjpeg```

Also, update numpy using this command ```pip install --upgrade numpy```


## Instruction
First, set up this repository on your local machine.
Installing all dependency in your local machine.

To run 
python3 mritopng.py

To make changes
At line 120 on ```./dcm_img```. this is your Dicom path.
At line 121 on ```png_folder``` this is your png path.


