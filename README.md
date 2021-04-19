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
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



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



* [Raspbery Pi Zero WH]
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
   ```

### Installation: via ssh over wifi

1. Start with a fresh install of Raspbian Lite OS

2. Clone the repo
   *Download the code from this git hub repo
   ```sh
   git clone https://github.com/Watrick117/Conway_ePaper.git
   ```
3. Clone the Waveshare Demo Code
   ```sh
   https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT
   ```
4. Update and Download Prerequisites
   ```sh
   sudo apt-get update
   sudo apt-get install python3-pip
   sudo apt-get install python3-pil
   sudo apt-get install python3-numpy
   sudo pip3 install RPi.GPIO
   sudo pip3 install spidev
   ```
5. Change to the directory that contains and build and install the setup.py file
   ```sh
   cd e-Paper-master
   cd RaspberryPi_JetsonNano
   cd python
   sudo python3 setup.py build
   sudo python3 setup.py install
   ```
6. Move the conway_epaper.py into the examples folder
   ```sh
   Drag and drop animation
   ```
7. Test run the code!
   ```sh
   sudo python3 conway_epaper.py --size 250 122 -p 15 -g 90
   ```
8. Modify your arguments to suit your tastes and needs
   * ['-s', '--size'] --Takes in two arguments that represent the size of your screen.
   * ['-g', '--generation'] --Sets the max generation.
   * ['-p', '--population'] --Percentage of times that random cells of life are added to based on board size.
9. Add the conway_epaper.py to crontab to run each time the raspbery pi restarts
   ```sh
   crontab -e
   @reboot sudo python3 /home/pi/code/python/examples/conway_epaper_2.13_V2.py --size 250 122 -p 15 -g 90
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





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
