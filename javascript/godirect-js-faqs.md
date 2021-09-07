# FAQs for Go Direct JavaScript

## What are the requirements for using godirect-js?
- A [Vernier Go Direct Sensor](https://www.vernier.com/products/sensors/go-direct-sensors) <sup>1</sup>
- A computer or mobile device that run the Chrome browser

<sup>1</sup> Go Direct spectrometers are not supported.

## How do I get started with JavaScript?
Here are some generally helpful links for getting started with JavaScript
- [JavaScript Tutorials](https://javascript.info/)

## How do I edit JavaScript code?
If you have programmed with Python or Arduino, you are probably familiar with using an integrated development environment (IDE) that is customized to the language you are using. Since JavaScript is typically embedded in html code it does not have a dedicated IDE. This can make things a bit tricky when it comes to get started coding with this language.  

We used, and can recommend using, Glitch.com or Visual Studio Code. Glitch is an online editor that makes getting started very easy -- with no installation required. Glitch facilitates an online community which makes sharing scripts and searching others’ projects straight forward. 

Visual Studio Code is more appropriate for coding more complex projects that may require version control or sophisticated debugging. VS Code provides syntax highlighting, bracket-matching, auto-indentation, and other tools to facilitate your coding experience.

Both Glitch and Visual Studio Code are free. 
- [Glitch](https://glitch.com/) 
- [Visual Studio Code](https://code.visualstudio.com/Download)

## How do I import the GDX library?
 The easiest way to import a library is through a Content Delivery Network (CDN). This allows you to import libraries with a single line. To create programs with Go Direct compatibility put this in the header of your html file:

 ``` html
 <script src="https://unpkg.com/@vernier/godirect/dist/godirect.min.umd.js"></script> 
 ```

## How can I use the GDX library?
### Creating a Device
The device class creates an object to represent the sensor to be used in the code. This object has many properties that can be used to collect information about the sensor like the battery level, the name, the serial number, and the charging state. In addition to accessing these properties you can also modify the sensor settings through this class. Using the line of code below will assign the selected device to gdxDevice to be used later in the program. 

```javascript
const gdxDevice = await godirect.selectDevice()
```

### Changing the Sample Rate

To change the sample rate of the sensor, use:

```javascript
gdxDevice.start(sampleRate);
```

### Changing the Sensor Channel

Many Vernier sensors come with a variety of sensors all bundled into one. For example, the GDX-Force sensor can measure force, but it can also has a gyroscope and an accelerometer. The examples all use the default channel, but you can change the sensor channel to collect different types of data with the same sensor. This can be done with:

 ```javascript
 const sensor =  gdxDevice.getSensor(channelNumber);
 sensor.setEnabled(true); 
```

 The channel number is an integer corresponding to the available sensors on each device. Use the example program  [gdx_getting_started_1.html](./gdx_getting_started_1.html) to see available sensor channels for your sensor.

## Where can I find examples of using the godirect-js library?
- Official examples that use godirect-js can be found in the Vernier [godirect-examples repository](./).
