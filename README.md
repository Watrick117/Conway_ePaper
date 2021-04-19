<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** Watrick117, Conway_ePaper, @PatrickWoltman, PatrickHWoltman@gmail.com, Conway_ePaper, Conway's Game of Life on e-Paper
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Watrick117/Conway_ePaper">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Conway_ePaper</h3>

  <p align="center">
    Conway's Game of Life on e-Paper
    <br />
    <a href="https://github.com/Watrick117/Conway_ePaper"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Watrick117/Conway_ePaper">View Demo</a>
    ·
    <a href="https://github.com/Watrick117/Conway_ePaper/issues">Report Bug</a>
    ·
    <a href="https://github.com/Watrick117/Conway_ePaper/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

### Built With



* [<a href="https://www.raspberrypi.org/products/raspberry-pi-zero-w/">Raspbery Pi Zero WH]
* [<a href="https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT">Waveshare 2.12inch_e-Paper_HAT</a>]
* [Python]



<!-- GETTING STARTED -->
## Getting Started

To get this project up and running follow the tutorial below.

### Tutorial

This is an example of how to list things you need to use the software and how to install them.

## Prerequisites
   ```sh
   sudo apt-get install python3-pip
   sudo apt-get install python3-pil
   sudo apt-get install python3-numpy
   sudo pip3 install RPi.GPIO
   sudo pip3 install spidev
   sudo pip3 install pypng
   ```

### Installation: via ssh over wifi

1. Start with a fresh install of Raspbian Lite OS with ssh and spi enabled

2. Update Raspbian and Download Prerequisites
   ```sh
   sudo apt-get update
   sudo apt-get install python3-pip
   sudo apt-get install python3-pil
   sudo apt-get install python3-numpy
   sudo pip3 install RPi.GPIO
   sudo pip3 install spidev
   sudo pip3 install pypng
   sudo apt install git
   ```
   
3. Create 'code' folder
   ```sh
   sudo mkdir code
   cd code
   ```
4. Clone the Waveshare Demo Code
   ```sh
   sudo git clone https://github.com/waveshare/e-Paper
   ```
5. Clone the repo
   *Download the code from this git hub repo
   ```sh
   sudo git clone https://github.com/Watrick117/Conway_ePaper.git
   ```
6. Change to the directory that contains and build and install the setup.py file
   ```sh
   cd e-Paper
   cd RaspberryPi_JetsonNano
   cd python
   sudo python3 setup.py build
   sudo python3 setup.py install
   ```
7. Copy the conway_epaper.py into the examples folder
   ```sh
   cd Conway_ePaper
   sudo cp conway_epaper.py ../examples/conway_epaper.py
   cd ..
   cd examples
   ```
8. Test run the code!
   ```sh
   sudo python3 conway_epaper.py --size 250 122 -p 15 -g 90
   ```
9. Modify your command line arguments to suit your tastes and needs
   * ['-s', '--size'] --Takes in two arguments that represent the size of your screen.
   * ['-g', '--generation'] --Sets the max generation.
   * ['-p', '--population'] --Percentage of times that random cells of life are added to based on board size.
10. Set code to run on startup
   ```sh
   crontab -e
   ```
   add this line to the bottom of the file
   ```sh
   @reboot sudo python3 /home/pi/code/e-Paper/RaspberryPi_JetsonNano/python/examples/conway_epaper.py --size 250 122 -p 15 -g 90
   ```




<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/Watrick117/Conway_ePaper/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request







<!-- CONTACT -->
## Contact

Patrick Woltman - [@PatrickWoltman](https://twitter.com/PatrickWoltman) - PatrickHWoltman@gmail.com

Project Link: [https://github.com/Watrick117/Conway_ePaper](https://github.com/Watrick117/Conway_ePaper)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* []()
* []()
* []()



[forks-shield]: https://img.shields.io/github/forks/Watrick117/repo.svg?style=for-the-badge
[forks-url]: https://github.com/Watrick117/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/Watrick117/repo.svg?style=for-the-badge
[stars-url]: https://github.com/Watrick117/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/Watrick117/repo.svg?style=for-the-badge
[issues-url]: https://github.com/Watrick117/repo/issues
