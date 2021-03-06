# picosdk-ps9300-python-examples

*picosdk-ps9300-python-examples* contains an example Python module for demonstrating how to control PicoScope<sup>®</sup> 9300 Series PC Sampling Oscilloscopes using ActiveX.

## Getting started

### Prerequisites

#### PicoScope 9300 Series

* PicoScope 9301
* PicoScope 9302 
* PicoScope 9311 
* PicoScope 9312 
* PicoScope 9321 
* PicoScope 9341

The above list includes all -15, -20 and -25 models.

#### Python

* [Python 2.7](https://www.python.org/download/releases/2.7/), or
* [Python 3.6](https://www.python.org/download/releases/3.6/) 
* [win32com]
* [numpy]
* [matplotlib]

*Note:* Anaconda 5.0.0 can also be installed to provide the above.

#### Windows

* [Microsoft Visual Studio 2017](https://www.visualstudio.com/) (including Community edition) or later (this is only required to open the solution files provided).

### Installing software

* Download the *PicoSample 3* software for PicoScope 9300 Series models from our [Downloads page](https://www.picotech.com/downloads).

### Installing the python driver wrapper

A COM object driver wrapper created using the win32 module for the *PicoSample* COM object is included in these examples.
This is required for running these examples in order to communicate with the COM object to control the PicoScope 9300 Series device.

### Programmer's Guides

You can download Programmer's Guides providing a description of the API functions for the PicoScope 9300 Series from our [Documentation page](https://www.picotech.com/library/documentation).

## Obtaining support

Please visit our [Support page](https://www.picotech.com/tech-support) to contact us directly or visit our [Test and Measurement Forum](https://www.picotech.com/support/forum17.html) to post questions.

## Contributing

Contributions are welcome. Please refer to our [guidelines for contributing](.github/CONTRIBUTING.md) for further information.

## Copyright and licensing

See [LICENSE.md](LICENSE.md) for license terms. 

*PicoScope* and *PicoSample* are registered trademarks of Pico Technology Ltd. 

*Windows* is a registered trademark of Microsoft Corporation. 

Copyright © 2018 Pico Technology Ltd. All rights reserved. 
