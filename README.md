# conway_epaper

<h1>A tribute to John Conway's game of life running on a waveshare 2.13 e-Paper V2 display<\h>

Tutorial:
  I followed this tutorial to start and then filled in what I needed.
    #https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT
  
  <div>
    <code>
    sudo apt-get update
    sudo apt-get install python3-pip
    sudo apt-get install python3-pil
    sudo apt-get install python3-numpy
    sudo pip3 install RPi.GPIO
    sudo pip3 install spidev
    </code>
  </div>
  
  <code>
  sudo git clone https://github.com/waveshare/e-Paper
  </code>
  
  <code>
  cd e-Paper-master
  cd RaspberryPi_JetsonNano
  cd python
  sudo python3 setup.py build
  sudo python3 setup.py install
  </code>
  
  "Drag and Drop" the conway_epaper.py into the examples folder
    
  And... test run the code!
  <code>sudo python3 conway_epaper.py --size 250 122 -p 15 -g 90</code>
  
  modify your arguments to suit your tastes and needs!
  
Arguments:
  '-s', '--size': "Takes in two arguments that represent the size of the board.")
  '-g', '--generation': "Sets the max generation.")
  '-p', '--population': "Percentage of times that random cells of life are added to based on board size.")
  
  RECOMENDED: 
    @reboot sudo python3 /home/pi/code/python/examples/conway_epaper_2.13_V2.py --size 250 122 -p 15 -g 90
