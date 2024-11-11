# Open Guided Waves

This GitHub repository is created in support of the paper **"Open Guided Waves: Long-Term Guided Wave Based Structural Health Monitoring under Uncontrolled and Highly Dynamic Conditions"**. You can access the full article [here](https://.........).  
This repository provides an introduction to the **Open Guided Waves**. We provide a long-term, real-world structural health monitoring (SHM) benchmark dataset to support damage detection and analysis under varying environmental conditions.

## Abstract
Modern society relies on structural health monitoring to assess the condition of mechanical systems and civil
infrastructure, ensuring they operate efficiently and safely. While many studies focus on evaluating structures under
controlled or stable lab conditions, a significant number of structures function in uncontrolled and dynamic environments
over extended periods. Long-term monitoring in such complex conditions presents additional challenges compared to
lab-based assessments. Despite this, few studies address structural health monitoring under these conditions, largely
due to the lack of a public benchmark dataset. Such a dataset is crucial for identifying signal features, understanding
patterns in guided waves from dynamic environments, and evaluating structural health monitoring methods. To address
this gap, this paper presents a public dataset from a long-term outdoor structural monitoring experiment conducted at
the University of Utah, Salt Lake City. The monitoring, spanning over 4.5 years, collected approximately 560 million
guided waves under both regular environmental variations (e.g., daily temperature changes ranging from −12.2◦C to
52.5◦C, and humidity ranged from 0.5% to 100%) and irregular variations (e.g., rain and snow). The measured guided
waves in the public dataset are also affected by sensor drift and installation shifts consistently over time. Additionally,
thirteen types of damage were introduced to the monitored structure to support damage detection and severity
evaluation under these conditions. The dataset includes measurement times, temperature, humidity, air pressure,
brightness, and weather information to aid in damage detection. This paper uses correlation coefficients between
adjacent guided waves and optimal correlation coefficients with baseline guided waves to highlight four key challenges in
long-term outdoor monitoring: the impact of regular and irregular environmental variations, sensor drift, and installation
shifts on guided waves, and the detection of minor damage that causes only slight changes in guided waves. These
insights aim to assist researchers in developing more practical methods for structural health monitoring in uncontrolled
and dynamic environments.

## Overview of the Monitoring Setup
![Overview of the Monitoring Setup](/figures/SensorLocation1.png)
*Figure 1. The actual positions of the lead zirconate titanate (PZT) transmitters (sensors 5 and 6) and receivers (sensors 1, 2, 3 and 4) are displayed in the left figure, while the precise coordinates (X: cm, Y: cm) are provided in the right figure.*
  
![Exp Setup](/figures/ExpSetup.png)
*Figure 2. Figure (a) shows the monitored structure, an aluminum plate, positioned on the first layer of a shelf. The data acquisition
system was housed in a foam box on the second layer of the shelf. Figures (b) and (c) display the locations of the temperature,
brightness, air pressure, and humidity sensors, which were mounted on the exterior of the foam box.*

![Raw Signal](figures/FullRawSignal.png)
*Figure 3. The original guided wave, consisting of 10,000 samples and lasting 10 ms. This guided wave was collected from path 5-4 at 20:18:06 on April
24, 2021, at a measurement temperature of 16.57 ◦ C.*
