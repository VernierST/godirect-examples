# FAQs for godirect-js (Work In Progress)

## What are the requirements for using godirect-js?
- A [Vernier Go Direct Sensor](https://www.vernier.com/products/sensors/go-direct-sensors)
- A computer or mobile device that run the Chrome browser

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

## How do I import the library?
 The easiest way to import a library is through a Content Delivery Network (CDN). This allows you to import libraries with a single line. To create programs with GoDirect compatibility put this in the heading of your html file:

 ``` <script src="https://unpkg.com/@vernier/godirect/dist/godirect.min.umd.js"></script> ```

## Where can I find examples of using the godirect-js library?
- Official examples that use godirect-js can be found in the Vernier [godirect-examples repository](./).
