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

## Background & Summary
To address the need of public benchmark data for evaluating the effectiveness of damage detection methods in practical environmental and operational conditions, this work presents a public benchmark dataset gathered from a long-term outdoor guided wave structural health monitoring experiment conducted under uncontrolled and dynamic conditions. The dataset was collected in outdoor environments at the University of Utah, Salt Lake City, between March 2018 and October 2022, amassing approximately 6.4 million guided wave data points under various environmental conditions. The dataset also includes corresponding measurements of surrounding environmental factors such as temperature, humidity, brightness, air pressure, and weather information during the guided wave collection process. A total of 13 different types of damage were introduced, ranging from minor to severe, including metal mass attachments, small dents, and through-hole damage. Detailed descriptions of the data acquisition equipment, collection processes, and damage generation methods are provided in this paper. Challenges in long-term structural health monitoring under uncontrolled and dynamic environmental conditions—including regular and irregular environmental variations, sensor drift, installation drift, and variations in damage severity—are demonstrated using correlation coefficients between adjacent guided waves and optimal correlation coefficients between guided waves and their baseline guided waves, based on the public benchmark dataset. The results show that certain regular and irregular environmental variations, sensor drift, and installation drift can distort guided waves more significantly than structural damage itself. Overall, this public dataset makes four key contributions to the structural health monitoring community:

1. **Public Dataset for Real-World SHM Evaluation**: We provide the first publicly available benchmark dataset specifically created to assess the effectiveness of guided wave-based methods for long-term structural health monitoring in uncontrolled and dynamic outdoor environments.

2. **Identification of Key Challenges**: The dataset highlights four primary challenges in the public dataset: regular (e.g., daily changes in temperature and humidity) and irregular environmental conditions (e.g., rain and snow), sensor drift, installation drift, and damage severity variation. These challenges will motivate researchers to develop more practical and robust damage detection techniques suitable for real-world outdoor monitoring.

3. **Comprehensive Damage Types**: We introduce 13 types of damage with gradually increasing severity, ranging from small dents to large through-hole damage. This enables the dataset to be used for evaluating the effectiveness of guided wave-based methods in assessing damage severity under uncontrolled, dynamic outdoor conditions.

4. **Large-Scale Measurement Collection**: The dataset includes measurements taken approximately every 170 seconds, with each measurement consisting of 8 guided waves (transmitted by 2 actuators and received by 4 sensors). The extensive data from various sensors facilitates research into data fusion. Over 4.5 years, the dataset contains about 6.4 million measurements, providing a rich benchmark for testing guided wave compression techniques and evaluating the efficiency of damage detection methods using fewer measurements.
## Methods
We developed a structural health monitoring system at the University of Utah in Salt Lake City to implement and investigate
long-term monitoring under uncontrolled and dynamic conditions. The monitored structure was initially an intact aluminum
plate of 53 cm x 53 cm x 3 mm. This plate was placed on the first layer of the shelf, as illustrated in part (a) of Fig. 1.The monitored plate was placed on the first layer of a
shelf, as shown in part (a) of Fig. 2. To generate and receive guided waves, we transmitted a 1 ms linear chirp with a center
frequency ranging from 5 kHz to 350 kHz using sensors 5 and 6. Each response was recorded at a sampling rate of 1 MHz.
Measurements were taken approximately every 8.6 seconds, with only the first 10, 000 samples (10 ms) recorded for each
guided wave, as shown in part (a) of Fig. 3. Details of the sensors and data acquisition system are provided in Table.1



![Overview of the Monitoring Setup](/figures/Fig1.png)
*Figure 1. The actual positions of the lead zirconate titanate (PZT) transmitters (sensors 5 and 6) and receivers (sensors 1, 2, 3 and 4) are displayed in the left figure, while the precise coordinates (X: cm, Y: cm) are provided in the right figure.*  

![ExpSetup](/figures/Fig2.png)
*Figure 2. Figure (a) shows the monitored structure, an aluminum plate, positioned on the first layer of a shelf. The data acquisition
system was housed in a foam box on the second layer of the shelf. Figures (b) and (c) display the locations of the temperature,
brightness, air pressure, and humidity sensors, which were mounted on the exterior of the foam box.*

![Raw Signal](/figures/Fig3.png)
*Figure 3. The original guided wave, consisting of 10,000 samples and lasting 10 ms. This guided wave was collected from path 5-4 at 20:18:06 on April
24, 2021, at a measurement temperature of 16.57 ◦ C.*

![Table 1](/figures/Table1.png)
*Table 1. Information of environmental sensors and DAQ system.*

The monitored structure (an aluminum plate), along with the sensors and data acquisition systems, were placed in a small room188
with four walls but no roof at the University of Utah, Salt Lake City, as illustrated in part (a) of Fig. 2. This setup exposed189
the monitored structure and the structural health monitoring system to the outdoor environment under natural and dynamic190
conditions. The monitored structure and guided wave sensors endured various harsh environmental conditions, as depicted in191
Fig. 4. 
