

Graphical Reporting framework for the Robotframework report ( output.xml)

## Reporting for the robot framework

- It takes the generated output.xml as the input. 
- Generates Graph using plotly library
- Use the shell scripts run.sh to create the virtual environment

## Installation

Create a virtual environment and install all the packages from requirements.txt
    
    virtualenv roboreport
    source roboreport/bin/activate
    pip install -r requirements.txt

Or You can also make use of the shell script run.sh for setting up virtual environment and installing the software

## Steps to generate the HTML report
    python robo_report.py

This should generate the HTML report called graph.html

## sample report screenshot 
![report](summary_1.png?raw=true "summary report")
![report](tag_wise_report.png?raw=true "summary report")



License
-------
The code uses the Plotly library to plot the graphs (Plotly, Inc.)

Plotly's Code is released under the [MIT license](LICENSE.txt).

Docs released under the [Creative Commons license](https://github.com/plotly/documentation/blob/source/LICENSE).. 